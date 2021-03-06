# -*- coding: utf-8 -*-

from .frame_writer import *

def generate(image_file_name, video_file_name,
             crop=None, border=5,
             seconds=60, fps=30, size=(1280, 720), bitrate='10240k', stdout=False):
    image = Image.open(image_file_name)
    if crop:
        image = image.crop(crop)
    video_width, video_height = size
    a0 = video_width / video_height
    a1 = image.width / image.height
    min_ratio = 2.0
    if stdout:
        print(f'           image : {image.width}x{image.height} (aspect ratio={a1:.4})')
        print(f'           video : {video_width}x{video_height} (aspect ratio={a0:.4})')
        print(f'     image/video : {a1/a0:.4} (must be >={min_ratio:.4})')
    if a1 / a0 < min_ratio:
        raise Exception('Aspect ratio of image file is not enough to generate panorama video:'
                        f'{image.width}x{image.height}')
    thumb_width, thumb_height = video_width, int(image.height * video_width / image.width)
    thumb = image.resize( (thumb_width, thumb_height), Image.LANCZOS )
    body_height = video_height - thumb_height - border
    body_width = int(image.width * body_height / image.height)
    body = image.resize((body_width, body_height), Image.LANCZOS)
    step = int(body_width / (seconds * fps))
    if step < 1:
        step = 1
    offset = (body_width % step) // 2

    athumb = np.asarray(thumb)
    abody = np.asarray(body)
    pos = lambda x: int(x * video_width / body_width)
    with FFmpegFrameWriter(video_file_name, fps, size, bitrate, stdout) as writer:
        writer.frame[0:thumb_height, :, :] = athumb[:, :, :3]
        for x in range(offset, body_width - video_width, step):
            writer.frame[thumb_height:(thumb_height + border), :, :]=40
            writer.frame[(thumb_height + border):, :, :] = abody[:, x:(x+video_width), :3]
            writer.frame[thumb_height:(thumb_height + border), pos(x):pos(x + video_width),:]=192
            writer.add_frame()

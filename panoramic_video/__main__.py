# -*- coding: utf-8 -*-

import argparse, re
from .generator import *

def main():
    parser = argparse.ArgumentParser(
        description='Panoramic Video generates the video file from the panorama photograph image file.')
    parser.add_argument('image_file_name', help='The name of the panorama photograph image file')
    parser.add_argument('video_file_name', nargs='?', help='The name of the output video file')
    parser.add_argument('--crop', type=int, nargs=4, metavar=('LEFT', 'UPPER', 'RIGHT', 'LOWER'),
                        help='The crop rectangle as the left, upper, right, and lower pixel')
    parser.add_argument('--seconds', type=int, default=60, help='The time length of the panorama video')
    parser.add_argument('--fps', type=int, default=30, help='The frame rate of the panorama video')
    parser.add_argument('--size', type=int, nargs=2, metavar=('WIDTH', 'HEIGHT'), default=(1280, 720),
                        help='The width and the height of the panorama video')
    parser.add_argument('--bitrate', default='10240k', help='The video bitrate')
    parser.add_argument('--verbose', action='store_true', help='Verbose mode')

    args = parser.parse_args()
    image_file_name, video_file_name = args.image_file_name, args.video_file_name
    if not video_file_name:
        video_file_name = re.sub(r'\.[^\.]+$', '.mp4', image_file_name)
    if video_file_name == image_file_name:
        video_file_name = image_file_name + '.mp4'

    if args.verbose:
        print('{0:>16s} : {1}'.format('image_file_name', image_file_name))
        print('{0:>16s} : {1}'.format('video_file_name', video_file_name))
        for key in ('crop', 'seconds', 'fps', 'size', 'bitrate', 'verbose'):
            print('{0:>16s} : {1}'.format(key, args.__dict__[key]))

    generate(
        image_file_name,
        video_file_name,
        crop=args.crop,
        seconds=args.seconds,
        fps=args.seconds,
        size=args.size,
        bitrate=args.bitrate,
        stdout=args.verbose
    )

if __name__ == '__main__':
    main()

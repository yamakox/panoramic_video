# Panoramic Video

The video generator from panorama photograph image

## Install

```
pip3 install -v git+https://github.com/yamakox/panoramic_video.git
```

## Uninstall

```
pip3 uninstall panoramic_video
```

## Usage

```
python3 -m panoramic_video [-h] [--crop LEFT UPPER RIGHT LOWER] [--seconds SECONDS]
                           [--fps FPS] [--size WIDTH HEIGHT] [--bitrate BITRATE]
                           [--verbose]
                           image_file_name [video_file_name]
```

|arguments |description |
|:---|:---|
|image_file_name       |The name of the panorama photograph image file|
|video_file_name       |The name of the output video file|
|-h, --help            |show this help message and exit|
|--crop LEFT UPPER RIGHT LOWER |The crop rectangle as the left, upper, right, and lower pixel|
|--seconds SECONDS     |The time length of the panorama video|
|--fps FPS             |The frame rate of the panorama video|
|--size WIDTH HEIGHT   |The width and the height of the panorama video|
|--bitrate BITRATE     |The video bitrate|
|--verbose             |Verbose mode|

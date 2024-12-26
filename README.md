
## About wait_icon

A small python program which generates wait icons. Uses [ffmpeg](https://www.ffmpeg.org/) via [ImageMagick](https://imagemagick.org/index.php) and the command line version of [Inkscape](https://inkscape.org/).

## Example


```
python generate_wait_icon.py
```

Creates the file ```wait.png``` file below:

![wait icon](https://github.com/fderepas/wait_icon/blob/main/image/default.png)

```
python generate_wait_icon.py --col ff0000ff 00ff00ff
```

Creates the file ```wait.png``` image below:

![wait icon](https://github.com/fderepas/wait_icon/blob/main/image/gree_red.png)


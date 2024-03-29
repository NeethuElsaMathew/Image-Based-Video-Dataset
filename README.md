This readme file will help you navigate through this folder structure.

This repository contains 100 videos of different geometrical shapes.
All the videos present in the master branch are either encoded in H.264/AVC or H.265/HEVC video codec.

There are two folders FFMPEG and OpenCV. Along with these,  the scripts used for the creation of these videos are also attached here which are "video_circle_point.py", "video_ffmpeg", "video_opencv". These are the standard scripts used for the creation of these videos since the specifications are configurable within the scripts.The specifications of the video which can be modified in the script are type of video codec, frame size and frames per second (fps).

For Example, The FFMPEG folder consists of all the videos which are made using the FFMPEG library. There are videos of 5 geometrical shapes and those shapes are triangle, rectangle, rhombus, square and trapezoid. 

For Example, The OpenCV folder consists of all the videos which are made using the OpenCV library. There are videos of 5 geometrical shapes and those shapes are point, circle, pentagon, hexagon, and octagon. 

The folder structure looks like below :
1) AVC videos -> 1024 * 1024 pixels videos and 800 * 600 pixels videos
2) HEVC videos -> 1024 * 1024 pixels videos and 800 * 600 pixels videos

Moreover the name of the video file also suggest the specification. For example if you open a video file named 'rectangle__1024x1024_red_30fps' inside FFMPEG->HEVC->1024 * 1024 pixels videos,
it means it is a video of a red color rectangle with frame size 1024*1024 and frame rate 30fps whose video codec is HEVC.

To create a diverse set of videos we have used different specifications for the videos. Even though the video appears to be the same each video differs to one another depending on the specifications used for video construction. The specifications which are configurable and changed in each video are :

            1) Video codec: H.264/AVC or H.265/HEVC
            2) Frame size: 1024*1024, 800*600
            3) Frames per second (fps): 30, 15
            4) Used different color settings for shapes : Red,yellow,green and blue





import numpy as np
import os
import cv2


def generate_frame(width, height, center, radius, angle):
    frame = (
        np.ones((height, width, 3), dtype=np.uint8) * 255
    )  # To Generate a white background

    x = int(center[0] + radius * np.cos(np.radians(angle)))
    y = int(center[1] + radius * np.sin(np.radians(angle)))

    cv2.circle(frame, (x, y), radius, (0, 255, 0), -1)
    cv2.circle(frame, (x, y), radius, (0, 100, 0), 2)

    return frame


def create_circle_video(output_path, width, height, duration, fps):
    center = (width // 2, height // 2)
    radius = 50
    num_frames = int(duration * fps)

    fourcc = cv2.VideoWriter_fourcc(*"hev1")  # H.265 codec
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for frame_count in range(num_frames):
        angle = frame_count * (360 / num_frames)
        frame = generate_frame(width, height, center, radius, angle)
        out.write(frame)

    out.release()


# Default values provided
width, height = 640, 480
duration = 10  # time in seconds
fps = 30

output_path = "circle_animation_h265.mp4"
create_circle_video(output_path, width, height, duration, fps)

current_directory = os.getcwd()
print("Current Working Directory:", current_directory)
print(cv2.getBuildInformation())

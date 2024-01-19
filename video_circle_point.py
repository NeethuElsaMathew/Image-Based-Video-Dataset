import cv2
import numpy as np
import os

def generate_frame_circle(width, height, center, radius, angle):
    frame = np.ones((height, width, 3), dtype=np.uint8) * 255  # White background

    x = int(center[0] + radius * np.cos(np.radians(angle)))
    y = int(center[1] + radius * np.sin(np.radians(angle)))

    cv2.circle(frame, (x, y), radius, (0, 255, 255), -1)
    cv2.circle(frame, (x, y), radius, (0, 100, 255), 2)

    return frame

def generate_frame_point(width, height, center, radius, angle):
    frame = np.ones((height, width, 3), dtype=np.uint8) * 255  # White background

    x = int(center[0] + radius * np.cos(np.radians(angle)))
    y = int(center[1] + radius * np.sin(np.radians(angle)))

    cv2.circle(frame, (x, y), 5, (0, 255, 255), -1)  # Green point (filled)

    return frame

def create_circle_motion_video(output_path, width, height, duration, fps):
    center = (width // 2, height // 2)
    radius = 100
    num_frames = int(duration * fps)

    fourcc = cv2.VideoWriter_fourcc(*"avc1")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for frame_count in range(num_frames):
        angle = frame_count * (360 / num_frames)  # Rotate 360 degrees over the duration
        frame = generate_frame_point(width, height, center, radius, angle)
        out.write(frame)

    out.release()

def create_circle_video(output_path, width, height, duration, fps):
    center = (width // 2, height // 2)
    radius = 50
    num_frames = int(duration * fps)

    fourcc = cv2.VideoWriter_fourcc(*"avc1")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for frame_count in range(num_frames):
        angle = frame_count * (360 / num_frames)
        frame = generate_frame_circle(width, height, center, radius, angle)
        out.write(frame)

    out.release()

# Example usage
width, height = 800, 600
duration = 10  # in seconds
fps = 30

output_directory = "/Users/ganesh/Desktop/ITSEC/Opencv/AVC/800*600"  # Specify the directory where you want to save videos

output_path_circle = os.path.join(output_directory, "circle_animation_yellow.mp4")
create_circle_video(output_path_circle, width, height, duration, fps)

output_path_point = os.path.join(output_directory, "point_circular_motion_animation_yellow.mp4")
create_circle_motion_video(output_path_point, width, height, duration, fps)

current_directory = os.getcwd()
print("Current Working Directory:", current_directory)
print(cv2.getBuildInformation())
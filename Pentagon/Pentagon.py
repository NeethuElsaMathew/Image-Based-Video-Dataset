import cv2
import numpy as np
import os


def generate_frame(width, height, center, radius, angle):
    # Create a white background
    frame = np.ones((height, width, 3), dtype=np.uint8) * 255  # White background

    # Calculate the vertices of a pentagon based on rotation angle
    vertices = []
    for i in range(5):
        x = int(center[0] + radius * np.cos(np.radians(angle + i * 360 / 5)))
        y = int(center[1] + radius * np.sin(np.radians(angle + i * 360 / 5)))
        vertices.append((x, y))

    # Draw the pentagon on the frame
    cv2.polylines(
        frame, [np.array(vertices)], isClosed=True, color=(0, 255, 0), thickness=2
    )

    return frame


def create_pentagon_motion_video(output_path, width, height, duration, fps):
    center = (width // 2, height // 2)
    radius = 100
    num_frames = int(duration * fps)

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for frame_count in range(num_frames):
        angle = frame_count * (360 / num_frames)  # Rotate 360 degrees over the duration
        frame = generate_frame(width, height, center, radius, angle)
        out.write(frame)

    out.release()


# Example usage
width, height = 640, 480
duration = 10  # in seconds
fps = 30

output_path = "pentagon_circular_motion_animation.mp4"
create_pentagon_motion_video(output_path, width, height, duration, fps)

current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

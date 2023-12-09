import cv2
import numpy as np
import os


def generate_frame(width, height, center, radius, angle):
    # Create a white background
    frame = np.ones((height, width, 3), dtype=np.uint8) * 255  # White background

    # Calculate circle position based on rotation angle
    x = int(center[0] + radius * np.cos(np.radians(angle)))
    y = int(center[1] + radius * np.sin(np.radians(angle)))

    # Draw the circle on the frame with a dark green border
    cv2.circle(frame, (x, y), radius, (0, 255, 0), -1)  # Green circle (filled)
    cv2.circle(frame, (x, y), radius, (0, 100, 0), 2)  # Dark green circle border

    return frame


def create_circle_video(output_path, width, height, duration, fps):
    center = (width // 2, height // 2)
    radius = 50
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

output_path = "circle_animation.mp4"
create_circle_video(output_path, width, height, duration, fps)

current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

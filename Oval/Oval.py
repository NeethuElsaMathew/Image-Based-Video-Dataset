import cv2
import numpy as np
import os


def generate_frame(width, height, center, radius_x, radius_y, angle):
    # Create a white background
    frame = np.ones((height, width, 3), dtype=np.uint8) * 255  # White background

    # Calculate the position of the center of the ellipse based on rotation angle
    x = int(center[0] + radius_x * np.cos(np.radians(angle)))
    y = int(center[1] + radius_y * np.sin(np.radians(angle)))

    # Draw the ellipse on the frame
    cv2.ellipse(
        frame, (x, y), (radius_x, radius_y), 0, 0, 360, (0, 255, 0), -1
    )  # Green filled ellipse

    return frame


def create_oval_motion_video(output_path, width, height, duration, fps):
    center = (width // 2, height // 2)
    radius_x = 100
    radius_y = 50  # You can adjust this value for a more elongated or squashed oval
    num_frames = int(duration * fps)

    fourcc = cv2.VideoWriter_fourcc(*"avc1")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for frame_count in range(num_frames):
        angle = frame_count * (360 / num_frames)  # Rotate 360 degrees over the duration
        frame = generate_frame(width, height, center, radius_x, radius_y, angle)
        out.write(frame)

    out.release()


# Example usage
width, height = 640, 480
duration = 10  # in seconds
fps = 30

output_path = "oval_circular_motion_animation.mp4"
create_oval_motion_video(output_path, width, height, duration, fps)

current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

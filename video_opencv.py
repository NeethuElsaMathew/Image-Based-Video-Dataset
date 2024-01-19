import cv2
import numpy as np
import os

def generate_pentagon_frame(width, height, center, radius, angle, num_frames):
    frame = np.ones((height, width, 3), dtype=np.uint8) * 255  # White background

    # Calculate the vertices of the pentagon based on the rotation angle
    vertices = []
    for i in range(5):
        x = int(center[0] + radius * np.cos(np.radians(angle + i * 360 / 5)))
        y = int(center[1] + radius * np.sin(np.radians(angle + i * 360 / 5)))
        vertices.append((x, y))

    # Draw the pentagon on the frame with yellow color
    cv2.polylines(frame, [np.array(vertices)], isClosed=True, color=(0, 255, 255), thickness=2)

    return frame

def generate_hexagon_frame(width, height, center, radius, angle, num_frames):
    frame = np.ones((height, width, 3), dtype=np.uint8) * 255  # White background

    # Calculate the vertices of the hexagon based on the rotation angle
    vertices = []
    for i in range(6):
        x = int(center[0] + radius * np.cos(np.radians(angle + i * 360 / 6)))
        y = int(center[1] + radius * np.sin(np.radians(angle + i * 360 / 6)))
        vertices.append((x, y))

    # Draw the hexagon on the frame with yellow color
    cv2.polylines(frame, [np.array(vertices)], isClosed=True, color=(0, 255, 255), thickness=2)

    return frame

def generate_octagon_frame(width, height, center, radius, angle, num_frames):
    frame = np.ones((height, width, 3), dtype=np.uint8) * 255  # White background

    # Calculate the vertices of the octagon based on the rotation angle
    vertices = []
    for i in range(8):
        x = int(center[0] + radius * np.cos(np.radians(angle + i * 360 / 8)))
        y = int(center[1] + radius * np.sin(np.radians(angle + i * 360 / 8)))
        vertices.append((x, y))

    # Draw the octagon on the frame with yellow color
    cv2.polylines(frame, [np.array(vertices)], isClosed=True, color=(0, 255, 255), thickness=2)

    return frame

def create_motion_video(output_directory, output_filename, width, height, duration, fps, generate_frame_func):
    center = (width // 2, height // 2)
    num_frames = int(duration * fps)

    output_path = os.path.join(output_directory, output_filename)

    fourcc = cv2.VideoWriter_fourcc(*"avc1")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for frame_count in range(num_frames):
        angle = frame_count * (360 / num_frames)  # Rotate 360 degrees over the duration
        frame = generate_frame_func(width, height, center, 100, angle, num_frames)
        out.write(frame)

    out.release()

# Example usage
width, height = 800, 600
duration = 10  # in seconds
fps = 30

output_directory = "/Users/ganesh/Desktop/ITSEC/Opencv/AVC/800*600"  # Specify the directory where you want to save videos

# Pentagon
create_motion_video(output_directory, "pentagon_animation_yellow.mp4", width, height, duration, fps, generate_pentagon_frame)

# Hexagon
create_motion_video(output_directory, "hexagon_animation_yellow.mp4", width, height, duration, fps, generate_hexagon_frame)

# Octagon
create_motion_video(output_directory, "octagon_animation_yellow.mp4", width, height, duration, fps, generate_octagon_frame)

print("Videos saved to:", output_directory)

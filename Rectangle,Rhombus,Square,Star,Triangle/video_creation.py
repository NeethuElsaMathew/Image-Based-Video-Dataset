import subprocess
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set the output directory for videos
output_dir = '/Users/ganesh/Desktop/Videos-FFMPEG/'

# Set video parameters
width, height = 1024, 1024  # Adjust as needed
fps = 30
duration = 10  # in seconds


# Function to draw different shapes on frames
def draw_shape(shape_type):
    if shape_type == 'triangle':
        size = np.random.randint(50, 150)
        x = np.random.randint(0, width - size)
        y = np.random.randint(0, height - size)
        points = np.array([
            [x + size / 2, y + size],
            [x, y],
            [x + size, y],
        ])
        triangle = patches.Polygon(points, fc='red')
        plt.gca().add_patch(triangle)
    elif shape_type == 'square':
        side_length = np.random.randint(50, 150)
        x = np.random.randint(0, width - side_length)
        y = np.random.randint(0, height - side_length)
        square = patches.Rectangle((x, y), side_length, side_length, fc='red')
        plt.gca().add_patch(square)
    elif shape_type == 'star':
        size = np.random.randint(30, 100)
        x = np.random.randint(100, width - size)
        y = np.random.randint(100, height - size)
        points = np.array([
            [0, 0.5],
            [0.3, 0.3],
            [0.5, 0],
            [0.7, 0.3],
            [1, 0.5],
            [0.8, 0.7],
            [0.5, 1],
            [0.2, 0.7],
            [0, 0.5],
        ])
        star = patches.Polygon(points * size + [x, y], fc='red')
        plt.gca().add_patch(star)
    elif shape_type == 'rhombus':
        size = np.random.randint(50, 150)
        x = np.random.randint(150, width - size)
        y = np.random.randint(150, height - size)
        rhombus = patches.RegularPolygon((x, y), numVertices=8, radius=size/np.sqrt(2), orientation=np.pi/4, fc='red')
        plt.gca().add_patch(rhombus)
    elif shape_type == 'rectangle':
        width_rect = np.random.randint(50, 200)
        height_rect = np.random.randint(50, 200)
        x = np.random.randint(0, width - width_rect)
        y = np.random.randint(0, height - height_rect)
        rectangle = patches.Rectangle((x, y), width_rect, height_rect, fc='red')
        plt.gca().add_patch(rectangle)



plt.axis('off')

# Generate videos for each shape
shapes = ['triangle', 'square', 'star', 'rhombus', 'rectangle']

for shape in shapes:
    # Set the output video file path for each shape
    output_video_path = os.path.join(output_dir, f'{shape}_video.mp4')

    # Create a temporary directory to store individual frame images
    temp_dir = 'temp_frames'
    os.makedirs(temp_dir, exist_ok=True)

    # Generate frames with the specific shape
    for frame_num in range(int(fps * duration)):
        # Create a blank frame
        plt.figure(figsize=(width / 100, height / 100), dpi=100)
        plt.axis('off')
        plt.xlim(0, width)
        plt.ylim(0, height)

        # Draw the selected shape on the frame
        draw_shape(shape)
        # Save the frame as an image
        frame_path = os.path.join(temp_dir, f'frame_{frame_num:03d}.png')
        plt.savefig(frame_path)
        plt.close()

    # Use FFmpeg to create a video from the frames
    ffmpeg_command = (
        f"ffmpeg -framerate {fps} -i {temp_dir}/frame_%03d.png "
        f"-c:v libx265 -pix_fmt yuv420p -y {output_video_path}"
    )
    subprocess.run(ffmpeg_command, shell=True)

    # Clean up: remove temporary frames
    for frame_file in os.listdir(temp_dir):
        frame_path = os.path.join(temp_dir, frame_file)
        os.remove(frame_path)

    # Remove the temporary directory
    os.rmdir(temp_dir)

    print(f"Video created: {output_video_path}")

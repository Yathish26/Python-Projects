from moviepy.editor import VideoFileClip
import numpy as np
from PIL import Image


def extract_frames(video_path, output_folder, interval=1):
    # Load the video file
    video = VideoFileClip(video_path)

    # Get the duration of the video in seconds
    duration = int(video.duration)

    # Extract frames at the specified interval
    for t in range(0, duration, interval):
        # Get the frame at time t
        frame = video.get_frame(t)

        # Convert the frame to an image
        image = Image.fromarray(np.uint8(frame))

        # Save the image
        image.save(f"{output_folder}/frame_{t}.png")

    print(f"Frames have been extracted and saved to {output_folder}.")


# Usage
video_path = "The Start of us.mp4"  # Replace with the path to your video file
output_folder = "output"  # Replace with the path to your output folder

extract_frames(video_path, output_folder)

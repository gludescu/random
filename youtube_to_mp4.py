import os
from pytube import YouTube
from moviepy.editor import *


def download_youtube_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension="mp4", progressive=True).order_by("resolution").desc().first()
    print(f"Downloading: {yt.title}")
    return stream.download(output_path)


def convert_to_mp4(input_file, output_file):
    clip = VideoFileClip(input_file)
    clip.write_videofile(output_file, codec="libx264")


def main():
    url = input("Enter the YouTube video URL: ")
    output_path = os.getcwd()

    video_path = download_youtube_video(url, output_path)
    output_file = os.path.join(output_path, os.path.splitext(os.path.basename(video_path))[0] + ".mp4")

    if video_path != output_file:
        convert_to_mp4(video_path, output_file)
        os.remove(video_path)
    print(f"Video saved as: {output_file}")


if __name__ == "__main__":
    main()

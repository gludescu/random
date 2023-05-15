import os
from pytube import YouTube
from moviepy.editor import *


def download_youtube_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).order_by("abr").desc().first()
    print(f"Downloading: {yt.title}")
    return stream.download(output_path)


def convert_to_mp3(input_file, output_file):
    clip = AudioFileClip(input_file)
    clip.write_audiofile(output_file, codec="mp3")


def main():
    url = input("Enter the YouTube video URL: ")
    output_path = os.getcwd()

    video_path = download_youtube_video(url, output_path)
    output_file = os.path.join(output_path, os.path.splitext(
        os.path.basename(video_path))[0] + ".mp3")

    if os.path.splitext(video_path)[1] != ".mp3":
        convert_to_mp3(video_path, output_file)
        os.remove(video_path)
    print(f"Audio saved as: {output_file}")


if __name__ == "__main__":
    main()

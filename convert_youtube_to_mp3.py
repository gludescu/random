"""
This Python script uses the 'pytube' and 'moviepy' libraries to download a YouTube video as an audio file (MP3 format). To use this script, follow the steps below:

1. Install the 'pytube' and 'moviepy' libraries if you haven't already by running pip install pytube moviepy.
2. Run the script. The script will prompt you to enter the YouTube video URL.
3. Enter the URL of the YouTube video you want to download as an audio file.
4. The script will download the video, convert it to an MP3 audio file, and save it in the current working directory.
5. After the conversion, the script will print the path of the saved audio file.

Example:

- Suppose you want to download the audio from a YouTube video with the URL 'https://youtu.be/dQw4w9WgXcQ'.
- Run the script and enter 'https://youtu.be/dQw4w9WgXcQ' when prompted.
- The script will download the video, convert it to an MP3 audio file, and save it in the current working directory.
- After the conversion, the script will print the path of the saved audio file, e.g., "/Users/username/Downloads/video_title.mp3".

Please note that this script might not work for all YouTube videos, as some videos might have restrictions on downloading or might be blocked by YouTube's content protection systems.
"""


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

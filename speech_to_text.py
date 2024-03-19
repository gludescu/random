from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

audio_file = open("4.mp3", "rb")
translation = client.audio.translations.create(
    model="whisper-1",
    file=audio_file,
    response_format="text"
)

print(translation)

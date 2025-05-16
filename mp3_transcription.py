import openai
import os

# Make sure your OpenAI API key is set in the environment
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Path to your MP3 file
audio_file_path = "input.mp3"

# Open the audio file
with open(audio_file_path, "rb") as audio_file:
    print("Sending file to Whisper for translation...")

    response = client.audio.translations.create(
        model="whisper-1",
        file=audio_file,
        response_format="text"
    )

    # Print the translated output
    print(response)
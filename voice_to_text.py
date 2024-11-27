#!/usr/bin/env python3

##############################################################################

from dotenv import load_dotenv
import os

load_dotenv()
STT_API_URL = str(os.getenv("STT_API_URL"))

from gradio_client import Client, handle_file

## WE NEED A BETTER MODEL FOR THIS, WHISPER-LARGE-V3 preferably

def voice_to_text(file_path="output.wav", server_url=STT_API_URL):
    """
    Transcribe audio file to text using a Gradio API.

    Args:
        file_path (str): Path to the audio file.
        server_url (str): URL of the Gradio server.

    Returns:
        str: The transcribed text or an error message if something goes wrong.
    """
    client = Client(server_url)

    try:
        return client.predict(
            file_path=handle_file(file_path),
            model="Systran/faster-whisper-large-v3",
            task="transcribe",
            temperature=0,
            stream=True,
            api_name="/predict"
        )
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    audio_file = "MZ2db44cf0728671ed59835a955cc8376f.wav"  # Replace with your audio file path

    transcription = voice_to_text(audio_file)

    print(f"Transcription result: {transcription}")

#!/usr/bin/env python3

import subprocess

def text_to_voice(text, output_file='output.wav', model='models/ro_RO-mihai-medium.onnx'): # models/en_US-lessac-medium.onnx
    """
    Convert text to voice using Piper TTS.

    Args:
        text (str): The text to convert to speech.
        output_file (str): The file to save the output audio.
        model (str): The TTS model to use.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """

    # Prepare the command to execute
    command = ['piper', '--model', model, '--output_file', output_file]

    try:
        # Use subprocess to call the Piper command
        process = subprocess.run(command, input=text, text=True, capture_output=True, check=True)

        # Check for errors in the output
        if process.stderr:
            print("Error:", process.stderr)
            return False

        print(f"Successfully converted text to voice. Audio saved as '{output_file}'")
        return True

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running Piper: {e}")
        print("Standard Output:", e.stdout)
        print("Standard Error:", e.stderr)
        return False

def text_to_voice_edge_tts(text, voice='ro-RO-AlinaNeural'):
    """
    Convert text to voice using Edge TTS.

    Args:
        text (str): The text to convert to speech.
        voice (str): The voice to use for the conversion.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """

    # Prepare the command to execute
    command = ['edge-playback', '-t', text, '-v', voice]

    try:
        # Use subprocess to call the Piper command
        process = subprocess.run(command, text=True, capture_output=True, check=True)

        # Check for errors in the output
        if process.stderr:
            print("Error:", process.stderr)
            return False

        print(f"Successfully converted text to voice.")
        return True

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running Edge TTS: {e}")
        print("Standard Output:", e.stdout)
        print("Standard Error:", e.stderr)
        return False

if __name__ == "__main__":
    text_input = "Welcome to the world of speech synthesis!"
    output_filename = "output.wav"

    # Call the function
    # success = text_to_voice(text_input, output_filename, model='models/en_US-lessac-medium.onnx')
    success = text_to_voice_edge_tts(text_input, voice='en-US-GuyNeural')

    if success:
        print(f"Audio file created successfully.")
    else:
        print("Failed to create audio file.")

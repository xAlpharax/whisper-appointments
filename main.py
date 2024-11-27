#!/usr/bin/env python3

from text_to_voice import text_to_voice, text_to_voice_edge_tts
from voice_to_text import voice_to_text
from audio_utils import play_audio, record_audio

from llm_query import query
from random import randint

if __name__ == "__main__":
    import asyncio

    initial_greeting = "Vorbeste in limba romana si prezinta-te."
    # initial_greeting = "Present yourself."
    chatId = randint(0, 1000000).__str__()
    output_filename = "output.wav"

    async def query_llm(question):
        output = await query({
            "question": question,
            "chatId": chatId,
        })
        return output

    output = asyncio.run(query_llm(initial_greeting))["text"]

    print(output)

    text_input = output

    # Call the function
    success = text_to_voice(text_input, output_filename)
    # success = text_to_voice_edge_tts(text_input)

    if success:
        print(f"Audio file '{output_filename}' created successfully.")
    else:
        print("Failed to create audio file.")

    # Play the audio file
    play_audio(output_filename)

    while KeyboardInterrupt:
        # Record audio
        record_audio(output_filename)

        # Convert the audio to feedable text
        text_output = voice_to_text(output_filename)

        if text_output:
            print(f"Text extracted from audio: '{text_output}'")
        else:
            print("Failed to extract text from audio.")

        # Process the user input
        output = asyncio.run(query_llm(text_output))["text"]

        print(output)

        text_input = output

        # Call the function
        success = text_to_voice(text_input, output_filename)
        # success = text_to_voice_edge_tts(text_input)

        if success:
            print(f"Audio file '{output_filename}' created successfully.")
        else:
            print("Failed to create audio file.")

        # Play the audio file
        play_audio(output_filename)

#!/usr/bin/env python3

import subprocess

def record_audio(output_file="output.wav"):
    try:
        print("Recording... Press Ctrl+C to stop.")
        subprocess.run([
            'arecord',
            '-D', 'plughw:0,0',   # Adjust the device as needed
            '-f', 'S16_LE',       # 16-bit little-endian
            '-r', '16000',        # 16000 sample rate
            '-c', '1',            # Single channel (mono)
            output_file           # Output file
        ])
    except KeyboardInterrupt:
        print("\nRecording stopped.")
        pass

def play_audio(input_file="output.wav"):
    try:
        print("Playing audio...")
        subprocess.run(['aplay', input_file])
    except KeyboardInterrupt:
        print("\nPlayback interrupted.")
        pass

if __name__ == "__main__":
    # Step 1: Record Audio
    record_audio('output.wav')

    # Step 2: Play the recorded audio
    play_audio('output.wav')

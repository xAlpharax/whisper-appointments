#!/usr/bin/env python3

from gradio_client import Client, handle_file

client = Client("http://192.168.100.136:8000/")
result = client.predict(
		# file_path=handle_file('https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav'),
        file_path=handle_file('./test.wav'),
        model="Systran/faster-whisper-large-v3",
        task="transcribe",
        temperature=0,
        stream=True,
        api_name="/predict"
)
print(result)

# Aditional api calls for cleaning up

# from gradio_client import Client, handle_file

# client = Client("http://192.168.100.136:8000/")

# client.predict(
  # api_name="/lambda"
# )

# result = client.predict(
  # file_path=handle_file('http://192.168.100.136:8000/file=/tmp/gradio/44e8f9cfd1a7cb73358f141516253feccbbbdf85cbc6a87c42f4d17622ddf2f3/hello_and_request.wav'),
  # file_path=handle_file('./test.wav'),
  # model="Systran/faster-whisper-large-v3",
  # task="transcribe",
  # temperature=0.4,
  # stream=True,
  # api_name="/predict"
# )

# client.predict(
  # api_name="/cleanup"
# )

# print(result)

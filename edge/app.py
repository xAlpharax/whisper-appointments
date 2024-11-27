import gradio as gr
import edge_tts
import asyncio
import tempfile

from typing import Optional, Tuple

# Fetch available voices once and cache them
async def get_voices() -> dict:
    voices = await edge_tts.list_voices()
    return {f"{v['ShortName']} ({v['Gender']})": v['ShortName'] for v in voices}

# Text-to-Speech conversion function
async def text_to_speech(text: str, voice: str, rate: int, volume: int, pitch: int) -> Tuple[Optional[str], Optional[str]]:
    try:
        if not text.strip():
            return None, "Please enter text to convert."
        if not voice:
            return None, "Please select a voice."

        voice_short_name = voice.split(" ")[0]
        rate_str = f"{rate:+d}%"
        volume_str = f"{volume:+d}%"
        pitch_str = f"{pitch:+d}Hz"

        communicate = edge_tts.Communicate(text, voice_short_name, rate=rate_str, volume=volume_str, pitch=pitch_str)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
            tmp_path = tmp_file.name
            await communicate.save(tmp_path)

        return tmp_path, None
    except Exception as e:
        return None, f"An error occurred: {str(e)}"

# Wrapper to integrate async function into Gradio
async def tts_interface(text: str, voice: str, rate: int, volume: int, pitch: int) -> Tuple[Optional[str], Optional[str]]:
    return await text_to_speech(text, voice, rate, volume, pitch)

# Create the Gradio application
async def create_demo():
    voices = await get_voices()

    description = """
    Convert Text to Speech using Microsoft Edge TTS. Adjust speech rate and pitch:
    - **Rate**: `0` is default; positive increases speed, negative decreases speed.
    - **Volume**: `0` is default; positive increases volume, negative decreases volume.
    - **Pitch**: `0` is default; positive raises pitch, negative lowers pitch.
    """

    return gr.Interface(
        fn=tts_interface,
        inputs=[
            gr.Textbox(label="Input Text", lines=5, placeholder="Type the text to convert here..."),
            gr.Dropdown(choices=list(voices.keys()), label="Select Voice", value="ro-RO-AlinaNeural (Female)"),
            gr.Slider(minimum=-50, maximum=50, value=0, label="Speech Rate Adjustment (%)", step=1),
            gr.Slider(minimum=-50, maximum=50, value=0, label="Speech Volume Adjustment (%)", step=1),
            gr.Slider(minimum=-50, maximum=50, value=0, label="Speech Pitch Adjustment (Hz)", step=1)
        ],
        outputs=[
            gr.Audio(label="Generated Audio", type="filepath"),
            gr.Markdown(label="Warning", visible=False)
        ],
        title="Edge TTS Text-To-Speech",
        description=description,
        theme=gr.themes.Origin(),
        analytics_enabled=False,
        flagging_mode="never",
        clear_btn=None,
    )

# Run the application
if __name__ == "__main__":
    demo = asyncio.run(create_demo())
    demo.launch()

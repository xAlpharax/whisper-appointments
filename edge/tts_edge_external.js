import { Client } from "@gradio/client";

const client = await Client.connect("http://127.0.0.1:7860/");

const result = await client.predict(
  "/predict", {
    text: "salut",
    voice: "ro-RO-AlinaNeural (Female)",
    rate: 0,
    volume: 0,
    pitch: 0,
});

console.log(result.data);

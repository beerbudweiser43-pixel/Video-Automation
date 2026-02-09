"""Simple HTTP wrapper to emulate a ComfyUI `/run` endpoint for local testing.

- POST /run { prompt, style, pipeline }
- Returns JSON { images: [base64,...] }

If you later implement a real runner that can execute ComfyUI workflows, replace the `generate_images` function.
"""
from flask import Flask, request, jsonify
import base64
from io import BytesIO
from omniflow.dummy_generator import dummy_generate

app = Flask(__name__)


def pil_to_base64(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    b = buf.getvalue()
    return base64.b64encode(b).decode("utf-8")


@app.route("/run", methods=["POST"])
def run():
    data = request.get_json(force=True)
    prompt = data.get("prompt", "test")
    style = data.get("style", "AI Character Avatar")
    # pipeline = data.get('pipeline')

    imgs = dummy_generate(prompt=prompt, style=style)
    encoded = [pil_to_base64(i) for i in imgs]
    return jsonify({"images": encoded})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8188)

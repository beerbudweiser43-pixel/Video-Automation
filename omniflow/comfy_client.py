import os
import requests
from typing import List
from io import BytesIO
from PIL import Image


def run_pipeline(prompt: str, style: str, comfy_api: str = "http://localhost:8188") -> List[Image.Image]:
    """Call a local ComfyUI HTTP API to run a predefined pipeline.

    This function assumes ComfyUI or a small wrapper exposes an endpoint like `/run` that accepts
    JSON payload with `prompt` and `pipeline` fields and returns a list of base64 images or image bytes.

    If you don't have such an API, use the PowerShell setup script to run ComfyUI locally and add a lightweight
    HTTP wrapper/plugin for ComfyUI. This module gracefully raises if the endpoint is not available.
    """
    endpoint = os.path.join(comfy_api.rstrip('/'), "run")
    payload = {
        "prompt": prompt,
        "style": style,
        "pipeline": "ultimate_pipeline.json",
    }

    resp = requests.post(endpoint, json=payload, timeout=60)
    if resp.status_code != 200:
        raise RuntimeError(f"ComfyUI API returned {resp.status_code}: {resp.text}")

    data = resp.json()
    images = []
    for item in data.get("images", []):
        # item expected to be base64 bytes or a URL; handle common cases
        if isinstance(item, str) and item.startswith("http"):
            r = requests.get(item)
            images.append(Image.open(BytesIO(r.content)).convert("RGB"))
        else:
            # assume base64-encoded bytes
            import base64

            b = base64.b64decode(item)
            images.append(Image.open(BytesIO(b)).convert("RGB"))

    return images

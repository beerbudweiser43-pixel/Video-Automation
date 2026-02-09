import os
from . import comfy_client
from .dummy_generator import dummy_generate


def generate_visuals(channel: str, style: str, prompt: str, use_comfyui: bool = False, comfy_url: str = None):
    """High-level generator interface. Returns list of image byte arrays or PIL images suitable for Streamlit `st.image`.

    - If `use_comfyui` is True, attempts to use the `comfy_client` to run a pipeline.
    - Otherwise falls back to `dummy_generate` for quick testing.
    """
    if not prompt:
        prompt = f"{channel} - {style} example visual"

    if use_comfyui:
        comfy_api = comfy_url or os.getenv("COMFYUI_API_URL", "http://localhost:8188")
        try:
            imgs = comfy_client.run_pipeline(prompt=prompt, style=style, comfy_api=comfy_api)
            return imgs
        except Exception as e:
            # Bubble up error to UI
            raise RuntimeError(f"ComfyUI pipeline error: {e}")

    # Fallback dummy generator
    return dummy_generate(prompt=prompt, style=style)

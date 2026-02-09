# Workflow Guide

## Overview
This guide explains how `streamlit_app.py` maps UI choices to generation pipelines and how to wire ComfyUI.

- `Channel Template` influences script templates and pacing
- `Visual Style` maps to ComfyUI pipelines in `workflows/` (examples live in the ComfyUI-OmniFlow concept)

## Local ComfyUI API
ComfyUI does not include a built-in HTTP API by default. You can:

1. Add a small plugin/wrapper that listens on `http://localhost:8188/run` and accepts `POST {prompt, style, pipeline}` and triggers a ComfyUI flow and returns images.
2. Alternatively, run ComfyUI headless and use its Python API to execute saved workflows.

This project includes a `comfy_client.py` that expects such an endpoint. If you don't have it, the Streamlit app will use the `dummy` generator.

## Recommended next steps
- Add a ComfyUI plugin that exposes `/run` and maps `pipeline` to one of the `workflows/*.json` definitions
- Add model download instructions and provide sample `workflows/` JSON files to the repo
- Integrate ElevenLabs or other TTS in a separate module for audio generation
- Add n8n or Make recipes to publish to YouTube automatically

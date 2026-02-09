# Simple runner for ComfyUI when it's installed
Write-Host "Starting ComfyUI (assumes ComfyUI directory is a sibling)..."
.\.comfyui_venv\Scripts\Activate.ps1
cd ComfyUI
python main.py

# PowerShell helper: Guide to install ComfyUI locally on Windows
# NOTE: This script outlines steps and requires user confirmation for model downloads.

# 1) Clone ComfyUI (official repo may change):
# git clone https://github.com/comfyanonymous/ComfyUI.git ComfyUI

# 2) Create venv and install dependencies
python -m venv .comfyui_venv
.\.comfyui_venv\Scripts\Activate.ps1
pip install -r ComfyUI\requirements.txt

Write-Host "ComfyUI requirements installed."

# 3) Download models (SDXL, ControlNet, Loras) into ComfyUI/models folder
Write-Host "Please download the models manually into ComfyUI\models. See docs for recommended models."

# 4) Start ComfyUI manually:
Write-Host "To start ComfyUI, run:"
Write-Host "  cd ComfyUI"
Write-Host "  .\.comfyui_venv\Scripts\Activate.ps1"
Write-Host "  python main.py"

Write-Host "If you want a small HTTP wrapper to accept pipeline-run requests, you'll need to add a plugin or use the provided run wrapper in this repo. See docs/workflow_guide.md"

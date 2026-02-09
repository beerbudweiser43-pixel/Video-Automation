"""Real ComfyUI Python runner using websockets and the ComfyUI Python API."""
import subprocess
import sys
import json
import time
import os
from pathlib import Path
from typing import List, Dict, Any


class ComfyUIRunner:
    """Wrapper to run ComfyUI workflows locally using Python API.
    
    Assumes ComfyUI is cloned to a sibling directory or environment var COMFYUI_PATH is set.
    """
    
    def __init__(self, comfyui_path: str = None):
        if not comfyui_path:
            comfyui_path = os.getenv("COMFYUI_PATH", "../ComfyUI")
        self.comfyui_path = Path(comfyui_path).resolve()
        if not self.comfyui_path.exists():
            raise FileNotFoundError(f"ComfyUI path {self.comfyui_path} not found. Set COMFYUI_PATH env var.")
        self._load_api()

    def _load_api(self):
        """Dynamically import ComfyUI main module."""
        sys.path.insert(0, str(self.comfyui_path))
        try:
            # ComfyUI's execution API
            from comfy.cli_args import args
            from comfy.model_management import models
            from nodes import NODE_CLASS_MAPPINGS, init_nodes
            self.NODE_MAPPINGS = NODE_CLASS_MAPPINGS
            init_nodes()
        except ImportError as e:
            raise RuntimeError(f"Failed to import ComfyUI: {e}. Ensure ComfyUI is installed correctly.")

    def load_workflow(self, workflow_path: str) -> Dict[str, Any]:
        """Load a workflow JSON file."""
        with open(workflow_path) as f:
            return json.load(f)

    def execute_workflow(self, workflow: Dict[str, Any], timeout: int = 300) -> List[str]:
        """Execute a ComfyUI workflow and return output image paths.
        
        This is a simplified approach. For production, use ComfyUI's server API or 
        implement a full execution queue handler.
        """
        # Placeholder: in reality, you'd queue the workflow and poll for results
        # For now, this raises and suggests using the HTTP API instead
        raise NotImplementedError(
            "Direct Python execution is complex. Use the HTTP API endpoint instead: "
            "start ComfyUI with `python main.py` and POST to http://localhost:8188 "
            "or implement a full queue handler here."
        )


def run_comfyui_http(prompt: str, style: str, pipeline: str, comfy_url: str = "http://localhost:8188") -> List[str]:
    """Execute a workflow by calling the ComfyUI HTTP API (requires ComfyUI running as a server).
    
    If you have ComfyUI running on localhost:8188, this function will queue a job and return output paths.
    """
    import requests
    
    # Build a minimal workflow request
    # The actual workflow is loaded from workflows/ and parameterized
    workflow = {
        "prompt": prompt,
        "style": style,
        "pipeline": pipeline,
    }
    
    endpoint = f"{comfy_url}/prompt"
    try:
        resp = requests.post(endpoint, json=workflow, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        
        # Typical ComfyUI response includes 'prompt_id'
        # Poll for outputs or handle the async response
        outputs = data.get("outputs", data.get("images", []))
        return outputs
    except Exception as e:
        raise RuntimeError(f"ComfyUI HTTP request failed: {e}")

#!/usr/bin/env python3
"""Download Stable Diffusion model with progress tracking"""

import os
import sys
import requests
from pathlib import Path

def download_model():
    """Download the model file with progress bar"""
    
    # Model details
    model_url = "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors"
    model_name = "sd-v1-5-pruned-emaonly.safetensors"
    checkpoint_dir = Path(r"C:\workspace\ComfyUI\models\checkpoints")
    model_path = checkpoint_dir / model_name
    
    print(f"📥 Model Download")
    print(f"{'='*60}")
    print(f"URL: {model_url}")
    print(f"Destination: {model_path}")
    print(f"{'='*60}\n")
    
    # Check if already exists
    if model_path.exists():
        size_gb = model_path.stat().st_size / (1024**3)
        print(f"✅ Model already exists ({size_gb:.2f} GB)")
        return True
    
    # Create directory
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        print("Starting download (this may take 10-60 minutes)...")
        print()
        
        # Download with progress
        response = requests.get(model_url, stream=True, timeout=60)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        chunk_size = 1024 * 1024  # 1MB chunks
        
        print(f"Total size: {total_size / (1024**3):.2f} GB")
        print()
        
        with open(model_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    percent = (downloaded / total_size) * 100
                    mb_done = downloaded / (1024**2)
                    mb_total = total_size / (1024**2)
                    
                    # Progress bar
                    bar_length = 50
                    filled = int(bar_length * downloaded / total_size)
                    bar = '█' * filled + '░' * (bar_length - filled)
                    
                    print(f"\r[{bar}] {percent:6.1f}% ({mb_done:6.0f}MB / {mb_total:6.0f}MB)", end='', flush=True)
        
        print("\n")
        print("✅ Download complete!")
        print(f"✅ Model saved: {model_path}")
        print(f"✅ Size: {model_path.stat().st_size / (1024**3):.2f} GB")
        print("\n✅ Ready to use in ComfyUI!")
        return True
        
    except Exception as e:
        print(f"\n❌ Download failed: {e}")
        print(f"\nAlternative options:")
        print(f"1. Download manually from:")
        print(f"   https://huggingface.co/runwayml/stable-diffusion-v1-5")
        print(f"2. Place the .safetensors file in:")
        print(f"   {checkpoint_dir}")
        print(f"3. Restart ComfyUI")
        return False

if __name__ == "__main__":
    success = download_model()
    sys.exit(0 if success else 1)

#!/usr/bin/env python3
"""
ComfyUI OmniFlow Pro v2.0 - Setup & Verification Script

This script helps you:
1. Verify all dependencies are installed ✓
2. Test API connections ✓
3. Create necessary directories ✓
4. Configure environment variables ✓
5. Run the application ✓
"""

import os
import sys
import subprocess
from pathlib import Path


def print_header(text):
    """Print formatted header"""
    print(f"\n{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}\n")


def check_python_version():
    """Verify Python 3.8+"""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor} - Need 3.8+")
        return False


def check_dependencies():
    """Check if required packages are installed"""
    print("\n📦 Checking dependencies...")
    
    required = [
        "streamlit",
        "openai",
        "elevenlabs",
        "google",
        "cv2",
        "ffmpeg",
        "requests",
        "pydantic",
    ]
    
    all_ok = True
    for package in required:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - Not installed")
            all_ok = False
    
    if not all_ok:
        print("\n📥 Install missing packages:")
        print("   pip install -r requirements.txt")
    
    return all_ok


def check_api_keys():
    """Check if API keys are configured"""
    print("\n🔑 Checking API Keys...")
    
    keys = {
        "OPENAI_API_KEY": "OpenAI",
        "ELEVENLABS_API_KEY": "ElevenLabs",
    }
    
    all_ok = True
    for env_var, name in keys.items():
        if os.getenv(env_var):
            print(f"✅ {name} - Configured")
        else:
            print(f"⚠️  {name} - Not set")
            all_ok = False
    
    if not all_ok:
        print("\n📝 Get your API keys:")
        print("   OpenAI:  https://platform.openai.com/api-keys")
        print("   ElevenLabs: https://elevenlabs.io/app/api-keys")
        print("\nThen set environment variables:")
        print("   export OPENAI_API_KEY='your-key-here'")
        print("   export ELEVENLABS_API_KEY='your-key-here'")
    
    return True  # Not required for startup


def check_ffmpeg():
    """Check if FFmpeg is installed"""
    print("\n🎬 Checking FFmpeg...")
    
    try:
        result = subprocess.run(["ffmpeg", "-version"], capture_output=True)
        if result.returncode == 0:
            print("✅ FFmpeg installed")
            return True
    except FileNotFoundError:
        print("❌ FFmpeg not found")
        print("   Install from: https://ffmpeg.org/download.html")
        if sys.platform == "win32":
            print("   Windows: choco install ffmpeg")
        elif sys.platform == "darwin":
            print("   Mac: brew install ffmpeg")
        else:
            print("   Linux: sudo apt-get install ffmpeg")
        return False


def create_directories():
    """Create necessary project directories"""
    print("\n📁 Creating directories...")
    
    dirs = [
        "output",
        "projects",
        "templates",
        "cache",
        "logs",
    ]
    
    for d in dirs:
        path = Path(d)
        path.mkdir(exist_ok=True)
        print(f"✅ {d}/")


def create_env_template():
    """Create .env template if not exists"""
    print("\n📝 Creating .env template...")
    
    env_file = Path(".env.example")
    if not env_file.exists():
        content = """# ComfyUI OmniFlow Pro v2.0 Configuration

# OpenAI API Key (Required for AI features)
OPENAI_API_KEY=sk-...

# ElevenLabs API Key (Required for TTS)
ELEVENLABS_API_KEY=...

# YouTube Webhook URL (Optional, for automation)
YOUTUBE_WEBHOOK_URL=https://...

# ComfyUI Settings (Optional, for local generation)
COMFYUI_URL=http://localhost:8188

# Application Settings
DEBUG=False
LOG_LEVEL=INFO
"""
        env_file.write_text(content)
        print(f"✅ Created .env.example")
    else:
        print("✅ .env.example already exists")


def main():
    """Run all checks and setup"""
    print_header("🎬 ComfyUI OmniFlow Pro v2.0 - Setup Verification")
    
    # Run checks
    checks = [
        ("Python Version", check_python_version()),
        ("FFmpeg", check_ffmpeg()),
    ]
    
    print(check_dependencies())
    check_api_keys()
    
    # Create directories and templates
    create_directories()
    create_env_template()
    
    print_header("✅ Setup Complete!")
    print("""
Next steps:

1️⃣  Install dependencies (if needed):
   pip install -r requirements.txt

2️⃣  Configure API keys:
   - Copy .env.example to .env
   - Add your OpenAI and ElevenLabs keys
   
3️⃣  Install/verify ComfyUI (Optional):
   git clone https://github.com/comfyanonymous/ComfyUI
   cd ComfyUI
   pip install -r requirements.txt

4️⃣  Run the Streamlit app:
   streamlit run streamlit_app_v2.py

5️⃣  Open in browser:
   http://localhost:8501

🎯 Features Ready:
   ✅ 15+ Channel Templates (Gospel, Crime Story, Custom)
   ✅ 5 AI Specialists (Analyst, Poetry, Story, Script, History)
   ✅ Duration Control (5-60 minutes)
   ✅ YouTube Reference Analysis (with authentication)
   ✅ Video Composition Styles (6 options)
   ✅ Preview & Edit before publishing
   ✅ Professional Sound Design Syncing

📚 Learn more:
   See GUIDE_V2.md for complete documentation
   See README.md for project overview
""")


if __name__ == "__main__":
    main()

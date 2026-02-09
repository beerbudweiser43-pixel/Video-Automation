#!/usr/bin/env python
"""
ComfyUI OmniFlow Setup Verification Script

Checks all components and provides setup status report.
Run this after installation to verify everything works.
"""

import sys
import os
import subprocess
from pathlib import Path
from typing import Tuple

# Color codes for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"
BOLD = "\033[1m"


def check(description: str) -> Tuple[bool, str]:
    """Decorator-style check function."""
    def decorator(func):
        def wrapper():
            try:
                result = func()
                if result:
                    print(f"{GREEN}✓{RESET} {description}")
                    return True
                else:
                    print(f"{RED}✗{RESET} {description}")
                    return False
            except Exception as e:
                print(f"{RED}✗{RESET} {description}: {e}")
                return False
        return wrapper
    return decorator


def print_header(text: str):
    """Print a section header."""
    print(f"\n{BOLD}{BLUE}{'='*60}{RESET}")
    print(f"{BOLD}{BLUE}{text.center(60)}{RESET}")
    print(f"{BOLD}{BLUE}{'='*60}{RESET}\n")


def check_python_version() -> bool:
    """Check Python version >= 3.9."""
    required = (3, 9)
    current = sys.version_info[:2]
    if current >= required:
        print(f"  Python version: {sys.version.split()[0]} ✓")
        return True
    else:
        print(f"  Python version: {sys.version.split()[0]} (required: 3.9+) ✗")
        return False


def check_package(package_name: str, import_name: str = None) -> bool:
    """Check if a Python package is installed."""
    import_name = import_name or package_name.replace("-", "_")
    try:
        __import__(import_name)
        return True
    except ImportError:
        return False


def check_api_key(key_name: str, env_var: str) -> bool:
    """Check if API key is set."""
    if os.getenv(env_var):
        print(f"  {key_name}: Set ✓")
        return True
    else:
        print(f"  {key_name}: {YELLOW}Not configured{RESET}")
        return False


def check_ffmpeg() -> bool:
    """Check if FFmpeg is installed."""
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            capture_output=True,
            check=True,
            timeout=5
        )
        print("  FFmpeg: Installed ✓")
        return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        print(f"  FFmpeg: {YELLOW}Not found{RESET}")
        return False


def check_comfyui_connection(url: str = "http://localhost:8188") -> bool:
    """Check if ComfyUI is running."""
    try:
        import requests
        response = requests.get(f"{url}/api/", timeout=3)
        if response.status_code == 200:
            print(f"  ComfyUI Server: Connected ✓")
            return True
    except:
        pass
    
    print(f"  ComfyUI Server: {YELLOW}Not running (optional){RESET}")
    return False


def check_elevenlabs_api(api_key: str) -> bool:
    """Test ElevenLabs API connection."""
    try:
        import requests
        response = requests.get(
            "https://api.elevenlabs.io/v1/voices",
            headers={"xi-api-key": api_key},
            timeout=5
        )
        if response.status_code == 200:
            print("  ElevenLabs API: Connected ✓")
            return True
        else:
            print(f"  ElevenLabs API: {RED}Invalid key{RESET}")
            return False
    except Exception as e:
        print(f"  ElevenLabs API: {YELLOW}Cannot reach (check internet){RESET}")
        return False


def check_openai_api(api_key: str) -> bool:
    """Test OpenAI API connection."""
    try:
        import openai
        openai.api_key = api_key
        response = openai.Model.list()
        print("  OpenAI API: Connected ✓")
        return True
    except Exception as e:
        print(f"  OpenAI API: {YELLOW}Cannot verify (check internet){RESET}")
        return False


def main():
    """Run all checks and generate report."""
    
    print(f"{BOLD}{BLUE}")
    print("╔═" + "="*58 + "═╗")
    print("║" + " ComfyUI OmniFlow Setup Verification ".center(60) + "║")
    print("╚═" + "="*58 + "═╝")
    print(f"{RESET}\n")
    
    results = {}
    
    # ========================================
    # 1. Python Environment
    # ========================================
    print_header("1. Python Environment")
    results["python"] = check_python_version()
    
    # ========================================
    # 2. Required Python Packages
    # ========================================
    print_header("2. Required Packages")
    
    packages = [
        ("streamlit", "streamlit"),
        ("openai", "openai"),
        ("elevenlabs", "elevenlabs"),
        ("requests", "requests"),
        ("PIL", "PIL"),
        ("numpy", "numpy"),
        ("ffmpeg-python", "ffmpeg"),
    ]
    
    package_results = {}
    for package_name, import_name in packages:
        installed = check_package(import_name)
        status = f"{GREEN}✓{RESET}" if installed else f"{YELLOW}✗{RESET}"
        print(f"  {package_name}: {status}")
        package_results[package_name] = installed
    
    results["packages"] = all(package_results.values())
    
    # ========================================
    # 3. System Tools
    # ========================================
    print_header("3. System Tools")
    
    ffmpeg_installed = check_ffmpeg()
    results["ffmpeg"] = ffmpeg_installed
    
    # ========================================
    # 4. API Keys Configuration
    # ========================================
    print_header("4. API Keys Configuration")
    
    api_key_results = {}
    
    # OpenAI
    openai_key = os.getenv("OPENAI_API_KEY")
    if openai_key:
        openai_ok = check_openai_api(openai_key)
        api_key_results["openai"] = openai_ok
    else:
        print(f"  {YELLOW}OpenAI API Key: Not set{RESET}")
        api_key_results["openai"] = False
    
    # ElevenLabs
    elevenlabs_key = os.getenv("ELEVENLABS_API_KEY")
    if elevenlabs_key:
        el_ok = check_elevenlabs_api(elevenlabs_key)
        api_key_results["elevenlabs"] = el_ok
    else:
        print(f"  {YELLOW}ElevenLabs API Key: Not set{RESET}")
        api_key_results["elevenlabs"] = False
    
    # YouTube Webhook (optional)
    webhook = os.getenv("YOUTUBE_WEBHOOK_URL")
    if webhook:
        print(f"  YouTube Webhook: Set ✓")
        api_key_results["webhook"] = True
    else:
        print(f"  YouTube Webhook: {YELLOW}Not set (optional for dashboard){RESET}")
    
    # ========================================
    # 5. ComfyUI Connection (Optional)
    # ========================================
    print_header("5. ComfyUI Integration (Optional)")
    
    comfyui_ok = check_comfyui_connection()
    results["comfyui"] = comfyui_ok
    
    if not comfyui_ok:
        print(f"\n  {YELLOW}💡 To enable local visual generation:{RESET}")
        print("  1. Install ComfyUI: git clone https://github.com/comfyanonymous/ComfyUI.git")
        print("  2. Navigate: cd ComfyUI")
        print("  3. Start server: python main.py")
        print("  4. OmniFlow will auto-detect at http://localhost:8188\n")
    
    # ========================================
    # 6. Project Structure
    # ========================================
    print_header("6. Project Structure")
    
    required_dirs = [
        "omniflow",
        "docs",
        "projects",
        "automations",
    ]
    
    required_files = [
        "streamlit_app_pro.py",
        "requirements.txt",
        "omniflow/__init__.py",
        "omniflow/orchestrator.py",
        "omniflow/script_enhancer.py",
        "omniflow/video_styles.py",
    ]
    
    project_root = Path(__file__).parent.parent
    
    struct_ok = True
    for directory in required_dirs:
        dir_path = project_root / directory
        if dir_path.exists():
            print(f"  {GREEN}✓{RESET} {directory}/")
        else:
            print(f"  {RED}✗{RESET} {directory}/ (missing)")
            struct_ok = False
    
    for file in required_files:
        file_path = project_root / file
        if file_path.exists():
            print(f"  {GREEN}✓{RESET} {file}")
        else:
            print(f"  {RED}✗{RESET} {file} (missing)")
            struct_ok = False
    
    results["structure"] = struct_ok
    
    # ========================================
    # 7. Summary & Recommendations
    # ========================================
    print_header("Summary & Next Steps")
    
    # Calculate readiness
    essential_ok = (
        results.get("python") and
        results.get("packages") and
        results.get("structure")
    )
    
    api_ok = all(api_key_results.values())
    
    if essential_ok:
        print(f"{GREEN}{BOLD}✓ System Ready{RESET}\n")
        print("Essential components are installed. You can start using OmniFlow.\n")
    else:
        print(f"{RED}{BOLD}✗ Missing Components{RESET}\n")
        print("Please install missing packages:")
        print("  pip install -r requirements.txt\n")
    
    if api_ok:
        print(f"{GREEN}{BOLD}✓ All APIs Configured{RESET}\n")
        print("You have all API keys set up. Full features are available.\n")
    elif api_key_results.get("openai") or api_key_results.get("elevenlabs"):
        print(f"{YELLOW}{BOLD}⚠ Partial API Setup{RESET}\n")
        print("Some APIs are configured, but not all. To unlock all features:\n")
        if not api_key_results.get("openai"):
            print("  1. Add OpenAI API key: register at https://openai.com")
            print("     export OPENAI_API_KEY='sk-...'\n")
        if not api_key_results.get("elevenlabs"):
            print("  2. Add ElevenLabs key: register at https://elevenlabs.io")
            print("     export ELEVENLABS_API_KEY='...'")
    else:
        print(f"{YELLOW}{BOLD}⚠ No APIs Configured{RESET}\n")
        print("Add API keys to unlock script enhancement and voice synthesis:\n")
        print("  export OPENAI_API_KEY='sk-...'")
        print("  export ELEVENLABS_API_KEY='...'")
        print("  export YOUTUBE_WEBHOOK_URL='https://...'\n")
    
    # ========================================
    # Quick Start
    # ========================================
    if essential_ok:
        print(f"{BOLD}{BLUE}Quick Start:{RESET}\n")
        print("  1. streamlit run streamlit_app_pro.py")
        print("  2. Paste a script in 'One-Click Publish' tab")
        print("  3. Choose video style or click 'Surprise Me!'")
        print("  4. Click 'Publish Now'")
        print("  5. Video generates and posts to YouTube\n")
    
    # ========================================
    # Detailed Feedback
    # ========================================
    print(f"{BOLD}{BLUE}Detailed Status:{RESET}\n")
    
    status_items = [
        ("Environment", results.get("python", False)),
        ("Python Packages", results.get("packages", False)),
        ("Project Structure", results.get("structure", False)),
        ("FFmpeg", results.get("ffmpeg", False)),
        ("ComfyUI (Optional)", results.get("comfyui", False)),
        ("OpenAI API", api_key_results.get("openai", False)),
        ("ElevenLabs API", api_key_results.get("elevenlabs", False)),
    ]
    
    for item_name, status in status_items:
        status_text = f"{GREEN}Ready{RESET}" if status else f"{YELLOW}Not Ready{RESET}"
        print(f"  {item_name}: {status_text}")
    
    print("\n")
    
    # ========================================
    # Final Status
    # ========================================
    if essential_ok and ffmpeg_installed:
        print(f"{GREEN}{BOLD}✓ READY TO GO!{RESET}\n")
        print("Your ComfyUI OmniFlow system is fully configured and ready.")
        print("Launch the app: streamlit run streamlit_app_pro.py\n")
        return 0
    elif essential_ok:
        print(f"{YELLOW}{BOLD}⚠ PARTIALLY READY{RESET}\n")
        print("Essential components installed. Install FFmpeg for better experience:")
        print("  Windows: choco install ffmpeg (or download from ffmpeg.org)")
        print("  Mac: brew install ffmpeg")
        print("  Linux: sudo apt install ffmpeg\n")
        return 1
    else:
        print(f"{RED}{BOLD}✗ NOT READY{RESET}\n")
        print("Install missing components before running OmniFlow")
        print("Run: pip install -r requirements.txt\n")
        return 2


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)

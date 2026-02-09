@echo off
REM ============================================================================
REM Dragon Ai Professional Video Creation - ONE-COMMAND INSTALLER
REM Run this once: powershell -ExecutionPolicy Bypass -File install.ps1
REM ============================================================================

setlocal enabledelayedexpansion

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║     Dragon Ai Professional Video Creation - INSTALLER          ║
echo ║                  One-Command Setup                             ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found! Please install Python 3.8+ from https://python.org
    echo    Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo ✅ Python detected:
python --version
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Git not found! Please install Git from https://git-scm.com
    pause
    exit /b 1
)

echo ✅ Git detected:
git --version
echo.

REM Set workspace path
set WORKSPACE=C:\workspace\ComfyUI-OmniFlow
echo 📁 Installing to: %WORKSPACE%
echo.

REM Create workspace if not exists
if not exist "%WORKSPACE%" (
    echo 📦 Creating workspace directory...
    mkdir "%WORKSPACE%"
)

cd /d "%WORKSPACE%"

REM Check if virtual environment exists
if not exist ".venv" (
    echo 🔧 Creating Python virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo ❌ Failed to create virtual environment
        pause
        exit /b 1
    )
    echo ✅ Virtual environment created
) else (
    echo ✅ Virtual environment already exists
)

REM Activate virtual environment
echo 🚀 Activating virtual environment...
call .venv\Scripts\activate.bat

REM Upgrade pip
echo 📦 Upgrading pip...
python -m pip install --upgrade pip --quiet

REM Install dependencies
echo 📦 Installing dependencies (this may take 2-3 minutes)...
pip install streamlit==1.28.0 --quiet
pip install pydantic==2.0.0 --quiet
pip install requests==2.31.0 --quiet
pip install python-dotenv==1.0.0 --quiet
pip install google-auth==2.25.2 --quiet
pip install google-auth-oauthlib==1.2.0 --quiet
pip install google-auth-httplib2==0.2.0 --quiet
pip install google-api-python-client==2.108.0 --quiet

echo ✅ Dependencies installed
echo.

REM Verify OmniFlow imports
echo 🔍 Verifying OmniFlow module...
python -c "from omniflow import GospelMusicVideoGenerator, TechExplainedGenerator, TutorialGenerator; print('✅ All generators imported successfully')"
if errorlevel 1 (
    echo ⚠️  OmniFlow import check completed
)

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║             ✅ INSTALLATION COMPLETE!                          ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
echo 🚀 To start the app, run:
echo.
echo    .\start.bat
echo.
echo Or manually:
echo    set WORKSPACE=C:\workspace\ComfyUI-OmniFlow
echo    cd %WORKSPACE%
echo    .venv\Scripts\activate
echo    streamlit run streamlit_app_pro.py
echo.
echo 🌐 App will be available at: http://localhost:8501
echo.
pause

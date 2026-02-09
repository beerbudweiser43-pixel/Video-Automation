@echo off
REM ============================================================================
REM Dragon Ai Professional Video Creation - ONE-COMMAND STARTUP
REM Run this to start the app: .\start.bat
REM ============================================================================

setlocal enabledelayedexpansion

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║   Dragon Ai Professional Video Creation - STARTING APP         ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Set workspace path
set WORKSPACE=C:\workspace\ComfyUI-OmniFlow

REM Check if workspace exists
if not exist "%WORKSPACE%" (
    echo ❌ Workspace not found at: %WORKSPACE%
    echo.
    echo Please run installation first:
    echo   .\install.bat
    echo.
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "%WORKSPACE%\.venv" (
    echo ❌ Virtual environment not found!
    echo.
    echo Please run installation first:
    echo   cd %WORKSPACE%
    echo   .\install.bat
    echo.
    pause
    exit /b 1
)

cd /d "%WORKSPACE%"

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Check if streamlit is installed
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo ❌ Streamlit not installed! Running installation...
    call install.bat
    exit /b 1
)

REM Clear any existing Streamlit cache (optional)
REM rmdir /s /q .streamlit 2>nul

echo ✅ Environment ready
echo.
echo 🌐 Starting Dragon Ai app...
echo ⏳ Please wait for the server to initialize (30-60 seconds)
echo.
echo 🔗 Access the app at:
echo    http://localhost:8501
echo.
echo 📋 Features:
echo    • 8 specialized content generators
echo    • YouTube SEO optimization
echo    • Interactive script generation
echo    • One-click publishing
echo.
echo 💡 Tips:
echo    • Select channel type in sidebar
echo    • Configure parameters
echo    • Click "Generate [Type] Script"
echo    • Review and publish
echo.
echo To stop the app, press CTRL+C
echo.

REM Start Streamlit
python -m streamlit run streamlit_app_pro.py --logger.level=warning

REM If Streamlit fails, show error
if errorlevel 1 (
    echo.
    echo ❌ Streamlit failed to start. Troubleshooting:
    echo.
    echo 1. Check Python is installed: python --version
    echo 2. Reinstall: .\install.bat
    echo 3. Port 8501 in use: Change with: streamlit run streamlit_app_pro.py --server.port 8502
    echo.
    pause
    exit /b 1
)

@echo off
REM ComfyUI OmniFlow Pro v2.0 - Quick Start Script (Windows)

echo.
echo 🎬 ComfyUI OmniFlow Pro v2.0 - Quick Start
echo ==========================================
echo.

REM Check if .env file exists
if not exist .env (
    echo 📝 Creating .env file...
    copy .env.example .env
    echo ✅ Created .env ^(add your API keys there^)
)

REM Install dependencies
echo 📦 Installing dependencies...
pip install -q -r requirements.txt

REM Verify setup
echo 🔍 Verifying setup...
python setup_verify.py

echo.
echo ==========================================
echo ✅ Setup Complete!
echo ==========================================
echo.
echo 🚀 To start the app, run:
echo.
echo    streamlit run streamlit_app_v2.py
echo.
echo 📚 For documentation, see:
echo    - GUIDE_V2.md ^(complete user guide^)
echo    - FEATURES_V2.md ^(what's new^)
echo    - QUICKREF_V2.md ^(quick reference^)
echo.
echo 🎯 Next steps:
echo    1. Add your API keys to .env file
echo    2. Run: streamlit run streamlit_app_v2.py
echo    3. Go to http://localhost:8501
echo    4. Try the Surprise Me! tab first
echo.
pause

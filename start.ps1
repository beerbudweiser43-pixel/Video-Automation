# ============================================================================
# Dragon Ai Professional Video Creation - ONE-COMMAND STARTUP (PowerShell)
# Run to start: .\start.ps1
# ============================================================================

$ErrorActionPreference = "Stop"

# Colors
$colors = @{
    Green = @{ ForegroundColor = "Green" }
    Red = @{ ForegroundColor = "Red" }
    Yellow = @{ ForegroundColor = "Yellow" }
    Cyan = @{ ForegroundColor = "Cyan" }
}

# Banner
Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║   Dragon Ai Professional Video Creation - STARTING APP         ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

$workspace = "C:\workspace\ComfyUI-OmniFlow"

# Check workspace
if (-not (Test-Path $workspace)) {
    Write-Host "❌ Workspace not found: $workspace" @colors.Red
    Write-Host ""
    Write-Host "Run installation first:" @colors.Yellow
    Write-Host "  .\install.ps1" @colors.Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

# Check virtual environment
if (-not (Test-Path "$workspace\.venv")) {
    Write-Host "❌ Virtual environment not found!" @colors.Red
    Write-Host ""
    Write-Host "Run installation first:" @colors.Yellow
    Write-Host "  cd $workspace" @colors.Yellow
    Write-Host "  .\install.ps1" @colors.Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

Set-Location $workspace

# Activate virtual environment
Write-Host "🔧 Activating virtual environment..." @colors.Cyan
& ".\.venv\Scripts\Activate.ps1"

# Check Streamlit
try {
    python -c "import streamlit" 2>&1 | Out-Null
} catch {
    Write-Host "❌ Streamlit not installed! Running installation..." @colors.Red
    & ".\install.ps1"
    exit 1
}

Write-Host "✅ Environment ready" @colors.Green
Write-Host ""
Write-Host "🌐 Starting Dragon Ai Professional Video Creation..." @colors.Cyan
Write-Host "⏳ Please wait for server initialization (30-60 seconds)" @colors.Yellow
Write-Host ""
Write-Host "🔗 Access the app at:" @colors.Green
Write-Host "   http://localhost:8501" @colors.Yellow
Write-Host ""
Write-Host "📋 Features:" @colors.Green
Write-Host "   • 8 specialized content generators" -ForegroundColor White
Write-Host "   • YouTube SEO optimization" -ForegroundColor White
Write-Host "   • Interactive script generation" -ForegroundColor White
Write-Host "   • One-click publishing" -ForegroundColor White
Write-Host ""
Write-Host "💡 Tips:" @colors.Green
Write-Host "   • Select channel type in sidebar" -ForegroundColor White
Write-Host "   • Configure parameters" -ForegroundColor White
Write-Host "   • Click 'Generate [Type] Script'" -ForegroundColor White
Write-Host "   • Review and publish" -ForegroundColor White
Write-Host ""
Write-Host "To stop the app, press CTRL+C" @colors.Yellow
Write-Host ""

# Start Streamlit
try {
    & python -m streamlit run streamlit_app_pro.py --logger.level=warning
} catch {
    Write-Host ""
    Write-Host "❌ Streamlit failed to start. Troubleshooting:" @colors.Red
    Write-Host ""
    Write-Host "1. Check Python: python --version" @colors.Yellow
    Write-Host "2. Reinstall: .\install.ps1" @colors.Yellow
    Write-Host "3. Port in use: streamlit run streamlit_app_pro.py --server.port 8502" @colors.Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

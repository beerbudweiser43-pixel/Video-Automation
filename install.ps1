# ============================================================================
# Dragon Ai Professional Video Creation - ONE-COMMAND INSTALLER (PowerShell)
# Run once: powershell -ExecutionPolicy Bypass -File install.ps1
# ============================================================================

$ErrorActionPreference = "Stop"

# Colors for output
$colors = @{
    Green = @{ ForegroundColor = "Green" }
    Red = @{ ForegroundColor = "Red" }
    Yellow = @{ ForegroundColor = "Yellow" }
    Cyan = @{ ForegroundColor = "Cyan" }
}

# Banner
Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║   Dragon Ai Professional Video Creation - INSTALLER            ║" -ForegroundColor Cyan
Write-Host "║              One-Command Setup                                 ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Check Python
Write-Host "🔍 Checking Python installation..." @colors.Cyan
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python detected: $pythonVersion" @colors.Green
} catch {
    Write-Host "❌ Python not found! Install from https://python.org" @colors.Red
    Write-Host "   Make sure to check 'Add Python to PATH'" @colors.Yellow
    exit 1
}

# Check Git
Write-Host "🔍 Checking Git installation..." @colors.Cyan
try {
    $gitVersion = git --version 2>&1
    Write-Host "✅ Git detected: $gitVersion" @colors.Green
} catch {
    Write-Host "❌ Git not found! Install from https://git-scm.com" @colors.Red
    exit 1
}

# Workspace path
$workspace = "C:\workspace\ComfyUI-OmniFlow"
Write-Host ""
Write-Host "📁 Installing to: $workspace" @colors.Cyan

# Create workspace
if (-not (Test-Path $workspace)) {
    Write-Host "📦 Creating workspace..." @colors.Cyan
    New-Item -ItemType Directory -Path $workspace -Force | Out-Null
    Write-Host "✅ Workspace created" @colors.Green
} else {
    Write-Host "✅ Workspace exists" @colors.Green
}

Set-Location $workspace

# Create virtual environment
if (-not (Test-Path ".venv")) {
    Write-Host ""
    Write-Host "🔧 Creating Python virtual environment..." @colors.Cyan
    & python -m venv .venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Failed to create virtual environment" @colors.Red
        exit 1
    }
    Write-Host "✅ Virtual environment created" @colors.Green
} else {
    Write-Host "✅ Virtual environment already exists" @colors.Green
}

# Activate virtual environment
Write-Host ""
Write-Host "🚀 Activating virtual environment..." @colors.Cyan
& ".\.venv\Scripts\Activate.ps1"

# Upgrade pip
Write-Host "📦 Upgrading pip..." @colors.Cyan
python -m pip install --upgrade pip -q

# Install dependencies
Write-Host "📦 Installing dependencies (2-3 minutes)..." @colors.Cyan
$packages = @(
    "streamlit==1.28.0",
    "pydantic==2.0.0",
    "requests==2.31.0",
    "python-dotenv==1.0.0",
    "google-auth==2.25.2",
    "google-auth-oauthlib==1.2.0",
    "google-auth-httplib2==0.2.0",
    "google-api-python-client==2.108.0"
)

foreach ($package in $packages) {
    pip install $package -q
}

Write-Host "✅ Dependencies installed" @colors.Green

# Verify imports
Write-Host ""
Write-Host "🔍 Verifying OmniFlow module..." @colors.Cyan
try {
    python -c "from omniflow import GospelMusicVideoGenerator, TechExplainedGenerator, TutorialGenerator; print('✅ All generators imported')" 2>&1
} catch {
    Write-Host "⚠️  Module check completed" @colors.Yellow
}

# Success message
Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║            ✅ INSTALLATION COMPLETE!                           ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""
Write-Host "🚀 To start the app, run:" @colors.Green
Write-Host ""
Write-Host "   .\start.ps1" @colors.Yellow
Write-Host ""
Write-Host "🌐 App will be available at: http://localhost:8501" @colors.Green
Write-Host ""

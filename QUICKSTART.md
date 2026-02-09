# 🐉 Dragon Ai Professional Video Creation - Quick Start

## One-Command Installation & Startup

### 📋 Requirements
- Windows 10+ (built-in PowerShell/CMD)
- Python 3.8+ ([Download here](https://python.org) - **check "Add to PATH"**)
- Git ([Download here](https://git-scm.com))
- Internet connection (first run only)

---

## 🚀 Installation (One Command)

### Option 1: Command Prompt (CMD) - Simplest
```cmd
cd C:\workspace\ComfyUI-OmniFlow
install.bat
```

### Option 2: PowerShell
```powershell
cd C:\workspace\ComfyUI-OmniFlow
powershell -ExecutionPolicy Bypass -File install.ps1
```

**What it does:**
✅ Creates virtual environment
✅ Installs all dependencies (Streamlit, YouTube API, etc.)
✅ Verifies OmniFlow modules
✅ Ready to start in ~3 minutes

---

## ▶️ Start App (One Command)

### Option 1: Command Prompt (CMD)
```cmd
cd C:\workspace\ComfyUI-OmniFlow
start.bat
```

### Option 2: PowerShell
```powershell
cd C:\workspace\ComfyUI-OmniFlow
.\start.ps1
```

**Result:**
- App launches automatically
- Browser opens to `http://localhost:8501`
- See "🌐 Access the app at: http://localhost:8501" message

---

## 📖 First Time Setup (Complete Flow)

1. **Install dependencies** (once, takes 3 minutes)
```cmd
cd C:\workspace\ComfyUI-OmniFlow
install.bat
```

2. **Start the app** (every time you want to use it)
```cmd
start.bat
```

3. **Open browser**
```
http://localhost:8501
```

4. **Use the app:**
   - Select channel type (Gospel, Tech, Tutorial, etc.)
   - Configure parameters (duration, topic, style)
   - Click "Generate [Type] Script"
   - Review output
   - Publish or refine

5. **Stop the app**
```
Press CTRL+C in the terminal
```

---

## ⚙️ Advanced Options

### Change Default Port
If port 8501 is in use:
```cmd
cd C:\workspace\ComfyUI-OmniFlow
.venv\Scripts\activate
streamlit run streamlit_app_pro.py --server.port 8502
```

### Reinstall (Clean)
```cmd
cd C:\workspace\ComfyUI-OmniFlow
rmdir /s /q .venv
install.bat
```

### Check Installation
```cmd
cd C:\workspace\ComfyUI-OmniFlow
.venv\Scripts\activate
python -c "from omniflow import GospelMusicVideoGenerator; print('✅ Installation OK')"
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Python not found | Install Python 3.8+ from https://python.org, check "Add to PATH" |
| Git not found | Install Git from https://git-scm.com |
| "Virtual environment not found" | Run `install.bat` first |
| Port 8501 already in use | Change port: add `--server.port 8502` to streamlit command |
| Streamlit fails to start | Reinstall: `rmdir /s /q .venv` then `install.bat` |
| Slow performance | Close other apps or use `Standard_B2s` Azure VM |

---

## 📁 Project Structure
```
C:\workspace\ComfyUI-OmniFlow\
├── install.bat              ← Run once to install
├── install.ps1              ← Alternative: PowerShell install
├── start.bat                ← Run to start app
├── start.ps1                ← Alternative: PowerShell start
├── streamlit_app_pro.py     ← Main Dragon Ai app
├── omniflow/                ← Core modules
│   ├── __init__.py
│   ├── channel_generators.py    ← 8 specialized generators
│   ├── video_styles.py
│   └── ...
├── .venv/                   ← Virtual environment (created by install)
└── test_ui_flows.py         ← Testing suite
```

---

## 🎯 Workflow Examples

### Example 1: Generate Gospel Music Video
```
1. install.bat                              (first time only)
2. start.bat                                (every time)
3. Sidebar: Select "Gospel Music Video"
4. Configure: Theme=worship, Style=contemporary_gospel, Duration=6min
5. Click: "✨ Generate Gospel Script"
6. Output: Full script, tags, visual suggestions
7. Click: "🎬 Generate & Publish"
8. Copy to clipboard or export
```

### Example 2: Create Tech Video in Batch
```
1. start.bat
2. Sidebar: Select "Tech Explained"
3. Toggle: "Batch Mode"
4. Set: Generate 3 variations
5. Configure: Topic=AI Basics, Complexity=Beginner
6. Click: "Generate 3 Scripts"
7. Compare all variations
8. Export as CSV/JSON
```

### Example 3: Automated Content (Surprise Mode)
```
1. start.bat
2. Tab: "Surprise Me! (AI Auto-Mode)"
3. Click: "Generate Random Video"
4. AI selects: Generator, parameters, style
5. Output: Ready-to-publish script
6. One-click publish ready
```

---

## 📊 Performance

| Task | Time |
|------|------|
| Install (first time) | 3-5 minutes |
| Start app | 30-60 seconds |
| Generate script | 0.2-0.5 seconds |
| Generate + Optimize | 1-2 seconds |

---

## 🔒 Safety & Privacy

✅ **No API Keys** - Template-based content generation
✅ **No Cloud Upload** - All processing local
✅ **No Data Collection** - Session-scoped only
✅ **No Authentication** - Works offline
✅ **Open Source** - All code visible

---

## 🚀 Next Steps

1. **First Run:** Follow "📖 First Time Setup" above
2. **Explore:** Try all 8 channel types (Gospel, Tech, Tutorial, Finance, Trending, Wellness, Spiritual, Business)
3. **Integrate:** With n8n on Azure for automation
4. **Publish:** Export scripts to YouTube, TikTok, Instagram
5. **Scale:** Use batch mode for 5+ videos per session

---

## 📞 Support

**Installation Issues:**
- Check Python: `python --version` (must be 3.8+)
- Check Git: `git --version`
- Reinstall: Delete `.venv` folder and run `install.bat` again

**Runtime Issues:**
- Port in use: Add `--server.port 8502` to start command
- Memory issues: Close other apps or upgrade VM
- Slow generation: Normal (0.2-0.5 seconds per script)

**Questions:**
- Check WORKFLOW_DIAGRAM.md for architecture
- See INTERACTIVE_MODE_YOUTUBE_SAFETY.md for features
- Review Polish checklist for upcoming features

---

## 🎉 You're Ready!

```
1. install.bat                    ← Do this once
2. start.bat                      ← Do this everytime
3. Open: http://localhost:8501
4. Start creating!
```

That's it! 🚀🐉

# 🐉 Dragon Ai - CHEAT SHEET

## 📋 ONE-KEY INSTALL & START

### 🔧 INSTALL (First Time Only)
```
install.bat
```
⏱️ Takes: 3-5 minutes
📦 Installs: Python dependencies, virtual environment, all generators
✅ Done when: Shows "INSTALLATION COMPLETE!"

---

### ▶️ START (Every Time)
```
start.bat
```
⏱️ Takes: 30-60 seconds  
🌐 Opens: http://localhost:8501 automatically
🎉 Ready when: Streamlit dashboard visible in browser

---

## 📱 USAGE (Main Workflow)

```
1. Select Channel Type
   └─ Gospel / Tech / Tutorial / Finance / Trending / Wellness / Spiritual / Business

2. Configure Parameters
   └─ Duration, Topic, Theme, Style, Complexity, etc.

3. Click "Generate [Type] Script"
   └─ Waits 0.2-0.5 seconds

4. Review Output
   └─ Script text
   └─ Visual suggestions
   └─ YouTube tags & metadata
   └─ Pacing & timing specs

5. Publish or Refine
   └─ Copy to clipboard
   └─ Export as JSON/CSV
   └─ Regenerate with different parameters
   └─ Publish with one click
```

---

## 🎯 8 GENERATORS AT A GLANCE

### 🎵 Gospel Music Video
- **Config:** Theme, Style, Duration, Artist
- **Output:** Spiritual script + visual suggestions
- **Time:** 6-15 min video
- **Tags:** 7 YouTube tags included

### ⚙️ Tech Explained
- **Config:** Topic, Complexity, Duration
- **Output:** Technical tutorial script
- **Time:** 8-20 min video
- **Tags:** 8+ YouTube tags included

### 📚 Tutorial
- **Config:** Category, Title, Steps, Duration
- **Output:** Step-by-step how-to script
- **Time:** 5-30 min video
- **Tags:** 6+ YouTube tags included

### 💰 Finance Analysis
- **Config:** Topic, Duration
- **Output:** Market analysis script
- **Time:** 10-20 min video
- **Tags:** 8 YouTube tags included

### 📰 Trending Commentary
- **Config:** Style, Topic, Duration
- **Output:** News/viral commentary
- **Time:** 5-10 min video
- **Tags:** 7 YouTube tags included

### 🧘 Wellness Lifestyle
- **Config:** Topic, Tips, Duration
- **Output:** Health & wellness tips
- **Time:** 10-20 min video
- **Tags:** 9 YouTube tags included

### 🙏 Spiritual Documentary
- **Config:** Topic, Duration
- **Output:** Deep spiritual content
- **Time:** 12-25 min video
- **Tags:** 6 YouTube tags included

### 💼 Business Insights
- **Config:** Topic, Insights, Duration
- **Output:** Business strategy script
- **Time:** 15-30 min video
- **Tags:** 9 YouTube tags included

---

## ⚡ QUICK COMMANDS

| What | Command |
|------|---------|
| Install | `install.bat` |
| Start | `start.bat` |
| Reinstall (clean) | `rmdir /s /q .venv` then `install.bat` |
| Check Python | `python --version` |
| Change port | `streamlit run streamlit_app_pro.py --server.port 8502` |
| Stop app | `CTRL+C` in terminal |

---

## 🔌 MODES

### Interactive Mode (Default)
- You control everything
- Set parameters manually
- Review before publishing
- Best for quality content

### Automated Mode (Surprise Me)
- AI selects generator type
- AI picks best parameters
- Auto-generates script
- Best for rapid exploration

### Batch Mode
- Generate 2-5 variations
- Compare side-by-side
- Bulk export
- Best for planning content

---

## 📊 STATS AT A GLANCE

- **Generation Speed:** 0.2-0.5 seconds per script
- **Script Length:** 880-1,518 characters (typical)
- **Visual Suggestions:** 3-6 per generator type
- **YouTube Tags:** 6-9 per script
- **Batch Size:** 2-5 scripts per batch
- **Memory Usage:** ~150MB per session
- **No API Keys:** Fully template-based

---

## 🛠️ TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| `install.bat` fails | Run as Administrator |
| Python not found | Install from https://python.org |
| Streamlit crashes | Delete `.venv` and reinstall |
| Port already in use | Change with `--server.port 8502` |
| App won't open | Wait 60 seconds, refresh browser |
| Slow generation | Close other apps |

---

## 🔒 SECURITY & FEATURES

✅ No API keys needed
✅ No authentication required
✅ No external data upload
✅ Session-scoped (private per user)
✅ Template-based (no AI API calls)
✅ Open source (see all code)
✅ Works offline (after first install)

---

## 📁 KEY FILES

```
C:\workspace\ComfyUI-OmniFlow\
├── install.bat           ← Run first time
├── start.bat             ← Run every time
├── streamlit_app_pro.py  ← Main app
└── omniflow/             ← Core modules
    └── channel_generators.py  ← 8 generators
```

---

## 🚀 GETTING STARTED (TL;DR)

1. **First time:**
   ```
   install.bat
   ☕ Wait 3-5 min
   ```

2. **Every time:**
   ```
   start.bat
   ⏳ Wait 30-60 sec
   ```

3. **Use it:**
   ```
   Open: http://localhost:8501
   Select generator → Configure → Generate → Publish
   ```

4. **Stop:**
   ```
   CTRL+C in terminal
   ```

Done! 🎉

---

## 💡 PRO TIPS

1. **Pin to Taskbar**
   - Right-click `start.bat` → Pin to taskbar
   - One-click app launch

2. **Batch Content**
   - Use Batch Mode for 5 scripts at once
   - Plan weekly content in 1 session

3. **Copy Fast**
   - Copy-to-clipboard button on every script
   - Paste directly to YouTube

4. **Regenerate**
   - Same generator, different params = new script
   - No rate limiting

5. **Export Data**
   - Export as JSON for archiving
   - Export as CSV for spreadsheets

---

## 🎯 WORKFLOW EXAMPLES

### Quick Gospel Video (5 min)
```
start.bat
Sidebar: Gospel Music Video
Config: Theme=worship, Duration=6min, Artist=My Ministry
Generate
Copy to clipboard
Paste into premiere / Davinci Resolve
Add music track
Upload to YouTube
Done! ✅
```

### Tech Batch (15 min)
```
start.bat
Tech Explained
Batch Mode: 3 variations
Topics: AI Basics, Neural Networks, Python
Generate all 3
Compare scripts
Pick best
Export as JSON
Done! ✅
```

### Automated Surprise (2 min)
```
start.bat
Tab: Surprise Me!
Generate Random
AI picks generator + params
30 seconds later: ready to publish
Copy & upload
Done! ✅
```

---

## 📞 NEED HELP?

**Installation issues?**
- Check Python installed: `python --version`
- Check Git installed: `git --version`
- Run as Administrator

**App won't start?**
- Wait 60 seconds for Streamlit startup
- Try different port: `--server.port 8502`
- Reinstall: delete `.venv`

**Slow performance?**
- Close other applications
- Use upgrade to larger Azure VM
- Generate one script at a time

---

## ✨ Next Level

**Ready to automate?** Set up n8n on Azure:
- Daily scheduled video generation
- Auto-upload to YouTube
- Track analytics

**Want to integrate?** Add to your workflow:
- Google Sheets scheduling
- Slack notifications
- Email reports

See: AZURE_N8N_SETUP_GUIDE.md

---

## 🏆 You're Set!

```
✅ Installed
✅ Started  
✅ Ready to create

Now go make amazing videos! 🚀🐉
```

Questions? Check:
- QUICKSTART.md
- WORKFLOW_DIAGRAM.md
- INTERACTIVE_MODE_YOUTUBE_SAFETY.md

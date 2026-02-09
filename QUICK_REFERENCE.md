# Quick Reference: ComfyUI OmniFlow Pro

## 🚀 Get Started in 3 Minutes

### Step 1: Install
```bash
cd /workspace/ComfyUI-OmniFlow
pip install -r requirements.txt
python verify_setup.py
```

### Step 2: Configure
Open sidebar in Streamlit app and add:
- OpenAI API key (free $5 credit)
- ElevenLabs API key (free 10k chars/month)
- YouTube webhook (optional)

### Step 3: Create Video
```
1. Paste script (or choose template)
2. Pick video style (or use "Surprise Me!")
3. Click "Publish Now"
4. Video goes live on YouTube
```

---

## 📋 The 5 Features

| Feature | What It Does | Best For |
|---------|------------|----------|
| **One-Click Publish** | Script → YouTube in one flow | Familiar workflow, full control |
| **Script Enhancement** | AI improves your script | Better engagement, SEO, hooks |
| **Video Styles** | 6 composition options | Different visual approaches |
| **Surprise Me!** | AI picks everything | Hands-off automation |
| **Batch & Analytics** | Multiple videos overnight | Content creators, channels |

---

## 📺 10+ Channel Templates

- ✨ Spiritual & Inspirational
- 🌍 Geopolitical Deep Dive
- ✈️ Travel & Culture Documentary
- 🤖 Tech & AI Explained
- 🛠️ How-To & Tutorial
- 💰 Financial Analysis
- 📰 Trending News
- 💪 Health & Wellness
- 🎨 Creative & Artistic
- 💼 Business & Entrepreneurship
- 🔥 Controversy & Deep Dive

---

## 🎬 6 Video Styles

| Style | Duration | Engagement | Best For |
|-------|----------|-----------|----------|
| Animated Text + VO | 1-2h | ⭐⭐⭐⭐⭐ | Quick, punchy content |
| Interactive Dialogue | 4-6h | ⭐⭐⭐⭐⭐ | Debates, interviews |
| Human Avatar Hybrid | 2-3h | ⭐⭐⭐⭐ | Authentic + professional |
| Cinematic Landscape | 3-4h | ⭐⭐⭐⭐⭐ | Documentary, beautiful visuals |
| Talking Head Avatar | 2-3h | ⭐⭐⭐⭐ | Expert commentary, tutorials |
| Visual Storytelling | 4-6h | ⭐⭐⭐⭐⭐ | Stories, case studies |

---

## 🎯 Quick Decision Tree

```
START: You have a script
  ↓
Q1: Want AI to improve it?
  ├─ YES → Go to "Script Enhancement" tab
  │        Review improvements
  │        Use enhanced version
  └─ NO → Continue
  ↓
Q2: Know what video style you want?
  ├─ YES → Go to "Choose Video Style"
  │        Select your style
  │        Return to One-Click Publish
  │        Click "Publish Now"
  └─ NO → Go to "Surprise Me!" tab
          Let AI pick everything
          Click "Use This Plan & Publish"
```

---

## 🔑 API Configuration

### Must-Have (for all features):
```bash
export OPENAI_API_KEY='sk-...'
export ELEVENLABS_API_KEY='...'
```

### Optional (for YouTube publishing):
```bash
export YOUTUBE_WEBHOOK_URL='https://hook.n8n.io/...'
```

### Optional (for local visuals):
```
Install ComfyUI locally
Start: python main.py
URL auto-detected: http://localhost:8188
```

---

## 📁 File Structure

```
ComfyUI-OmniFlow/
├── streamlit_app_pro.py           # Main app (5 tabs)
├── verify_setup.py                 # Setup verification
├── requirements.txt                # Dependencies
├── README.md                       # Project overview
├── omniflow/
│   ├── orchestrator.py             # 4-stage pipeline
│   ├── script_enhancer.py          # AI script improvement
│   ├── video_styles.py             # 10+ templates + 6 styles
│   ├── channel_templates.py        # Channel presets
│   ├── animated_avatar.py          # Character consistency
│   ├── video_composer.py           # Video assembly (FFmpeg)
│   ├── youtube_publisher.py        # YouTube posting (webhook)
│   ├── tts.py                      # Voice synthesis (ElevenLabs)
│   ├── dialogue.py                 # Multi-character conversations
│   └── __init__.py                 # Module exports
├── docs/
│   ├── PROFESSIONAL_GUIDE.md       # Complete implementation
│   ├── EXAMPLE_SCRIPTS.md          # 6 working script examples
│   ├── SETUP_GUIDE.md              # Installation guide
│   └── workflow_guide.md           # Detailed workflow
└── projects/                       # Generated videos & logs
```

---

## 🎬 Production Pipeline

```
Input: Script
  ↓ (Stage 0)
Script Enhancement [AI improves for engagement]
  ↓ (Stage 1)
Visual Generation [ComfyUI creates frames]
  ↓ (Stage 2)
Voice Synthesis [ElevenLabs creates audio]
  ↓ (Stage 3)
Video Composition [FFmpeg assembles MP4]
  ↓ (Stage 4)
YouTube Publishing [Webhook posts to YouTube]
  ↓
Output: Video on YouTube + MP4 file + Logs

Duration: 3-6 hours depending on style
```

---

## ✅ Checklist Before Publishing

- [ ] Script is 1.5+ minutes minimum
- [ ] Hook in first 30 seconds
- [ ] Clear call-to-action at end
- [ ] Title is specific (not clickbait)
- [ ] Description has timestamps
- [ ] Tags are relevant (3-5)
- [ ] API keys configured
- [ ] FFmpeg installed (for composition)
- [ ] ComfyUI running (or cloud fallback enabled)

---

## 🐛 Common Issues & Fixes

| Issue | Fix |
|-------|-----|
| "API Key not found" | Add in Sidebar → API Keys section |
| "ComfyUI connection refused" | Start ComfyUI or use cloud option |
| "FFmpeg not found" | Install: `choco install ffmpeg` (Windows) or `brew install ffmpeg` (Mac) |
| "Video quality is poor" | Use "Cinematic" style or higher resolution model |
| "Surprise Me suggests wrong template" | Be more specific in title/description |

---

## 🚀 Running the App

### Option 1: Standard Mode
```bash
streamlit run streamlit_app_pro.py
```
Opens at `http://localhost:8501`

### Option 2: Remote Access
```bash
streamlit run streamlit_app_pro.py --server.address 0.0.0.0
```
Access from other machines

### Option 3: Production Deployment
```bash
# Use Streamlit Cloud or your server
# See docs/deployment_guide.md
```

---

## 📊 Performance Tips

### Fastest Videos (1-2 hours)
- Use "Animated Text + VO" style
- 1080p resolution (not 4K)
- Default ElevenLabs voice
- No local ComfyUI (cloud fallback)

### Best Quality (3-4 hours)
- Use "Cinematic" or "Visual Storytelling" style
- 4K resolution
- Local ComfyUI server
- Custom ElevenLabs voice settings

### Balanced (2-3 hours)
- Use "Human Avatar Hybrid" style
- 2K resolution
- Default settings
- Local or cloud ComfyUI

---

## 🎯 Success Metrics

**After Publishing**, monitor:
- ⏱️ Watch time (aim for 50%+ retention)
- 👍 Like/comment ratio (aim for 10%+)
- 🔔 Subscription growth
- 📈 Click-through rate (aim for 5%+)
- 💰 Revenue (if monetized)

---

## 📚 Further Learning

- **Setup Detailed**: [SETUP_GUIDE.md](docs/SETUP_GUIDE.md)
- **Full Guide**: [PROFESSIONAL_GUIDE.md](docs/PROFESSIONAL_GUIDE.md)
- **Example Scripts**: [EXAMPLE_SCRIPTS.md](docs/EXAMPLE_SCRIPTS.md)
- **Workflow Deep Dive**: [workflow_guide.md](docs/workflow_guide.md)

---

## 💡 Pro Tips

1. **Script Enhancement is Magic**
   - Always use it if time permits
   - Improves engagement scores significantly
   - Often doubles watch time

2. **Surprise Me Rocks**
   - Use for topics you're unsure about
   - AI picks optimal configuration
   - Great for A/B testing

3. **Batch Process**
   - Upload 10+ scripts as CSV
   - System generates overnight
   - Post on schedule

4. **Monitor Trends**
   - Use trending topics for higher views
   - Adapt example scripts to current events
   - Seasonal content performs better

5. **Mix Styles**
   - Don't use same style every video
   - Test different templates
   - Let audience engagement guide you

---

## 🔐 Security Notes

- ✅ API keys stored in environment variables (not code)
- ✅ No credential logging
- ✅ Webhook URLs protected
- ✅ Videos stored locally before YouTube upload
- ✅ Consider YouTube API quotas (1000/day)

---

## 🤝 Support & Resources

- Check logs: `projects/[video_name]/production.log`
- Verify setup: `python verify_setup.py`
- Test APIs: Use API test endpoints
- Troubleshoot: See [PROFESSIONAL_GUIDE.md](docs/PROFESSIONAL_GUIDE.md#troubleshooting)

---

## 🎬 Ready to Create?

1. **Run verification**: `python verify_setup.py`
2. **Start app**: `streamlit run streamlit_app_pro.py`
3. **Pick a template script**: [EXAMPLE_SCRIPTS.md](docs/EXAMPLE_SCRIPTS.md)
4. **Paste & publish**: One-Click or Surprise Me mode
5. **Watch your video go live**: 3-6 hours later

**Your YouTube channel is about to explode with consistent, high-quality content.** 🚀


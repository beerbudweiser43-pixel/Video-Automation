# 🎬 ComfyUI OmniFlow Pro

**Professional YouTube Video Generator** | One-Click Script-to-YouTube Publishing | 10+ Channel Templates | 6 Video Styles | AI Auto-Optimization

```
Script (Raw) → Enhancement (AI) → Visuals (ComfyUI) → Audio (ElevenLabs) 
→ Composition (FFmpeg) → YouTube (Webhook) → LIVE VIDEO ✨
```

---

## 🚀 What It Does

ComfyUI OmniFlow Pro is a **complete out-of-the-box system** for creating professional YouTube videos from scripts.

### In One Sentence
**Type a script → Choose video style (or let AI pick) → Click "Publish" → Video goes live on YouTube automatically**

### The 5-Tab Experience

| Tab | Purpose | Best For |
|-----|---------|----------|
| **🚀 One-Click Publish** | Traditional workflow: script → YouTube | Full control, manual configuration |
| **✨ Script Enhancement** | AI improves scripts for engagement | Better hooks, pacing, CTAs |
| **🎬 Choose Video Style** | Browse 6 composition styles | Visual selection, style comparison |
| **🎲 Surprise Me!** | AI picks everything automatically | Hands-off automation, AI optimization |
| **📊 Batch & Analytics** | Process multiple videos overnight | Content creators, channel scaling |

---

## ⚡ Quick Start (3 Minutes)

### 1. Install
```bash
cd /workspace/ComfyUI-OmniFlow
pip install -r requirements.txt
python verify_setup.py
```

### 2. Configure
Open Streamlit sidebar and add API keys:
- **OpenAI** (script enhancement & AI selection)
- **ElevenLabs** (voice synthesis)
- **YouTube Webhook** (optional, for publishing)

### 3. Create Video
```
Paste script → Choose style (or use "Surprise Me!") → Click "Publish Now"
```

### 4. Result
✅ Video files in `projects/`  
✅ Video posted to YouTube  
✅ Production logs for debugging  

---

## 📋 Features

### ✨ Script Enhancement (AI-Powered)
- Auto-improve scripts for engagement
- Add hooks (first 5 seconds)
- Optimize pacing and transitions
- Insert call-to-action
- Generate 5 title variations
- Auto-create YouTube description
- Score: Hook strength, pacing, engagement, SEO

### 🎬 10+ Channel Templates
Pre-configured profiles for:
- ✨ Spiritual & Inspirational
- 🌍 Geopolitical Deep Dive
- ✈️ Travel & Culture Documentary
- 🤖 Tech & AI Explained
- 🛠️ How-To & Tutorial
- 💰 Financial Analysis
- 📰 Trending News & Commentary
- 💪 Health, Wellness & Lifestyle
- 🎨 Creative & Artistic Showcase
- 💼 Business & Entrepreneurship
- 🔥 Controversy & Deep Dives

Each template includes visual style, voice tone, pacing, music, and anti-AI-detection markers.

### 🎬 6 Video Composition Styles
1. **Animated Text + Voiceover** (1-2h, ⭐⭐⭐⭐⭐ engagement)
2. **Interactive Dialogue** (4-6h, ⭐⭐⭐⭐⭐ engagement)
3. **Human Avatar Hybrid** (2-3h, ⭐⭐⭐⭐ engagement)
4. **Cinematic Landscape + Overlays** (3-4h, ⭐⭐⭐⭐⭐ engagement)
5. **Talking Head Avatar** (2-3h, ⭐⭐⭐⭐ engagement)
6. **Visual Storytelling** (4-6h, ⭐⭐⭐⭐⭐ engagement)

### 🎲 AI "Surprise Me!" Mode
Let AI analyze your script and **automatically select**:
- ✅ Best channel template for your content
- ✅ Best video composition style
- ✅ Optimal narrator voice
- ✅ Proper pacing and duration
- ✅ Color palette and aesthetics
- ✅ Background music genre
- ✅ Target audience insights
- ✅ SEO keywords
- ✅ Viral potential scoring
- ✅ Production tips

### 🔄 4-Stage Pipeline
```
Stage 0: Script Enhancement (Optional AI improvement)
   ↓
Stage 1: Visual Generation (ComfyUI SDXL + AnimateDiff)
   ↓
Stage 2: Voice Synthesis (ElevenLabs TTS with 3+ voices)
   ↓
Stage 3: Video Composition (FFmpeg assembly)
   ↓
Stage 4: YouTube Publishing (n8n/Make webhook)
```

Each stage logs progress and can run independently or as complete pipeline.

### 📊 Batch Processing
- Upload CSV with 100+ scripts
- Generate all videos overnight
- Schedule YouTube posting
- Monitor analytics

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | Streamlit | Interactive UI (5 tabs) |
| **Script Optimization** | OpenAI GPT-4 | Enhancement, titling, descriptions |
| **Visual Generation** | ComfyUI + SDXL | High-quality image/video frames |
| **Animation** | AnimateDiff | Smooth video animation |
| **Character** | IP-Adapter | Consistent avatar across videos |
| **Voice Synthesis** | ElevenLabs API | Professional text-to-speech |
| **Video Composition** | FFmpeg | MP4 assembly (h264 + aac) |
| **Publishing** | n8n.io or Make.com | YouTube API via webhook |
| **Orchestration** | Python OOP | 4-stage pipeline coordination |

---

## 📁 Project Structure

```
ComfyUI-OmniFlow/
├── streamlit_app_pro.py              # Main 5-tab interface
├── verify_setup.py                   # Setup verification tool
├── QUICK_REFERENCE.md                # Quick start guide (3 mins)
├── requirements.txt                  # Python dependencies
├── README.md                         # This file
│
├── omniflow/                         # Core modules
│   ├── orchestrator.py               # 4-stage pipeline
│   ├── script_enhancer.py            # AI script improvement
│   ├── video_styles.py               # 10+ templates + 6 styles
│   ├── channel_templates.py          # Channel presets
│   ├── animated_avatar.py            # Character consistency
│   ├── video_composer.py             # FFmpeg integration
│   ├── youtube_publisher.py          # YouTube webhook
│   ├── tts.py                        # ElevenLabs integration
│   ├── dialogue.py                   # Multi-character conversations
│   └── __init__.py                   # Module exports
│
├── docs/                             # Documentation
│   ├── PROFESSIONAL_GUIDE.md         # Complete implementation (600+ lines)
│   ├── EXAMPLE_SCRIPTS.md            # 6 working script templates
│   ├── SETUP_GUIDE.md                # Detailed installation
│   └── workflow_guide.md             # Advanced workflows
│
└── projects/                         # Generated videos
    └── [video_name]/
        ├── visuals/                  # Generated frames
        ├── audio/                    # Synthesized audio
        ├── final_video.mp4           # Composed video
        ├── metadata.json             # Production metadata
        └── production.log            # Detailed logs
```

---

## 🚀 Installation

### Step 1: Prerequisites
- Python 3.9+
- pip (Python package manager)
- 4GB+ free disk space

### Step 2: Clone Repository
```bash
cd /workspace/ComfyUI-OmniFlow
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Verify Setup
```bash
python verify_setup.py
```

This checks:
- ✅ Python version
- ✅ All packages installed
- ✅ API connectivity
- ✅ System tools (FFmpeg)
- ✅ Project structure

### Step 5: Configure APIs
Add to your shell profile or `.env`:
```bash
export OPENAI_API_KEY="sk-..."          # Get from openai.com
export ELEVENLABS_API_KEY="..."         # Get from elevenlabs.io
export YOUTUBE_WEBHOOK_URL="https://..." # (Optional, for publishing)
```

---

## 📺 Usage Examples

### Example 1: One-Click Publish
```
1. Open Streamlit app
2. Go to "One-Click Publish" tab
3. Paste script:
   "Today we discuss AI trends in 2026..."
4. Add title: "5 Game-Changing AI Trends 2026"
5. Add description: "Breaking down the future of AI..."
6. Select video style: "Animated Text + VO"
7. Click "🚀 PUBLISH NOW"
8. Wait 2-4 hours
9. Video goes LIVE on YouTube ✨
```

### Example 2: Script Enhancement
```
1. Go to "Script Enhancement" tab
2. Paste raw script
3. Click "✨ Enhance Script"
4. Review improvements:
   - Hook strength: 92/100
   - Pacing: 88/100
   - Engagement: 95/100
5. Copy enhanced version
6. Use in One-Click Publish
```

### Example 3: Surprise Me! Mode
```
1. Go to "Surprise Me!" tab
2. Paste: Script + Title + Description
3. Click "🎲 Let AI Decide Everything"
4. AI recommends:
   - Channel: "Tech & AI Explained"
   - Style: "Cinematic Landscape + Overlays"
   - Voice: "Adam (Professional)"
   - Duration: 720 seconds
   - Engagement Score: 92/100
5. Click "Use This Plan & Publish"
6. Video generates with optimal config
```

### Example 4: Batch Processing
```
1. Create CSV:
   script,title,description,channel
   "AI trends...", "5 Trends...", "Description", "Tech"
   "Travel story...", "Hidden Island", "Discovery", "Travel"
   
2. Upload to "Batch & Analytics" tab
3. Click "Start Batch Generation"
4. System generates all videos overnight
5. Posts on schedule
```

---

## 🎯 Real-World Workflow

### Day 1: Create 5 Scripts
```
- Morning: Write 5 script ideas
- Noon: Paste into OmniFlow "Script Enhancement"
- Evening: Review AI improvements
```

### Day 2-3: Generate Videos
```
- Use "Surprise Me!" mode for hands-off optimization
- OR manually choose video styles
- System generates 5 videos (3-6 hours each)
```

### Day 3-4: Post & Monitor
```
- Videos auto-publish to YouTube (via webhook)
- Monitor engagement metrics
- Adjust next batch based on performance
```

### Result: 5 Viral Videos
```
- Consistent quality (professional production)
- Optimal length/style per script
- YouTube optimized metadata
- Posted on schedule
- You did minimal work ✨
```

---

## 🔑 API Configuration

### Must-Have
**OpenAI** (Script Enhancement + AI Selection)
- Sign up: https://openai.com
- Get free $5 credits
- Add key to environment

```bash
export OPENAI_API_KEY="sk-..."
```

**ElevenLabs** (Voice Synthesis)
- Sign up: https://elevenlabs.io
- Free tier: 10,000 characters/month
- Add key to environment

```bash
export ELEVENLABS_API_KEY="..."
```

### Optional
**YouTube Webhook** (Auto-Publishing)
- Sign up: https://n8n.io or https://make.com
- Create webhook trigger
- Route to YouTube API

```bash
export YOUTUBE_WEBHOOK_URL="https://hook.n8n.io/webhook/..."
```

---

## 🎬 Video Generation Timeline

| Style | Time | Quality | Best For |
|-------|------|---------|----------|
| Animated Text + VO | 1-2 hours | Professional | Quick news, tips, tutorials |
| Interactive Dialogue | 4-6 hours | Very High | Debates, interviews, stories |
| Human Hybrid | 2-3 hours | High | Reviews, authentic analysis |
| Cinematic Landscape | 3-4 hours | Very High | Travel, nature, documentary |
| Talking Head Avatar | 2-3 hours | High | Expert commentary, courses |
| Visual Storytelling | 4-6 hours | Very High | Brand stories, case studies |

---

## 📊 Quality Assurance

### Anti-AI-Detection Strategy
Each template includes:
- ✅ Real footage or authentic visuals (60%+)
- ✅ Natural pacing (pauses, hesitations, variation)
- ✅ Imperfect but authentic elements (slight stutters, "um", "ah")
- ✅ Real people in footage where applicable
- ✅ Proper YouTube metadata (not clickbait)
- ✅ Varied upload times
- ✅ Genuine call-to-actions

### Quality Scores
System tracks:
- Hook strength (0-100)
- Pacing quality (0-100)
- Emotional engagement (0-100)
- SEO optimization (0-100)
- Overall engagement score
- Viral potential assessment

---

## 🐛 Troubleshooting

### "API Key not found"
→ Add in Streamlit sidebar: Configuration Hub → API Keys

### "ComfyUI connection refused"
→ Keep ComfyUI running: `python main.py` in ComfyUI directory

### "FFmpeg not found"
```bash
# Windows: choco install ffmpeg
# Mac: brew install ffmpeg
# Linux: sudo apt-get install ffmpeg
```

### "Video quality is poor"
→ Select "Cinematic" or "Visual Storytelling" style instead

### "Surprise Me suggests wrong template"
→ Be more specific in script title/description, or choose manually

See [PROFESSIONAL_GUIDE.md](docs/PROFESSIONAL_GUIDE.md#troubleshooting) for more.

---

## 📚 Documentation

- **Quick Start**: [QUICK_REFERENCE.md](QUICK_REFERENCE.md) (3 minutes)
- **Full Guide**: [PROFESSIONAL_GUIDE.md](docs/PROFESSIONAL_GUIDE.md) (600+ lines)
- **Example Scripts**: [EXAMPLE_SCRIPTS.md](docs/EXAMPLE_SCRIPTS.md) (6 templates)
- **Setup Details**: [SETUP_GUIDE.md](docs/SETUP_GUIDE.md)
- **Workflows**: [workflow_guide.md](docs/workflow_guide.md)

---

## 🎯 Success Metrics

Track these after publishing:
- ⏱️ **Watch time**: Aim for 50%+ average view duration
- 👍 **Engagement**: Target 10%+ like/comment ratio
- 🔔 **Subscribers**: Track growth per 100 videos
- 📈 **CTR**: Target 5%+ click-through rate
- 💰 **Revenue**: Monitor if monetized
- 🔍 **SEO**: Track search impressions

---

## 💡 Pro Tips

1. **Always Enhance Scripts**
   - Use "Script Enhancement" tab
   - Typically doubles watch time
   - Takes 2-3 minutes

2. **Use "Surprise Me!" for Testing**
   - Test AI-selected config on new topics
   - Compare to manual selection
   - Refine based on engagement

3. **Batch Process for Scale**
   - Create 10 scripts at once
   - Upload as CSV
   - Generate overnight
   - Post on schedule

4. **Mix Video Styles**
   - Don't use same style every video
   - Test different templates
   - Let engagement metrics guide you

5. **Leverage Trending Topics**
   - Adapt templates to current events
   - Faster publication times
   - Higher initial views

---

## 🔐 Privacy & Security

- ✅ API keys stored in environment variables
- ✅ No credentials logged or saved in code
- ✅ Webhook URLs protected
- ✅ Videos stored locally before upload
- ✅ YouTube API quotas monitored (1,000/day)
- ✅ No personal data retained

---

## 📜 License

MIT License - Feel free to use, modify, extend.

See LICENSE file for details.

---

## 🤝 Contributing

Have improvements? Found bugs? Want to add features?

1. Test verify_setup.py
2. Document changes
3. Keep API integrations working
4. Add tests for new features

---

## 🚀 Next Steps

**Ready to start?**

1. Run setup: `python verify_setup.py`
2. Start app: `streamlit run streamlit_app_pro.py`
3. Choose template: [EXAMPLE_SCRIPTS.md](docs/EXAMPLE_SCRIPTS.md)
4. Publish: One-Click or Surprise Me mode
5. Monitor: Check YouTube and logs

**Your YouTube channel is about to explode with consistent, high-quality content.** ✨

---

## 📞 Support

- **Setup issues**: See [SETUP_GUIDE.md](docs/SETUP_GUIDE.md)
- **Advanced workflows**: See [PROFESSIONAL_GUIDE.md](docs/PROFESSIONAL_GUIDE.md)
- **API problems**: Check API provider documentation
- **Video quality**: Try different style or ScriptEnhancer

---

**Happy creating! 🎬**

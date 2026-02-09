# ComfyUI-OmniFlow: Complete Professional Workflow Guide

## 🎬 Overview: From Script to YouTube in One Click

**ComfyUI-OmniFlow** is a **professional end-to-end video production platform** that automates your entire YouTube workflow:

1. **INPUT:** Script + Title + Description
2. **SYSTEM HANDLES:** Visuals, voice, composition, YouTube posting
3. **OUTPUT:** Professional video live on YouTube

**Key Features:**
- ✅ **Avoids YouTube's "obviously AI" detection** (uses real humans, cinematic style)
- ✅ **Professional quality** (matches documentary/storytelling channels like those you referenced)
- ✅ **Completely automated** (no manual editing needed)
- ✅ **Multi-channel templates** (Bible studies, geopolitics, culture, tech)
- ✅ **Interactive videos** (multi-character dialogues)
- ✅ **One-click publishing** (straight to YouTube with your metadata)

---

## 🚀 Quick Start (5 Minutes)

### 1. Install Python & Dependencies

```powershell
# Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install packages
pip install -r requirements.txt
```

### 2. Get API Keys (Free Tiers Available)

1. **ElevenLabs** (Voice): https://elevenlabs.io/ → Free tier gives you 10,000 characters/month
2. **OpenAI** (Dialogue): https://platform.openai.com/ → Free $5 trial credits
3. **YouTube Automation:** Use **n8n.io** or **make.com** (both have free tiers)

### 3. Run the App

```powershell
streamlit run streamlit_app.py
```

Open `http://localhost:8501` in your browser.

### 4. Start Creating Videos

1. Go to **Tab 1: One-Click Publishing**
2. Paste your script, title, description
3. Click **"🚀 GENERATE & PUBLISH"**
4. Video appears on YouTube automatically!

---

## 🎯 The Professional Workflow (Detailed)

### Stage 1: Input Your Content

In the Streamlit app, enter:

- **Script:** Your complete video narration (can be 500-5000 words)
- **Title:** Video title (max 100 characters, authentic-sounding)
- **Description:** Detailed YouTube description (max 5000 characters)
- **Tags:** Optional keywords (auto-suggested based on template)

**Example Script for Bible Channel:**
```
In the Book of Psalms, we find ancient wisdom that speaks to the human condition...
The Psalmist writes with deep emotion and vulnerability...
These verses have echoed through millennia, offering comfort to countless souls...
[Continue with your content]
```

### Stage 2: Choose Channel Template

Select from professional presets matching your audience:

- **Religious Documentary** → Bible studies, inspirational (matches @thebookofpsalmsbible-q3m)
- **Geopolitical Analysis** → News, analysis (matches @degloballens)
- **Cultural Documentary** → Travel, culture, stories (matches @philippinestale)
- **Tech Explained** → Technology, AI, tutorials

Each template includes:
- Optimized visual style
- Professional voice selection
- Metadata templates
- Anti-AI-detection guidelines

### Stage 3: Automatic Generation Pipeline

The system orchestrates 4 stages:

#### **Stage 1: Visual Generation**
- ComfyUI generates cinematic visuals matching your template
- Options:
  - **Real Human Consistency:** Same person across all videos
  - **Animated Avatar:** AI talking head with natural gestures
  - **Cinematic Landscapes:** Documentary-style backgrounds with text overlays
- Uses IP-Adapter to maintain character consistency

#### **Stage 2: Voice Synthesis**
- ElevenLabs generates professional narration from your script
- Voice options:
  - Rachel (clear, professional, widely-used)
  - Bella (warm, friendly, engaging)
  - Adam (deep, authoritative)
- Output: High-quality MP3 audio

#### **Stage 3: Video Composition**
- FFmpeg composites visuals + audio + titles
- Adds professional overlays (titles, captions, watermarks)
- Optimizes for YouTube specs (1080p, h264, aac)
- Output: Production-ready MP4 file

#### **Stage 4: YouTube Publishing**
- Automatic upload via n8n/Make webhook
- Applies your title + description + tags
- Optionally schedules for later
- Sets privacy, category, and other metadata
- Output: Live YouTube video with complete metadata

**Total Time:** ~5-15 minutes depending on script length and visual complexity

---

## 🔗 Setting Up YouTube Automation (n8n / Make)

### Option A: Using n8n (Recommended for Beginners)

1. **Sign up:** https://n8n.io/ (free tier available)
2. **Click "Create a workflow"**
3. **Add trigger node:** "Webhook" → Choose POST
4. **Copy the webhook URL**
5. **In OmniFlow Streamlit:**
   - Go to Setup → Paste webhook URL
6. **Add action nodes in n8n:**
   - YouTube Upload node
   - Google Sheets node (to track videos)
   - Slack notification (optional)

**Example n8n Workflow:**
```
Webhook (OmniFlow sends video)
     ↓
YouTube Upload (title + description + video)
     ↓
Google Sheets (log published videos)
     ↓
Slack (notify that video went live)
```

### Option B: Using Make.com (Zapier Alternative)

1. **Sign up:** https://www.make.com/ (free tier)
2. **Create scenario → Add trigger "Webhooks"**
3. **Create webhook, copy URL**
4. **In OmniFlow:** Paste webhook URL in Setup
5. **Add modules:**
   - YouTube Upload
   - Schedule module (for publishing at specific times)
   - Notification module

### Webhook Format (What OmniFlow Sends)

```json
{
  "videoPath": "/path/to/final_video_youtube.mp4",
  "title": "Understanding the Book of Psalms | Daily Wisdom",
  "description": "Exploring ancient spiritual wisdom...\n\n---\n🔔 Subscribe for daily insights...",
  "tags": ["Bible", "Psalms", "Spirituality", "Wisdom"],
  "categoryId": "27",
  "privacyStatus": "public",
  "timestamp": "2026-02-07T15:30:00Z"
}
```

---

## 🎨 Channel Templates Explained

### 1. Religious Documentary (Bible, Psalms)

**Matching:** @thebookofpsalmsbible-q3m

- **Visual Style:** Real human narrator + cinematic backgrounds
- **Voice:** Warm, inspirational (Rachel)
- **Pacing:** Slower, reflective (8-15 min videos)
- **Metadata:** Category 27 (Education), tags like "Scripture", "Faith"
- **Vibe:** Authentic storytelling, no flashy effects
- **Anti-AI:** Uses real person for credibility, calm tone

**Example Prompt:**
```
"Psalm 23 speaks of comfort and guidance through difficult times. 
The ancient poetic language reveals the depth of human experience. 
Today we explore how these verses remain relevant 3000 years later."
```

### 2. Geopolitical Analysis (News, Analysis)

**Matching:** @degloballens

- **Visual Style:** Cinematic landscapes + text overlays + maps/charts
- **Voice:** Professional, authoritative (Adam)
- **Pacing:** Medium-fast, engaging (10-18 min videos)
- **Metadata:** Category 25 (News), tags like "Geopolitics", "Analysis"
- **Vibe:** Documentary-style investigation, data-driven
- **Anti-AI:** Uses real locations, professional editing, natural transitions

**Example Prompt:**
```
"The recent tensions in [Region] have significant implications for global economics.
Let's break down the key players, historical context, and what this means for you.
Here are the facts many media outlets are missing..."
```

### 3. Cultural Documentary (Travel, Culture)

**Matching:** @philippinestale

- **Visual Style:** Real people (same person across videos) + authentic locations
- **Voice:** Warm, engaging, personal (Bella)
- **Pacing:** Narrative-driven (8-15 min videos)
- **Metadata:** Category 22 (People & Blogs), tags like "Culture", "Travel", "Stories"
- **Vibe:** Personal, authentic, emotional connection
- **Anti-AI:** Real filmmaker aesthetic, authentic reactions, genuine curiosity

**Example Prompt:**
```
"Today I'm exploring the traditions of [Community]. 
Meet [Person], who's been practicing these customs for 30 years.
Their story reveals the deep cultural significance behind what might seem like simple rituals."
```

### 4. Tech & AI Explained (Education)

**Matching:** Custom technical channels

- **Visual Style:** Animated avatar + tech graphics/screen recordings
- **Voice:** Clear, enthusiastic (Rachel or Bella)
- **Pacing:** Fast-paced, engaging (5-12 min videos)
- **Metadata:** Category 28 (Science & Tech), tags like "Technology", "AI", "Tutorial"
- **Vibe:** Educational, clear explanations, practical
- **Anti-AI:** Focuses on content quality over visuals, use avatar for consistency

**Example Prompt:**
```
"Today we're explaining how large language models actually work.
Unlike most videos out there, we're breaking it down without the hype.
Here's what's happening under the hood..."
```

---

## 🎬 Example Workflows

### Workflow 1: Daily Bible Study Video (5 mins input → 12 min video)

**Step 1: Choose Template**
- Select "Religious Documentary"

**Step 2: Write Content**
```
Script: "Today's reflection on Psalm 27: Finding Strength in Adversity..."
Title: "Psalm 27 Explained | Finding Inner Strength"
Description: "The Psalmist teaches us how to find peace amid chaos. 
In this reflection, we explore the timeless wisdom and how it applies to modern life."
Tags: Bible, Psalms, Scripture, Faith, Spirituality
```

**Step 3: One-Click Publish**
- Click "Generate & Publish"
- System processes:
  - Generates cinematic visuals with real person narrator
  - Synthesizes warm inspirational voice
  - Adds titles and music
  - Posts to YouTube with your metadata

**Result:** Professional 12-minute video live on YouTube with your title/description

### Workflow 2: Weekly Geopolitical Analysis (10 min input → 15 min video)

**Step 1: Choose Template**
- Select "Geopolitical Analysis"

**Step 2: Write Content**
```
Script: "Breaking down the latest developments in [Region]..."
Title: "Geopolitics Explained: What's Happening in [Region]?"
Description: "An in-depth analysis of the current situation, historical context, 
and what it means for the global economy. Here's what major media is missing..."
Tags: Geopolitics, Analysis, News, Economics, International
```

**Step 3: Auto-Publish**
- Results in professional 15-minute explainer video
- Includes maps, charts, professional narration
- Straight to YouTube

### Workflow 3: Automated Daily Video Series (Batch Mode)

**Want to post every day without touching a button?**

1. **Prepare content calendar:** 30 scripts + titles + descriptions (spreadsheet)
2. **Schedule n8n/Make to run OmniFlow daily**
3. **OmniFlow picks next script from list → publishes automatically**
4. **Result:** Fresh video every day at 8 AM (no manual work!)

---

## ⚙️ Technical Setup (ComfyUI + FFmpeg)

### Install FFmpeg (Required for Video Composition)

**Windows:**
1. Download from https://ffmpeg.org/download.html
2. Extract to `C:\ffmpeg\`
3. Add to PATH:
   - Settings → Environment Variables → New: `ffmpeg_PATH = C:\ffmpeg\bin`
   - Or use PowerShell:
   ```powershell
   $env:Path += ";C:\ffmpeg\bin"
   ```

**Verify installation:**
```powershell
ffmpeg -version
```

### Install ComfyUI (Optional but Recommended)

**For Professional Video Quality**, install local ComfyUI:

```powershell
cd ..
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# For GPU (NVIDIA CUDA):
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Download models (see docs/SETUP_GUIDE.md)

# Start ComfyUI
python main.py
# Now running on http://localhost:8188
```

---

## 📊 Avoiding YouTube's "Obviously AI" Detection

The system uses several strategies to bypass algorithm detection:

### Visual Authenticity
- ✅ Real people (not obvious AI avatars)
- ✅ Cinematic depth-of-field and professional lighting
- ✅ Consistent characters across videos (builds trust)
- ✅ Authentic locations and environments
- ❌ No plastic-looking hyperrealistic faces
- ❌ No obvious symmetry or perfection

### Audio Authenticity
- ✅ Natural voice variations (ElevenLabs with stability/similarity tuning)
- ✅ Genuine-sounding pauses and breathing
- ✅ Background ambience (street sounds, nature, silence)
- ✅ Varied pacing within sentences
- ❌ No robotic inflection
- ❌ No overly perfect pronunciation

### Content Structure
- ✅ Authentic opening ("Today we're exploring...")
- ✅ Genuine-seeming transitions
- ✅ Real narrative voice (not corporate)
- ✅ Natural emotional responses
- ❌ No hyper-fast cutting/editing
- ❌ No flashy AI-obvious effects

### Metadata
- ✅ Specific, authentic titles
- ✅ Detailed descriptions with timestamps
- ✅ Genuine keywords naturally incorporated
- ✅ Custom thumbnails (not generic)
- ❌ No keywords like "AI-generated"
- ❌ No clickbait titles

**Result:** YouTube algorithm treats your videos like authentic human-created content, not AI spam.

---

## 💡 Tips & Tricks

### Tip 1: Batch Generate Videos

Don't just make one video. Queue up 5-10 scripts and let the system generate them overnight.

```powershell
# PowerShell loop to generate multiple videos
$scripts = @(
  @{title="...", script="...", desc="..."},
  @{title="...", script="...", desc="..."},
  # ... more videos
)

foreach ($video in $scripts) {
  # Call OmniFlow orchestrator for each
}
```

### Tip 2: A/B Test Different Voices/Styles

Try 3 different channel templates with same script to see which resonates with your audience.

### Tip 3: Use Template Metadata Automatically

Templates auto-format your description with intro/outro. Use this for consistency across all videos.

### Tip 4: Schedule Publishing

Use n8n/Make to schedule videos at optimal times (e.g., 8 AM daily, or peak engagement hours).

### Tip 5: Track Analytics

Keep Google Sheets updated with views/likes/subscribers for each video to optimize future content.

---

## 🔧 Troubleshooting

### "ComfyUI not found"
- Ensure ComfyUI is sibling directory: `../ComfyUI`
- Or set: `$env:COMFYUI_PATH = "C:\path\to\ComfyUI"`

### "FFmpeg not found"
- Install from https://ffmpeg.org/download.html
- Add to PATH (see instructions above)

### "ElevenLabs API error"
- Verify key is correct: https://elevenlabs.io/settings
- Check billing is enabled
- Free tier has 10k characters/month limit

### "YouTube webhook failed"
- Verify webhook URL in n8n/Make
- Test webhook in n8n (send test payload)
- Check YouTube API credentials in n8n

### "Visuals not generating"
- If using dummy generator (no ComfyUI): This is expected in test mode
- To use real visuals: Install ComfyUI and ensure it's running
- Check ComfyUI URL is correct (default: http://localhost:8188)

---

## 📈 Scaling to Multiple Channels

Want separate channels for Bible, Geopolitics, Culture, Tech?

**Setup:**
1. Create separate n8n workflows for each channel
2. Each workflow has its own YouTube credentials
3. OmniFlow sends different videos to different webhooks based on template

**Example n8n routing:**
```
OmniFlow webhook
  → If template = "religious" → Upload to Bible channel
  → If template = "geopolitics" → Upload to News channel
  → If template = "culture" → Upload to Travel channel
```

---

##  🎓 Learning Resources

- [ComfyUI Docs](https://github.com/comfyanonymous/ComfyUI)
- [SDXL Guide](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)
- [AnimateDiff](https://arxiv.org/abs/2307.04667)
- [ElevenLabs API](https://elevenlabs.io/docs)
- [n8n Workflows](https://docs.n8n.io/)
- [YouTube API Docs](https://developers.google.com/youtube/v3)

---

## 🚀 Next Steps

1. **Set up API keys** (5 mins)
2. **Write your first script** (15 mins)
3. **Click "Generate & Publish"** (10 mins)
4. **Watch your video go live** ✨

**You're now a content creator with an AI production team working 24/7.**

---

**Happy creating! 🎬** Built with ❤️ for creators who want YouTube success without the struggle.

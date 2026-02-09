# 🎬 ComfyUI OmniFlow Pro v2.0 - Quick Reference

## New Imports

```python
# AI Specialists
from omniflow import (
    AISpecialistSelector,
    YouTubeAnalyst,
    PoetryGenerator,
    StoryCraft,
    ScriptDeveloper,
    HistoryInsight,
)

# YouTube Integration
from omniflow import (
    YouTubeAuthenticator,
    YouTubeVideoAnalyzer,
    YouTubeVideoReference,
)
```

---

## 🧠 AI Specialists Quick Usage

### YouTube Analyst
```python
from omniflow import YouTubeAnalyst

analyst = YouTubeAnalyst()

# Get trending topics
topics = analyst.analyze_trending_topics(niche="Technology")

# Get viral score
score = analyst.estimate_viral_score(
    title="Amazing AI Tool",
    script="Your script here...",
    niche="Technology"
)
```

### Poetry Generator
```python
from omniflow import PoetryGenerator

poet = PoetryGenerator()

script = poet.generate_poetic_narration(
    topic="Journey of discovery",
    style="inspirational"  # or "dramatic", "mysterious", "romantic"
)
```

### Story Craft
```python
from omniflow import StoryCraft

craft = StoryCraft()

# Create story arc
arc = craft.create_story_arc(
    premise="Overcoming obstacles",
    duration_minutes=15
)

# Generate character development
chars = craft.generate_character_development(
    character_name="Alex",
    arc_type="hero"
)
```

### Script Developer
```python
from omniflow import ScriptDeveloper

dev = ScriptDeveloper()

# Professional refinement
refined = dev.refine_script_professionally(
    script="Your script",
    target_duration_seconds=600  # 10 minutes
)

# Add comedic timing
comedic = dev.add_comedic_timing(script)
```

### History Insight
```python
from omniflow import HistoryInsight

historian = HistoryInsight()

# Create historical narrative
narrative = historian.create_historical_narrative(
    period="World War II",
    topic="Battle of Normandy",
    duration_minutes=15
)

# Verify accuracy
verified = historian.verify_historical_accuracy(script)

# Timeline visual guide
timeline = historian.create_timeline_visual_guide(
    events=["Event 1", "Event 2"],
    duration_minutes=10
)
```

### AI Specialist Selector
```python
from omniflow import AISpecialistSelector

# Get specific specialist
poet = AISpecialistSelector.get_specialist("poetry_generator")

# Get all specialists
selector = AISpecialistSelector()
all_specialists = selector.get_all_specialists()

# Combine multiple specialists
result = selector.combine_specialists(
    script="Your script",
    specialists=["poem_generator", "script_developer"],
    niche="Technology"
)
```

---

## 📺 YouTube Integration Quick Usage

### Authenticate with YouTube
```python
from omniflow import YouTubeAuthenticator

# Authenticate user
service = YouTubeAuthenticator.authenticate_user()

# Or force new authentication
service = YouTubeAuthenticator.authenticate_user(force_new=True)
```

### Analyze Video Details
```python
from omniflow import YouTubeVideoAnalyzer

analyzer = YouTubeVideoAnalyzer(service)

# Get video details
details = analyzer.get_video_details(video_id="dQw4w9WgXcQ")
# Returns: views, likes, comments, duration, tags, description

# Analyze video quality
quality = analyzer.analyze_video_quality(video_id="dQw4w9WgXcQ")
# Returns: engagement rate, production insights, best practices

# Compare videos
comparison = analyzer.compare_videos(video_ids=["vid1", "vid2", "vid3"])
# Returns: common patterns, best practices
```

### Analyze Reference Video
```python
from omniflow import YouTubeVideoReference

reference = YouTubeVideoReference()

# Full analysis from URL
analysis = reference.analyze_reference_video(
    url="https://www.youtube.com/watch?v=..."
)
# Returns: comprehensive production insights

# Get from video ID
analysis = reference.get_video_from_url(video_id="dQw4w9WgXcQ")
```

---

## 📺 Channel Templates

### Available Templates (15+)

```python
from omniflow import EXPANDED_CHANNEL_TEMPLATES

templates = list(EXPANDED_CHANNEL_TEMPLATES.keys())
# [
#   "spiritual_awakening",
#   "geopolitical_insights",
#   "cultural_storytelling",
#   "tech_reviews",
#   "how_to_tutorials",
#   "finance_insights",
#   "trending_stories",
#   "wellness_guidance",
#   "creative_shorts",
#   "business_strategy",
#   "controversy_analysis",
#   "gospel_music",
#   "crime_story_narrative",
#   "custom_channel",
# ]

# Get template config
gospel = EXPANDED_CHANNEL_TEMPLATES["gospel_music"]
print(gospel["name"])          # Gospel Music
print(gospel["duration_range"]) # 3-10 minutes
print(gospel["voice"])          # {name: "Bella", ...}
```

### New Templates in v2.0

1. **gospel_music** - Gospel, Spiritual Music
2. **crime_story_narrative** - Crime, True Crime
3. **custom_channel** - Fully customizable

---

## 🎬 Video Styles (6 Options)

```python
from omniflow import VideoStyleSelector

# Get all styles
styles = VideoStyleSelector.get_all_styles()
# Keys: "text_voiceover", "dialogue_driven", "animated_avatar",
#       "cinematic_storytelling", "mixed_hybrid", "talking_head"

# Suggest style for script
suggested = VideoStyleSelector.suggest_style_for_script(
    script="Your script here",
    channel_type="tech_reviews"
)

# Access style config
style_config = VideoStyleSelector.VIDEO_COMPOSITION_STYLES["cinematic_storytelling"]
print(style_config["name"])        # Cinematic Storytelling
print(style_config["use_case"])    # Story-based, emotional content
```

---

## 🎲 Surprise Me! Mode

```python
from omniflow import SurpriseGameMode

surprise = SurpriseGameMode()

# Get AI recommendations for everything
recommendations = surprise.analyze_and_generate(
    script="Your script",
    title="Your title",
    description="Your description"
)
# Returns complete AI-recommended configuration
```

---

## 🎬 Complete Workflow Example

```python
from omniflow import (
    YouTubeAnalyst,
    PoetryGenerator,
    YouTubeAuthenticator,
    YouTubeVideoReference,
    VideoProductionOrchestrator,
    EXPANDED_CHANNEL_TEMPLATES,
)

# Step 1: Get inspiration from reference
ref = YouTubeVideoReference()
reference_analysis = ref.analyze_reference_video(
    "https://www.youtube.com/watch?v=..."
)

# Step 2: Use specialists
analyst = YouTubeAnalyst()
trends = analyst.analyze_trending_topics("Technology")

poet = PoetryGenerator()
script = poet.generate_poetic_narration(
    topic=trends[0],
    style="inspirational"
)

# Step 3: Generate video
orchestrator = VideoProductionOrchestrator("my_project")
result = orchestrator.produce_video(
    script=script,
    title="Amazing Technology",
    description="Learn about latest tech trends",
    channel_template="tech_reviews",
    visual_style="cinematic_storytelling",
    tags=["AI", "Technology", "Trends"],
    voice_id="21m00Tcm4TlvDq8ikWAM",  # Bella
    publish_to_youtube=True,
)

print(result)
```

---

## 🔑 Environment Variables

```bash
# Required
export OPENAI_API_KEY="sk-..."
export ELEVENLABS_API_KEY="..."

# Optional
export YOUTUBE_WEBHOOK_URL="https://..."
export COMFYUI_URL="http://localhost:8188"
export DEBUG="False"
```

---

## 🎯 Streamlit UI Tabs

### Tab 1: 🚀 One-Click Publishing
- Paste script
- Set duration (5-60 min)
- Select channel template
- Choose video style
- Click publish

### Tab 2: ✨ Script Enhancement
- Paste script
- Select tone/style
- Enhance automatically
- Get quality metrics

### Tab 3: 🧠 AI Specialists
- Choose specialist
- Input parameters
- Get specialist output
- Copy or use directly

### Tab 4: 🎬 Video Styles
- Browse 6 styles
- See use cases
- Compare complexity
- Select style

### Tab 5: 🎲 Surprise Me!
- Paste content
- Let AI recommend everything
- Review configuration
- Generate video

### Tab 6: 👁️ Preview & Edit
- Review script/title/description
- Edit any content
- Check quality scores
- Publish or save draft

---

## 📊 Common Tasks

### Task: Generate Gospel Music Video
```python
# In Streamlit:
# 1. Tab 3: Select Poetry Generator
# 2. Enter: Topic = "Faith Journey"
# 3. Generate poetic script
# 4. Copy script
# 5. Tab 1: Paste script
# 6. Select: gospel_music template
# 7. Set duration: 8 minutes
# 8. Click Publish
```

### Task: Match Successful Video Quality
```python
# 1. Find successful video in your niche
# 2. Sidebar: Paste YouTube URL
# 3. Click "Analyze Reference Video"
# 4. Review recommendations
# 5. Use same settings for your video
# 6. Generate video
# 7. Quality should match reference
```

### Task: Create Professional Script
```python
# Method 1: Poetry Generator
# 1. Tab 3: Poetry Generator
# 2. Input topic and style
# 3. Get poetic script

# Method 2: Script Developer
# 1. Write raw script
# 2. Tab 3: Script Developer
# 3. Paste raw script
# 4. Get professionally refined version

# Method 3: Combine (Best)
# 1. Tab 3: Poetry Generator → poetic script
# 2. Tab 3: Script Developer → refine it
# 3. Tab 3: YouTube Analyst → optimize for trends
# 4. Use final script for video
```

---

## 🚀 Running the App

```bash
# Terminal
cd /workspace/ComfyUI-OmniFlow

# Install dependencies
pip install -r requirements.txt

# Verify setup
python setup_verify.py

# Run Streamlit app
streamlit run streamlit_app_v2.py

# Open browser
# http://localhost:8501
```

---

## 📈 API Costs (Approximate)

| Service | Cost | Usage |
|---------|------|-------|
| OpenAI (GPT-4) | $0.05-0.15 | Per video |
| ElevenLabs (TTS) | $0.01-0.03 | Per minute |
| YouTube API | Free | Video analysis |
| ComfyUI | Local free | Visuals |
| **Total** | **~$0.06-0.18** | **Per video** |

---

## ❓ Common Questions

**Q: Which specialist should I use?**
A: 
- Content strategy → YouTube Analyst
- Emotional stories → Poetry Generator
- Story structure → Story Craft
- Polish & timing → Script Developer
- Historical accuracy → History Insight

**Q: How do I analyze reference videos?**
A:
1. Sidebar: "YouTube Reference (Login)"
2. Click "Authenticate with YouTube"
3. Paste YouTube URL
4. Click "Analyze Reference Video"

**Q: How long does generation take?**
A: 2-8 minutes depending on video length

**Q: Can I edit after generating?**
A: Yes! Use "Preview & Edit" tab

**Q: What video length works best?**
A: 10-15 minutes for most niches (adjust with slider)

---

## 🎓 Learning Path

1. **Start**: Run setup_verify.py
2. **Learn**: Read GUIDE_V2.md
3. **Explore**: Try each specialist in Tab 3
4. **Practice**: Generate video with Tab 1
5. **Analyze**: Use reference video analysis
6. **Refine**: Use Preview & Edit
7. **Publish**: Upload to YouTube
8. **Scale**: Automate with webhooks

---

## 📞 Support

- 📚 **Documentation**: See GUIDE_V2.md
- 🆘 **Troubleshooting**: See GUIDE_V2.md → Troubleshooting
- 💬 **Issues**: Check README.md
- 🐛 **Bugs**: GitHub issues

---

**Version**: v2.0  
**Last Updated**: 2024  
**Status**: Production Ready  
**Features**: 15+ Templates, 5 AI Specialists, YouTube Integration, Preview & Edit

Happy Creating! 🚀

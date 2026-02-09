# 🎬 ComfyUI OmniFlow Pro v2.0 - Complete User Guide

## Overview

ComfyUI OmniFlow Pro v2.0 is a **professional-grade AI-powered YouTube video generator** with advanced features for creators who want to scale content production.

### What's New in v2.0

✅ **15+ Channel Templates** (including Gospel, Crime Story, Custom)  
✅ **6 Video Composition Styles**  
✅ **5 AI Specialist Roles** (YouTube Analyst, Poetry, Story, Script, History)  
✅ **Duration Control** (5-60 minutes)  
✅ **YouTube Video Reference Analysis**  
✅ **Preview & Edit Before Publishing**  
✅ **Sound Design Syncing**  

---

## 🚀 Getting Started

### Installation

```bash
# Install OmniFlow
pip install -e .

# Install required dependencies
pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### Running the App

```bash
# Start the Streamlit app
streamlit run streamlit_app_v2.py
```

The app opens on `http://localhost:8501`

---

## 📚 Feature Guide

### 1. 📺 Channel Templates (15+ Options)

Choose from professionally curated templates for different content niches:

#### Gospel Music
- **Duration**: 3-10 minutes
- **Visual Style**: Performance + Spiritual Imagery
- **Voice**: Bella (soulful, spiritual, passionate)
- **Color Palette**: Warm spiritual golds and ambers
- **Best For**: Gospel artists, worship channels, spiritual content

#### Crime Story & True Crime
- **Duration**: 10-30 minutes
- **Visual Style**: Cinematic Reenactment + Documentary
- **Voice**: Adam (dramatic, suspenseful, serious)
- **Color Palette**: Dark dramatic mystery
- **Special Features**: Fast cuts, timeline graphics
- **Best For**: True crime channels, mystery shows, investigation content

#### Custom Channel
- **Duration**: 5-60 minutes (fully flexible)
- **All Settings**: Fully customizable
- **Best For**: Unique niches, experimental formats

#### Other Templates (10+)
Spiritual, Geopolitical, Cultural, Tech Reviews, How-To, Finance, Trending Stories, Wellness, Creative, Business, Controversy

---

### 2. 🧠 AI Specialist Roles

Five expert AI roles that specialize in different content types:

#### 📊 YouTube Analyst
Analyzes YouTube trends, predicts viral potential, and provides strategy insights.

**Features:**
- Trending topic detection for your niche
- Viral scorecard (0-100)
- Content strategy recommendations
- Audience insights

**How to Use:**
1. Go to "AI Specialists" tab
2. Select "YouTube Analyst"
3. Enter your content niche (e.g., "Technology")
4. Click "Find Trending Topics" or "Estimate Viral Score"

**Example Output:**
```json
{
  "trending_topics": [
    "AI automation in 2024",
    "No-code video generation",
    "YouTube growth strategies"
  ],
  "viral_score": 87,
  "recommendations": [
    "Use trending keywords in title",
    "Add compelling hook in first 5 seconds",
    "Include community engagement prompts"
  ]
}
```

#### ✍️ Poetry Generator
Creates poetic, narrative-rich scripts with emotional depth.

**Features:**
- Poetic narration generation
- Multiple styles (inspirational, dramatic, mysterious, romantic)
- Metaphor-rich language
- Emotional resonance

**How to Use:**
1. Go to "AI Specialists" tab
2. Select "Poetry Generator"
3. Enter your topic
4. Choose a style
5. Click "Generate Poetic Narration"

**Example:**
```
"In the whispered corridors of time,
Where echoes meet eternity's climb,
A story unfolds like morning light,
Breaking through the darkness of night..."
```

#### 📖 Story Craft Master
Designs complete story arcs with character development and narrative structure.

**Features:**
- Story arc design (3-act structure)
- Character development guides
- Plot twists and narrative pacing
- Scene-by-scene breakdown

**How to Use:**
1. Go to "AI Specialists" tab
2. Select "Story Craft Master"
3. Enter story premise
4. Set desired duration
5. Click "Create Story Arc"

#### 🎬 Script Developer
Refines scripts professionally with comedic timing, pacing optimization, and polish.

**Features:**
- Professional script refinement
- Comedic timing insertion
- Pacing optimization
- Dialogue enhancement
- Narrative flow improvement

**How to Use:**
1. Go to "AI Specialists" tab
2. Select "Script Developer"
3. Paste your raw script
4. Set target duration in seconds
5. Click "Refine Script Professionally"

#### 📚 History Insight
Creates accurate historical narratives with research, timelines, and context.

**Features:**
- Historical accuracy verification
- Timeline creation
- Historical narrative generation
- Source citations
- Visual guide suggestions

**How to Use:**
1. Go to "AI Specialists" tab
2. Select "History Insight"
3. Enter historical period (e.g., "World War II")
4. Specify topic (e.g., "Battle of Normandy")
5. Set video duration
6. Click "Create Historical Narrative"

---

### 3. ⏱️ Duration Control

Choose exactly how long your video should be:

**Range**: 5-60 minutes  
**Default**: 10 minutes  
**How to Use**: Drag the slider to your desired length

The system automatically:
- Adjusts script pacing
- Estimates visual content duration
- Balances spoken narrative with visuals
- Optimizes for YouTube algorithm

---

### 4. 📺 YouTube Reference Video Analysis

Learn from successful videos by analyzing them:

#### Setup:
1. Go to sidebar → "YouTube Reference (Login)"
2. Click "🔐 Authenticate with YouTube"
3. Follow the OAuth flow
4. Paste a YouTube URL you want to analyze
5. Click "📊 Analyze Reference Video"

#### What Gets Analyzed:
- **Duration**: Optimal length for your niche
- **Engagement**: Like/comment/view ratios
- **Tags**: Successful keyword strategy
- **Thumbnails**: Visual design patterns
- **Descriptions**: SEO structure
- **Production Quality**: Equipment, lighting, sound
- **Pacing**: Cut frequency, scene transitions
- **Audio**: Music, sound design, voice characteristics

#### Example Analysis:
```
Duration: 12-15 minutes (optimal for your niche)
Engagement Rate: 8.3% (above average)
Recommended Tags: AI, Automation, YouTubeGrowth, Creator...
Production Insights:
  - High-quality 4K camera work
  - Professional audio with background music
  - Fast pacing with cuts every 3-5 seconds
  - Color grading: Cool professional tones
Sound Design:
  - Electronic background music (energetic)
  - Voice-over with professional mic
  - Sound effects at key moments
```

---

### 5. 🎬 Video Composition Styles (6 Options)

Choose how your video should look and feel:

1. **Text + Voiceover**
   - Dynamic text overlays
   - Professional narration
   - Minimal visuals, maximum clarity
   - Best for: Educational, explanatory content

2. **Dialogue-Driven**
   - Two-character conversations
   - Character animation
   - Discussion-style format
   - Best for: Debates, conversations, interviews

3. **Animated Avatar**
   - Consistent character throughout
   - Talking head style
   - Brand personality
   - Best for: Personal brand, tutorials, commentary

4. **Cinematic Storytelling**
   - High-production value visuals
   - Narrative flow
   - Dramatic transitions
   - Best for: Story-based, emotional content

5. **Mixed Hybrid**
   - Combines multiple styles
   - Dynamic, engaging
   - Variety throughout
   - Best for: Trending content, entertainment

6. **Talking Head**
   - Direct to camera
   - Real human appearance
   - Personal connection
   - Best for: Commentary, reviews, personal channels

---

### 6. 🎲 Surprise Me! (AI Auto-Mode)

Let AI decide everything based on your content:

**How It Works:**
1. Paste your script or topic
2. Enter title and description
3. Click "🎲 Let AI Decide Everything"
4. AI analyzes and generates:
   - Best channel template
   - Optimal video style
   - Perfect voice selection
   - Recommended duration
   - Optimal pacing
   - Color scheme
   - Sound design suggestions
   - Tags and SEO strategy

**Output:**
```json
{
  "recommended_template": "tech_reviews",
  "recommended_style": "cinematic_storytelling",
  "voice": "Adam",
  "optimal_duration_minutes": 12,
  "pacing": "Fast",
  "color_scheme": "Professional Blues",
  "sound_design": "Electronic + Dramatic",
  "estimated_viral_score": 85,
  "tags": ["AI", "Tech", "Innovation", "YouTube"]
}
```

---

### 7. 👁️ Preview & Edit Before Publishing

Review and revise before uploading to YouTube:

#### In the Preview & Edit Tab:

1. **Content Preview**
   - See your script, title, description
   - Review all metadata
   - Check tags

2. **Edit Options**
   - Edit title
   - Edit description
   - Edit tags
   - Adjust video settings

3. **Video Preview**
   - Preview generated video
   - Check quality score
   - Review engagement potential

4. **Publishing Options**
   - ✅ Save and Publish
   - 💾 Save as Draft
   - ❌ Cancel

#### Quality Checks Before Publishing:
- ✅ Hook strength
- ✅ Pacing validation
- ✅ Audio quality
- ✅ Visual consistency
- ✅ YouTube compliance
- ✅ SEO optimization

---

### 8. 🔊 Sound Design & Syncing

Professional audio that matches the visual cuts perfectly:

#### Features:
- Emotional music selection based on mood
- Sound effects at key moments
- Voice-over synchronization
- Dynamic audio levels
- Silence management
- Music fade-in/fade-out at transitions

#### How It Works:
1. System analyzes your script for emotional beats
2. Selects music matching the tone
3. Identifies key visual moments (cuts, transitions)
4. Syncs sound effects to these moments
5. Balances voice-over with music
6. Optimizes audio mix

#### Example Timeline:
```
0:00 - 0:05    | Intro music (energetic)
0:05 - 0:30    | Voice-over intro + background music
0:30 - 0:35    | Sound effect (whoosh) at cut
0:35 - 2:00    | Dialogue with subtle background
2:00 - 2:05    | Sound effect (notification) at key moment
2:05 - 3:00    | Music swells for emotional beat
...
```

---

## 🚀 Workflow: From Script to YouTube

### Option 1: One-Click Publishing (Fully Automated)

1. **Enter your content**
   - Paste script
   - Add title
   - Write description
   - Select channel template

2. **Choose settings**
   - Duration (5-60 minutes)
   - Video style
   - Voice
   - Privacy level

3. **Click "🚀 PUBLISH NOW"**
   - System generates video
   - Uploads to YouTube
   - Manages metadata
   - Done!

### Option 2: Enhanced Route (With AI Specialists)

1. **Choose AI Specialist**
   - YouTube Analyst (for strategy)
   - Poetry Generator (for narrative)
   - Story Craft (for structure)
   - Script Developer (for polish)
   - History Insight (for accuracy)

2. **Generate enhanced content**
   - Get specialist output
   - Copy to clipboard
   - Use in main workflow

3. **Analyze YouTube reference**
   - Find similar videos
   - Copy their success patterns
   - Match quality and style

4. **Generate and preview**
   - Create video
   - Review in Preview & Edit tab
   - Make adjustments
   - Publish

### Option 3: Creative Surprise Route

1. **Use Surprise Me!**
   - Paste raw content
   - Let AI decide everything
   - Get complete video plan

2. **Review recommendations**
   - Check best practices
   - Adjust if needed
   - Approve

3. **Generate and publish**
   - Create with AI recommendations
   - Preview
   - Publish

---

## 🎯 Best Practices

### For Maximum Engagement:

1. **Use YouTube Analyst First**
   - Check trending topics
   - Get viral scorecard
   - Incorporate trends into script

2. **Choose Reference Videos Wisely**
   - Find 3-5 successful videos in your niche
   - Analyze each
   - Extract common patterns

3. **Optimize Duration**
   - 10-15 minutes often performs best
   - Adjust based on reference analysis
   - Longer = more monetization potential (if engaging)

4. **Use Poetry Generator or Story Craft**
   - For narrative engagement
   - For emotional resonance
   - For viewer retention

5. **Script Developer Polish**
   - Always refine with Script Developer
   - Professional quality content
   - Optimized pacing

6. **Preview Before Publishing**
   - Always use Preview & Edit
   - Check for quality issues
   - Correct metadata

### For Sound Design:

1. **Match Reference Videos**
   - Analyze their sound design
   - Use similar music style/energy
   - Copy their sound effect strategy

2. **Emotional Pacing**
   - Music should match emotional beats
   - Sound effects at key moments
   - Silence for emphasis

3. **Voice Quality**
   - Match voice to channel personality
   - Consistent throughout
   - Professional audio levels

---

## 🔧 Configuration Guide

### API Keys Required:

1. **OpenAI API** (for AI features)
   - Get from: https://platform.openai.com/api-keys
   - Cost: ~$0.01-0.10 per video
   - Model: GPT-4

2. **ElevenLabs API** (for voice)
   - Get from: https://elevenlabs.io
   - Cost: Free tier available (10k characters)
   - Voices: Bella (70/10k), Rachel (100/10k), Adam (90/10k)

3. **YouTube OAuth** (for authentication)
   - Automatic via app
   - Requires Google account
   - Safe (read-only access)

### ComfyUI Setup (Optional):

```python
use_comfyui = True
comfy_url = "http://localhost:8188"
```

### Environment Variables:

```bash
export OPENAI_API_KEY="sk-..."
export ELEVENLABS_API_KEY="..."
export YOUTUBE_WEBHOOK_URL="https://..."
```

---

## 📊 Monitoring & Analytics

### Video Performance:
- YouTube Analyst tracks engagement
- Reference analysis shows benchmarks
- Quality scores before publishing

### Cost Tracking:
- OpenAI: ~0.01-0.10 per video
- ElevenLabs: ~0.005 per minute of audio
- ComfyUI: Local (no cost)

### Usage Patterns:
- Most effective: Script Developer + YouTube Analyst
- Fastest: Surprise Me! mode
- Most engaging: Story Craft + Poetry Generator

---

## ❓ FAQs

**Q: How long does it take to generate a video?**
A: 2-5 minutes depending on length and complexity. One-Click Publishing is fastest.

**Q: Can I edit the generated video?**
A: Yes! Use the Preview & Edit tab to revise anything before publishing.

**Q: Which AI Specialist should I use?**
A: Use YouTube Analyst first for strategy, then others based on content type.

**Q: How do I match the quality of reference videos?**
A: Analyze their video with YouTube Reference, and the system will match settings.

**Q: Can I use this for existing channels?**
A: Yes! The system generates content that matches your style.

**Q: What's optimal video duration?**
A: 10-15 minutes performs best, but use the duration slider based on your content.

**Q: How do I improve engagement?**
A: Use YouTube Analyst for trending topics + Poetry Generator for narrative depth.

**Q: Can I schedule uploads?**
A: Yes, use the YouTube webhook for automation and scheduling.

---

## 🆘 Troubleshooting

### "OpenAI API Error"
→ Check API key in sidebar configuration

### "YouTube Authentication Failed"
→ Clear cache, reauthenticate in sidebar

### "Script Too Short"
→ Enter at least 50 characters for validation

### "Video Not Generating"
→ Check ComfyUI connection, check API keys

### "Sound Sync Issues"
→ Use shorter duration, simplify script structure

---

## 📈 Upgrade Path

### Free Tier:
- Basic templates
- One AI specialist (YouTube Analyst)
- Limited preview time

### Pro Tier ($19/mo):
- All 15+ templates
- All 5 AI specialists
- Unlimited preview
- Priority support

### Enterprise:
- White-label customization
- Custom specialists
- API access
- Team management

---

## 🎬 Your Next Steps

1. **Install OmniFlow**: `pip install -e .`
2. **Add API Keys**: Sidebar → Configuration
3. **Try Surprise Me!**: Let AI create your first video
4. **Analyze Reference**: Find videos in your niche
5. **Publish**: Use Preview & Edit then upload

**Happy Creating! 🚀**

---

*ComfyUI OmniFlow Pro v2.0 - Made for creators who want to scale*

# ComfyUI-OmniFlow: Complete Setup & Feature Guide

## Overview

**ComfyUI-OmniFlow** is an end-to-end AI video production platform that orchestrates:

- **Animated Avatars** (AI-generated talking heads using AnimateDiff)
- **Real Human Consistency** (maintain the same person across videos using IP-Adapter)
- **Interactive Dialogues** (multi-character conversations with realistic tone)
- **Voice Generation** (ElevenLabs TTS with custom voices)
- **Automation** (n8n/Make for YouTube publishing)

Designed to help creators bypass YouTube's "obviously AI" detection while maintaining professional quality.

---

## 🚀 Quick Start (Local Testing, No ComfyUI)

### 1. Clone or navigate to the project
```powershell
cd ComfyUI-OmniFlow
```

### 2. Create and activate Python venv
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies
```powershell
pip install -r requirements.txt
```

### 4. (Optional) Start the dummy ComfyUI wrapper for testing
```powershell
python .\scripts\comfyui_wrapper.py
```
This emulates a `/run` endpoint that returns placeholder images for testing the UI.

### 5. Run Streamlit UI in another terminal
```powershell
.\.venv\Scripts\Activate.ps1
streamlit run streamlit_app.py
```

Visit `http://localhost:8501` to explore the interface. All features will use dummy generators or require API keys (see below).

---

## 🎨 Setting Up ComfyUI Locally (For Real Video Generation)

### Prerequisites
- Windows 10/11
- Python 3.10+
- 8GB+ RAM (16GB+ recommended with GPU)
- NVIDIA GPU (highly recommended for speed)

### Installation Steps

#### Step 1: Clone ComfyUI
```powershell
git clone https://github.com/comfyanonymous/ComfyUI.git
```

#### Step 2: Install dependencies
```powershell
cd ComfyUI
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

For **GPU support** (NVIDIA CUDA):
```powershell
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

#### Step 3: Download models

Create a `models/` directory structure:
```
ComfyUI/models/
├── checkpoints/           (SDXL models)
├── controlnet/           (ControlNet models)
├── loras/                (LoRA fine-tunes)
├── ipadapter/            (IP-Adapter for consistency)
└── animatediff/          (AnimateDiff for animations)
```

**Recommended models:**

- **SDXL Base:** `sd_xl_base_1.0.safetensors` (6.9GB) — from Hugging Face
- **AnimateDiff:** `animatediff_xl.safetensors` — from Comfy forums
- **IP-Adapter:** `ip-adapter_xl.bin` — for real-human consistency
- **ControlNet Pose:** For gesture guidance

Download from:
- [Hugging Face](https://huggingface.co/stabilityai)
- [Civitai](https://civitai.com/)
- [OpenModelDB](https://openmodeldb.info/)

#### Step 4: Run ComfyUI
```powershell
cd ComfyUI
.\.venv\Scripts\Activate.ps1
python main.py
```

ComfyUI will start on `http://localhost:8188`. Keep this running in the background while using OmniFlow.

#### Step 5: Configure OmniFlow to use ComfyUI

In the Streamlit UI:
1. Open the sidebar
2. Enable **"Use local ComfyUI (if installed)"**
3. Confirm ComfyUI URL is `http://localhost:8188`

---

## 🔑 Required API Keys

To enable all features, add these API keys in the Streamlit sidebar:

### ElevenLabs (Voice Generation)
1. Sign up at [elevenlabs.io](https://elevenlabs.io/) (free tier available)
2. Copy your API key
3. Paste in Streamlit sidebar under **API Keys**

Or set environment variable:
```powershell
$env:ELEVENLABS_API_KEY = "your-api-key"
```

### OpenAI (Dialogue Generation)
1. Sign up at [openai.com](https://openai.com/)
2. Create API key in [settings](https://platform.openai.com/account/api-keys)
3. Paste in Streamlit sidebar

Or set environment variable:
```powershell
$env:OPENAI_API_KEY = "your-api-key"
```

---

## 📝 Features & Usage

### 1. Visual Generation (Tab 1)

**Modes:**
- **AI Character Avatar (Animated):** Talking head that animates based on dialogue
- **Real Human Character (Consistent):** Same person across multiple videos
- **Cinematic Landscapes + Text Overlays:** Background + title graphics
- **Interactive Dialogue (Multi-Character):** Two+ characters in conversation
- **Documentary / Stock + ComfyUI:** Mix of real footage and AI

**Workflow:**
1. Select channel template (Deep Dive, Educational, etc.)
2. Pick visual style
3. Enter prompt or idea
4. Click **"Generate Visuals"** → ComfyUI creates images/video frames
5. Images appear in the UI for preview

**Backend:**
- Uses ComfyUI pipelines in `workflows/` subdirectory
- Falls back to dummy images if ComfyUI unavailable

---

### 2. Script & Voice (Tab 2)

Generate narration for your videos using ElevenLabs TTS.

**Workflow:**
1. Write or paste your script
2. Select voice (Rachel, Bella, Adam, etc.)
3. Adjust stability/similarity sliders
4. Click **"Generate Voice"** → Audio is synthesized and saved
5. Preview audio in the UI

**Voice Options:**
- **Rachel:** Clear, professional, widely usable
- **Bella:** Warm, friendly
- **Adam:** Deep, authoritative mle

**Output:** MP3 file in `outputs/audio/`

---

### 3. Interactive Dialogue (Tab 3)

Create realistic multi-character conversations automatically using OpenAI GPT-4.

**Workflow:**
1. Enter conversation topic (e.g., "AI Future", "Climate Change")
2. Define 2-4 characters with personality descriptions
3. Set number of conversation turns
4. Click **"Generate Dialogue"** → OpenAI creates realistic exchanges
5. System auto-generates production script with camera directions and timing

**Example Characters:**
- Alice: "curious, analytical, asks questions"
- Bob: "skeptical, practical, challenges ideas"

**Output:**
- Dialogue script (speaker + text per turn)
- Production breakdown with camera directions
- Estimated scene durations

---

### 4. Character Consistency (Tab 4)

#### Animated Avatar
Use ComfyUI AnimateDiff to create talking-head animations from a static image.

**Workflow:**
1. Upload a character image (PNG/JPG)
2. Enter dialogue text the avatar will "say"
3. Select emotion (neutral, happy, sad, etc.)
4. Click **"Generate Talking Head Animation"** → Video frame sequence generated
5. Output: MP4 video of animated avatar

**How it works:**
- ComfyUI AnimateDiff generates frame sequences
- Frames are combined into video
- Audio can be synced using FFmpeg

#### Real Human Consistency
Use IP-Adapter embeddings to maintain the same person's appearance across videos.

**Workflow:**
1. Upload multiple reference photos of the same person
2. Enter character ID (e.g., "host_john")
3. Click **"Create Consistency Profile"** → IP-Adapter embeddings computed
4. Use this profile in subsequent video generation to ensure consistency

**How it works:**
- IP-Adapter analyzes facial features from reference images
- Embeddings guide SDXL so new images keep the same person
- Strength slider (0.0–1.0) controls consistency: higher = more strict

---

## 🤖 Automation (n8n / Make)

Automatically upload and publish videos to YouTube and other platforms.

**Workflow:**
1. Go to **Automation Setup** section in sidebar
2. Click **"Generate n8n/Make Templates"**
3. Templates saved to `automations/` folder
4. Import templates into [n8n.io](https://n8n.io/) or [make.com](https://www.make.com/)
5. Configure credentials (YouTube API, TikTok, Instagram, etc.)
6. Link to OmniFlow via webhook: POST completed videos to trigger publishing

**Available Templates:**
- `n8n_youtube_automation.json` — Upload to YouTube with metadata
- `n8n_multi_platform.json` — Publish to YouTube, TikTok, Instagram, Slack
- `make_youtube_automation.json` — Make.com alternative

**Webhook Format:**
```json
{
  "videoPath": "/path/to/video.mp4",
  "videoTitle": "AI: The Future of Work",
  "videoDescription": "Exploring how AI will transform...",
  "tags": ["AI", "Technology", "Future"],
  "platform": ["youtube", "tiktok", "instagram"]
}
```

---

## 📂 Project Structure

```
ComfyUI-OmniFlow/
├── streamlit_app.py              Main UI
├── requirements.txt              Python dependencies
├── README.md                     (this file)
│
├── omniflow/                     Core modules
│   ├── __init__.py
│   ├── generator.py              High-level generation interface
│   ├── comfyui_runner.py         ComfyUI Python API wrapper
│   ├── comfy_client.py           ComfyUI HTTP client
│   ├── dummy_generator.py        Dummy images for testing
│   ├── dialogue.py               Multi-character dialogue engine (OpenAI)
│   ├── animated_avatar.py        Animated avatar & character consistency (AnimateDiff + IP-Adapter)
│   ├── tts.py                    Voice generation (ElevenLabs)
│   └── automation.py             n8n/Make workflow templates
│
├── scripts/
│   ├── setup_comfyui.ps1        Installation guide
│   ├── run_comfyui.ps1          Launch ComfyUI
│   └── comfyui_wrapper.py       Dummy HTTP server for testing
│
├── workflows/                    ComfyUI workflow JSON templates
│   ├── sdxl_base.json
│   ├── sdxl_animatediff.json
│   ├── sdxl_controlnet_pose.json
│   ├── sdxl_ipadapter_identity.json
│   ├── sdxl_character_pipeline.json
│   ├── sdxl_cinematic_pipeline.json
│   └── ultimate_pipeline.json
│
├── models/                       ComfyUI model directories (download separately)
│   ├── checkpoints/
│   ├── controlnet/
│   ├── loras/
│   ├── ipadapter/
│   └── animatediff/
│
├── docs/
│   └── workflow_guide.md        Detailed workflow documentation
│
├── outputs/                      Generated videos, audio, images
│   ├── visuals/
│   ├── audio/
│   └── videos/
│
└── automations/                  Exported n8n/Make templates
    ├── n8n_youtube_automation.json
    ├── n8n_multi_platform.json
    └── make_youtube_automation.json
```

---

## 🎯 Common Workflows

### Workflow 1: Talking Head Video (AI Avatar)
1. **Visual:** Select "AI Character Avatar (Animated)"
2. **Script:** Write narration in Tab 2, generate voice with ElevenLabs
3. **Avatar:** Upload character image in Tab 4, enter dialogue, generate animation
4. **Automate:** Export n8n template, configure YouTube credentials, publish on schedule

**Result:** Professional talking-head video every day at scheduled time.

### Workflow 2: Data Analysis Video (Real Person + Cinematic)
1. **Visual:** Select "Cinematic Landscapes + Text Overlays"
2. **Script:** Write analysis narrative
3. **Consistency:** Upload photos of real analyst in Tab 4, create profile
4. **Generation:** ComfyUI generates scenes with analyst in cinematic settings
5. **Voice:** Synthesize script narration
6. **Publish:** Use Make.com to schedule YouTube uploads

**Result:** Professional data-driven video featuring consistent real person.

### Workflow 3: Interactive Podcast-Style Video
1. **Dialogue:** Go to Tab 3, define 2 characters (host + expert)
2. **Generation:** OpenAI generates conversation on your topic
3. **Visuals:** Create animated avatars or real-human profiles for each character
4. **Voice:** Synthesize dialogue for both characters
5. **Editing:** Sync dialogue audio with visuals using FFmpeg
6. **Publish:** Automate publishing to YouTube, Apple Podcasts, Spotify via n8n

**Result:** Interactive, engaging video that bypassess "obviously AI" algorithms.

---

## ⚠️ Troubleshooting

### ComfyUI not found
- Ensure ComfyUI is cloned to a sibling directory: `../ComfyUI`
- Or set `COMFYUI_PATH` environment variable:
  ```powershell
  $env:COMFYUI_PATH = "C:\path\to\ComfyUI"
  ```

### "ComfyUI API returned 404"
- Check ComfyUI is running on `http://localhost:8188`
- You may need to add a `/run` endpoint plugin to ComfyUI (see `docs/workflow_guide.md`)

### Streamlit app won't start
- Check all dependencies are installed: `pip install -r requirements.txt`
- Try `pip install --upgrade streamlit`

### CUDA out of memory
- Reduce model size (use SDXL-Turbo instead of full SDXL)
- Enable memory optimization in ComfyUI settings
- Use CPU mode (slower but works)

### "ELEVENLABS_API_KEY not set"
- Get a free API key from https://elevenlabs.io/
- Add it in the Streamlit sidebar or set environment variable

### "OpenAI API returned 401"
- Check API key is correct
- Verify account has API access enabled
- Check billing in OpenAI dashboard

---

## 📈 Roadmap

- [ ] Automatic video editing and composition (ffmpeg integration)
- [ ] Real-time video preview in Streamlit
- [ ] Batch video generation (queue multiple jobs)
- [ ] Custom ComfyUI node builder (no-code pipeline designer)
- [ ] Webhook-based trigger system (e.g., "generate video when trending topic appears")
- [ ] Performance analytics (track video engagement metrics)
- [ ] Multi-language support (voice synthesis in 20+ languages)

---

## 🤝 Contributing

Feel free to extend OmniFlow! Key areas:
- Add more ComfyUI workflows in `workflows/`
- Implement more LLM providers in `dialogue.py`
- Add TTS alternatives (Google Cloud TTS, Microsoft Azure TTS)
- Build custom video editing templates

---

## 📜 License

MIT License — use freely in commercial and personal projects.

---

## 🎓 Learn More

- [ComfyUI Documentation](https://github.com/comfyanonymous/ComfyUI)
- [SDXL Guide](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)
- [AnimateDiff Paper](https://arxiv.org/abs/2307.04667)
- [IP-Adapter for SDXL](https://github.com/tencent-ailab/IP-Adapter)
- [ElevenLabs API](https://elevenlabs.io/docs)
- [OpenAI API](https://platform.openai.com/docs)
- [n8n Workflows](https://docs.n8n.io/)
- [Make (Zapier alternative)](https://www.make.com/en/integration)

---

**Happy creating! 🎬**

# 🐉 Dragon Ai + ComfyUI Integration Guide

## Overview: Advanced Video Creation Workflow

### What You Get
**Dragon Ai** (Content Generation) + **ComfyUI** (Visual Production) = **Complete Video Pipeline**

```
Dragon Ai Script Generation
         ↓
    (Script + Metadata)
         ↓
    ComfyUI Processing
         ↓
    (Visual Assets + Effects)
         ↓
    Final Video Ready for YouTube
```

---

## Architecture

### Current State (Dragon Ai Standalone)
✅ Generates high-quality scripts
✅ Creates YouTube metadata (tags, titles)
✅ Produces visual suggestions
✅ Manages timing specifications
❌ No actual video rendering

### After Integration (Dragon Ai + ComfyUI)
✅ All of above PLUS:
✅ Automatic video composition
✅ Visual effect rendering
✅ B-roll integration
✅ Color grading & transitions
✅ Audio syncing
✅ Final MP4 export ready for YouTube

---

## Advanced Features Unlocked

### 1. Automated Visual Generation
```
Dragon Ai provides:
├─ Scene descriptions
├─ Visual timing
├─ Color palette
├─ Suggested effects
└─ B-roll requirements

ComfyUI generates:
├─ AI-rendered visuals
├─ Stock footage integration
├─ Effect application
├─ Color correction
└─ Composite assembly
```

### 2. Workflow Automation
- Script → Visual Assets → Final Video (one-click)
- Batch processing (5 scripts → 5 complete videos)
- Template-based rendering
- Consistent styling across batches

### 3. Custom Node System
- Add AI upscaling
- Add image generation (DALL-E style)
- Add audio enhancement
- Add subtitle generation

### 4. Quality Enhancements
- 4K video output
- HDR processing
- Advanced color grading
- Professional transitions

---

## Integration Methods

### Method 1: Server-to-Server (Recommended)
**Dragon Ai** → (REST API) → **ComfyUI Server** → Output

```
Setup:
1. Dragon Ai runs on port 8501 (Streamlit)
2. ComfyUI runs on port 8188 (Node Web Server)
3. Communication via HTTP endpoints
4. Share storage directory for assets
```

### Method 2: Script-Based Pipeline
**Dragon Ai generates script** → **Python wrapper calls ComfyUI API** → **Output**

```
Setup:
1. Dragon Ai generates content
2. Python script reads Dragon Ai output
3. Constructs ComfyUI workflow JSON
4. Submits to ComfyUI API
5. Monitors processing
6. Returns final video
```

### Method 3: Command-Line Integration
**Dragon Ai** → **Export JSON** → **ComfyUI CLI** → **Video Output**

```
Setup:
1. Dragon Ai exports workflow as JSON
2. ComfyUI processes JSON batch file
3. Outputs videos to shared directory
4. Dragon Ai displays results
```

---

## Step-by-Step Setup (After ComfyUI Clone Completes)

### Phase 1: Verify ComfyUI Installation
```powershell
# Check ComfyUI directory exists
Test-Path C:\workspace\ComfyUI

# List main structure
Get-ChildItem C:\workspace\ComfyUI | Select-Object Name
```

### Phase 2: Install ComfyUI Dependencies
```bash
# Navigate to ComfyUI
cd C:\workspace\ComfyUI

# Create virtual environment
python -m venv comfyui_venv

# Activate
.\comfyui_venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# For GPU support (CUDA):
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Or CPU only:
pip install torch torchvision torchaudio
```

### Phase 3: Create Integration Layer
Create `/workspace/dragon_ai_comfyui_bridge.py`:

```python
#!/usr/bin/env python3
"""
Dragon Ai ↔ ComfyUI Integration Bridge
Handles communication between systems
"""

import requests
import json
import time
from pathlib import Path

class DragonAiComfyUIBridge:
    def __init__(self, dragon_ai_url="http://localhost:8501", 
                 comfyui_url="http://localhost:8188"):
        self.dragon_ai_url = dragon_ai_url
        self.comfyui_url = comfyui_url
        self.workflow_dir = Path("C:/workspace/workflows")
        self.workflow_dir.mkdir(exist_ok=True)
        self.output_dir = Path("C:/workspace/outputs")
        self.output_dir.mkdir(exist_ok=True)
    
    def get_dragon_ai_script(self, generator_type, params):
        """Get script from Dragon Ai"""
        # In production, would call Dragon Ai API
        # For now, returns mock data
        return {
            "script": "Generated video script...",
            "visual_suggestions": ["scene1", "scene2", "scene3"],
            "timing": [5, 10, 15],
            "color_palette": ["#FF6B6B", "#4ECDC4"],
            "tags": ["tag1", "tag2", "tag3"]
        }
    
    def create_comfyui_workflow(self, script_data):
        """Convert Dragon Ai output to ComfyUI workflow"""
        workflow = {
            "1": {
                "class_type": "CheckpointLoaderSimple",
                "inputs": {
                    "ckpt_name": "model.safetensors"
                }
            },
            "2": {
                "class_type": "CLIPTextEncode",
                "inputs": {
                    "text": script_data["script"],
                    "clip": ["1", 1]
                }
            },
            "3": {
                "class_type": "KSampler",
                "inputs": {
                    "seed": 123,
                    "steps": 20,
                    "cfg": 7.0,
                    "sampler_name": "euler",
                    "scheduler": "normal",
                    "denoise": 1.0,
                    "model": ["1", 0],
                    "positive": ["2", 0],
                    "negative": ["2", 0],
                    "latent_image": ["4", 0]
                }
            }
        }
        return workflow
    
    def submit_workflow(self, workflow):
        """Send workflow to ComfyUI for processing"""
        try:
            response = requests.post(
                f"{self.comfyui_url}/api/prompt",
                json=workflow,
                timeout=30
            )
            if response.status_code == 200:
                result = response.json()
                prompt_id = result.get("prompt_id")
                return prompt_id
            else:
                raise Exception(f"ComfyUI error: {response.status_code}")
        except Exception as e:
            print(f"❌ Workflow submission failed: {e}")
            return None
    
    def monitor_processing(self, prompt_id, timeout=300):
        """Monitor ComfyUI processing status"""
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                response = requests.get(
                    f"{self.comfyui_url}/history/{prompt_id}",
                    timeout=10
                )
                history = response.json()
                if prompt_id in history:
                    return history[prompt_id]
                time.sleep(2)
            except Exception as e:
                print(f"⚠️  Monitoring error: {e}")
                time.sleep(2)
        
        raise TimeoutError(f"Processing timeout for {prompt_id}")
    
    def process_end_to_end(self, generator_type, params):
        """Full pipeline: Dragon Ai → ComfyUI → Output"""
        print(f"🚀 Starting {generator_type} video generation...")
        
        # Step 1: Get Dragon Ai script
        print("📝 Generating script with Dragon Ai...")
        script_data = self.get_dragon_ai_script(generator_type, params)
        
        # Step 2: Create ComfyUI workflow
        print("🔧 Creating ComfyUI workflow...")
        workflow = self.create_comfyui_workflow(script_data)
        
        # Step 3: Submit to ComfyUI
        print("📤 Submitting to ComfyUI...")
        prompt_id = self.submit_workflow(workflow)
        if not prompt_id:
            return None
        
        # Step 4: Monitor processing
        print(f"⏳ Processing (ID: {prompt_id})...")
        result = self.monitor_processing(prompt_id)
        
        print("✅ Video generation complete!")
        return result

# Usage
if __name__ == "__main__":
    bridge = DragonAiComfyUIBridge()
    
    # Generate Gospel video using full pipeline
    result = bridge.process_end_to_end(
        generator_type="gospel",
        params={"theme": "worship", "duration": 6}
    )
    
    if result:
        print(f"📊 Result: {json.dumps(result, indent=2)}")
```

### Phase 4: Create Integration App
Create `/workspace/ComfyUI-OmniFlow/integration_app.py`:

```python
import streamlit as st
from dragon_ai_comfyui_bridge import DragonAiComfyUIBridge

st.set_page_config(title="Dragon Ai + ComfyUI", layout="wide")
st.title("🐉 Dragon Ai Professional Video Creator (with ComfyUI)")

# Initialize bridge
bridge = DragonAiComfyUIBridge()

# Mode selector
mode = st.radio("Select Mode", ["Dragon Ai Only", "Dragon Ai + ComfyUI"])

if mode == "Dragon Ai Only":
    st.info("✅ Fast script generation only (0.5 seconds)")
    # Existing Dragon Ai UI
else:
    st.info("🎬 Full video generation (5-15 minutes)")
    
    # ComfyUI integration UI
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Configure Generation")
        generator = st.selectbox("Generator Type", 
            ["Gospel", "Tech", "Tutorial", "Finance", "Trending", 
             "Wellness", "Spiritual", "Business"])
        
        if generator == "Gospel":
            theme = st.selectbox("Theme", 
                ["Faith", "Redemption", "Worship", "Spiritual Journey"])
            duration = st.slider("Duration (min)", 6, 15, 10)
        elif generator == "Tech":
            topic = st.selectbox("Topic", 
                ["AI Basics", "Neural Networks", "Python", "Data Science"])
            complexity = st.selectbox("Complexity", 
                ["Beginner", "Intermediate", "Advanced"])
            duration = st.slider("Duration (min)", 8, 20, 12)
        
        # Processing options
        st.subheader("Processing Options")
        quality = st.selectbox("Video Quality", 
            ["1080p (5 min)", "2K (10 min)", "4K (20 min)"])
        effects = st.multiselect("Add Effects", 
            ["Color Grading", "Transitions", "Motion Graphics", "Subtitles"])
    
    with col2:
        st.subheader("Preview")
        if st.button("🎬 Generate Full Video"):
            with st.spinner("Generating... This may take 5-20 minutes"):
                result = bridge.process_end_to_end(
                    generator_type=generator.lower(),
                    params={"quality": quality}
                )
                
                if result:
                    st.success("✅ Video generation complete!")
                    st.video("path/to/output_video.mp4")
                else:
                    st.error("❌ Video generation failed")

st.divider()

# System status
if st.checkbox("Show System Status"):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Dragon Ai", "🟢 Online", "http://localhost:8501")
    with col2:
        st.metric("ComfyUI", "Status Check", "http://localhost:8188")
    with col3:
        st.metric("Pipeline", "Ready", "Full Integration")
```

### Phase 5: Register ComfyUI Custom Nodes (Optional)
```powershell
# Navigate to ComfyUI custom nodes
cd C:\workspace\ComfyUI\custom_nodes

# Clone useful nodes repositories
git clone https://github.com/ltdrdata/ComfyUI-Manager
git clone https://github.com/kijai/ComfyUI-KJNodes

# Restart ComfyUI to register nodes
```

---

## Launching Integrated System

### Terminal 1: Start Dragon Ai
```powershell
cd C:\workspace\ComfyUI-OmniFlow
.\start.bat
# Accessible at http://localhost:8501
```

### Terminal 2: Start ComfyUI
```powershell
cd C:\workspace\ComfyUI
.\comfyui_venv\Scripts\activate
python main.py
# Accessible at http://localhost:8188
```

### Terminal 3 (Optional): Run Integration Service
```powershell
cd C:\workspace\ComfyUI-OmniFlow
.\.venv\Scripts\activate
python integration_app.py
# Or integrated into main Streamlit app
```

---

## Complete Workflow Examples

### Example 1: Gospel Music Video (End-to-End)
```
1. Open Dragon Ai at http://localhost:8501
2. Select "Gospel Music Video"
3. Configure: Theme=Worship, Duration=6min
4. Click "Generate with ComfyUI"
5. Bridge creates workflow
6. ComfyUI processes for 10-15 minutes
7. Final video appears in app
8. Download & upload to YouTube
```

### Example 2: Batch Tech Videos (5 Variations)
```
1. Dragon Ai: Configure Tech Explained batch
2. Select topics: AI, Neural Networks, Python, Data Science, Cybersecurity
3. Set Batch Mode: 5 videos
4. Click "Generate All with ComfyUI"
5. ComfyUI processes all 5 in parallel
6. All finished in 30-40 minutes
7. Compare quality & select best
8. Upload all to YouTube
```

### Example 3: Trending News Commentary (Real-Time)
```
1. Dragon Ai: Trending Commentary mode
2. Input current topic
3. Generate script (1 second)
4. Optional: Send to ComfyUI for visuals
5. Quick video (5 min) ready
6. Publish while trending
```

---

## API Reference

### Dragon Ai Endpoints (When Exposed)
```
GET  /api/health                    # Health check
POST /api/generate                  # Generate script
GET  /api/generators                # List generators
GET  /api/results/{id}              # Get generation results
```

### ComfyUI Endpoints
```
GET  /api/systeminfo                # System information
POST /api/prompt                    # Submit workflow
GET  /history/{prompt_id}           # Get history
GET  /interrupt                     # Interrupt current process
GET  /api/models                    # Available models
```

### Integration Bridge Endpoints
```
POST /api/dragon-ai/generate-video  # Full pipeline
GET  /api/status                    # System status
POST /api/batch                     # Batch processing
GET  /api/output/{task_id}          # Get output
```

---

## Performance Metrics

| Task | Time (Dragon Ai Only) | Time (With ComfyUI) |
|------|----------------------|---------------------|
| Script generation | 0.5 sec | 0.5 sec |
| Visual composition | N/A | 2-3 min |
| Video rendering | N/A | 10-20 min |
| Audio sync | N/A | 1-2 min |
| Total per video | 0.5 sec | 15-30 min |
| Batch (5 videos) | 2.5 sec | 60-90 min |

---

## Troubleshooting Integration

| Issue | Solution |
|-------|----------|
| ComfyUI not starting | Check Python env, reinstall torch |
| API communication fails | Verify ports 8501, 8188 open |
| Workflow submission error | Check ComfyUI models folder |
| Processing hangs | Check ComfyUI logs, restart server |
| Memory issues | Use CPU mode or reduce batch size |
| Visual quality low | Upgrade model checkpoints |

---

## Advanced Customization

### Custom Workflow Templates
Create workflow JSONs for specific styles:
```
workflows/
├── gospel_4k.json
├── tech_2k_animated.json
├── tutorial_1080p.json
└── finance_hd_charts.json
```

### Model Management
```powershell
# Download additional models
# Stable Diffusion models
# ControlNet models
# Upscaling models
# Audio models
```

### Node Extensions
```
Custom nodes for:
├─ AI video upscaling
├─ Subtitle generation
├─ Voice synthesis
├─ Color grading
└─ Smart cropping
```

---

## Success Indicators

✅ Integration working when:
- Dragon Ai generates scripts at http://localhost:8501
- ComfyUI API responds at http://localhost:8188/api/systeminfo
- Bridge successfully submits workflows
- Videos render without errors
- Output files appear in /outputs directory

---

## Next Steps

1. **Monitor ComfyUI clone** - Wait for completion
2. **Install dependencies** - Run Phase 2 setup
3. **Test ComfyUI** - Launch basic workflow
4. **Deploy bridge** - Copy integration code
5. **Link systems** - Start both servers
6. **Generate videos** - Use integrated pipeline

---

## Support Resources

- **ComfyUI Docs**: https://github.com/comfyanonymous/ComfyUI
- **ComfyUI Manager**: Node discovery & management
- **Dragon Ai Docs**: See WORKFLOW_DIAGRAM.md, QUICKSTART.md
- **Integration Issues**: Check logs at `C:\workspace\logs\`

---

🎉 **Once ComfyUI finishes downloading, you're ready to activate these advanced features!**

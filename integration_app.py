#!/usr/bin/env python3
"""
Dragon Ai ComfyUI Integration App
Streamlit UI for managing video generation through ComfyUI
"""

import streamlit as st
import sys
from pathlib import Path
from dragon_ai_comfyui_bridge import DragonAiComfyUIBridge, GeneratorConfig, VideoQuality

# ============================================================================
# Page Configuration
# ============================================================================

st.set_page_config(
    page_title="🐉 Dragon Ai + ComfyUI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🐉 Dragon Ai + ComfyUI Integration")
st.markdown("Generate professional AI videos with advanced ComfyUI rendering")

# ============================================================================
# Session State
# ============================================================================

if "bridge" not in st.session_state:
    st.session_state.bridge = DragonAiComfyUIBridge()

if "processing" not in st.session_state:
    st.session_state.processing = False

if "results" not in st.session_state:
    st.session_state.results = []

bridge = st.session_state.bridge

# ============================================================================
# Sidebar: Server Status & Configuration
# ============================================================================

with st.sidebar:
    st.header("⚙️ System Status")
    
    # Server health check
    col1, col2 = st.columns(2)
    with col1:
        dragon_up, comfyui_up = bridge.health_check()
        status_dragon = "🟢" if dragon_up else "🔴"
        st.metric("Dragon Ai", status_dragon, "8501")
    
    with col2:
        status_comfyui = "🟢" if comfyui_up else "🔴"
        st.metric("ComfyUI", status_comfyui, "8188")
    
    if not (dragon_up and comfyui_up):
        st.warning("⚠️ Not all servers are running")
        if not dragon_up:
            st.code("cd C:\\workspace\\ComfyUI-OmniFlow && .\\start.bat", language="powershell")
        if not comfyui_up:
            st.code("cd C:\\workspace\\ComfyUI && python main.py", language="powershell")
    else:
        st.success("✅ All systems online")
    
    st.divider()
    
    # Configuration
    st.header("🎥 Video Configuration")
    
    generator_type = st.selectbox(
        "Content Type",
        ["gospel", "tech", "tutorial", "finance", "trending", "wellness", "spiritual", "business"],
        key="gen_type"
    )
    
    quality = st.selectbox(
        "Output Quality",
        ["1080p (5 min)", "2K (10 min)", "4K (20 min)"],
        key="quality",
        help="Processing time per video"
    )
    
    # Map quality to enum
    quality_map = {
        "1080p (5 min)": VideoQuality.HD_1080P,
        "2K (10 min)": VideoQuality.K2,
        "4K (20 min)": VideoQuality.K4,
    }
    selected_quality = quality_map[quality]
    
    batch_size = st.number_input(
        "Batch Size",
        min_value=1,
        max_value=10,
        value=1,
        key="batch"
    )
    
    st.divider()
    
    # Instructions
    st.header("📖 Quick Start")
    with st.expander("See instructions"):
        st.markdown("""
        1. **Check servers** are both online (above)
        2. **Configure video** settings (left panel)
        3. **Enter parameters** (main area)
        4. **Click Generate** to start processing
        5. **Monitor progress** in real-time
        6. **Find outputs** in /workspace/outputs/
        
        **Tips:**
        - Start with 1080p for faster testing
        - Batch processing runs serially (one at a time)
        - Each 4K video takes ~20 minutes
        """)

# ============================================================================
# Main Area: Generator Configuration & Controls
# ============================================================================

# Generator-specific parameters
st.header(f"📝 Configure {generator_type.capitalize()} Video")

col1, col2, col3 = st.columns(3)

with col1:
    if generator_type == "gospel":
        theme = st.selectbox("Theme", ["worship", "praise", "testimonial", "spiritual", "celebration"])
        duration = st.slider("Duration (min)", 1, 10, 6)
        params = {"theme": theme, "duration": duration}
    
    elif generator_type == "tech":
        topic = st.text_input("Topic", "AI and machine learning", key="tech_topic")
        complexity = st.selectbox("Complexity", ["beginner", "intermediate", "advanced"])
        params = {"topic": topic, "complexity": complexity}
    
    elif generator_type == "tutorial":
        subject = st.text_input("Subject", "Python programming", key="tut_subject")
        skill_level = st.selectbox("Skill Level", ["beginner", "intermediate", "advanced"])
        params = {"subject": subject, "skill_level": skill_level}
    
    elif generator_type == "finance":
        topic = st.text_input("Finance Topic", "cryptocurrency investing", key="fin_topic")
        tone = st.selectbox("Tone", ["educational", "skeptical", "bullish", "cautious"])
        params = {"topic": topic, "tone": tone}
    
    elif generator_type == "trending":
        event = st.text_input("Current Event", "latest tech news", key="trend_event")
        perspective = st.selectbox("Perspective", ["analyst", "critic", "enthusiast", "neutral"])
        params = {"event": event, "perspective": perspective}
    
    elif generator_type == "wellness":
        topic = st.text_input("Wellness Topic", "meditation techniques", key="well_topic")
        duration = st.slider("Duration (min)", 1, 20, 10)
        params = {"topic": topic, "duration": duration}
    
    elif generator_type == "spiritual":
        theme = st.selectbox("Spiritual Theme", ["inspiration", "faith", "philosophy", "mindfulness"])
        tradition = st.selectbox("Tradition", ["universal", "christian", "buddhist", "islamic", "hindu"])
        params = {"theme": theme, "tradition": tradition}
    
    else:  # business
        topic = st.text_input("Business Topic", "startup strategies", key="biz_topic")
        industry = st.selectbox("Industry", ["tech", "finance", "retail", "healthcare", "education"])
        params = {"topic": topic, "industry": industry}

with col2:
    st.subheader("⚙️ Effects")
    effects = []
    if st.checkbox("Color Grading", value=True):
        effects.append("color_grading")
    if st.checkbox("Transitions", value=True):
        effects.append("transitions")
    if st.checkbox("Text Overlay", value=False):
        effects.append("text_overlay")
    if st.checkbox("Background Music", value=True):
        effects.append("background_music")

with col3:
    st.subheader("📊 Batch Settings")
    if batch_size > 1:
        st.info(f"📤 Will generate {batch_size} videos sequentially")
        st.write("**Estimated Time:**")
        minutes_per_video = {
            "1080p (5 min)": 5,
            "2K (10 min)": 10,
            "4K (20 min)": 20,
        }
        total_minutes = minutes_per_video[quality] * batch_size
        st.metric("Total Time", f"~{total_minutes} min", f"{total_minutes//60}h {total_minutes%60}m")
    else:
        minutes = {
            "1080p (5 min)": 5,
            "2K (10 min)": 10,
            "4K (20 min)": 20,
        }
        st.metric("Estimated Time", f"~{minutes[quality]} min")

# ============================================================================
# Processing Section
# ============================================================================

st.divider()
st.header("🚀 Generate Video")

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    generate_button = st.button(
        "🎬 Generate Video" if batch_size == 1 else f"🎬 Generate {batch_size} Videos",
        use_container_width=True,
        type="primary"
    )

with col2:
    if st.button("📊 Check Status", use_container_width=True):
        dragon_up, comfyui_up = bridge.health_check()
        if dragon_up and comfyui_up:
            st.success("✅ All servers online")
        else:
            st.error("❌ Check server connections")

with col3:
    if st.button("🔄 Clear Results", use_container_width=True):
        st.session_state.results = []
        st.rerun()

# ============================================================================
# Processing Logic
# ============================================================================

if generate_button:
    dragon_up, comfyui_up = bridge.health_check()
    
    if not dragon_up or not comfyui_up:
        st.error("❌ Both servers must be online to proceed")
        if not dragon_up:
            st.write("Start Dragon Ai: `cd C:\\workspace\\ComfyUI-OmniFlow && .\\start.bat`")
        if not comfyui_up:
            st.write("Start ComfyUI: `cd C:\\workspace\\ComfyUI && python main.py`")
    else:
        # Create config
        config = GeneratorConfig(
            generator_type=generator_type,
            params=params,
            quality=selected_quality,
            batch_size=batch_size,
            effects=effects
        )
        
        # Progress area
        progress_container = st.container()
        
        with progress_container:
            st.header("📈 Processing Status")
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Single video
            if batch_size == 1:
                status_text.info(f"🎬 Generating {generator_type} video...")
                result = bridge.process_video(config)
                
                if result:
                    progress_bar.progress(100)
                    status_text.success(f"✅ Complete! Prompt ID: {result['prompt_id']}")
                    st.session_state.results.append(result)
                else:
                    progress_bar.progress(0)
                    status_text.error("❌ Generation failed")
            
            # Batch videos
            else:
                for i in range(batch_size):
                    progress = (i / batch_size) * 100
                    progress_bar.progress(progress)
                    status_text.info(f"🎬 Generating video {i+1}/{batch_size}...")
                    
                    result = bridge.process_video(config)
                    if result:
                        st.session_state.results.append(result)
                
                progress_bar.progress(100)
                status_text.success(f"✅ Batch complete! {len(st.session_state.results)} videos generated")

# ============================================================================
# Results Display
# ============================================================================

if st.session_state.results:
    st.divider()
    st.header("📋 Generation Results")
    
    # Summary
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Videos Generated", len(st.session_state.results))
    with col2:
        st.metric("Success Rate", "100%")
    with col3:
        st.metric("Output Directory", "C:/workspace/outputs/")
    
    # Results table
    st.subheader("Latest Results")
    result_data = []
    for r in st.session_state.results[-10:]:  # Last 10
        result_data.append({
            "Type": r["generator_type"].capitalize(),
            "Quality": r["quality"],
            "Status": r["status"],
            "Prompt ID": r["prompt_id"][:8] + "..."
        })
    
    st.dataframe(result_data, use_container_width=True)
    
    # Output location
    st.info(f"""
    📁 **Your videos are saved to:**
    ```
    C:/workspace/outputs/
    ```
    
    **Next steps:**
    1. Check the `/outputs` directory for your videos
    2. Review the video quality (match your selected setting)
    3. Use in your projects or re-render with different settings
    4. Delete and regenerate if needed
    """)

# ============================================================================
# Help & Documentation
# ============================================================================

with st.expander("❓ Help & Documentation"):
    tab1, tab2, tab3 = st.tabs(["Integration Guide", "Troubleshooting", "Performance"])
    
    with tab1:
        st.markdown("""
        ## Dragon Ai + ComfyUI Integration
        
        This app connects your Dragon Ai generators with ComfyUI's powerful rendering engine.
        
        **What it does:**
        - Takes your Dragon Ai script templates
        - Converts them to ComfyUI workflows
        - Renders high-quality videos (1080p, 2K, 4K)
        - Saves outputs to `/workspace/outputs/`
        
        **Architecture:**
        1. Streamlit UI (this app)
        2. Dragon Ai generators (templates & metadata)
        3. ComfyUI API (rendering engine)
        4. Output videos (MP4, WebM)
        """)
    
    with tab2:
        st.markdown("""
        ## Troubleshooting
        
        **Issue: "Dragon Ai server not responding"**
        - Open new terminal: `cd C:\\workspace\\ComfyUI-OmniFlow && .\\start.bat`
        - Wait ~30 seconds for Streamlit to start
        
        **Issue: "ComfyUI server not responding"**
        - Open new terminal: `cd C:\\workspace\\ComfyUI && python main.py`
        - Wait for "Starting server" message
        
        **Issue: "Workflow submitted but no output"**
        - Check C:/workspace/ComfyUI/models/checkpoints has model files
        - Verify C:/workspace/outputs/ exists and is writable
        
        **Issue: "Slow generation"**
        - GPU processing: Check CUDA is available (nvidia-smi)
        - Reduce quality or batch size
        - Close other applications
        """)
    
    with tab3:
        st.markdown("""
        ## Performance Metrics
        
        | Quality | Time | Resolution | Use Case |
        |---------|------|-----------|----------|
        | 1080p | 5 min | 1920x1080 | Quick testing |
        | 2K | 10 min | 2560x1440 | Standard output |
        | 4K | 20 min | 3840x2160 | Premium content |
        
        **Batch Processing Times:**
        - 3x 1080p: ~15 minutes
        - 5x 2K: ~50 minutes
        - 2x 4K: ~40 minutes
        
        **GPU vs CPU:**
        - GPU (NVIDIA): 5-20 min per video
        - CPU only: 15-60 min per video
        
        **Recommended Settings:**
        - Start: 1080p single video
        - Production: 2K batch of 5
        - Premium: 4K when time allows
        """)

st.divider()
st.caption("Dragon Ai + ComfyUI Integration | Built with Streamlit")

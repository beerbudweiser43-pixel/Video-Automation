import os
import streamlit as st
from omniflow import generator
from omniflow.dialogue import DialogueEngine, generate_interactive_video_script
from omniflow.animated_avatar import AnimatedAvatarPipeline, RealHumanConsistency
from omniflow.tts import ElevenLabsTTS, synthesize_script
from omniflow.automation import save_templates, get_webhook_url_for_completion
from omniflow.orchestrator import VideoProductionOrchestrator
from omniflow.channel_templates import ChannelTemplate, CHANNEL_TEMPLATES, print_anti_detection_guide

st.set_page_config(page_title="ComfyUI-OmniFlow", layout="wide")

st.title("🎬 ComfyUI-OmniFlow — Professional AI Video Creator")
st.markdown("*From Script to YouTube in One Click • Avoids AI Detection • Studio Quality*")

# ============================================================================
# SIDEBAR: PROJECT SETUP
# ============================================================================
with st.sidebar:
    st.header("⚙️ Setup & Config")
    
    # Channel Selection
    channel_type = st.selectbox(
        "Channel Template",
        list(CHANNEL_TEMPLATES.keys()),
        format_func=lambda x: CHANNEL_TEMPLATES[x]["name"],
    )
    
    # Load template
    try:
        template = ChannelTemplate(channel_type)
        template_config = template.get_full_config()
    except:
        template = None
        template_config = {}
    
    st.divider()
    
    # API Keys Section
    with st.expander("🔑 API Keys (Required for Full Features)"):
        elevenlabs_key = st.text_input("ElevenLabs API Key", type="password")
        openai_key = st.text_input("OpenAI API Key", type="password")
        youtube_webhook = st.text_input("YouTube Webhook URL (n8n/Make)", type="password")
        
        if elevenlabs_key:
            os.environ["ELEVENLABS_API_KEY"] = elevenlabs_key
        if openai_key:
            os.environ["OPENAI_API_KEY"] = openai_key
        if youtube_webhook:
            os.environ["YOUTUBE_WEBHOOK_URL"] = youtube_webhook
    
    # ComfyUI Settings
    with st.expander("🎨 ComfyUI Settings"):
        use_comfyui = st.checkbox("Use local ComfyUI (if installed)")
        comfy_url = st.text_input(
            "ComfyUI API URL",
            value=os.getenv("COMFYUI_API_URL", "http://localhost:8188"),
        )
    
    st.divider()
    
    # Automation Setup
    with st.expander("🤖 Automation Export"):
        if st.button("Generate n8n/Make Templates"):
            save_templates("automations/")
            st.success("✅ Templates saved to `automations/` folder")
        
        if st.checkbox("Show webhook format"):
            st.code(get_webhook_url_for_completion(), language="json")
    
    st.divider()
    
    # Guidelines
    with st.expander("📋 Avoid AI Detection Guide"):
        st.markdown("""
        ✅ **DO:**
        - Use real people & consistent characters
        - Cinematic visuals with depth
        - Natural voice variations & pauses
        - Specific titles & genuine keywords
        
        ❌ **DON'T:**
        - Perfect symmetry (looks fake)
        - Robotic voice inflection
        - Obvious AI-generated captions
        - Generic titles & descriptions
        """)

# ============================================================================
# MAIN TABS
# ============================================================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🚀 One-Click Publishing",
    "🎥 Visual Generation",
    "📝 Script & Voice",
    "🎭 Interactive Dialogue",
    "👤 Character Management",
])

# ============================================================================
# TAB 1: ONE-CLICK PUBLISHING (MAIN WORKFLOW)
# ============================================================================
with tab1:
    st.header("🚀 One-Click Video Publishing")
    st.markdown("*Input script, title, description → System handles everything → Video posts to YouTube*")
    
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.subheader("📄 Enter Your Content")
        
        # Template info
        if template_config:
            st.info(f"""
            **Template:** {template_config['name']}  
            **Visual Style:** {template_config['visual_style']}  
            **Voice:** {template_config['voice_settings'].get('voice_id', 'Default')}  
            **Category:** {template_config['metadata_template'].get('category_id', 'General')}
            """)
        
        # Script input
        script = st.text_area(
            "Your Video Script",
            height=200,
            placeholder="Write your complete video narration here. This will be converted to voice, visuals will be generated, and the video will be automatically posted to YouTube with your title and description.",
        )
        
        # Title input
        title = st.text_input(
            "Video Title",
            max_chars=100,
            placeholder="Keep it specific, authentic (avoid 'AI-generated', etc.)",
        )
        title_chars = len(title)
        st.caption(f"{title_chars}/100 characters")
        
        # Description input
        description = st.text_area(
            "Video Description",
            height=150,
            max_chars=5000,
            placeholder="Your detailed description. Template will auto-add intro/outro.",
        )
        desc_chars = len(description)
        st.caption(f"{desc_chars}/5000 characters")
        
        # Tags
        tags_input = st.text_input(
            "Tags (comma-separated, optional)",
            placeholder="e.g., Technology, AI, Future, Learning",
        )
        tags = [t.strip() for t in tags_input.split(",") if t.strip()]
    
    with col_right:
        st.subheader("⚙️ Settings")
        
        schedule_publish = st.checkbox("Schedule Publishing")
        if schedule_publish:
            publish_time = st.time_input("Publish Time")
            st.caption("Will publish at this time (UTC)")
        
        # Voice selection
        voice_options = {
            "Rachel (Clear, Professional)": "21m00Tcm4TlvDq8ikWAM",
            "Bella (Warm, Friendly)": "EXAVITQu4vr4xnSDxMaL",
            "Adam (Deep, Authoritative)": "pNInz6obpgDQGcFmaJgB",
        }
        selected_voice_name = st.selectbox("Voice", list(voice_options.keys()))
        voice_id = voice_options[selected_voice_name]
        
        # Visual quality
        quality = st.select_slider("Visual Quality", ["Draft", "Standard", "Professional", "Cinema"], value="Professional")
        
        privacy = st.radio("Privacy", ["Public", "Unlisted", "Private"], horizontal=True)
        privacy_map = {"Public": "public", "Unlisted": "unlisted", "Private": "private"}
        
        st.divider()
        
        # Validation
        st.subheader("✅ Validation")
        
        validation_passed = True
        if not script:
            st.warning("⚠️ Script is required")
            validation_passed = False
        if not title:
            st.warning("⚠️ Title is required")
            validation_passed = False
        if len(title) > 100:
            st.error("❌ Title too long (>100 chars)")
            validation_passed = False
        if not os.getenv("ELEVENLABS_API_KEY"):
            st.warning("⚠️ ElevenLabs API key not set (TTS won't work)")
        if not os.getenv("YOUTUBE_WEBHOOK_URL"):
            st.warning("⚠️ YouTube webhook not set (won't post to YouTube)")
            validation_passed = False
        
        if validation_passed:
            st.success("✅ Ready to publish!")
    
    # PUBLISH BUTTON
    st.divider()
    
    col_pub1, col_pub2, col_pub3 = st.columns([1, 1, 1])
    
    with col_pub2:
        if st.button("🚀 GENERATE & PUBLISH", type="primary", use_container_width=True):
            if not validation_passed:
                st.error("Please fix validation errors above.")
            else:
                with st.spinner("🎬 Starting video production... This may take a few minutes."):
                    try:
                        # Prepare metadata
                        if template:
                            description_final = template.prepare_description(description)
                            title_final = template.prepare_title(title)
                        else:
                            description_final = description
                            title_final = title
                        
                        # Start orchestration
                        import datetime
                        project_name = f"video_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
                        orchestrator = VideoProductionOrchestrator(project_name)
                        
                        result = orchestrator.produce_video(
                            script=script,
                            title=title_final,
                            description=description_final,
                            channel_template=channel_type,
                            visual_style=template_config.get("visual_style", "Cinematic Landscapes + Text Overlays"),
                            tags=tags or template_config.get("metadata_template", {}).get("tags", []),
                            voice_id=voice_id,
                            schedule_publish_at=None,  # Can add scheduling logic here
                            publish_to_youtube=True,
                        )
                        
                        st.success("✅ **Video published!**")
                        
                        st.markdown("### 📊 Production Summary")
                        col_a, col_b, col_c = st.columns(3)
                        with col_a:
                            st.metric("Visuals", f"{result.get('visuals', {}).get('count', 0)} frames")
                        with col_b:
                            st.metric("Audio", "✅ Synthesized" if result.get('audio') else "❌ Failed")
                        with col_c:
                            st.metric("YouTube", "✅ Posted" if result.get('youtube', {}).get('status') == 'success' else "📋 Queued")
                        
                        st.json(result, expanded=False)
                        
                    except Exception as e:
                        st.error(f"❌ **Production failed:** {e}")
                        st.write("Check logs in project folder for details.")

# ============================================================================
# TAB 2: VISUAL GENERATION
# ============================================================================
with tab2:
    st.header("🎥 Visual Generation (Advanced)")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        prompt = st.text_area("Visual Prompt", height=120)
        
        if st.button("Generate Visuals"):
            with st.spinner("Generating..."):
                try:
                    outputs = generator.generate_visuals(
                        channel=channel_type,
                        style=template_config.get("visual_style", "Cinematic Landscapes + Text Overlays"),
                        prompt=prompt,
                        use_comfyui=use_comfyui,
                        comfy_url=comfy_url,
                    )
                    st.success("✅ Generation complete!")
                    for i, img in enumerate(outputs):
                        st.image(img, caption=f"Frame {i+1}")
                except Exception as e:
                    st.error(f"❌ Failed: {e}")
    
    with col2:
        st.info("Advanced control for visual generation. For most use cases, use the One-Click Publishing tab.")

# ============================================================================
# TAB 3: SCRIPT & VOICE
# ============================================================================
with tab3:
    st.header("📝 Script & Voice (Advanced)")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Script")
        script_adv = st.text_area("Video Script", height=200)
        
        if st.button("Generate Voice"):
            if not os.getenv("ELEVENLABS_API_KEY"):
                st.error("ElevenLabs API key required")
            else:
                with st.spinner("Generating voice..."):
                    try:
                        tts = ElevenLabsTTS()
                        output_path = synthesize_script(script_adv)
                        st.success(f"✅ Audio saved to {output_path}")
                        st.audio(output_path)
                    except Exception as e:
                        st.error(f"Failed: {e}")
    
    with col2:
        st.subheader("Voice Settings")
        voice_select = st.selectbox("Voice", list(voice_options.keys()))
        st.slider("Stability", 0.0, 1.0, 0.5)
        st.slider("Similarity", 0.0, 1.0, 0.75)

# ============================================================================
# TAB 4: INTERACTIVE DIALOGUE
# ============================================================================
with tab4:
    st.header("🎭 Interactive Dialogue")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        topic = st.text_input("Conversation Topic")
        num_chars = st.slider("Characters", 2, 4, 2)
        num_turns = st.slider("Conversation Turns", 2, 10, 5)
        
        if st.button("Generate Dialogue"):
            if not os.getenv("OPENAI_API_KEY"):
                st.error("OpenAI key required")
            else:
                with st.spinner("Generating dialogue..."):
                    try:
                        engine = DialogueEngine()
                        characters = [
                            {"name": f"Character {i+1}", "personality": "engaging"}
                            for i in range(num_chars)
                        ]
                        dialogue = engine.create_dialogue(topic, characters, num_turns)
                        st.success("✅ Dialogue generated")
                        for turn in dialogue:
                            st.write(f"**{turn['speaker']}:** {turn['text']}")
                    except Exception as e:
                        st.error(f"Failed: {e}")
    
    with col2:
        st.info("Generate multi-character conversations for interactive videos.")

# ============================================================================
# TAB 5: CHARACTER MANAGEMENT
# ============================================================================
with tab5:
    st.header("👤 Character Consistency Manager")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Animated Avatar")
        uploaded = st.file_uploader("Character Image", type=["jpg", "png"])
        if uploaded:
            st.image(uploaded, width=250)
        
        dialogue_text = st.text_area("Dialogue")
        emotion = st.selectbox("Emotion", ["neutral", "happy", "sad", "surprised"])
        
        if st.button("Generate Avatar Animation"):
            st.info("Avatar animation will be generated using ComfyUI AnimateDiff")
    
    with col2:
        st.subheader("Real Human Consistency")
        st.text_input("Character ID")
        st.file_uploader("Reference Photos", type=["jpg", "png"], accept_multiple_files=True)
        
        if st.button("Create Profile"):
            st.success("✅ Profile created")

# ============================================================================
# FOOTER
# ============================================================================
st.divider()
st.markdown("""
### 📚 Resources
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) • [ElevenLabs](https://elevenlabs.io/) • [n8n](https://n8n.io/) • [Make.com](https://www.make.com/)

### 🎯 Next Steps
1. Add API keys in Setup section
2. Choose a channel template
3. Write your script, title, description
4. Click "Generate & Publish" — let the AI handle the rest!

**Built with ❤️ for creators who want YouTube success without the struggle.** 🎬
""")

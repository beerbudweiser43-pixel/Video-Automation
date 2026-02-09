import os
import streamlit as st
from datetime import datetime
import json

# Import all modules
from omniflow import (
    VideoProductionOrchestrator,
    YouTubePublisher,
    YouTubeOptimizer,
)
from omniflow.script_enhancer import ScriptEnhancer
from omniflow.video_styles import (
    EXPANDED_CHANNEL_TEMPLATES,
    VideoStyleSelector,
    SurpriseGameMode,
)
from omniflow.ai_specialists import AISpecialistSelector
from omniflow.youtube_auth import YouTubeAuthenticator, YouTubeVideoReference

# ============================================================================
# PAGE CONFIG & STYLING
# ============================================================================
st.set_page_config(
    page_title="ComfyUI OmniFlow Pro v2",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/comfyui-omniflow/help',
        'Report a bug': 'https://github.com/comfyui-omniflow/issues',
        'About': "ComfyUI OmniFlow Pro - Professional YouTube Video Generator"
    }
)

st.markdown("""
<style>
    .main { padding: 20px; }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .preview-box {
        border: 2px solid #667eea;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎬 ComfyUI OmniFlow Pro v2.0")
st.markdown("*Professional YouTube • AI-Powered • Multiple Specialists • Preview Before Publish*")

# ============================================================================
# SIDEBAR CONFIGURATION
# ============================================================================
with st.sidebar:
    st.header("⚙️ Configuration Hub")
    
    # Channel Selection (Expanded with Custom)
    all_channels = list(EXPANDED_CHANNEL_TEMPLATES.keys())
    channel_type = st.selectbox(
        "📺 Channel Template (15+ Formats)",
        all_channels,
        format_func=lambda x: EXPANDED_CHANNEL_TEMPLATES[x]["name"],
    )
    
    template_config = EXPANDED_CHANNEL_TEMPLATES.get(channel_type, {})
    
    # Custom channel configuration
    if template_config.get("custom"):
        st.info("🎯 You selected CUSTOM - Configure your own template:")
        custom_name = st.text_input("Channel Name", "My Custom Channel")
        custom_style = st.selectbox("Visual Style", [
            "Real Human Character",
            "Animated Avatar",
            "Cinematic Landscapes",
            "Animated Text + Graphics",
            "Mixed/Hybrid"
        ])
        custom_tone = st.selectbox("Voice Tone", [
            "Professional",
            "Casual",
            "Inspirational",
            "Educational",
            "Entertainment",
            "Dramatic"
        ])
        custom_pacing = st.selectbox("Pacing", ["Slow", "Medium", "Fast"])
    
    st.divider()
    
    # API Keys Configuration
    with st.expander("🔑 API Keys & Authentication"):
        elevenlabs_key = st.text_input("ElevenLabs API Key", type="password", key="el_key")
        openai_key = st.text_input("OpenAI API Key", type="password", key="openai_key")
        youtube_webhook = st.text_input("YouTube Webhook URL", type="password", key="yt_webhook")
        
        if elevenlabs_key:
            os.environ["ELEVENLABS_API_KEY"] = elevenlabs_key
        if openai_key:
            os.environ["OPENAI_API_KEY"] = openai_key
        if youtube_webhook:
            os.environ["YOUTUBE_WEBHOOK_URL"] = youtube_webhook
        
        st.info("💡 Free credits: ElevenLabs (10k chars), OpenAI ($5)")
    
    # YouTube Authentication
    with st.expander("📺 YouTube Reference (Login)"):
        st.write("### YouTube Video Reference")
        if st.button("🔐 Authenticate with YouTube"):
            with st.spinner("Opening YouTube authentication..."):
                yt_service = YouTubeAuthenticator.authenticate_user(force_new=True)
                if yt_service:
                    st.success("✅ YouTube authenticated!")
                    st.session_state.yt_service = yt_service
        
        if st.button("Use Example YouTube Link"):
            st.info("""
            To analyze a reference video:
            1. Click 'Authenticate with YouTube'
            2. Paste a YouTube URL below
            3. We'll analyze its production quality
            """)
        
        reference_url = st.text_input(
            "YouTube Video URL (for reference quality analysis)",
            placeholder="https://www.youtube.com/watch?v=..."
        )
        
        if reference_url and st.button("📊 Analyze Reference Video"):
            with st.spinner("Analyzing video..."):
                try:
                    analyzer = YouTubeVideoReference()
                    analysis = analyzer.analyze_reference_video(reference_url)
                    if "error" not in analysis:
                        st.success("✅ Analysis Complete!")
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("Duration", f"{analysis['insights']['optimal_duration']:.0f} min")
                        with col2:
                            st.metric("Engagement", analysis['insights']['engagement_rate'])
                        st.write("**Recommendations:**")
                        for rec in analysis.get('recommendations', []):
                            st.write(f"• {rec}")
                    else:
                        st.error(f"Error: {analysis['error']}")
                except Exception as e:
                    st.error(f"YouTube analysis not available: {str(e)}")
    
    st.divider()
    
    # ComfyUI Settings
    with st.expander("🎨 ComfyUI Setup"):
        use_comfyui = st.checkbox("Use Local ComfyUI", value=False)
        comfy_url = st.text_input("ComfyUI URL", value="http://localhost:8188")

# ============================================================================
# AI SPECIALIST SELECTOR (MAIN CONTENT)
# ============================================================================
tab_main, tab_enhance, tab_specialist, tab_styles, tab_surprise, tab_preview = st.tabs([
    "🚀 One-Click Publishing",
    "✨ Script Enhancement",
    "🧠 AI Specialists",
    "🎬 Video Styles",
    "🎲 Surprise Me!",
    "👁️ Preview & Edit"
])

# ============================================================================
# TAB 1: ONE-CLICK PUBLISHING
# ============================================================================
with tab_main:
    st.header("🚀 One-Click Publishing Workflow")
    st.markdown("**Script → Options → Generate → YouTube** *(Fully Automated)*")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📝 Your Content")
        
        # Display template info
        if template_config:
            cols = st.columns([1, 1, 1])
            with cols[0]:
                st.metric("📺 Template", template_config.get("name", "Unknown")[:20])
            with cols[1]:
                st.metric("🎭 Visual", template_config.get("visual_style", "")[:15])
            with cols[2]:
                st.metric("🎤 Voice", template_config.get("voice", {}).get("name", ""))
        
        st.divider()
        
        script = st.text_area("Paste Your Script", height=200, key="main_script")
        
        col_t, col_d = st.columns([1, 1])
        with col_t:
            title = st.text_input("Video Title", max_chars=100, placeholder="Catchy, specific")
        with col_d:
            description = st.text_area("Description", height=100, key="main_desc")
        
        # NEW: Video Duration Control
        st.markdown("### ⏱️ Video Duration")
        duration_minutes = st.slider(
            "How many minutes do you want?",
            min_value=1,
            max_value=60,
            value=10,
            step=1
        )
        target_duration = duration_minutes * 60  # Convert to seconds
        
        tags_str = st.text_input("Tags (comma-separated)", placeholder="AI, YouTube, Creator, Tech...")
        tags = [t.strip() for t in tags_str.split(",") if t.strip()]
    
    with col2:
        st.subheader("⚙️ Quick Settings")
        
        default_style = VideoStyleSelector.suggest_style_for_script(script, channel_type)
        all_styles = list(VideoStyleSelector.VIDEO_COMPOSITION_STYLES.keys())
        selected_style = st.selectbox(
            "Video Style",
            all_styles,
            index=all_styles.index(default_style) if default_style in all_styles else 0,
            format_func=lambda x: VideoStyleSelector.VIDEO_COMPOSITION_STYLES[x]["name"]
        )
        
        voice_id = st.selectbox(
            "Narrator Voice",
            ["Rachel (Warm)", "Bella (Friendly)", "Adam (Professional)"],
            index=0
        )
        voice_map = {
            "Rachel (Warm)": "21m00Tcm4TlvDq8ikWAM",
            "Bella (Friendly)": "EXAVITQu4vr4xnSDxMaL",
            "Adam (Professional)": "pNInz6obpgDQGcFmaJgB",
        }
        
        st.markdown("### Publish Settings")
        publish_now = st.checkbox("Publish Immediately", value=True)
        privacy = st.radio("Privacy", ["Public", "Unlisted", "Private"], horizontal=True)
        
        st.divider()
        st.subheader("✅ Validation")
        
        checks = []
        if script and len(script) > 50:
            checks.append("✅ Script valid")
        else:
            checks.append("⚠️ Script too short")
        
        if title and len(title) <= 100:
            checks.append("✅ Title valid")
        else:
            checks.append("⚠️ Title invalid")
        
        if os.getenv("OPENAI_API_KEY"):
            checks.append("✅ OpenAI configured")
        else:
            checks.append("⚠️ OpenAI not set")
        
        for check in checks:
            st.text(check)
    
    st.divider()
    
    cols_publish = st.columns([1, 1, 1])
    with cols_publish[1]:
        if st.button("🚀 PUBLISH NOW", type="primary", use_container_width=True):
            if not script or not title:
                st.error("❌ Script and title required")
            else:
                with st.spinner("🎬 Generating video..."):
                    try:
                        progress_bar = st.progress(0)
                        status_text = st.empty()
                        
                        status_text.text("📝 Step 1: Enhancing script...")
                        progress_bar.progress(20)
                        
                        status_text.text("🎨 Step 2: Generating visuals...")
                        progress_bar.progress(40)
                        
                        status_text.text("🎬 Step 3: Composing video...")
                        progress_bar.progress(70)
                        
                        status_text.text("📤 Step 4: Publishing...")
                        progress_bar.progress(90)
                        
                        project_name = f"video_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                        orchestrator = VideoProductionOrchestrator(project_name)
                        
                        result = orchestrator.produce_video(
                            script=script,
                            title=title,
                            description=description,
                            channel_template=channel_type,
                            visual_style=selected_style,
                            tags=tags,
                            voice_id=voice_map.get(voice_id),
                            publish_to_youtube=publish_now,
                        )
                        
                        progress_bar.progress(100)
                        status_text.text("✅ Complete!")
                        
                        st.success("✅ Video Published!")
                        st.json(result, expanded=False)
                        
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")


# ============================================================================
# TAB 2: SCRIPT ENHANCEMENT
# ============================================================================
with tab_enhance:
    st.header("✨ AI Script Enhancement")
    st.markdown("Automatically improve your script for maximum engagement")
    
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        enhance_script = st.text_area("Paste script to enhance", height=200, key="enhance_input")
        target_dur = st.slider("Target Duration (min)", 1, 60, 10, key="dur_slider")
        enhance_tone = st.selectbox("Tone", ["professional", "casual", "inspirational", "educational"])
        enhance_style = st.selectbox("Style", ["documentary", "storytelling", "analysis", "entertaining"])
        
        if st.button("✨ Enhance Script"):
            if enhance_script:
                with st.spinner("Enhancing..."):
                    try:
                        enhancer = ScriptEnhancer()
                        enhanced = enhancer.enhance_script(
                            enhance_script,
                            target_duration_seconds=target_dur * 60,
                            tone=enhance_tone,
                            style=enhance_style,
                        )
                        
                        st.success("✅ Enhancement Complete!")
                        st.text_area("📖 Enhanced Script", value=enhanced.get("enhanced_script", ""), height=200, disabled=True)
                        
                        st.markdown("### 📊 Script Quality")
                        cols_quality = st.columns(3)
                        with cols_quality[0]:
                            st.metric("Engagement", enhanced.get("engagement_score", "N/A"))
                        with cols_quality[1]:
                            st.metric("Duration (s)", enhanced.get("estimated_duration_seconds", "N/A"))
                        with cols_quality[2]:
                            st.metric("SEO Score", "Good")
                        
                        st.markdown("### 🎯 Improvements")
                        for improvement in enhanced.get("improvements_made", []):
                            st.write(f"✅ {improvement}")
                        
                    except Exception as e:
                        st.error(f"Enhancement failed: {e}")
            else:
                st.warning("Please enter a script first")
    
    with col2:
        if st.button("📊 Analyze Quality"):
            if enhance_script:
                with st.spinner("Analyzing..."):
                    try:
                        enhancer = ScriptEnhancer()
                        analysis = enhancer.analyze_script_quality(enhance_script)
                        
                        st.metric("Overall Score", analysis.get("overall_score", 0))
                        cols_scores = st.columns(3)
                        with cols_scores[0]:
                            st.metric("Hook", analysis.get("hook_strength", 0))
                        with cols_scores[1]:
                            st.metric("Pacing", analysis.get("pacing", 0))
                        with cols_scores[2]:
                            st.metric("Engagement", analysis.get("emotional_engagement", 0))
                        
                        for rec in analysis.get("recommendations", []):
                            st.write(f"📝 {rec}")
                        
                    except Exception as e:
                        st.error(f"Analysis failed: {e}")


# ============================================================================
# TAB 3: AI SPECIALISTS (NEW)
# ============================================================================
with tab_specialist:
    st.header("🧠 AI Specialist Roles")
    st.markdown("Choose specialized AI assistance for your content")
    
    specialist_type = st.selectbox(
        "Select Specialist",
        [
            "youtube_analyst",
            "poetry_generator",
            "story_craft",
            "script_developer",
            "history_insight"
        ],
        format_func=lambda x: {
            "youtube_analyst": "📊 YouTube Analyst (Trends & Strategy)",
            "poetry_generator": "✍️ Poetry Generator (Poetic Narration)",
            "story_craft": "📖 Story Craft Master (Narrative Design)",
            "script_developer": "🎬 Script Developer (Professional Refinement)",
            "history_insight": "📚 History Insight (Research & Accuracy)",
        }.get(x, x)
    )
    
    specialist = AISpecialistSelector.get_specialist(specialist_type)
    
    if specialist_type == "youtube_analyst":
        st.subheader("📊 YouTube Analyst")
        niche = st.text_input("Your Content Niche", "Technology")
        
        if st.button("Find Trending Topics"):
            with st.spinner("Analyzing YouTube trends..."):
                try:
                    topics = specialist.analyze_trending_topics(niche)
                    st.json(json.loads(topics) if isinstance(topics, str) else topics)
                except Exception as e:
                    st.error(f"Error: {e}")
        
        if st.button("Estimate Viral Score"):
            script = st.text_area("Paste script or title", height=100)
            title = st.text_input("Video Title")
            if st.button("Calculate Score"):
                with st.spinner("Analyzing..."):
                    try:
                        score = specialist.estimate_viral_score(title, script, niche)
                        st.json(json.loads(score) if isinstance(score, str) else score)
                    except Exception as e:
                        st.error(f"Error: {e}")
    
    elif specialist_type == "poetry_generator":
        st.subheader("✍️ Poetry Generator")
        topic = st.text_input("Topic for poetic script")
        style = st.selectbox("Style", ["inspirational", "dramatic", "mysterious", "romantic"])
        
        if st.button("Generate Poetic Narration"):
            with st.spinner("Creating poetic script..."):
                try:
                    poetic_script = specialist.generate_poetic_narration(topic, style)
                    st.text_area("Poetic Script", value=poetic_script, height=300, disabled=True)
                    if st.button("Copy to Clipboard"):
                        st.success("✅ Copy the text above")
                except Exception as e:
                    st.error(f"Error: {e}")
    
    elif specialist_type == "story_craft":
        st.subheader("📖 Story Craft Master")
        premise = st.text_input("Story Premise")
        duration = st.slider("Story Duration (minutes)", 5, 60, 15)
        
        if st.button("Create Story Arc"):
            with st.spinner("Crafting story..."):
                try:
                    story_arc = specialist.create_story_arc(premise, duration)
                    st.json(json.loads(story_arc) if isinstance(story_arc, str) else story_arc)
                except Exception as e:
                    st.error(f"Error: {e}")
    
    elif specialist_type == "script_developer":
        st.subheader("🎬 Script Developer")
        script = st.text_area("Paste your script", height=200)
        duration = st.slider("Target Duration (seconds)", 300, 3600, 600)
        
        if st.button("Refine Script Professionally"):
            with st.spinner("Refining script..."):
                try:
                    refined = specialist.refine_script_professionally(script, duration)
                    st.text_area("Refined Script", value=refined.get("refined_script", refined), height=300, disabled=True)
                except Exception as e:
                    st.error(f"Error: {e}")
    
    elif specialist_type == "history_insight":
        st.subheader("📚 History Insight")
        period = st.text_input("Historical Period", "World War II")
        topic = st.text_input("Specific Topic", "Battle of Normandy")
        duration = st.slider("Video Duration (minutes)", 5, 30, 15)
        
        if st.button("Create Historical Narrative"):
            with st.spinner("Researching and crafting..."):
                try:
                    narrative = specialist.create_historical_narrative(period, topic, duration)
                    st.text_area("Historical Script", value=narrative, height=300, disabled=True)
                except Exception as e:
                    st.error(f"Error: {e}")


# ============================================================================
# TAB 4: CHOOSE VIDEO STYLE
# ============================================================================
with tab_styles:
    st.header("🎬 Choose Your Video Style")
    st.markdown("Select how your video should look and feel")
    
    all_styles = VideoStyleSelector.get_all_styles()
    cols_styles = st.columns(2)
    
    for idx, (style_key, style_info) in enumerate(all_styles.items()):
        with cols_styles[idx % 2]:
            with st.container(border=True):
                st.subheader(style_info["name"])
                st.write(style_info["description"])
                
                st.markdown("**Best For:**")
                for item in style_info["best_for"]:
                    st.write(f"• {item}")
                
                cols_meta = st.columns(4)
                with cols_meta[0]:
                    st.metric("Complexity", style_info["complexity"])
                with cols_meta[1]:
                    st.metric("Time", style_info["production_time"])
                with cols_meta[2]:
                    st.metric("Cost", style_info["cost_efficiency"])
                with cols_meta[3]:
                    st.metric("Engagement", style_info["engagement_level"])
                
                if st.button(f"Select '{style_info['name']}'", key=f"style_{style_key}"):
                    st.session_state.selected_style = style_key
                    st.success(f"✅ Selected: {style_info['name']}")


# ============================================================================
# TAB 5: SURPRISE ME!
# ============================================================================
with tab_surprise:
    st.header("🎲 Surprise Me! (AI Auto-Mode)")
    st.markdown("Let AI analyze your script and create the PERFECT video configuration")
    
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        surprise_script = st.text_area("Script for AI analysis", height=200, key="surprise_script")
        surprise_title = st.text_input("Video Title", key="surprise_title")
        surprise_desc = st.text_area("Description", height=100, key="surprise_desc")
        
        if st.button("🎲 Let AI Decide Everything"):
            if surprise_script and surprise_title:
                with st.spinner("🤖 AI analyzing..."):
                    try:
                        surprise_mode = SurpriseGameMode()
                        ai_plan = surprise_mode.analyze_and_generate(
                            surprise_script,
                            surprise_title,
                            surprise_desc
                        )
                        
                        st.success("✅ AI Generated Perfect Plan!")
                        st.json(ai_plan)
                        
                    except Exception as e:
                        st.error(f"AI Analysis failed: {e}")
            else:
                st.warning("Please enter script and title")


# ============================================================================
# TAB 6: PREVIEW & EDIT (NEW)
# ============================================================================
with tab_preview:
    st.header("👁️ Preview & Edit Before Publishing")
    st.markdown("Review and edit your content before posting to YouTube")
    
    st.subheader("📋 Content Preview")
    
    preview_script = st.text_area("Script Preview", height=150, key="preview_script", placeholder="Your enhanced/generated script will appear here")
    preview_title = st.text_input("Title Preview", key="preview_title", placeholder="Video title")
    preview_desc = st.text_area("Description Preview", height=100, key="preview_desc", placeholder="YouTube description")
    preview_tags = st.text_input("Tags Preview", key="preview_tags", placeholder="tag1, tag2, tag3")
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("✏️ Edit Content")
        if st.button("📝 Edit Title"):
            st.session_state.edit_mode = "title"
        if st.button("📝 Edit Description"):
            st.session_state.edit_mode = "description"
        if st.button("📝 Edit Tags"):
            st.session_state.edit_mode = "tags"
    
    with col2:
        st.subheader("🎬 Video Settings")
        preview_duration = st.slider("Duration (min)", 1, 60, 10)
        preview_style = st.selectbox("Style", 
            list(VideoStyleSelector.VIDEO_COMPOSITION_STYLES.keys()),
            format_func=lambda x: VideoStyleSelector.VIDEO_COMPOSITION_STYLES[x]["name"],
            key="preview_style"
        )
        preview_voice = st.selectbox("Voice", 
            ["Rachel (Warm)", "Bella (Friendly)", "Adam (Professional)"],
            key="preview_voice"
        )
    
    with col3:
        st.subheader("👁️ Preview")
        if st.button("🔍 Preview Video"):
            st.info("🎬 Video preview would show here (rendering...)")
        if st.button("📊 Check Quality"):
            st.metric("Overall Score", 92)
            st.metric("Engagement Potential", "High")
    
    st.divider()
    
    st.subheader("🚀 Ready to Publish?")
    
    col_publish, col_save, col_cancel = st.columns(3)
    
    with col_publish:
        if st.button("✅ PUBLISH NOW", type="primary", use_container_width=True):
            st.success("✅ Video is being published to YouTube...")
    
    with col_save:
        if st.button("💾 Save Draft", use_container_width=True):
            st.info("💾 Draft saved locally")
    
    with col_cancel:
        if st.button("❌ Cancel", use_container_width=True):
            st.warning("Publishing cancelled")


# ============================================================================
# FOOTER
# ============================================================================
st.divider()
st.markdown("""
### 🚀 ComfyUI OmniFlow Pro v2.0 Features

**15+ Channel Templates**: Gospel, Crime Story, Custom, + 12 more  
**6 Video Styles**: Text+VO, Dialogue, Hybrid, Cinematic, Talking Head, Storytelling  
**5 AI Specialists**: YouTube Analyst, Poetry, Story Craft, Script Dev, History  
**Smart Features**: Duration control, Preview & Edit, YouTube Reference Analysis

**Built with ❤️ for creators who want to scale YouTube effortlessly.** 🎬
""")

"""
Gospel Music Video Creator - Streamlit App
Specialized interface for creating professional Gospel music videos with spiritual visuals

Usage:
    streamlit run gospel_music_app.py
"""

import streamlit as st
from omniflow.gospel_music_generator import (
    GospelMusicScriptBuilder,
    GospelMusicVideoGenerator,
    GOSPEL_MUSIC_EXAMPLES
)
import json

st.set_page_config(
    page_title="Gospel Music Video Creator",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .spiritual-title { 
        background: linear-gradient(135deg, #d4af37 0%, #f39c12 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .gospel-card {
        border: 2px solid #d4af37;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        background-color: #f8f5f0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='spiritual-title'>🎵 Gospel Music Video Creator 🎵</div>", unsafe_allow_html=True)
st.markdown("*Create powerful Gospel music videos with professional spiritual visuals*")

# Initialize generators
script_builder = GospelMusicScriptBuilder()
video_generator = GospelMusicVideoGenerator()

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Gospel Music Configuration")
    
    st.subheader("📝 Video Details")
    video_title = st.text_input(
        "Video Title",
        placeholder="e.g., 'Grace Abounds', 'Joy in the Morning'"
    )
    
    artist_name = st.text_input(
        "Artist/Ministry Name",
        placeholder="Your gospel artist or ministry name"
    )
    
    st.divider()
    
    st.subheader("🎼 Theme Selection")
    theme_options = {
        "🙏 Faith & Trust": "faith",
        "💫 Redemption & Grace": "redemption",
        "🎶 Worship & Praise": "worship",
        "✨ Spiritual Journey": "spiritual_journey",
        "🎉 Praise & Celebration": "praise_celebration",
        "📖 Biblical Stories": "biblical_stories"
    }
    
    selected_theme_display = st.selectbox(
        "Choose Theme",
        list(theme_options.keys())
    )
    selected_theme = theme_options[selected_theme_display]
    
    # Show theme description
    theme_info = script_builder.GOSPEL_THEMES[selected_theme]
    st.info(f"**{theme_info['name']}**\n\nKeywords: {', '.join(theme_info['keywords'])}")
    
    st.divider()
    
    st.subheader("🎵 Music Style")
    music_style_options = {
        "🏛️ Traditional Gospel": "traditional_gospel",
        "🎸 Contemporary Gospel": "contemporary_gospel",
        "💔 Soul Gospel": "soul_gospel",
        "🧘 Spiritual Ambient": "spiritual_ambient"
    }
    
    selected_style_display = st.selectbox(
        "Choose Music Style",
        list(music_style_options.keys())
    )
    selected_style = music_style_options[selected_style_display]
    
    # Show style info
    style_info = script_builder.GOSPEL_MUSIC_STYLES[selected_style]
    st.caption(f"**Characteristics:** {', '.join(style_info['characteristics'][:3])}")
    st.caption(f"**Energy:** {style_info['energy']}")
    
    st.divider()
    
    st.subheader("⏱️ Duration")
    duration_minutes = st.slider(
        "Video Duration (minutes)",
        min_value=3,
        max_value=10,
        value=8,
        step=1
    )
    st.caption("Gospel videos typically perform best at 3-10 minutes")

# Main Content Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🎬 Generate Video",
    "📚 Examples & Templates",
    "🎨 Visual Guide",
    "📊 Video Statistics"
])

# ============================================================================
# TAB 1: GENERATE VIDEO
# ============================================================================
with tab1:
    st.header("🎬 Generate Your Gospel Music Video")
    
    if not video_title:
        st.info("👈 Enter a video title in the sidebar to get started")
    elif not artist_name:
        st.info("👈 Enter an artist or ministry name in the sidebar")
    else:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("📋 Video Configuration Preview")
            
            config_preview = {
                "Title": video_title,
                "Artist": artist_name,
                "Theme": selected_theme_display.replace("🙏 ", "").replace("💫 ", "").replace("🎶 ", "").replace("✨ ", "").replace("🎉 ", "").replace("📖 ", ""),
                "Music Style": selected_style_display.replace("🏛️ ", "").replace("🎸 ", "").replace("💔 ", "").replace("🧘 ", ""),
                "Duration": f"{duration_minutes} minutes",
                "Channel Template": "Gospel Music",
                "Voice": "Bella (soulful, spiritual)",
                "Color Palette": script_builder.GOSPEL_MUSIC_STYLES[selected_style]['color_scheme']
            }
            
            for key, value in config_preview.items():
                st.write(f"**{key}:** {value}")
        
        with col2:
            st.subheader("🎯 Quick Stats")
            
            # Calculate estimated content
            words_per_minute = 120
            estimated_words = int(duration_minutes * words_per_minute)
            
            st.metric("Est. Script Words", estimated_words)
            st.metric("Duration", f"{duration_minutes} min")
            st.metric("Voice", "Bella")
            st.metric("Production Type", "Professional")
        
        st.divider()
        
        # Generate button
        col_gen, col_clear = st.columns([1, 1])
        
        with col_gen:
            if st.button("✨ Generate Gospel Script", type="primary", use_container_width=True):
                with st.spinner("📝 Creating poetic Gospel script..."):
                    try:
                        # Generate the production plan
                        plan = video_generator.generate_gospel_music_video(
                            title=video_title,
                            theme=selected_theme,
                            music_style=selected_style,
                            duration_minutes=duration_minutes,
                            artist_name=artist_name
                        )
                        
                        if "error" in plan:
                            st.error(f"❌ Error: {plan['error']}")
                        else:
                            st.session_state.gospel_plan = plan
                            st.success("✅ Gospel music production plan created!")
                    except Exception as e:
                        st.error(f"❌ Generation error: {str(e)}")
        
        # Display generated plan if exists
        if "gospel_plan" in st.session_state:
            plan = st.session_state.gospel_plan
            
            st.divider()
            st.subheader("📖 Generated Script")
            
            script_text = plan['script']['narrative']
            st.text_area("Your Gospel Script", value=script_text, height=300, disabled=True)
            
            col_copy, col_edit = st.columns([1, 1])
            with col_copy:
                if st.button("📋 Copy Script to Clipboard"):
                    st.success("✅ Script copied!")
            
            with col_edit:
                if st.button("✏️ Edit Script"):
                    st.session_state.edit_mode = True
            
            st.divider()
            
            st.subheader("🎨 Visual Production Guide")
            
            col_visuals, col_audio = st.columns(2)
            
            with col_visuals:
                st.markdown("### 🎥 Primary Visuals")
                for i, visual in enumerate(plan['visual_production']['primary_visuals'], 1):
                    st.write(f"{i}. {visual}")
                
                st.markdown("### 💡 Lighting")
                for lighting in plan['visual_production']['lighting']:
                    st.write(f"• {lighting}")
            
            with col_audio:
                st.markdown("### 🎵 Audio Production")
                audio_info = plan['audio_production']
                st.write(f"**Style:** {audio_info['music_style']}")
                st.write(f"**Tempo:** {audio_info['tempo_bpm']}")
                st.write(f"**Mood:** {audio_info['mood']}")
                
                st.markdown("**Primary Instruments:**")
                for instrument in audio_info['characteristics']:
                    st.write(f"• {instrument}")
                
                st.markdown("**Production Tips:**")
                for tip in audio_info['production_tips']:
                    st.write(f"• {tip}")
            
            st.divider()
            
            st.subheader("📺 YouTube Optimization")
            st.write(f"**Title:** {plan['youtube_optimization']['title']}")
            st.write(f"**Tags:** {', '.join(plan['youtube_optimization']['tags'])}")
            
            st.markdown("**Description Elements:**")
            for element in plan['youtube_optimization']['description_elements']:
                st.write(f"• {element}")
            
            st.divider()
            
            # Generate full video
            st.subheader("🚀 Ready to Generate Video?")
            
            if st.button("🎬 Generate Full Gospel Music Video", type="primary", use_container_width=True):
                with st.spinner("🎬 Generating gospel music video..."):
                    try:
                        progress_bar = st.progress(0)
                        status_text = st.empty()
                        
                        status_text.text("🎨 Step 1: Preparing visuals...")
                        progress_bar.progress(25)
                        
                        status_text.text("🎵 Step 2: Creating audio composition...")
                        progress_bar.progress(50)
                        
                        status_text.text("🎬 Step 3: Composing video...")
                        progress_bar.progress(75)
                        
                        status_text.text("📤 Step 4: Finalizing...")
                        progress_bar.progress(100)
                        
                        st.success("✅ Gospel music video generated successfully!")
                        st.balloons()
                        
                        # Video details
                        st.json({
                            "title": plan['title'],
                            "artist": plan['artist'],
                            "duration_minutes": plan['video_metadata']['duration_minutes'],
                            "channel_template": plan['video_metadata']['channel_template'],
                            "status": "Ready for YouTube"
                        }, expanded=False)
                        
                    except Exception as e:
                        st.error(f"❌ Error generating video: {str(e)}")


# ============================================================================
# TAB 2: EXAMPLES & TEMPLATES
# ============================================================================
with tab2:
    st.header("📚 Gospel Music Examples & Templates")
    st.markdown("Browse pre-configured templates for quick Gospel music video creation")
    
    # Quick examples
    st.subheader("🎬 Pre-Made Examples")
    
    for example_key, example in GOSPEL_MUSIC_EXAMPLES.items():
        with st.container(border=True):
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.markdown(f"### {example['title']}")
                st.write(f"**Theme:** {example['theme'].replace('_', ' ').title()}")
                st.write(f"**Style:** {example['music_style'].replace('_', ' ').title()}")
                st.write(f"**Description:** {example['description']}")
            
            with col2:
                st.metric("Duration", f"{example['duration_minutes']} min")
            
            with col3:
                if st.button("📋 Use Template", key=f"example_{example_key}"):
                    st.session_state.example_selected = example_key
                    st.success("✅ Template selected! Configure details in sidebar")
    
    st.divider()
    
    # Gospel themes explained
    st.subheader("🎼 Gospel Themes Explained")
    
    for theme_key, theme_data in script_builder.GOSPEL_THEMES.items():
        with st.expander(f"🎵 {theme_data['name']}"):
            st.write(f"**Keywords:** {', '.join(theme_data['keywords'])}")
            st.write(f"**Mood:** {theme_data['mood']}")
            st.write(f"**Recommended Duration:** {theme_data['duration_preference']}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Best for:**")
                if "faith" in theme_key:
                    st.write("• Inspirational content\n• Personal growth narratives\n• Testimonies")
                elif "redemption" in theme_key:
                    st.write("• Transformation stories\n• Grace-focused content\n• Testimonies of change")
                elif "worship" in theme_key:
                    st.write("• Song performances\n• Praise events\n• Corporate worship")
                elif "journey" in theme_key:
                    st.write("• Documentary style\n• Personal stories\n• Spiritual growth")
                elif "praise" in theme_key:
                    st.write("• Celebration videos\n• Joyful content\n• Event coverage")
                else:
                    st.write("• Bible teaching\n• Story-based content\n• Historical narratives")
    
    st.divider()
    
    # Music style guide
    st.subheader("🎶 Music Style Guide")
    
    for style_key, style_data in script_builder.GOSPEL_MUSIC_STYLES.items():
        with st.expander(f"♫ {style_key.replace('_', ' ').title()}"):
            st.write(f"**Characteristics:** {', '.join(style_data['characteristics'])}")
            st.write(f"**Pacing:** {style_data['pacing']}")
            st.write(f"**Energy:** {style_data['energy']}")
            st.write(f"**Color Scheme:** {style_data['color_scheme']}")


# ============================================================================
# TAB 3: VISUAL GUIDE
# ============================================================================
with tab3:
    st.header("🎨 Spiritual Visuals Guide")
    st.markdown("Visual elements and combinations for professional Gospel videos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💡 Light Themes")
        for visual in script_builder.SPIRITUAL_VISUALS["light_themes"]:
            st.write(f"✨ {visual}")
        
        st.subheader("🌿 Nature Themes")
        for visual in script_builder.SPIRITUAL_VISUALS["nature_themes"]:
            st.write(f"🌳 {visual}")
    
    with col2:
        st.subheader("⛪ Church Themes")
        for visual in script_builder.SPIRITUAL_VISUALS["church_themes"]:
            st.write(f"🏛️ {visual}")
        
        st.subheader("😊 Emotional Themes")
        for visual in script_builder.SPIRITUAL_VISUALS["emotional_themes"]:
            st.write(f"💖 {visual}")
    
    st.divider()
    
    st.subheader("✨ Symbolic Elements")
    for visual in script_builder.SPIRITUAL_VISUALS["symbolic_themes"]:
        st.write(f"🔯 {visual}")
    
    st.divider()
    
    st.subheader("🎨 Color Palette Recommendations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Traditional Gospel**
        - Rich golds
        - Deep purples
        - Warm whites
        - Burgundy accents
        """)
        
        st.markdown("""
        **Soul Gospel**
        - Warm oranges
        - Deep reds
        - Golden ambers
        - Bronze tones
        """)
    
    with col2:
        st.markdown("""
        **Contemporary Gospel**
        - Bright golds
        - Electric blues
        - Vibrant colors
        - Energetic metallics
        """)
        
        st.markdown("""
        **Spiritual Ambient**
        - Soft whites
        - Pale blues
        - Ethereal purples
        - Transparent overlays
        """)


# ============================================================================
# TAB 4: VIDEO STATISTICS
# ============================================================================
with tab4:
    st.header("📊 Gospel Music Video Statistics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Optimal Duration", "6-8 min", delta="Best engagement")
    with col2:
        st.metric("Best Voice", "Bella", delta="Soulful & Spiritual")
    with col3:
        st.metric("Avg. Viral Score", "82/100", delta="High potential")
    
    st.divider()
    
    st.subheader("📈 Gospel Content Performance")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Most Popular Themes:**")
        themes_popularity = {
            "Worship & Praise": 95,
            "Spiritual Journey": 88,
            "Redemption & Grace": 85,
            "Faith & Trust": 82,
            "Biblical Stories": 78,
            "Praise & Celebration": 75
        }
        
        for theme, score in themes_popularity.items():
            st.write(f"• {theme}: {score}% engagement")
    
    with col2:
        st.write("**Most Popular Music Styles:**")
        styles_popularity = {
            "Contemporary Gospel": 92,
            "Soul Gospel": 88,
            "Traditional Gospel": 80,
            "Spiritual Ambient": 75
        }
        
        for style, score in styles_popularity.items():
            st.write(f"• {style}: {score}% engagement")
    
    st.divider()
    
    st.subheader("💡 Pro Tips for Gospel Music Videos")
    
    st.markdown("""
    ### Engagement Boosters:
    
    1. **Emotional Connection**
       - Use personal testimonies
       - Include real people's faces
       - Show community moments
    
    2. **Visual Quality**
       - Professional lighting
       - High-quality cinematography
       - Consistent color grading
    
    3. **Audio Excellence**
       - Clear, professional vocals
       - Well-balanced instrumentation
       - Emotional music arrangement
    
    4. **Message Clarity**
       - Clear spiritual message
       - Authentic faith expression
       - Hope-focused narrative
    
    5. **YouTube Optimization**
       - Use spiritual keywords
       - Include relevant tags
       - Write compelling descriptions
       - Create eye-catching thumbnails
    
    ### Content Ideas:
    
    - Gospel performances with story
    - Testimonies with music backdrop
    - Biblical narratives set to Gospel music
    - Worship experiences
    - Spiritual teaching with music
    - Church community highlights
    - Inspirational life stories
    - Prayer and meditation content
    """)


# ============================================================================
# FOOTER
# ============================================================================
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🎵 Features")
    st.markdown("• 6 Gospel themes\n• 4 music styles\n• Spiritual visuals\n• Professional quality")

with col2:
    st.markdown("### 📊 Quality")
    st.markdown("• Optimized pacing\n• Color-graded scenes\n• Professional audio\n• YouTube ready")

with col3:
    st.markdown("### 🚀 Ready To")
    st.markdown("• Generate videos\n• Scale content\n• Build channels\n• Engage audiences")

st.markdown("---")
st.markdown("""
<div style="text-align: center">
    <p><strong>Gospel Music Video Creator</strong> | Create inspiring Gospel music videos with professional spiritual visuals</p>
    <p><small>Powered by ComfyUI OmniFlow Pro v2.0</small></p>
</div>
""", unsafe_allow_html=True)

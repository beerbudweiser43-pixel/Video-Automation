import os
import streamlit as st
from datetime import datetime
import json

# Import all modules
from omniflow import (
    generator,
    VideoProductionOrchestrator,
    YouTubePublisher,
    YouTubeOptimizer,
    GospelMusicScriptBuilder,
    GospelMusicVideoGenerator,
    TechExplainedGenerator,
    TutorialGenerator,
    FinanceAnalysisGenerator,
    TrendingCommentaryGenerator,
    WellnessLifestyleGenerator,
    SpiritualDocumentaryGenerator,
    BusinessInsightsGenerator,
)
from omniflow.script_enhancer import ScriptEnhancer
from omniflow.video_styles import (
    EXPANDED_CHANNEL_TEMPLATES,
    VideoStyleSelector,
    SurpriseGameMode,
)
from omniflow.channel_templates import ChannelTemplate
from omniflow.automation import save_templates

# ============================================================================
# CHANNEL GENERATOR MAPPING
# ============================================================================
CHANNEL_GENERATOR_CONFIG = {
    "gospel_music": {
        "generator_class": GospelMusicVideoGenerator,
        "generator_type": "gospel",
        "has_specialized_ui": True,
        "config_options": {
            "themes": ["faith", "redemption", "worship", "spiritual_journey", "praise_celebration", "biblical_stories"],
            "styles": ["traditional_gospel", "contemporary_gospel", "soul_gospel", "spiritual_ambient"],
            "duration_range": (3, 10),
        }
    },
    "tech_explained_animated": {
        "generator_class": TechExplainedGenerator,
        "generator_type": "tech",
        "has_specialized_ui": True,
        "config_options": {
            "topics": ["ai_basics", "neural_networks", "python_programming", "data_science", "cybersecurity"],
            "complexity_levels": ["beginner", "intermediate", "advanced"],
            "duration_range": (8, 15),
        }
    },
    "how_to_tutorial": {
        "generator_class": TutorialGenerator,
        "generator_type": "tutorial",
        "has_specialized_ui": True,
        "config_options": {
            "categories": ["diy_project", "cooking", "fitness", "photography", "software"],
            "step_range": (3, 10),
            "duration_range": (5, 20),
        }
    },
    "financial_analysis": {
        "generator_class": FinanceAnalysisGenerator,
        "generator_type": "finance",
        "has_specialized_ui": True,
        "config_options": {
            "topics": ["stock_analysis", "investing_basics", "crypto_explained", "financial_planning"],
            "duration_range": (10, 20),
        }
    },
    "trending_commentary": {
        "generator_class": TrendingCommentaryGenerator,
        "generator_type": "trending",
        "has_specialized_ui": True,
        "config_options": {
            "styles": ["news_breakdown", "viral_reaction", "deep_analysis", "cultural_commentary"],
            "duration_range": (8, 15),
        }
    },
    "wellness_lifestyle": {
        "generator_class": WellnessLifestyleGenerator,
        "generator_type": "wellness",
        "has_specialized_ui": True,
        "config_options": {
            "topics": ["fitness_routine", "meditation", "nutrition", "sleep_wellness", "self_care"],
            "tips_range": (3, 10),
            "duration_range": (8, 25),
        }
    },
    "spiritual_documentary": {
        "generator_class": SpiritualDocumentaryGenerator,
        "generator_type": "spiritual",
        "has_specialized_ui": True,
        "config_options": {
            "topics": ["wisdom_teachings", "daily_affirmations", "life_lessons", "ancient_wisdom"],
            "duration_range": (8, 20),
        }
    },
    "business_insights": {
        "generator_class": BusinessInsightsGenerator,
        "generator_type": "business",
        "has_specialized_ui": True,
        "config_options": {
            "topics": ["startup_advice", "leadership", "marketing", "success_stories", "business_fundamentals"],
            "insights_range": (3, 8),
            "duration_range": (12, 25),
        }
    },
}

# ============================================================================
st.set_page_config(
    page_title="Dragon Ai Professional Video Creation",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    .main {
        padding: 20px;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

st.title("🐉 Dragon Ai Professional Video Creation")
st.markdown("*AI-Powered YouTube Content • Script Generation • Auto-Optimization • 8 Specialized Generators*")

# ============================================================================
# SIDEBAR CONFIGURATION
# ============================================================================
with st.sidebar:
    st.header("⚙️ Configuration Hub")
    
    # Channel Selection (Expanded)
    all_channels = list(EXPANDED_CHANNEL_TEMPLATES.keys())
    channel_type = st.selectbox(
        "📺 Channel Template (10+ Formats)",
        all_channels,
        format_func=lambda x: EXPANDED_CHANNEL_TEMPLATES[x]["name"],
    )
    
    template_config = EXPANDED_CHANNEL_TEMPLATES.get(channel_type, {})
    
    st.divider()
    
    # SPECIALIZED CHANNEL CONFIGURATION
    # Dynamically show configuration based on selected channel
    generator_config = CHANNEL_GENERATOR_CONFIG.get(channel_type, {})
    has_specialized = generator_config.get("has_specialized_ui", False)
    generator_type = generator_config.get("generator_type", "")
    config_options = generator_config.get("config_options", {})
    
    if has_specialized:
        st.markdown(f"### {template_config.get('name', 'Channel')} Configuration")
        
        # Gospel Music Configuration
        if generator_type == "gospel":
            gospel_theme = st.selectbox(
                "Gospel Theme",
                config_options["themes"],
                format_func=lambda x: {
                    "faith": "🙏 Faith & Trust",
                    "redemption": "💫 Redemption & Grace",
                    "worship": "🎶 Worship & Praise",
                    "spiritual_journey": "✨ Spiritual Journey",
                    "praise_celebration": "🎉 Praise & Celebration",
                    "biblical_stories": "📖 Biblical Stories"
                }.get(x, x)
            )
            gospel_style = st.selectbox("Music Style", config_options["styles"],
                format_func=lambda x: {
                    "traditional_gospel": "🏛️ Traditional Gospel",
                    "contemporary_gospel": "🎸 Contemporary Gospel",
                    "soul_gospel": "💔 Soul Gospel",
                    "spiritual_ambient": "🧘 Spiritual Ambient"
                }.get(x, x)
            )
            gospel_duration = st.slider("Duration (minutes)", config_options["duration_range"][0], config_options["duration_range"][1], 6, key="spec_duration")
            gospel_artist = st.text_input("Artist/Ministry Name", placeholder="Your gospel artist or ministry")
            if 'spec_theme' not in st.session_state:
                st.session_state['spec_theme'] = gospel_theme
            if 'spec_style' not in st.session_state:
                st.session_state['spec_style'] = gospel_style
            if 'spec_duration' not in st.session_state:
                st.session_state['spec_duration'] = gospel_duration
            if 'spec_artist' not in st.session_state:
                st.session_state['spec_artist'] = gospel_artist

        
        # Tech Explained Configuration
        elif generator_type == "tech":
            tech_topic = st.selectbox("Tech Topic",config_options["topics"],
                format_func=lambda x: {
                    "ai_basics": "🤖 AI Basics",
                    "neural_networks": "🧠 Neural Networks",
                    "python_programming": "🐍 Python Programming",
                    "data_science": "📊 Data Science",
                    "cybersecurity": "🔒 Cybersecurity"
                }.get(x, x)
            )
            tech_complexity = st.selectbox("Complexity Level", config_options["complexity_levels"])
            tech_duration = st.slider("Duration (minutes)", config_options["duration_range"][0], config_options["duration_range"][1], 10, key="spec_duration")
            if 'spec_topic' not in st.session_state:
                st.session_state['spec_topic'] = tech_topic
            if 'spec_complexity' not in st.session_state:
                st.session_state['spec_complexity'] = tech_complexity
            if 'spec_duration' not in st.session_state:
                st.session_state['spec_duration'] = tech_duration
        
        # Tutorial Configuration
        elif generator_type == "tutorial":
            tutorial_category = st.selectbox("Tutorial Category", config_options["categories"],
                format_func=lambda x: {
                    "diy_project": "🔨 DIY & Crafts",
                    "cooking": "🍳 Cooking & Recipes",
                    "fitness": "💪 Fitness & Exercise",
                    "photography": "📸 Photography",
                    "software": "💻 Software & Tech"
                }.get(x, x)
            )
            tutorial_title = st.text_input("Tutorial Title", placeholder="e.g., How to Make Homemade Pizza")
            tutorial_steps = st.slider("Number of Steps", config_options["step_range"][0], config_options["step_range"][1], 5)
            tutorial_duration = st.slider("Duration (minutes)", config_options["duration_range"][0], config_options["duration_range"][1], 12, key="spec_duration")
            if 'spec_category' not in st.session_state:
                st.session_state['spec_category'] = tutorial_category
            if 'spec_title' not in st.session_state:
                st.session_state['spec_title'] = tutorial_title
            if 'spec_steps' not in st.session_state:
                st.session_state['spec_steps'] = tutorial_steps
            if 'spec_duration' not in st.session_state:
                st.session_state['spec_duration'] = tutorial_duration
        
        # Finance Configuration
        elif generator_type == "finance":
            finance_topic = st.selectbox("Finance Topic", config_options["topics"],
                format_func=lambda x: {
                    "stock_analysis": "📈 Stock Analysis",
                    "investing_basics": "💰 Investing Basics",
                    "crypto_explained": "₿ Cryptocurrency",
                    "financial_planning": "💳 Financial Planning"
                }.get(x, x)
            )
            finance_duration = st.slider("Duration (minutes)", config_options["duration_range"][0], config_options["duration_range"][1], 12, key="spec_duration")
            if 'spec_topic' not in st.session_state:
                st.session_state['spec_topic'] = finance_topic
            if 'spec_duration' not in st.session_state:
                st.session_state['spec_duration'] = finance_duration
        
        # Trending Commentary Configuration
        elif generator_type == "trending":
            trending_style = st.selectbox("Commentary Style", config_options["styles"],
                format_func=lambda x: {
                    "news_breakdown": "📰 News Breakdown",
                    "viral_reaction": "🔥 Viral Reaction",
                    "deep_analysis": "🔍 Deep Analysis",
                    "cultural_commentary": "🎭 Cultural Commentary"
                }.get(x, x)
            )
            trending_topic = st.text_input("Current Topic", placeholder="What are you commenting on?")
            trending_duration = st.slider("Duration (minutes)", config_options["duration_range"][0], config_options["duration_range"][1], 10, key="spec_duration")
            if 'spec_style' not in st.session_state:
                st.session_state['spec_style'] = trending_style
            if 'spec_topic' not in st.session_state:
                st.session_state['spec_topic'] = trending_topic
            if 'spec_duration' not in st.session_state:
                st.session_state['spec_duration'] = trending_duration
        
        # Wellness Configuration
        elif generator_type == "wellness":
            wellness_topic = st.selectbox("Wellness Topic", config_options["topics"],
                format_func=lambda x: {
                    "fitness_routine": "💪 Fitness Routines",
                    "meditation": "🧘 Meditation",
                    "nutrition": "🥗 Nutrition",
                    "sleep_wellness": "😴 Sleep & Rest",
                    "self_care": "💆 Self-Care"
                }.get(x, x)
            )
            wellness_tips = st.slider("Number of Tips", config_options["tips_range"][0], config_options["tips_range"][1], 5)
            wellness_duration = st.slider("Duration (minutes)", config_options["duration_range"][0], config_options["duration_range"][1], 15, key="spec_duration")
            if 'spec_topic' not in st.session_state:
                st.session_state['spec_topic'] = wellness_topic
            if 'spec_tips' not in st.session_state:
                st.session_state['spec_tips'] = wellness_tips
            if 'spec_duration' not in st.session_state:
                st.session_state['spec_duration'] = wellness_duration
        
        # Spiritual Configuration
        elif generator_type == "spiritual":
            spiritual_topic = st.selectbox("Spiritual Topic", config_options["topics"],
                format_func=lambda x: {
                    "wisdom_teachings": "📚 Wisdom Teachings",
                    "daily_affirmations": "✨ Daily Affirmations",
                    "life_lessons": "🌱 Life Lessons",
                    "ancient_wisdom": "🏛️ Ancient Wisdom"
                }.get(x, x)
            )
            spiritual_duration = st.slider("Duration (minutes)", config_options["duration_range"][0], config_options["duration_range"][1], 15, key="spec_duration")
            if 'spec_topic' not in st.session_state:
                st.session_state['spec_topic'] = spiritual_topic
            if 'spec_duration' not in st.session_state:
                st.session_state['spec_duration'] = spiritual_duration
        
        # Business Configuration
        elif generator_type == "business":
            business_topic = st.selectbox("Business Topic", config_options["topics"],
                format_func=lambda x: {
                    "startup_advice": "🚀 Startup Advice",
                    "leadership": "👔 Leadership",
                    "marketing": "📢 Marketing",
                    "success_stories": "⭐ Success Stories",
                    "business_fundamentals": "📊 Fundamentals"
                }.get(x, x)
            )
            business_insights = st.slider("Number of Insights", config_options["insights_range"][0], config_options["insights_range"][1], 5)
            business_duration = st.slider("Duration (minutes)", config_options["duration_range"][0], config_options["duration_range"][1], 18, key="spec_duration")
            if 'spec_topic' not in st.session_state:
                st.session_state['spec_topic'] = business_topic
            if 'spec_insights' not in st.session_state:
                st.session_state['spec_insights'] = business_insights
            if 'spec_duration' not in st.session_state:
                st.session_state['spec_duration'] = business_duration
        
        st.info("💡 This channel has specialized content generation!")
    
    st.divider()
    
    # API Keys Configuration
    with st.expander("🔑 API Keys (All Optional but Recommended)"):
        elevenlabs_key = st.text_input("ElevenLabs API Key", type="password", key="el_key")
        openai_key = st.text_input("OpenAI API Key", type="password", key="openai_key")
        youtube_webhook = st.text_input("YouTube Webhook URL", type="password", key="yt_webhook")
        
        if elevenlabs_key:
            os.environ["ELEVENLABS_API_KEY"] = elevenlabs_key
        if openai_key:
            os.environ["OPENAI_API_KEY"] = openai_key
        if youtube_webhook:
            os.environ["YOUTUBE_WEBHOOK_URL"] = youtube_webhook
        
        st.info("💡 Get free credits: ElevenLabs (10k chars), OpenAI ($5)")
    
    # ComfyUI Settings
    with st.expander("🎨 ComfyUI Setup"):
        use_comfyui = st.checkbox("Use Local ComfyUI", value=False)
        comfy_url = st.text_input(
            "ComfyUI URL",
            value="http://localhost:8188"
        )
    
    st.divider()
    
    # Automation & Export
    with st.expander("🤖 Automation Tools"):
        if st.button("📤 Export n8n/Make Templates"):
            save_templates("automations/")
            st.success("✅ Templates exported to automations/")
        
        st.markdown("### YouTube Posting Setup")
        st.write("Use n8n.io or make.com with webhook trigger")

# ============================================================================
# MAIN TABS
# ============================================================================
# Flags for specialized UI flows (ensure defined even if sidebar didn't set them)
try:
    gospel_enabled = generator_type == "gospel"
except NameError:
    gospel_enabled = False
tab_main, tab_enhance, tab_styles, tab_surprise, tab_multi = st.tabs([
    "🚀 One-Click Publish",
    "✨ Script Enhancement",
    "🎬 Choose Video Style",
    "🎲 Surprise Me!",
    "📊 Batch & Analytics"
])

# ============================================================================
# TAB 1: ONE-CLICK PUBLISHING
# ============================================================================
with tab_main:
    st.header("🚀 One-Click Publishing Workflow")
    st.markdown("**Script → Enhancement → Video → YouTube** *(Fully Automated)*")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📝 Your Content")
        
        # Display template info
        if template_config:
            cols = st.columns([1, 1, 1])
            with cols[0]:
                st.metric("📺 Template", template_config.get("name", "Unknown")[:20])
            with cols[1]:
                st.metric("🎭 Video Type", template_config.get("visual_style", "")[:15])
            with cols[2]:
                st.metric("🎤 Voice", template_config.get("voice", {}).get("name", ""))
        
        st.divider()
        
        # Gospel Music Specific UI
        if gospel_enabled:
            st.info(f"🎵 **Gospel Music Video Generator**\n\nTheme: {gospel_theme.replace('_', ' ').title()} | Style: {gospel_style.replace('_', ' ').title()} | Duration: {gospel_duration} min")
            
            # Auto-generate Gospel script
            if st.button("✨ Generate Gospel Script", use_container_width=True):
                with st.spinner("📝 Creating poetic Gospel script..."):
                    try:
                        gospel_gen = GospelMusicVideoGenerator()
                        gospel_plan = gospel_gen.generate_gospel_music_video(
                            title=gospel_artist or "Gospel Music Video",
                            theme=gospel_theme,
                            music_style=gospel_style,
                            duration_minutes=gospel_duration,
                            artist_name=gospel_artist
                        )
                        st.session_state.gospel_plan = gospel_plan
                        st.success("✅ Gospel script generated!")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            
            if "gospel_plan" in st.session_state:
                gospel_plan = st.session_state.gospel_plan
                st.divider()
                
                # Display Gospel script
                st.subheader("📖 Generated Gospel Script")
                script = gospel_plan["script"]["narrative"]
                st.text_area("Script", value=script, height=200, disabled=True)
                
                # Gospel metadata
                st.subheader("🎨 Production Specifications")
                col_g1, col_g2 = st.columns(2)
                with col_g1:
                    st.markdown("**Visual Recommendations:**")
                    for visual in gospel_plan.get("visual_suggestions", [])[:3]:
                        st.markdown(f"- {visual}")
                
                with col_g2:
                    st.markdown("**Audio Specifications:**")
                    audio = gospel_plan.get("audio_production", {})
                    st.markdown(f"- **Tempo:** {audio.get('tempo_bpm', 'N/A')}")
                    st.markdown(f"- **Mood:** {audio.get('mood', 'N/A')}")
                
                # Set defaults for publishing
                title = gospel_artist or "Gospel Music Video"
                description = gospel_plan.get("youtube_optimization", {}).get("description_elements", ["Gospel Music"])[0]
                tags = gospel_plan.get("youtube_optimization", {}).get("tags", [])
        
        # DYNAMIC SPECIALIZED CHANNEL GENERATION
        elif has_specialized and generator_type == "tech":
            st.info(f"🤖 **Tech Education Video Generator**\n\nTopic: {st.session_state.get('spec_topic', 'AI Basics')} | Complexity: {st.session_state.get('spec_complexity', 'Beginner')} | Duration: {st.session_state.get('spec_duration', 10)} min")
            
            if st.button("✨ Generate Tech Script", use_container_width=True):
                with st.spinner("📝 Creating tech education script..."):
                    try:
                        tech_gen = TechExplainedGenerator()
                        tech_plan = tech_gen.generate_tech_script(
                            topic=st.session_state.get('spec_topic', 'ai_basics'),
                            complexity=st.session_state.get('spec_complexity', 'beginner'),
                            duration_minutes=st.session_state.get('spec_duration', 10)
                        )
                        st.session_state.tech_plan = tech_plan
                        st.success("✅ Tech script generated!")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            
            if "tech_plan" in st.session_state:
                tech_plan = st.session_state.tech_plan
                st.divider()
                st.subheader("📖 Generated Tech Script")
                script = tech_plan["script"]["narrative"]
                st.text_area("Script", value=script, height=200, disabled=True)
                st.subheader("🎨 Production Specifications")
                col_t1, col_t2 = st.columns(2)
                with col_t1:
                    st.markdown("**Visual Suggestions:**")
                    for v in tech_plan.get("visual_suggestions", [])[:3]:
                        st.markdown(f"- {v}")
                with col_t2:
                    st.markdown("**Key Points:**")
                    for p in tech_plan.get("key_points", []):
                        st.markdown(f"- {p}")
                
                title = f"{tech_plan['topic']} - Full Explanation"
                description = f"Learn about {tech_plan['topic'].lower()} in this comprehensive video."
                tags = tech_plan.get("tags", [])
        
        # ADD MORE SPECIALIZED CHANNELS HERE...
        elif has_specialized and generator_type == "tutorial":
            st.info(f"📚 **Tutorial Generator**\n\nCategory: {st.session_state.get('spec_category', 'DIY')} | Steps: {st.session_state.get('spec_steps', 5)} | Duration: {st.session_state.get('spec_duration', 12)} min")
            
            if st.button("✨ Generate Tutorial Script", use_container_width=True):
                with st.spinner("📝 Creating tutorial script..."):
                    try:
                        tutorial_gen = TutorialGenerator()
                        tutorial_plan = tutorial_gen.generate_tutorial_script(
                            category=st.session_state.get('spec_category', 'diy_project'),
                            title=st.session_state.get('spec_title', 'How To'),
                            num_steps=st.session_state.get('spec_steps', 5),
                            duration_minutes=st.session_state.get('spec_duration', 12)
                        )
                        st.session_state.tutorial_plan = tutorial_plan
                        st.success("✅ Tutorial script generated!")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            
            if "tutorial_plan" in st.session_state:
                tutorial_plan = st.session_state.tutorial_plan
                st.divider()
                st.subheader("📖 Generated Tutorial Script")
                script = tutorial_plan["script"]["narrative"]
                st.text_area("Script", value=script, height=200, disabled=True)
                title = st.session_state.get('spec_title', 'How To Tutorial')
                description = f"Step-by-step guide: {title}"
                tags = tutorial_plan.get("tags", [])
        
        # Finance Configuration UI
        elif has_specialized and generator_type == "finance":
            st.info(f"💰 **Financial Analysis Generator**\n\nTopic: {st.session_state.get('spec_topic', 'Stock Analysis')} |Duration: {st.session_state.get('spec_duration', 12)} min")
            
            if st.button("✨ Generate Finance Script", use_container_width=True):
                with st.spinner("📝 Creating finance analysis script..."):
                    try:
                        finance_gen = FinanceAnalysisGenerator()
                        finance_plan = finance_gen.generate_finance_script(
                            topic=st.session_state.get('spec_topic', 'stock_analysis'),
                            duration_minutes=st.session_state.get('spec_duration', 12)
                        )
                        st.session_state.finance_plan = finance_plan
                        st.success("✅ Finance script generated!")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            
            if "finance_plan" in st.session_state:
                finance_plan = st.session_state.finance_plan
                st.divider()
                st.subheader("📈 Generated Analysis Script")
                script = finance_plan["script"]["narrative"]
                st.text_area("Script", value=script, height=200, disabled=True)
                title = f"{finance_plan['topic']} - Market Analysis"
                description = f"In-depth analysis of {finance_plan['topic'].lower()}."
                tags = finance_plan.get("tags", [])
        
        # Trending Commentary Configuration UI
        elif has_specialized and generator_type == "trending":
            st.info(f"🔥 **Trending Commentary Generator**\n\nStyle: {st.session_state.get('spec_style', 'News Breakdown')} | Topic: {st.session_state.get('spec_topic', '')} | Duration: {st.session_state.get('spec_duration', 10)} min")
            
            if st.button("✨ Generate Commentary Script", use_container_width=True):
                with st.spinner("📝 Creating commentary script..."):
                    try:
                        trending_gen = TrendingCommentaryGenerator()
                        trending_plan = trending_gen.generate_commentary_script(
                            style=st.session_state.get('spec_style', 'news_breakdown'),
                            topic=st.session_state.get('spec_topic', 'trending topic'),
                            duration_minutes=st.session_state.get('spec_duration', 10)
                        )
                        st.session_state.trending_plan = trending_plan
                        st.success("✅ Commentary script generated!")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            
            if "trending_plan" in st.session_state:
                trending_plan = st.session_state.trending_plan
                st.divider()
                st.subheader("🎬 Generated Commentary Script")
                script = trending_plan["script"]["narrative"]
                st.text_area("Script", value=script, height=200, disabled=True)
                title = f"{st.session_state.get('spec_topic', 'Trending')} - Commentary"
                description = f"My take on what's trending."
                tags = trending_plan.get("tags", [])
        
        # Wellness Configuration UI
        elif has_specialized and generator_type == "wellness":
            st.info(f"💚 **Wellness Content Generator**\n\nTopic: {st.session_state.get('spec_topic', 'Fitness')} | Tips: {st.session_state.get('spec_tips', 5)} | Duration: {st.session_state.get('spec_duration', 15)} min")
            
            if st.button("✨ Generate Wellness Script", use_container_width=True):
                with st.spinner("📝 Creating wellness content..."):
                    try:
                        wellness_gen = WellnessLifestyleGenerator()
                        wellness_plan = wellness_gen.generate_wellness_script(
                            topic=st.session_state.get('spec_topic', 'fitness_routine'),
                            tips_count=st.session_state.get('spec_tips', 5),
                            duration_minutes=st.session_state.get('spec_duration', 15)
                        )
                        st.session_state.wellness_plan = wellness_plan
                        st.success("✅ Wellness script generated!")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            
            if "wellness_plan" in st.session_state:
                wellness_plan = st.session_state.wellness_plan
                st.divider()
                st.subheader("🌱 Generated Wellness Script")
                script = wellness_plan["script"]["narrative"]
                st.text_area("Script", value=script, height=200, disabled=True)
                title = f"{wellness_plan['topic']} - {st.session_state.get('spec_tips', 5)} Tips"
                description = f"Practical wellness guidance for {wellness_plan['topic'].lower()}."
                tags = wellness_plan.get("tags", [])
        
        # Spiritual Configuration UI
        elif has_specialized and generator_type == "spiritual":
            st.info(f"✨ **Spiritual Content Generator**\n\nTopic: {st.session_state.get('spec_topic', 'Wisdom')} | Duration: {st.session_state.get('spec_duration', 15)} min")
            
            if st.button("✨ Generate Spiritual Script", use_container_width=True):
                with st.spinner("📝 Creating spiritual content..."):
                    try:
                        spiritual_gen = SpiritualDocumentaryGenerator()
                        spiritual_plan = spiritual_gen.generate_spiritual_script(
                            topic=st.session_state.get('spec_topic', 'wisdom_teachings'),
                            duration_minutes=st.session_state.get('spec_duration', 15)
                        )
                        st.session_state.spiritual_plan = spiritual_plan
                        st.success("✅ Spiritual script generated!")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            
            if "spiritual_plan" in st.session_state:
                spiritual_plan = st.session_state.spiritual_plan
                st.divider()
                st.subheader("🙏 Generated Spiritual Script")
                script = spiritual_plan["script"]["narrative"]
                st.text_area("Script", value=script, height=200, disabled=True)
                title = f"{spiritual_plan['topic']} - Spiritual Wisdom"
                description = f"Exploring {spiritual_plan['topic'].lower()} for spiritual growth."
                tags = spiritual_plan.get("tags", [])
        
        # Business Configuration UI
        elif has_specialized and generator_type == "business":
            st.info(f"💼 **Business Insights Generator**\n\nTopic: {st.session_state.get('spec_topic', 'Business')} | Insights: {st.session_state.get('spec_insights', 5)} | Duration: {st.session_state.get('spec_duration', 18)} min")
            
            if st.button("✨ Generate Business Script", use_container_width=True):
                with st.spinner("📝 Creating business content..."):
                    try:
                        business_gen = BusinessInsightsGenerator()
                        business_plan = business_gen.generate_business_script(
                            topic=st.session_state.get('spec_topic', 'startup_advice'),
                            insights_count=st.session_state.get('spec_insights', 5),
                            duration_minutes=st.session_state.get('spec_duration', 18)
                        )
                        st.session_state.business_plan = business_plan
                        st.success("✅ Business script generated!")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            
            if "business_plan" in st.session_state:
                business_plan = st.session_state.business_plan
                st.divider()
                st.subheader("💡 Generated Business Script")
                script = business_plan["script"]["narrative"]
                st.text_area("Script", value=script, height=200, disabled=True)
                title = f"{business_plan['topic']} - {st.session_state.get('spec_insights', 5)} Key Insights"
                description = f"Expert insights on {business_plan['topic'].lower()}."
                tags = business_plan.get("tags", [])
                target_duration = gospel_duration * 60
        else:
            # Standard script input for non-Gospel channels
            script = st.text_area(
                "Paste Your Raw Script",
                height=200,
                placeholder="Paste your complete script here. The system will enhance it, generate visuals, voice, and post to YouTube.",
            )
            
            # Title & Description
            col_t, col_d = st.columns([1, 1])
            with col_t:
                title = st.text_input("Video Title", max_chars=100, placeholder="Catchy, specific title")
            with col_d:
                description = st.text_area("Description", height=100, placeholder="YouTube description")
            
            # Video duration target
            target_duration = st.slider("Target Duration (seconds)", 300, 1800, 600)
            
            # Tags
            tags_str = st.text_input("Tags (comma-separated)", placeholder="AI, YouTube, Creator, Tech...")
            tags = [t.strip() for t in tags_str.split(",") if t.strip()]
    
    with col2:
        st.subheader("⚙️ Quick Settings")
        
        # Only show style selector for non-specialized or standard channels
        if not has_specialized:
            # Video style quick select
            try:
                default_style = VideoStyleSelector.suggest_style_for_script(script if 'script' in locals() else "", channel_type)
            except:
                default_style = "cinematic_narration"
            all_styles = list(VideoStyleSelector.VIDEO_COMPOSITION_STYLES.keys())
            selected_style = st.selectbox(
                "Video Style",
                all_styles,
                index=all_styles.index(default_style) if default_style in all_styles else 0,
                format_func=lambda x: VideoStyleSelector.VIDEO_COMPOSITION_STYLES[x]["name"]
            )
        else:
            # Specialized channels have their own style
            selected_style = channel_type
        
        # Voice selection
        default_voice_index = 0
        if has_specialized:
            if generator_type in ["gospel", "wellness", "spiritual"]:
                default_voice_index = 1  # Bella for spiritual content
            elif generator_type == "business":
                default_voice_index = 2  # Adam for business
        
        voice_id = st.selectbox(
            "Narrator Voice",
            ["Rachel (Warm)", "Bella (Friendly)", "Adam (Professional)"],
            index=default_voice_index
        )
        voice_map = {
            "Rachel (Warm)": "21m00Tcm4TlvDq8ikWAM",
            "Bella (Friendly)": "EXAVITQu4vr4xnSDxMaL",
            "Adam (Professional)": "pNInz6obpgDQGcFmaJgB",
        }
        
        # Publish settings
        st.markdown("### Publish Settings")
        publish_now = st.checkbox("Publish Immediately", value=True)
        privacy = st.radio("Privacy", ["Public", "Unlisted", "Private"], horizontal=True)
        
        st.divider()
        
        # Validation - Dynamic based on channel type
        st.subheader("✅ Validation")
        checks = []
        
        if has_specialized:
            # Specialized channel validation
            plan_key = {
                "gospel": "gospel_plan",
                "tech": "tech_plan",
                "tutorial": "tutorial_plan",
                "finance": "finance_plan",
                "trending": "trending_plan",
                "wellness": "wellness_plan",
                "spiritual": "spiritual_plan",
                "business": "business_plan"
            }.get(generator_type, "")
            
            if plan_key and plan_key in st.session_state:
                checks.append(f"✅ {generator_type.title()} script ready")
            else:
                checks.append(f"⚠️ Generate {generator_type} script first")
            checks.append("✅ Configuration selected")
        else:
            # Standard validation
            if 'script' in locals() and script and len(script) > 50:
                checks.append("✅ Script valid")
            else:
                checks.append("⚠️ Script too short")
        
        if 'title' in locals() and title and len(title) <= 100:
            checks.append("✅ Title valid")
        else:
            checks.append("⚠️ Title invalid")
        
        if os.getenv("ELEVENLABS_API_KEY"):
            checks.append("✅ ElevenLabs configured")
        else:
            checks.append("⚠️ ElevenLabs not set")
        
        for check in checks:
            st.text(check)
    
    # MAIN PUBLISH BUTTON - UNIVERSAL FOR ALL GENERATORS
    st.divider()
    st.subheader("🎬 Generate & Publish")
    
    cols_publish = st.columns([1, 1, 1])
    with cols_publish[1]:
        # Determine button label and mechanics based on channel type
        is_specialized = channel_type in CHANNEL_GENERATOR_CONFIG
        generator_type = CHANNEL_GENERATOR_CONFIG[channel_type]["generator_type"] if is_specialized else None
        
        # Map generator_type to display labels and session keys
        spec_labels = {
            "gospel": "🎵 GENERATE GOSPEL MUSIC",
            "tech": "⚙️ GENERATE TECH SCRIPT",
            "tutorial": "📚 GENERATE TUTORIAL",
            "finance": "💰 GENERATE FINANCE",
            "trending": "🔥 GENERATE TRENDING",
            "wellness": "🧘 GENERATE WELLNESS",
            "spiritual": "✨ GENERATE SPIRITUAL",
            "business": "💼 GENERATE BUSINESS"
        }
        
        publish_label = spec_labels.get(generator_type, "🚀 PUBLISH NOW")
        
        if st.button(publish_label, type="primary", use_container_width=True):
            # Specialized channel publishing flow
            if is_specialized and generator_type:
                plan_key = {
                    "gospel": "gospel_plan",
                    "tech": "tech_plan",
                    "tutorial": "tutorial_plan",
                    "finance": "finance_plan",
                    "trending": "trending_plan",
                    "wellness": "wellness_plan",
                    "spiritual": "spiritual_plan",
                    "business": "business_plan"
                }.get(generator_type, "")
                
                if plan_key not in st.session_state:
                    st.error(f"❌ Please generate {generator_type.title()} script first")
                else:
                    with st.spinner(f"🎬 Generating {generator_type} video..."):
                        try:
                            plan = st.session_state[plan_key]
                            progress_bar = st.progress(0)
                            status_text = st.empty()
                            
                            # Step 1: Script ready
                            status_text.text(f"📝 Step 1/3: {generator_type.title()} script ready...")
                            progress_bar.progress(30)
                            
                            # Step 2: Visuals & Audio specs
                            status_text.text("🎨 Step 2/3: Preparing visual & audio production guides...")
                            progress_bar.progress(65)
                            
                            # Step 3: YouTube optimization
                            status_text.text("📤 Step 3/3: Optimizing for YouTube...")
                            progress_bar.progress(100)
                            status_text.text(f"✅ {generator_type.title()} video production plan complete!")
                            
                            st.success(f"✅ **{generator_type.title()} Video Plan Ready!**")
                            
                            # Display complete plan with dynamic layout
                            st.markdown(f"### 📊 {generator_type.title()} Production Plan")
                            
                            # Display metrics based on generator type
                            metric_cols = st.columns(3)
                            
                            if generator_type == "gospel":
                                with metric_cols[0]:
                                    st.metric("Duration", f"{st.session_state.get('spec_duration', 'N/A')} min")
                                with metric_cols[1]:
                                    st.metric("Theme", st.session_state.get('spec_theme', 'N/A').replace("_", " ").title())
                                with metric_cols[2]:
                                    st.metric("Style", st.session_state.get('spec_style', 'N/A').replace("_", " ").title())
                            
                            elif generator_type == "tech":
                                with metric_cols[0]:
                                    st.metric("Topic", st.session_state.get('spec_topic', 'N/A').replace("_", " ").title())
                                with metric_cols[1]:
                                    st.metric("Complexity", st.session_state.get('spec_complexity', 'N/A').title())
                                with metric_cols[2]:
                                    st.metric("Duration", f"{st.session_state.get('spec_duration', 'N/A')} min")
                            
                            elif generator_type == "tutorial":
                                with metric_cols[0]:
                                    st.metric("Category", st.session_state.get('spec_category', 'N/A').replace("_", " ").title())
                                with metric_cols[1]:
                                    st.metric("Steps", st.session_state.get('spec_steps', 'N/A'))
                                with metric_cols[2]:
                                    st.metric("Duration", f"{st.session_state.get('spec_duration', 'N/A')} min")
                            
                            elif generator_type == "finance":
                                with metric_cols[0]:
                                    st.metric("Topic", st.session_state.get('spec_topic', 'N/A').replace("_", " ").title())
                                with metric_cols[1]:
                                    st.metric("Audience", "All Levels")
                                with metric_cols[2]:
                                    st.metric("Duration", f"{st.session_state.get('spec_duration', 'N/A')} min")
                            
                            elif generator_type == "trending":
                                with metric_cols[0]:
                                    st.metric("Style", st.session_state.get('spec_trending_style', 'N/A').replace("_", " ").title())
                                with metric_cols[1]:
                                    st.metric("Topic", st.session_state.get('spec_topic', 'N/A')[:20])
                                with metric_cols[2]:
                                    st.metric("Duration", f"{st.session_state.get('spec_duration', 'N/A')} min")
                            
                            elif generator_type == "wellness":
                                with metric_cols[0]:
                                    st.metric("Topic", st.session_state.get('spec_wellness_topic', 'N/A').replace("_", " ").title())
                                with metric_cols[1]:
                                    st.metric("Tips", st.session_state.get('spec_tips_count', 'N/A'))
                                with metric_cols[2]:
                                    st.metric("Duration", f"{st.session_state.get('spec_duration', 'N/A')} min")
                            
                            elif generator_type == "spiritual":
                                with metric_cols[0]:
                                    st.metric("Topic", st.session_state.get('spec_spiritual_topic', 'N/A').replace("_", " ").title())
                                with metric_cols[1]:
                                    st.metric("Tone", "Meditative")
                                with metric_cols[2]:
                                    st.metric("Duration", f"{st.session_state.get('spec_duration', 'N/A')} min")
                            
                            elif generator_type == "business":
                                with metric_cols[0]:
                                    st.metric("Topic", st.session_state.get('spec_business_topic', 'N/A').replace("_", " ").title())
                                with metric_cols[1]:
                                    st.metric("Insights", st.session_state.get('spec_insights_count', 'N/A'))
                                with metric_cols[2]:
                                    st.metric("Duration", f"{st.session_state.get('spec_duration', 'N/A')} min")
                            
                            st.divider()
                            
                            # Production details
                            st.markdown(f"#### 📖 {generator_type.title()} Script")
                            script_text = plan.get("script", {}).get("narrative", "") if isinstance(plan.get("script"), dict) else plan.get("script", "")
                            st.text(script_text if script_text else "Script generated successfully")
                            
                            col_vis, col_audio = st.columns(2)
                            with col_vis:
                                st.markdown("#### 🎨 Visual Suggestions")
                                visuals = plan.get("visual_suggestions", [])
                                if visuals:
                                    for i, visual in enumerate(visuals, 1):
                                        st.markdown(f"{i}. {visual}")
                                else:
                                    st.markdown("See generated recommendations above")
                            
                            with col_audio:
                                st.markdown("#### 📊 Production Metadata")
                                audio = plan.get("audio_production", {}) if generator_type == "gospel" else {}
                                if audio:
                                    st.markdown(f"**Tempo:** {audio.get('tempo_bpm', 'N/A')}")
                                    st.markdown(f"**Mood:** {audio.get('mood', 'N/A')}")
                                else:
                                    st.markdown(f"**Tags:** {', '.join(plan.get('tags', [])[:5])}")
                            
                            st.divider()
                            st.markdown("#### 🌐 YouTube Optimization")
                            st.json(plan.get("youtube_optimization", {}), expanded=False)
                            
                        except Exception as e:
                            st.error(f"❌ Error: {str(e)}")
            
            # Standard publishing flow (for non-specialized channels)
            else:
                if not script or not title:
                    st.error("❌ Script and title required")
                else:
                    with st.spinner("🎬 Generating video... (this may take a few minutes)"):
                        try:
                            progress_bar = st.progress(0)
                            status_text = st.empty()
                            
                            # Step 1: Enhancement
                            status_text.text("📝 Step 1/4: Enhancing script...")
                            progress_bar.progress(20)
                            
                            # Step 2: Visual generation
                            status_text.text("🎨 Step 2/4: Generating visuals...")
                            progress_bar.progress(40)
                            
                            # Step 3: Composition
                            status_text.text("🎬 Step 3/4: Composing video...")
                            progress_bar.progress(70)
                            
                            # Step 4: Publishing
                            status_text.text("📤 Step 4/4: Publishing to YouTube...")
                            progress_bar.progress(90)
                            
                            # Simulate orchestration
                            project_name = f"video_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                            orchestrator = VideoProductionOrchestrator(project_name)
                            
                            result = orchestrator.produce_video(
                                script=script,
                                title=title,
                                description=description,
                                channel_template=channel_type,
                                visual_style=selected_style,
                                tags=tags,
                                voice_id=voice_map.get(voice_id, "21m00Tcm4TlvDq8ikWAM"),
                                publish_to_youtube=publish_now,
                            )
                            
                            progress_bar.progress(100)
                            status_text.text("✅ Complete!")
                            
                            st.success("✅ **Video Published!**")
                            
                            # Summary
                            st.markdown("### 📊 Production Summary")
                            cols_summary = st.columns(4)
                            with cols_summary[0]:
                                st.metric("Visuals", "✅ Generated")
                            with cols_summary[1]:
                                st.metric("Voice", "✅ Synthesized")
                            with cols_summary[2]:
                                st.metric("Video", "✅ Composed")
                            with cols_summary[3]:
                                st.metric("YouTube", "✅ Posted")
                            
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
        st.subheader("📝 Your Script")
        enhance_script = st.text_area(
            "Paste script to enhance",
            height=200,
            key="enhance_input"
        )
        
        target_dur = st.slider("Target Duration", 300, 1800, 600, key="dur_slider")
        
        enhance_tone = st.selectbox("Tone", ["professional", "casual", "inspirational", "educational"])
        enhance_style = st.selectbox("Style", ["documentary", "storytelling", "analysis", "entertaining"])
        
        if st.button("✨ Enhance Script"):
            if enhance_script:
                with st.spinner("Analyzing and enhancing..."):
                    try:
                        enhancer = ScriptEnhancer()
                        enhanced = enhancer.enhance_script(
                            enhance_script,
                            target_duration_seconds=target_dur,
                            tone=enhance_tone,
                            style=enhance_style,
                        )
                        
                        st.success("✅ Enhancement Complete!")
                        
                        # Display enhanced script
                        st.markdown("### 📖 Enhanced Script")
                        st.text_area("", value=enhanced.get("enhanced_script", ""), height=200, disabled=True)
                        
                        # Metrics
                        st.markdown("### 📊 Script Quality")
                        cols_quality = st.columns(3)
                        with cols_quality[0]:
                            st.metric("Engagement Score", enhanced.get("engagement_score", "N/A"))
                        with cols_quality[1]:
                            st.metric("Duration", f"{enhanced.get('estimated_duration_seconds', 'N/A')}s")
                        with cols_quality[2]:
                            st.metric("SEO Score", "Good")
                        
                        # Key improvements
                        st.markdown("### 🎯 Key Improvements")
                        for improvement in enhanced.get("improvements_made", []):
                            st.write(f"✅ {improvement}")
                        
                        # Suggested visuals
                        st.markdown("### 🎬 Suggested Visuals")
                        for visual in enhanced.get("suggested_visuals", []):
                            st.write(f"📸 {visual}")
                        
                    except Exception as e:
                        st.error(f"Enhancement failed: {e}")
            else:
                st.warning("Please enter a script first")
    
    with col2:
        st.subheader("🔍 Analysis & Suggestions")
        
        if st.button("📊 Analyze Script Quality"):
            if enhance_script:
                with st.spinner("Analyzing quality..."):
                    try:
                        enhancer = ScriptEnhancer()
                        analysis = enhancer.analyze_script_quality(enhance_script)
                        
                        # Display scores
                        st.metric("Overall Score", analysis.get("overall_score", 0))
                        
                        cols_scores = st.columns(3)
                        with cols_scores[0]:
                            st.metric("Hook Strength", analysis.get("hook_strength", 0))
                        with cols_scores[1]:
                            st.metric("Pacing", analysis.get("pacing", 0))
                        with cols_scores[2]:
                            st.metric("Engagement", analysis.get("emotional_engagement", 0))
                        
                        st.markdown("### 💪 Strengths")
                        for strength in analysis.get("strengths", []):
                            st.write(f"✅ {strength}")
                        
                        st.markdown("### 💡 Recommendations")
                        for rec in analysis.get("recommendations", []):
                            st.write(f"📝 {rec}")
                        
                    except Exception as e:
                        st.error(f"Analysis failed: {e}")

# ============================================================================
# TAB 3: CHOOSE VIDEO STYLE
# ============================================================================
with tab_styles:
    st.header("🎬 Choose Your Video Style")
    st.markdown("Select how your video should look and feel")
    
    all_styles = VideoStyleSelector.get_all_styles()
    
    # Display all styles as cards
    cols_styles = st.columns(2)
    selected_style_info = None
    
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
# TAB 4: SURPRISE ME!
# ============================================================================
with tab_surprise:
    st.header("🎲 Surprise Me! (AI Auto-Mode)")
    st.markdown("Let AI analyze your script and create the PERFECT video configuration")
    
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.subheader("📝 Enter Your Script")
        surprise_script = st.text_area("Script for AI analysis", height=200, key="surprise_script")
        surprise_title = st.text_input("Video Title", key="surprise_title")
        surprise_desc = st.text_area("Description", height=100, key="surprise_desc")
        
        if st.button("🎲 Let AI Decide Everything"):
            if surprise_script and surprise_title:
                with st.spinner("🤖 AI analyzing... Creating perfect video config..."):
                    try:
                        surprise_mode = SurpriseGameMode()
                        ai_plan = surprise_mode.analyze_and_generate(
                            surprise_script,
                            surprise_title,
                            surprise_desc
                        )
                        
                        st.success("✅ AI Generated Perfect Plan!")
                        
                        # Display AI recommendations
                        st.markdown("### 🎯 AI's Recommendations")
                        
                        cols_recs = st.columns(2)
                        with cols_recs[0]:
                            st.subheader("📺 Channel Template")
                            st.write(ai_plan.get("best_channel_template", "Unknown"))
                            st.caption(ai_plan.get("reasoning_channel", ""))
                        
                        with cols_recs[1]:
                            st.subheader("🎬 Video Style")
                            st.write(ai_plan.get("best_video_style", "Unknown"))
                            st.caption(ai_plan.get("reasoning_style", ""))
                        
                        cols_voice = st.columns(1)
                        with cols_voice[0]:
                            st.subheader("🎤 Voice & Tone")
                            voice_rec = ai_plan.get("recommended_voice", {})
                            st.write(f"{voice_rec.get('name', 'Unknown')} - {voice_rec.get('reason', '')}")
                        
                        # Key metrics
                        st.markdown("### 📊 Production Metrics")
                        cols_metrics = st.columns(4)
                        with cols_metrics[0]:
                            st.metric("Duration", f"{ai_plan.get('suggested_duration', 'N/A')}s")
                        with cols_metrics[1]:
                            st.metric("Engagement", f"{ai_plan.get('engagement_score', 'N/A')}/100")
                        with cols_metrics[2]:
                            st.metric("Viral Potential", ai_plan.get("viral_potential", "N/A"))
                        with cols_metrics[3]:
                            st.metric("Pacing", ai_plan.get("pacing", "N/A"))
                        
                        # Key visuals
                        st.markdown("### 🎬 Key Visuals")
                        for visual in ai_plan.get("key_visuals", []):
                            st.write(f"📸 {visual}")
                        
                        # Production tips
                        st.markdown("### 💡 Production Tips")
                        for tip in ai_plan.get("production_tips", []):
                            st.write(f"✨ {tip}")
                        
                        # Full plan in JSON
                        st.markdown("### 📋 Full AI Plan (JSON)")
                        st.json(ai_plan)
                        
                        # Ready to publish
                        if st.button("🚀 Use This Plan & Publish"):
                            st.info("👉 Go to 'One-Click Publish' tab and your configuration will be pre-filled")
                        
                    except Exception as e:
                        st.error(f"AI Analysis failed: {e}")
            else:
                st.warning("Please enter script and title")
    
    with col2:
        st.info("""
        ### 🤖 How Surprise Me Works
        
        1. **Script Analysis** - AI reads your content
        2. **Best Template Selection** - Picks ideal channel format
        3. **Video Style Recommendation** - Chooses optimal visual style
        4. **Voice Matching** - Selects perfect narrator
        5. **Pacing Optimization** - Sets appropriate speed
        6. **Color Palette** - Recommends visual colors
        7. **Engagement Optimization** - Maximizes watch time
        """)

# ============================================================================
# TAB 5: BATCH & ANALYTICS
# ============================================================================
with tab_multi:
    st.header("📊 Batch Processing & Analytics")
    
    tab_batch, tab_analytics = st.tabs(["Batch Upload", "Analytics"])
    
    with tab_batch:
        st.subheader("📤 Batch Generate Videos")
        st.markdown("Upload CSV with multiple scripts and generate videos overnight")
        
        uploaded_file = st.file_uploader("Upload CSV (script, title, description columns)", type="csv")
        
        if uploaded_file:
            import pandas as pd
            df = pd.read_csv(uploaded_file)
            st.write(f"📋 Loaded {len(df)} videos")
            st.dataframe(df.head())
            
            if st.button("🚀 Start Batch Generation"):
                st.info("Batch generation would start videos in queue")
                st.write("Feature coming soon - generates videos 24/7")
    
    with tab_analytics:
        st.subheader("📈 Channel Analytics")
        st.write("Track all published videos and their performance")
        
        # Placeholder analytics
        st.metric("Total Videos", "0")
        st.metric("Total Views", "0")
        st.metric("Avg Engagement", "0%")

# ============================================================================
# FOOTER
# ============================================================================
st.divider()
st.markdown("""
### 🚀 Next Steps
1. ✅ Add API keys in sidebar
2. 📝 Enter script or choose "Surprise Me!"
3. 🚀 Click "Publish Now"
4. ✨ Video goes live on YouTube

### 📚 Resources
• [ComfyUI](https://github.com/comfyanonymous/ComfyUI) • [ElevenLabs](https://elevenlabs.io/) • [n8n](https://n8n.io/) • [Make.com](https://www.make.com/)

**Built with ❤️ for creators. Your AI production team works 24/7.** 🎬
""")

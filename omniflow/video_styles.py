"""Extended channel templates with more professional presets.

Includes:
- 10+ proven YouTube channel formats
- Pre-configured settings for each
- Visual style, voice, pacing presets
- Anti-AI detection optimizations
"""
from typing import Dict, List

EXPANDED_CHANNEL_TEMPLATES = {
    # STORYTELLING & DOCUMENTARY
    "spiritual_documentary": {
        "name": "Spiritual & Inspirational",
        "reference": "The Book of Psalms Bible",
        "category": "Spirituality, Religion, Personal Growth",
        "visual_style": "Real Human Character (Consistent)",
        "animation_type": "Cinematic Fade + Ambient Music",
        "voice": {"id": "21m00Tcm4TlvDq8ikWAM", "name": "Rachel", "tone": "warm, reflective"},
        "pacing": "slow_meditative",
        "video_duration_range": (8, 20),
        "color_palette": "calm_earth_tones",
        "description_template": "Explore spiritual wisdom and timeless teachings. Daily inspiration for the soul.",
        "tags": ["Spirituality", "Inspiration", "Religious", "Wisdom", "Faith", "Meditation"],
    },
    
    "geopolitical_deep_dive": {
        "name": "Geopolitical Analysis & World News",
        "reference": "DeGlobal Lens",
        "category": "News, Politics, Analysis",
        "visual_style": "Cinematic Landscapes + Data Overlays",
        "animation_type": "Professional Transitions + Maps",
        "voice": {"id": "pNInz6obpgDQGcFmaJgB", "name": "Adam", "tone": "authoritative, analytical"},
        "pacing": "professional_medium",
        "video_duration_range": (10, 25),
        "color_palette": "professional_blues_grays",
        "description_template": "Breaking down complex geopolitical events. In-depth analysis with expert insights.",
        "tags": ["Geopolitics", "News", "Analysis", "International", "Politics", "Economics"],
    },
    
    "cultural_travel": {
        "name": "Cultural & Travel Documentary",
        "reference": "Philippine's Tale",
        "category": "Travel, Culture, Lifestyle",
        "visual_style": "Real Human Character (Consistent)",
        "animation_type": "Natural Transitions + Location Vibes",
        "voice": {"id": "EXAVITQu4vr4xnSDxMaL", "name": "Bella", "tone": "warm, engaging, personal"},
        "pacing": "narrative_storytelling",
        "video_duration_range": (8, 18),
        "color_palette": "vibrant_warm_natural",
        "description_template": "Discovering authentic cultures and stories from around the world. Real people, real stories.",
        "tags": ["Travel", "Culture", "Documentary", "People", "Stories", "Authentic"],
    },
    
    # EDUCATION & EXPLANATION
    "tech_explained_animated": {
        "name": "Technology & AI Explained",
        "reference": "Professional Tech Education",
        "category": "Technology, Science, Education",
        "visual_style": "AI Character Avatar (Animated)",
        "animation_type": "Dynamic Talking Head + Graphics",
        "voice": {"id": "21m00Tcm4TlvDq8ikWAM", "name": "Rachel", "tone": "clear, enthusiastic"},
        "pacing": "educational_moderate",
        "video_duration_range": (5, 15),
        "color_palette": "tech_modern_bright",
        "description_template": "Breaking down complex tech concepts in simple terms. Clear explanations, practical applications.",
        "tags": ["Technology", "AI", "Tutorial", "Learning", "Explained", "Education"],
    },
    
    "how_to_tutorial": {
        "name": "How-To & Tutorial",
        "reference": "Professional DIY Tutorials",
        "category": "Education, DIY, How-To",
        "visual_style": "Interactive Dialogue (Expert + Steps)",
        "animation_type": "Screen Recording + Voiceover + Tips",
        "voice": {"id": "21m00Tcm4TlvDq8ikWAM", "name": "Rachel", "tone": "instructional, encouraging"},
        "pacing": "step_by_step_detailed",
        "video_duration_range": (5, 20),
        "color_palette": "clean_instructional",
        "description_template": "Step-by-step guide with timestamps. Follow along to master this skill.",
        "tags": ["Tutorial", "How-To", "DIY", "Learning", "Steps", "Guide"],
    },
    
    "financial_analysis": {
        "name": "Finance & Investment Analysis",
        "reference": "Professional Finance Channels",
        "category": "Finance, Business, Investing",
        "visual_style": "Cinematic Landscapes + Charts/Data",
        "animation_type": "Professional Charts + Real Person Commentary",
        "voice": {"id": "pNInz6obpgDQGcFmaJgB", "name": "Adam", "tone": "professional, confident"},
        "pacing": "analytical_detailed",
        "video_duration_range": (8, 20),
        "color_palette": "professional_golds_grays",
        "description_template": "Data-driven financial insights and market analysis. Research-backed recommendations.",
        "tags": ["Finance", "Investing", "Money", "Analysis", "Trading", "Economics"],
    },
    
    # ENTERTAINMENT & LIFESTYLE
    "trending_commentary": {
        "name": "Trending News & Commentary",
        "reference": "Professional News Commentary",
        "category": "News, Entertainment, Meta-Commentary",
        "visual_style": "Real Human Character + Trending Clips",
        "animation_type": "Fast Cuts + Reactions + B-Roll",
        "voice": {"id": "EXAVITQu4vr4xnSDxMaL", "name": "Bella", "tone": "engaging, opinionated"},
        "pacing": "fast_energetic",
        "video_duration_range": (5, 15),
        "color_palette": "vibrant_trendy",
        "description_template": "My take on what's trending. Weekly commentary on news, culture, and viral moments.",
        "tags": ["Trending", "News", "Commentary", "Culture", "Opinion", "Viral"],
    },
    
    "wellness_lifestyle": {
        "name": "Health, Wellness & Lifestyle",
        "reference": "Professional Lifestyle Channels",
        "category": "Health, Wellness, Lifestyle",
        "visual_style": "Real Human Character + Serene Environments",
        "animation_type": "Peaceful Transitions + Demo Footage",
        "voice": {"id": "EXAVITQu4vr4xnSDxMaL", "name": "Bella", "tone": "calming, supportive"},
        "pacing": "relaxed_mindful",
        "video_duration_range": (10, 25),
        "color_palette": "calm_wellness_greens",
        "description_template": "Practical wellness tips and lifestyle advice. Improve your health and happiness.",
        "tags": ["Health", "Wellness", "Lifestyle", "Tips", "Self-Care", "Personal-Growth"],
    },
    
    "creative_showcase": {
        "name": "Creative & Artistic Showcase",
        "reference": "Professional Art Channels",
        "category": "Art, Music, Creative",
        "visual_style": "Process Footage + Artist Interview",
        "animation_type": "Creative Transitions + Time-Lapse",
        "voice": {"id": "EXAVITQu4vr4xnSDxMaL", "name": "Bella", "tone": "artistic, inspiring"},
        "pacing": "cinematic_artistic",
        "video_duration_range": (8, 20),
        "color_palette": "artistic_vibrant",
        "description_template": "Exploring creative processes, techniques, and artistic inspiration.",
        "tags": ["Art", "Creative", "Music", "Design", "Process", "Inspiration"],
    },
    
    # BUSINESS & ENTREPRENEURSHIP
    "business_insights": {
        "name": "Business & Entrepreneurship",
        "reference": "Professional Business Channels",
        "category": "Business, Entrepreneurship, Self-Help",
        "visual_style": "Real Human Expert + Office/Professional Settings",
        "animation_type": "Interview Style + Key Points Overlay",
        "voice": {"id": "pNInz6obpgDQGcFmaJgB", "name": "Adam", "tone": "authoritative, inspiring"},
        "pacing": "expert_paced",
        "video_duration_range": (10, 25),
        "color_palette": "professional_power_colors",
        "description_template": "Business strategies, entrepreneurial insights, and success principles.",
        "tags": ["Business", "Entrepreneurship", "Strategy", "Success", "Growth", "Leadership"],
    },
    
    "controversy_analysis": {
        "name": "Controversy & Deep Dives",
        "reference": "Professional Investigation Channels",
        "category": "News, Investigation, Analysis",
        "visual_style": "Cinematic Recreation + Real Footage",
        "animation_type": "Dramatic Pacing + B-Roll + Interviews",
        "voice": {"id": "pNInz6obpgDQGcFmaJgB", "name": "Adam", "tone": "serious, investigative"},
        "pacing": "investigative_detailed",
        "video_duration_range": (15, 30),
        "color_palette": "serious_dark_tones",
        "description_template": "In-depth investigation into complex controversies. Research-backed, fact-checked reporting.",
        "tags": ["Investigation", "Controversy", "Deep-Dive", "Analysis", "News", "Truth"],
    },
    
    # SPECIALIZED CHANNELS
    "gospel_music": {
        "name": "Gospel & Spiritual Music Videos",
        "reference": "Professional Gospel Music Channels",
        "category": "Music, Spiritual, Gospel, Religious",
        "visual_style": "Spiritual Cinematography + Light Effects + Worship Imagery",
        "animation_type": "Gospel Production + Emotional Transitions + Lyrical Graphics",
        "voice": {"id": "EXAVITQu4vr4xnSDxMaL", "name": "Bella", "tone": "soulful, spiritual, passionate"},
        "pacing": "rhythmic_musical",
        "video_duration_range": (3, 10),
        "color_palette": "warm_spiritual_golds",
        "description_template": "Original gospel music with inspiring messages. Soul-stirring melodies for worship and prayer.",
        "tags": ["Gospel", "Music", "Spiritual", "Religious", "Worship", "Faith", "Soul", "Christian"],
        "specialty_generator": "gospel_music",  # Uses GospelMusicVideoGenerator
        "gospel_themes": ["faith", "redemption", "worship", "spiritual_journey", "praise_celebration", "biblical_stories"],
        "gospel_styles": ["traditional_gospel", "contemporary_gospel", "soul_gospel", "spiritual_ambient"],
    },
    
    "crime_story_narrative": {
        "name": "Crime Story & True Crime",
        "reference": "Professional True Crime Channels",
        "category": "True Crime, Mystery, Investigation",
        "visual_style": "Cinematic Reenactment + Documentary Footage + Dramatic Edits",
        "animation_type": "Fast Cuts + Suspenseful Transitions + Timeline Graphics",
        "voice": {"id": "pNInz6obpgDQGcFmaJgB", "name": "Adam", "tone": "dramatic, suspenseful, serious"},
        "pacing": "fast_suspenseful",
        "video_duration_range": (10, 30),
        "color_palette": "dark_dramatic_mystery",
        "description_template": "Untold stories from crime investigations. Evidence, psychology, and justice.",
        "tags": ["True-Crime", "Investigation", "Mystery", "Drama", "Justice", "Cases"],
    },
    
    "custom_channel": {
        "name": "Custom Channel (Your Own Template)",
        "reference": "Create Your Own Niche",
        "category": "Fully Customizable",
        "visual_style": "Your Choice (or describe)",
        "animation_type": "Your Choice",
        "voice": {"id": "21m00Tcm4TlvDq8ikWAM", "name": "Rachel", "tone": "customizable"},
        "pacing": "flexible",
        "video_duration_range": (5, 60),
        "color_palette": "your_choice",
        "description_template": "Your custom channel description here.",
        "tags": ["Custom", "Your-Niche", "Personalized"],
        "custom": True,
    },
}


class VideoStyleSelector:
    """Select video composition style based on script and preferences."""
    
    VIDEO_COMPOSITION_STYLES = {
        "animated_text_voiceover": {
            "name": "Animated Text + Voiceover",
            "description": "Text animations, graphics, and voiceover narration. No humans needed.",
            "best_for": ["Tech Explained", "How-To", "Finance Analysis", "Data Stories"],
            "complexity": "medium",
            "production_time": "medium",
            "cost_efficiency": "high",
            "engagement_level": "medium",
            "examples": "Explainer videos, tutorials, educational content",
        },
        "interactive_dialogue": {
            "name": "Interactive Multi-Character Dialogue",
            "description": "Multiple characters having conversations with natural interactions.",
            "best_for": ["Trending Commentary", "Controversy Analysis", "Interviews"],
            "complexity": "high",
            "production_time": "long",
            "cost_efficiency": "medium",
            "engagement_level": "very_high",
            "examples": "Podcast-style debates, interviews, dramatic conversations",
        },
        "human_avatar_hybrid": {
            "name": "Real Human + Animated Avatar (Hybrid)",
            "description": "Combine real human footage with AI avatars for visual variety.",
            "best_for": ["Spiritual", "Cultural", "Travel", "Wellness"],
            "complexity": "high",
            "production_time": "long",
            "cost_efficiency": "medium",
            "engagement_level": "very_high",
            "examples": "Documentary style, authentic storytelling",
        },
        "cinematic_landscape": {
            "name": "Cinematic Landscape + Overlays",
            "description": "Professional cinematic backgrounds with text overlays and voiceover.",
            "best_for": ["Documentary", "Geopolitical", "Travel", "Nature"],
            "complexity": "medium",
            "production_time": "medium",
            "cost_efficiency": "high",
            "engagement_level": "high",
            "examples": "Documentary narration, landscape videography",
        },
        "talking_head_avatar": {
            "name": "Talking Head Avatar (Animated)",
            "description": "AI-generated animated avatar speaking directly to camera.",
            "best_for": ["Tech", "Business", "Education", "Lifestyle"],
            "complexity": "low",
            "production_time": "short",
            "cost_efficiency": "very_high",
            "engagement_level": "medium",
            "examples": "News anchors, expert commentary, educational videos",
        },
        "visual_storytelling": {
            "name": "Visual Storytelling (Cinematic Montage)",
            "description": "Series of cinematic shots synced to emotional narrative.",
            "best_for": ["Spiritual", "Cultural", "Travel", "Personal Stories"],
            "complexity": "medium",
            "production_time": "medium",
            "cost_efficiency": "high",
            "engagement_level": "high",
            "examples": "Documentary-style storytelling, brand stories",
        },
    }
    
    @staticmethod
    def suggest_style_for_script(script: str, template: str) -> str:
        """AI-suggest best video style for given script and template."""
        # Simple heuristic-based suggestion
        script_lower = script.lower()
        
        if any(word in script_lower for word in ["explain", "how to", "tutorial", "step", "guide"]):
            return "animated_text_voiceover"
        elif any(word in script_lower for word in ["discuss", "debate", "interview", "conversation", "think"]):
            return "interactive_dialogue"
        elif any(word in script_lower for word in ["spiritual", "faith", "peace", "journey", "discover"]):
            return "visual_storytelling"
        elif any(word in script_lower for word in ["analyze", "chart", "data", "trend", "market"]):
            return "animated_text_voiceover"
        elif any(word in script_lower for word in ["travel", "culture", "explore", "local", "community"]):
            return "human_avatar_hybrid"
        else:
            return "cinematic_landscape"
    
    @staticmethod
    def get_all_styles() -> Dict:
        """Return all available video composition styles."""
        return VideoStyleSelector.VIDEO_COMPOSITION_STYLES
    
    @staticmethod
    def get_style_details(style_name: str) -> Dict:
        """Get detailed info about a specific style."""
        return VideoStyleSelector.VIDEO_COMPOSITION_STYLES.get(style_name, {})


class SurpriseGameMode:
    """Auto-generate perfect matching video for script (AI decides everything)."""
    
    @staticmethod
    def analyze_and_generate(
        script: str,
        title: str,
        description: str
    ) -> Dict:
        """Analyze script and auto-select channel, style, voice, everything.
        
        Returns optimal config for maximum engagement.
        """
        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError("Install openai: pip install openai")
        
        import os
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        prompt = f"""Analyze this YouTube script and create the PERFECT video production plan.

SCRIPT: {script[:500]}...
TITLE: {title}
DESCRIPTION: {description[:200]}...

Analyze and return JSON with:
{{
    "best_channel_template": "Name of template",
    "reasoning_channel": "Why this channel template fits",
    "best_video_style": "Video composition style",
    "reasoning_style": "Why this style will maximize engagement",
    "recommended_voice": {{"id": "...", "name": "...", "reason": "..."}},
    "pacing": "slow/medium/fast",
    "suggested_duration": 600,
    "color_palette": "suggested colors",
    "music_genre": "recommended music genre",
    "tone": "How narrator should sound",
    "key_visuals": ["visual1", "visual2"],
    "engagement_score": 0-100,
    "viral_potential": "low/medium/high",
    "target_audience": "who will watch this",
    "seo_keywords": ["keyword1", "keyword2"],
    "production_tips": ["tip1", "tip2", "tip3"]
}}
"""
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        
        try:
            result = json.loads(response.choices[0].message.content)
        except:
            import re
            match = re.search(r"\{[\s\S]*\}", response.choices[0].message.content)
            result = json.loads(match.group()) if match else {}
        
        return result

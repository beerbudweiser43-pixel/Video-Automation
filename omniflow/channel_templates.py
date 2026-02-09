"""Professional channel templates matching reference channels.

These templates are pre-configured for:
- The Book of Psalms Bible (religious/documentary storytelling)
- DeGlobal Lens (geopolitical analysis with real humans)
- Philippine's Tale (cultural documentary with consistent narrator)
"""
from typing import Dict, List


CHANNEL_TEMPLATES = {
    "religious_documentary": {
        "name": "Religious Documentary (Bible, Psalms, etc.)",
        "reference": "@thebookofpsalmsbible-q3m",
        "description": "Professional storytelling with consistent narrator, cinematic visuals, and authentic mood",
        "visual_style": "Real Human Character (Consistent)",
        "voice_settings": {
            "voice_id": "21m00Tcm4TlvDq8ikWAM",  # Rachel - warm, clear
            "stability": 0.65,
            "similarity": 0.8,
        },
        "metadata_template": {
            "category_id": "27",  # Education
            "tags": ["Bible", "Psalms", "Scripture", "Religious", "Faith", "Spirituality"],
            "description_intro": "Exploring the wisdom and teachings of the Bible...",
            "description_outro": "Like and subscribe for daily spiritual inspiration.",
        },
        "thumbnail_style": "Text overlay + calming colors + religious iconography",
        "pacing": {
            "intro_duration": 5,
            "main_content_duration": 8,
            "outro_duration": 2,
        },
        "branding": {
            "watermark": "small_corner",
            "intro_animation": "elegant_fade",
            "music_tone": "inspirational",
        },
    },
    
    "geopolitical_analysis": {
        "name": "Geopolitical Analysis (News, Analysis)",
        "reference": "@degloballens",
        "description": "In-depth analysis with real human expert, cinematic locations, documentary-style pacing",
        "visual_style": "Cinematic Landscapes + Text Overlays",
        "voice_settings": {
            "voice_id": "pNInz6obpgDQGcFmaJgB",  # Adam - professional, deep
            "stability": 0.7,
            "similarity": 0.85,
        },
        "metadata_template": {
            "category_id": "25",  # News & Politics
            "tags": ["Geopolitics", "Analysis", "News", "World", "Current Events"],
            "description_intro": "Breaking down complex geopolitical events...",
            "description_outro": "What's your take? Comment below.",
        },
        "thumbnail_style": "Bold fonts + map graphics + analytics charts",
        "pacing": {
            "intro_duration": 3,
            "main_content_duration": 12,
            "outro_duration": 2,
        },
        "branding": {
            "watermark": "moderate_bottom",
            "intro_animation": "professional_slide",
            "music_tone": "investigative",
        },
    },
    
    "cultural_documentary": {
        "name": "Cultural Documentary (Travel, Culture)",
        "reference": "@philippinestale",
        "description": "Warm, engaging storytelling about culture with consistent narrator, authentic locations",
        "visual_style": "Real Human Character (Consistent)",
        "voice_settings": {
            "voice_id": "EXAVITQu4vr4xnSDxMaL",  # Bella - warm, friendly
            "stability": 0.6,
            "similarity": 0.75,
        },
        "metadata_template": {
            "category_id": "26",  # Howto & Style / 22 = People & Blogs
            "tags": ["Culture", "Travel", "Documentary", "Story", "People", "Community"],
            "description_intro": "Discovering the rich culture and stories of...",
            "description_outro": "Follow along for more real stories from around the world.",
        },
        "thumbnail_style": "Warm colors + smiling faces + cultural elements",
        "pacing": {
            "intro_duration": 4,
            "main_content_duration": 10,
            "outro_duration": 3,
        },
        "branding": {
            "watermark": "subtle_corner",
            "intro_animation": "warm_fade",
            "music_tone": "uplifting_cultural",
        },
    },
    
    "tech_explained": {
        "name": "Tech & AI Explained (Education)",
        "reference": "Custom - Professional tech channel",
        "description": "Clear explanations with visuals, consistent AI avatar, upbeat tone",
        "visual_style": "AI Character Avatar (Animated)",
        "voice_settings": {
            "voice_id": "21m00Tcm4TlvDq8ikWAM",  # Rachel - clear
            "stability": 0.7,
            "similarity": 0.75,
        },
        "metadata_template": {
            "category_id": "28",  # Science & Technology
            "tags": ["Technology", "AI", "Coding", "Tutorial", "Explained", "Learning"],
            "description_intro": "Breaking down complex tech concepts in simple terms...",
            "description_outro": "Comment what topic you want us to explain next!",
        },
        "thumbnail_style": "Bold text + tech icons + bright colors",
        "pacing": {
            "intro_duration": 3,
            "main_content_duration": 10,
            "outro_duration": 2,
        },
        "branding": {
            "watermark": "small_corner",
            "intro_animation": "modern_pop",
            "music_tone": "upbeat_tech",
        },
    },
}


class ChannelTemplate:
    """Load and apply pre-configured channel templates."""
    
    def __init__(self, template_name: str):
        if template_name not in CHANNEL_TEMPLATES:
            raise ValueError(f"Unknown template: {template_name}. Available: {list(CHANNEL_TEMPLATES.keys())}")
        
        self.config = CHANNEL_TEMPLATES[template_name]
    
    def get_visual_style(self) -> str:
        return self.config["visual_style"]
    
    def get_voice_settings(self) -> Dict:
        return self.config["voice_settings"]
    
    def get_metadata_template(self) -> Dict:
        return self.config["metadata_template"]
    
    def get_branding(self) -> Dict:
        return self.config["branding"]
    
    def get_pacing(self) -> Dict:
        return self.config["pacing"]
    
    def prepare_description(self, custom_description: str) -> str:
        """Format description according to template."""
        template = self.config["metadata_template"]
        intro = template.get("description_intro", "")
        outro = template.get("description_outro", "")
        
        return f"{intro}\n\n{custom_description}\n\n{outro}"
    
    def prepare_title(self, base_title: str) -> str:
        """Optimize title based on template (avoid AI-obvious keywords)."""
        # Remove AI-obvious phrases
        ai_phrases = ["AI-generated", "AI-created", "AI narrator", "AI voice"]
        title = base_title
        for phrase in ai_phrases:
            title = title.replace(phrase, "")
        
        return title.strip()
    
    def get_full_config(self) -> Dict:
        """Get complete template config."""
        return self.config
    
    @staticmethod
    def list_templates() -> Dict[str, str]:
        """List all available templates with descriptions."""
        return {
            name: config["description"]
            for name, config in CHANNEL_TEMPLATES.items()
        }


# Presets for avoiding YouTube "obviously AI" detection
ANTI_DETECTION_GUIDELINES = {
    "visual_quality": [
        "✓ Use cinematic visuals with depth-of-field",
        "✓ Add real people/humans when possible",
        "✓ Use consistent characters across videos",
        "✓ Include authentic locations/backgrounds",
        "✗ Avoid perfect symmetry and hyper-realistic plastic look",
        "✗ Avoid uncanny valley animations",
        "✗ Avoid obvious image artifacts",
    ],
    "audio": [
        "✓ Use natural voice variations and pauses",
        "✓ Add background ambience (street sounds, nature, room tone)",
        "✓ Vary speaking pace and emphasis naturally",
        "✗ Avoid robotic inflection",
        "✗ Avoid overly perfect pronunciations",
        "✗ Avoid obvious lip-sync issues",
    ],
    "content_structure": [
        "✓ Start with authentic introductions",
        "✓ Include genuine-seeming reactions to material",
        "✓ Use natural transitions, not flashy effects",
        "✓ Have consistent narrative voice throughout series",
        "✗ Avoid hyper-fast pacing",
        "✗ Avoid corporate-sounding overlays",
        "✗ Avoid obvious AI-generated captions",
    ],
    "metadata": [
        "✓ Use authentic, specific titles (not too vague)",
        "✓ Include genuine keywords naturally in description",
        "✓ Add detailed timestamps for multi-section videos",
        "✗ Avoid keywords like 'generated', 'automated', 'AI'",
        "✗ Avoid clickbait-style titles",
        "✗ Avoid generic descriptions",
    ],
}


def print_anti_detection_guide():
    """Print guidelines for creating authentic-looking videos."""
    print("=" * 60)
    print("HOW TO AVOID YOUTUBE'S 'OBVIOUSLY AI' DETECTION")
    print("=" * 60)
    
    for category, guidelines in ANTI_DETECTION_GUIDELINES.items():
        print(f"\n{category.upper().replace('_', ' ')}")
        print("-" * 40)
        for guideline in guidelines:
            print(guideline)

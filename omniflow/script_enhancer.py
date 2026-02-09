"""Script enhancement and optimization module.

Automatically improves user scripts for:
- Engagement and pacing
- SEO and keywords
- Narrative flow
- Hook strength
- Call-to-action effectiveness
"""
import os
from typing import Dict, List, Optional
import json


class ScriptEnhancer:
    """AI-powered script optimization using OpenAI."""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not set")

    def enhance_script(
        self,
        original_script: str,
        target_duration_seconds: int = 600,  # 10 minutes
        tone: str = "professional",
        style: str = "documentary",
        enhance_hook: bool = True,
        enhance_cta: bool = True,
        add_transitions: bool = True,
    ) -> Dict[str, str]:
        """Enhance script for better engagement and pacing.
        
        Args:
            original_script: User's raw script
            target_duration_seconds: Desired video length (assumes ~150 words/minute)
            tone: 'professional', 'casual', 'inspirational', 'educational'
            style: 'documentary', 'storytelling', 'analysis', 'entertaining'
            enhance_hook: Add a strong opening hook
            enhance_cta: Add call-to-action
            add_transitions: Add natural scene transitions
            
        Returns:
            Dict with enhanced script and metadata
        """
        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError("Install 'openai' package: pip install openai")
        
        client = OpenAI(api_key=self.api_key)
        
        target_words = int((target_duration_seconds / 60) * 150)
        
        enhancement_instructions = []
        if enhance_hook:
            enhancement_instructions.append(
                "- Start with a compelling hook (question, stat, or statement) that captures attention in first 10 seconds"
            )
        if enhance_cta:
            enhancement_instructions.append(
                "- End with clear call-to-action (subscribe, like, comment, visit link)"
            )
        if add_transitions:
            enhancement_instructions.append(
                "- Add natural scene/section transitions (e.g., 'Now let's explore...', 'Here's where it gets interesting...')"
            )
        
        prompt = f"""You are a professional YouTube video script writer and narrator coach.

ORIGINAL SCRIPT:
{original_script}

ENHANCEMENT REQUEST:
- Target length: ~{target_words} words (approximately {target_duration_seconds} seconds at natural speaking pace)
- Tone: {tone}
- Style: {style}
{chr(10).join(enhancement_instructions)}

INSTRUCTIONS:
1. Improve the script for maximum engagement and viewer retention
2. Enhance pacing and flow
3. Make it more conversational and natural
4. Add vivid descriptions for visual elements
5. Strengthen weak points and transitions
6. Maintain the core message and intent
7. Optimize for YouTube algorithm (specific keywords, natural language)
8. Add directional cues for visuals (e.g., [Show chart here], [Close-up on speaker])

OUTPUT FORMAT:
Return ONLY valid JSON (no markdown, no code blocks):
{{
    "enhanced_script": "The full enhanced script here...",
    "key_points": ["point 1", "point 2", "point 3"],
    "suggested_visuals": ["visual 1", "visual 2", "visual 3"],
    "estimated_duration_seconds": 600,
    "engagement_score": 0-100,
    "seo_keywords": ["keyword1", "keyword2", "keyword3"],
    "hook": "The opening hook used",
    "cta": "The call-to-action used",
    "improvements_made": ["improvement 1", "improvement 2", "improvement 3"]
}}
"""
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        
        try:
            result_text = response.choices[0].message.content
            # Try to parse as JSON
            result = json.loads(result_text)
        except json.JSONDecodeError:
            # Try to extract JSON from response
            import re
            match = re.search(r"\{[\s\S]*\}", result_text)
            if match:
                result = json.loads(match.group())
            else:
                raise ValueError(f"Could not parse script enhancement response: {result_text}")
        
        return result

    def optimize_for_shorts(self, script: str, max_seconds: int = 60) -> Dict:
        """Optimize script for YouTube Shorts (vertical, fast-paced)."""
        client = OpenAI(api_key=self.api_key)
        
        prompt = f"""Create a YouTube Shorts version of this script.
        
ORIGINAL SCRIPT:
{script}

REQUIREMENTS:
- Maximum {max_seconds} seconds (~{int(max_seconds * 150 / 60)} words)
- Fast-paced, punchy delivery
- Hook within first 2 seconds
- Vertical video format (9:16)
- Call-to-action at the end
- Use emojis/text overlays to maintain engagement

Return JSON with:
- shorts_script: The optimized script
- key_moments: Critical visual moments to highlight
- music_suggestions: Genre recommendations
- text_overlays: Text to display over video
"""
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
        )
        
        try:
            result = json.loads(response.choices[0].message.content)
        except:
            import re
            match = re.search(r"\{[\s\S]*\}", response.choices[0].message.content)
            result = json.loads(match.group()) if match else {}
        
        return result

    def generate_title_variations(self, script: str, num_variations: int = 5) -> List[str]:
        """Generate multiple YouTube title options."""
        client = OpenAI(api_key=self.api_key)
        
        prompt = f"""Generate {num_variations} compelling YouTube titles for this video script.

SCRIPT SUMMARY:
{script[:500]}...

REQUIREMENTS FOR EACH TITLE:
- Max 100 characters
- Include power words (Revealed, Explained, Secret, Ultimate, etc.)
- Include numbers when possible (#1, 5 Ways, etc.)
- Avoid clickbait (be authentic)
- Include target keyword naturally

Return a JSON array: ["Title 1", "Title 2", "Title 3", ...]
"""
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
        )
        
        try:
            titles = json.loads(response.choices[0].message.content)
            return titles if isinstance(titles, list) else [str(titles)]
        except:
            return ["Untitled Video"]

    def generate_description_from_script(self, script: str, title: str) -> str:
        """Auto-generate YouTube description from script."""
        client = OpenAI(api_key=self.api_key)
        
        prompt = f"""Create a compelling YouTube description for this video.

TITLE: {title}

SCRIPT:
{script[:1000]}...

REQUIREMENTS:
- First line: Hook/summary (most important - appears before "read more")
- Timestamps for major sections
- 3-5 key takeaways
- Relevant hashtags
- Call-to-action
- Links/resources mentioned
- Creator info

Keep under 5000 characters. Return as plain text (no JSON).
"""
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        
        return response.choices[0].message.content

    def analyze_script_quality(self, script: str) -> Dict:
        """Analyze script for engagement, pacing, clarity."""
        client = OpenAI(api_key=self.api_key)
        
        prompt = f"""Analyze this YouTube script and provide detailed feedback.

SCRIPT:
{script}

EVALUATE:
1. Hook strength (0-100)
2. Pacing and flow (0-100)
3. Information density (0-100)
4. Emotional engagement (0-100)
5. Call-to-action clarity (0-100)
6. SEO optimization (0-100)

Return JSON:
{{
    "overall_score": 0-100,
    "hook_strength": 0-100,
    "pacing": 0-100,
    "info_density": 0-100,
    "emotional_engagement": 0-100,
    "cta_clarity": 0-100,
    "seo_optimization": 0-100,
    "strengths": ["strength1", "strength2"],
    "weaknesses": ["weakness1", "weakness2"],
    "recommendations": ["recommendation1", "recommendation2"]
}}
"""
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
        )
        
        try:
            result = json.loads(response.choices[0].message.content)
        except:
            import re
            match = re.search(r"\{[\s\S]*\}", response.choices[0].message.content)
            result = json.loads(match.group()) if match else {}
        
        return result

"""Interactive dialogue engine for multi-character conversations.

Supports:
- Multi-turn conversations between 2+ characters
- Character personality and tone consistent responses
- Script generation for interactive videos
"""
import os
from typing import List, Dict, Optional
import json


class DialogueEngine:
    """Generate multi-character dialogues for interactive videos."""
    
    def __init__(self, llm_api_key: Optional[str] = None, llm_provider: str = "openai"):
        """
        Args:
            llm_api_key: API key for LLM (OpenAI, Anthropic, etc.).
            llm_provider: 'openai', 'anthropic', or 'huggingface'.
        """
        self.llm_api_key = llm_api_key or os.getenv(f"{llm_provider.upper()}_API_KEY")
        self.llm_provider = llm_provider
        
        if not self.llm_api_key:
            raise ValueError(f"{llm_provider.upper()}_API_KEY not set.")

    def create_dialogue(
        self,
        topic: str,
        characters: List[Dict[str, str]],
        num_turns: int = 5,
    ) -> List[Dict[str, str]]:
        """Generate a dialogue between characters.
        
        Args:
            topic: The conversation topic.
            characters: List of dicts with 'name' and 'personality' keys.
                Example: [
                    {'name': 'Alice', 'personality': 'curious, analytical'},
                    {'name': 'Bob', 'personality': 'skeptical, practical'},
                ]
            num_turns: Number of back-and-forth exchanges.
            
        Returns:
            List of dicts: [
                {'speaker': 'Alice', 'text': '...'},
                {'speaker': 'Bob', 'text': '...'},
                ...
            ]
        """
        if self.llm_provider == "openai":
            return self._create_dialogue_openai(topic, characters, num_turns)
        else:
            raise NotImplementedError(f"Provider {self.llm_provider} not yet supported.")

    def _create_dialogue_openai(self, topic: str, characters: List[Dict], num_turns: int):
        """Generate dialogue using OpenAI API."""
        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError("Install 'openai' package: pip install openai")
        
        client = OpenAI(api_key=self.llm_api_key)
        
        char_descriptions = "\n".join(
            [f"- {c['name']}: {c['personality']}" for c in characters]
        )
        
        prompt = f"""Generate a natural, engaging dialogue for an interactive video.

Topic: {topic}
Characters:
{char_descriptions}

Instructions:
- Create {num_turns} back-and-forth exchanges.
- Each character should speak in a way that matches their personality.
- Keep responses concise (1-3 sentences per turn).
- Make it conversational and natural.

Output format (JSON):
[
  {{"speaker": "Name", "text": "dialogue text"}},
  {{"speaker": "Name", "text": "dialogue text"}},
  ...
]
"""
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
        )
        
        try:
            # Extract JSON from response
            content = response.choices[0].message.content
            # Try parsing it directly
            dialogue = json.loads(content)
        except json.JSONDecodeError:
            # If response includes markdown code, extract it
            import re
            match = re.search(r"```(?:json)?\s*([\s\S]*?)```", content)
            if match:
                dialogue = json.loads(match.group(1))
            else:
                raise ValueError(f"Could not parse dialogue response: {content}")
        
        return dialogue


def generate_interactive_video_script(
    dialogue: List[Dict[str, str]],
    camera_directions: Optional[List[str]] = None,
) -> Dict[str, any]:
    """Convert dialogue to video production script with camera/visual cues.
    
    Example output:
    {
        "scenes": [
            {
                "turn": 1,
                "speaker": "Alice",
                "dialogue": "Let's talk about AI...",
                "visual": "Alice speaking, medium shot",
                "duration_seconds": 5,
            },
            ...
        ],
        "total_duration": 45,
    }
    """
    scenes = []
    for i, turn in enumerate(dialogue):
        visual = camera_directions[i % len(camera_directions)] if camera_directions else f"{turn['speaker']} speaking"
        scenes.append({
            "turn": i + 1,
            "speaker": turn["speaker"],
            "dialogue": turn["text"],
            "visual": visual,
            "duration_seconds": max(3, len(turn["text"].split()) // 3),  # ~3 words/sec
        })
    
    total_duration = sum(s["duration_seconds"] for s in scenes)
    
    return {
        "scenes": scenes,
        "total_duration": total_duration,
    }

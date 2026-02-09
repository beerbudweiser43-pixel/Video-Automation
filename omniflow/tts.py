"""ElevenLabs TTS integration for voice generation."""
import os
import requests
from typing import Optional
from pathlib import Path


class ElevenLabsTTS:
    """Simple wrapper for ElevenLabs text-to-speech API."""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("ELEVENLABS_API_KEY")
        if not self.api_key:
            raise ValueError("ELEVENLABS_API_KEY not set. Get a free tier key from https://elevenlabs.io/")
        self.api_url = "https://api.elevenlabs.io/v1"

    def get_voices(self):
        """Fetch available voices."""
        url = f"{self.api_url}/voices"
        resp = requests.get(url, headers={"xi-api-key": self.api_key})
        resp.raise_for_status()
        return resp.json()

    def synthesize(
        self,
        text: str,
        voice_id: str = "21m00Tcm4TlvDq8ikWAM",  # Default: Rachel (pleasant, clear)
        stability: float = 0.5,
        similarity: float = 0.75,
        output_path: Optional[str] = None,
    ) -> bytes:
        """Generate audio from text.
        
        Args:
            text: The text to synthesize.
            voice_id: ElevenLabs voice ID (default: Rachel).
            stability: Voice stability (0.0–1.0).
            similarity: Speaker similarity (0.0–1.0).
            output_path: Optional file path to save audio.
            
        Returns:
            Audio bytes (MP3 format).
        """
        url = f"{self.api_url}/text-to-speech/{voice_id}"
        headers = {"xi-api-key": self.api_key}
        payload = {
            "text": text,
            "voice_settings": {
                "stability": stability,
                "similarity_boost": similarity,
            },
        }
        
        resp = requests.post(url, json=payload, headers=headers)
        resp.raise_for_status()
        
        if output_path:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(resp.content)
        
        return resp.content


def synthesize_script(script: str, output_dir: str = "outputs/audio", voice_id: str = None) -> str:
    """Helper: synthesize an entire script and save to file."""
    tts = ElevenLabsTTS()
    output_path = f"{output_dir}/narration.mp3"
    tts.synthesize(script, voice_id=voice_id or "21m00Tcm4TlvDq8ikWAM", output_path=output_path)
    return output_path

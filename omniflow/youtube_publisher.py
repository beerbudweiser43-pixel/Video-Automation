"""YouTube publishing module - automatic upload with metadata.

Handles:
- Uploading videos to YouTube via API or webhook
- Setting title, description, tags, category
- Scheduling publication
- Setting privacy settings
"""
import os
import json
import requests
from typing import Optional, List, Dict


class YouTubePublisher:
    """Publish videos to YouTube with metadata."""
    
    def __init__(self, api_key: Optional[str] = None, webhook_url: Optional[str] = None):
        """
        Args:
            api_key: YouTube API key (for direct API uploads). Optional if using webhook.
            webhook_url: n8n/Make webhook URL to trigger YouTube upload automation.
        """
        self.api_key = api_key or os.getenv("YOUTUBE_API_KEY")
        self.webhook_url = webhook_url or os.getenv("YOUTUBE_WEBHOOK_URL")
        
        if not self.webhook_url and not self.api_key:
            raise ValueError(
                "Either YOUTUBE_WEBHOOK_URL or YOUTUBE_API_KEY must be set. "
                "For easiest setup, use n8n/Make webhook."
            )

    def publish_via_webhook(
        self,
        video_path: str,
        title: str,
        description: str,
        tags: List[str] = None,
        category_id: str = "28",  # Science & Technology
        privacy_status: str = "public",
        thumbnail_path: Optional[str] = None,
        schedule_publish_at: Optional[str] = None,
    ) -> Dict:
        """Publish video via n8n/Make webhook (recommended for automation).
        
        Args:
            video_path: Path to video file to upload.
            title: YouTube video title (max 100 chars).
            description: Video description (max 5000 chars).
            tags: List of tags/keywords.
            category_id: YouTube category ID (28 = Science & Tech, 23 = Comedy, etc.).
            privacy_status: 'public', 'private', 'unlisted'.
            thumbnail_path: Optional custom thumbnail image.
            schedule_publish_at: ISO 8601 timestamp to schedule publishing.
            
        Returns:
            Response from webhook (should include videoId, URL, etc.).
        """
        if not self.webhook_url:
            raise ValueError("Webhook URL not set. Configure YOUTUBE_WEBHOOK_URL env var.")
        
        # Validate inputs
        if len(title) > 100:
            raise ValueError(f"Title too long ({len(title)}/100 chars)")
        if len(description) > 5000:
            raise ValueError(f"Description too long ({len(description)}/5000 chars)")
        
        payload = {
            "videoPath": video_path,
            "title": title,
            "description": description,
            "tags": tags or ["AI", "Technology", "Video"],
            "categoryId": category_id,
            "privacyStatus": privacy_status,
            "thumbnailPath": thumbnail_path,
            "schedulePublishAt": schedule_publish_at,
            "timestamp": __import__("datetime").datetime.utcnow().isoformat(),
        }
        
        try:
            response = requests.post(self.webhook_url, json=payload, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Webhook request failed: {e}")

    def publish_via_api(
        self,
        video_path: str,
        title: str,
        description: str,
        tags: List[str] = None,
        category_id: str = "28",
        privacy_status: str = "public",
    ) -> Dict:
        """Publish video via YouTube API (requires OAuth setup).
        
        Note: This is a placeholder. Full implementation requires:
        1. Google OAuth setup
        2. google-auth-oauthlib library
        3. User authentication flow
        
        For simplicity, use webhook-based approach instead.
        """
        if not self.api_key:
            raise ValueError("YouTube API key not configured.")
        
        raise NotImplementedError(
            "Direct API upload requires complex OAuth setup. "
            "Recommended: Use n8n/Make webhook instead (see docs). "
            "Configure YOUTUBE_WEBHOOK_URL in .env and call publish_via_webhook()."
        )

    def prepare_metadata(
        self,
        title: str,
        description: str,
        tags: List[str] = None,
        channel_branding: Dict = None,
    ) -> Dict:
        """Prepare and validate metadata for publishing.
        
        Returns:
            Clean metadata dict ready for YouTube API/webhook.
        """
        # Auto-add channel branding if provided
        if channel_branding:
            title = f"{title} | {channel_branding.get('channel_name', '')}"
            description = f"{description}\n\n{channel_branding.get('channel_outro', '')}"
        
        # Sanitize
        title = title.strip()[:100]
        description = description.strip()[:5000]
        
        return {
            "title": title,
            "description": description,
            "tags": tags or [],
            "categoryId": "28",
        }

    def get_upload_status(self, upload_id: str) -> Dict:
        """Check status of a pending upload (requires webhook to return upload_id)."""
        # This would typically query n8n/Make status endpoint
        # Placeholder for webhook status checking
        return {
            "upload_id": upload_id,
            "status": "pending",  # pending, processing, published, failed
            "message": "Check n8n/Make dashboard for detailed status",
        }


class YouTubeOptimizer:
    """Optimize videos and metadata for YouTube algorithm (avoid obviously AI)."""
    
    @staticmethod
    def generate_description(
        base_description: str,
        keywords: List[str] = None,
        include_timestamps: bool = True,
        include_cta: bool = True,
    ) -> str:
        """Enhance description for YouTube algorithm visibility.
        
        Args:
            base_description: Your main description.
            keywords: Target keywords to include naturally.
            include_timestamps: Add [0:00] START timestamps if applicable.
            include_cta: Add call-to-action (subscribe, like, comment).
            
        Returns:
            Enhanced description (max 5000 chars).
        """
        enhanced = base_description
        
        if include_cta:
            enhanced += "\n\n---\n🔔 Subscribe for more!\n👍 Like if you found this helpful\n💬 Share your thoughts in the comments"
        
        if keywords:
            enhanced += "\n\n" + " • ".join(keywords[:10])
        
        return enhanced[:5000]

    @staticmethod
    def suggest_tags(
        title: str,
        description: str,
        channel_niche: str = "technology",
    ) -> List[str]:
        """Suggest tags to match reference channels (documentaries, real-human style).
        
        Avoids obvious AI-generated patterns.
        """
        base_tags = {
            "documentary": ["documentary", "storytelling", "real", "authentic", "narrative"],
            "technology": ["AI", "tech", "innovation", "future", "explained"],
            "education": ["education", "learning", "tutorial", "how to", "guide"],
            "news": ["news", "analysis", "current events", "update", "commentary"],
        }
        
        tags = base_tags.get(channel_niche, base_tags["technology"])
        
        # Extract keywords from title/description
        import re
        words = re.findall(r"\b\w{4,}\b", (title + " " + description).lower())
        tags.extend(list(set(words))[:5])
        
        return list(set(tags))[:30]  # YouTube max 500 chars of tags

"""
YouTube Authentication & Video Analysis

Handle YouTube login and fetch video details for quality reference.
"""

import os
import json
from typing import Dict, Optional, List

try:
    from google.auth.transport.requests import Request
    from google.oauth2.service_account import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    import googleapiclient.discovery
except ImportError:
    pass


class YouTubeAuthenticator:
    """Handle YouTube authentication and token management."""
    
    SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
    TOKEN_FILE = os.path.expanduser('~/.omniflow_yt_token.json')
    CREDENTIALS_FILE = os.path.expanduser('~/.omniflow_yt_credentials.json')
    
    @staticmethod
    def authenticate_user(force_new: bool = False) -> Optional[object]:
        """Authenticate with YouTube using OAuth 2.0.
        
        Args:
            force_new: If True, force new authentication
            
        Returns:
            YouTube service object
        """
        try:
            from google_auth_oauthlib.flow import InstalledAppFlow
            import google.auth.transport.requests
            from google.oauth2.credentials import Credentials
        except ImportError:
            print("Install: pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client")
            return None
        
        credentials = None
        
        # Try to load existing token
        if os.path.exists(YouTubeAuthenticator.TOKEN_FILE) and not force_new:
            try:
                from google.oauth2.credentials import Credentials
                credentials = Credentials.from_authorized_user_file(
                    YouTubeAuthenticator.TOKEN_FILE,
                    YouTubeAuthenticator.SCOPES
                )
                print("✅ Loaded existing YouTube credentials")
                return YouTubeAuthenticator._build_service(credentials)
            except Exception as e:
                print(f"Token expired or invalid: {e}")
        
        # Need new authentication
        if not os.path.exists(YouTubeAuthenticator.CREDENTIALS_FILE):
            print("\n" + "="*60)
            print("YouTube Authentication Required")
            print("="*60)
            print("\nTo access your YouTube data:")
            print("1. Visit: https://console.cloud.google.com/")
            print("2. Create a new project")
            print("3. Enable YouTube Data API v3")
            print("4. Create OAuth 2.0 Desktop App credentials")
            print("5. Download credentials as JSON")
            print(f"6. Save to: {YouTubeAuthenticator.CREDENTIALS_FILE}")
            print("\n" + "="*60)
            return None
        
        try:
            flow = InstalledAppFlow.from_client_secrets_file(
                YouTubeAuthenticator.CREDENTIALS_FILE,
                YouTubeAuthenticator.SCOPES
            )
            credentials = flow.run_local_server(port=0)
            
            # Save token for future use
            with open(YouTubeAuthenticator.TOKEN_FILE, 'w') as f:
                f.write(credentials.to_json())
            
            print("✅ YouTube authentication successful!")
            return YouTubeAuthenticator._build_service(credentials)
        except Exception as e:
            print(f"❌ Authentication failed: {e}")
            return None
    
    @staticmethod
    def _build_service(credentials):
        """Build YouTube service."""
        try:
            import googleapiclient.discovery
            return googleapiclient.discovery.build(
                'youtube', 'v3',
                credentials=credentials
            )
        except Exception as e:
            print(f"Error building YouTube service: {e}")
            return None


class YouTubeVideoAnalyzer:
    """Analyze YouTube videos for production insights."""
    
    def __init__(self, youtube_service=None):
        """Initialize with YouTube service."""
        self.youtube = youtube_service or YouTubeAuthenticator.authenticate_user()
    
    def get_video_details(self, video_id: str) -> Dict:
        """Fetch detailed video information."""
        if not self.youtube:
            return {}
        
        try:
            request = self.youtube.videos().list(
                part="snippet,statistics,contentDetails,fileDetails",
                id=video_id
            )
            response = request.execute()
            
            if response['items']:
                video = response['items'][0]
                return {
                    "title": video['snippet'].get('title', ''),
                    "description": video['snippet'].get('description', ''),
                    "channel": video['snippet'].get('channelTitle', ''),
                    "duration": video['contentDetails'].get('duration', ''),
                    "view_count": video['statistics'].get('viewCount', 0),
                    "like_count": video['statistics'].get('likeCount', 0),
                    "comment_count": video['statistics'].get('commentCount', 0),
                    "published_at": video['snippet'].get('publishedAt', ''),
                    "thumbnail_url": video['snippet']['thumbnails'].get('high', {}).get('url', ''),
                    "tags": video['snippet'].get('tags', []),
                    "category_id": video['snippet'].get('categoryId', ''),
                }
            return {}
        except Exception as e:
            print(f"Error fetching video: {e}")
            return {}
    
    def analyze_video_quality(self, video_id: str) -> Dict:
        """Analyze video for production quality insights."""
        if not self.youtube:
            return {}
        
        details = self.get_video_details(video_id)
        
        if not details:
            return {}
        
        # Calculate engagement rate
        total_views = int(details.get('view_count', 0)) or 1
        likes = int(details.get('like_count', 0))
        comments = int(details.get('comment_count', 0))
        
        engagement_rate = ((likes + comments) / total_views * 100) if total_views > 0 else 0
        
        return {
            "video_info": details,
            "engagement_metrics": {
                "views": total_views,
                "likes": likes,
                "comments": comments,
                "engagement_rate": f"{engagement_rate:.2f}%",
                "like_ratio": f"{(likes/total_views*100):.2f}%" if total_views > 0 else "N/A",
            },
            "quality_indicators": {
                "high_engagement": engagement_rate > 5,
                "high_likes": likes > 1000,
                "active_community": comments > 100,
                "viral_potential": "high" if engagement_rate > 10 else "medium" if engagement_rate > 5 else "low",
            },
            "production_insights": {
                "duration_minutes": YouTubeVideoAnalyzer._parse_duration(details.get('duration', 'PT0M')),
                "tag_count": len(details.get('tags', [])),
                "description_length": len(details.get('description', '')),
                "has_links": "http" in details.get('description', '') or "youtube.com" in details.get('description', ''),
            }
        }
    
    def compare_videos(self, video_ids: List[str]) -> Dict:
        """Compare multiple videos for best practices."""
        analyses = []
        
        for vid_id in video_ids:
            analyses.append(self.analyze_video_quality(vid_id))
        
        if not analyses:
            return {}
        
        # Find common patterns
        avg_engagement = sum(
            float(a['engagement_metrics']['engagement_rate'].rstrip('%')) 
            for a in analyses if 'engagement_rate' in a.get('engagement_metrics', {})
        ) / len(analyses) if analyses else 0
        
        avg_duration = sum(
            a['production_insights']['duration_minutes'] 
            for a in analyses if 'duration_minutes' in a.get('production_insights', {})
        ) / len(analyses) if analyses else 0
        
        all_tags = []
        for a in analyses:
            all_tags.extend(a['video_info'].get('tags', []))
        
        most_common_tags = sorted(
            set((tag, all_tags.count(tag)) for tag in all_tags),
            key=lambda x: x[1],
            reverse=True
        )[:10]
        
        return {
            "analysis_count": len(analyses),
            "average_engagement_rate": f"{avg_engagement:.2f}%",
            "average_duration_minutes": round(avg_duration, 1),
            "common_tags": [tag[0] for tag in most_common_tags],
            "best_practices": YouTubeVideoAnalyzer._extract_best_practices(analyses),
        }
    
    @staticmethod
    def _parse_duration(iso_duration: str) -> float:
        """Parse ISO 8601 duration to minutes."""
        import re
        pattern = r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?'
        match = re.match(pattern, iso_duration)
        
        if match:
            hours = int(match.group(1) or 0)
            minutes = int(match.group(2) or 0)
            seconds = int(match.group(3) or 0)
            return hours * 60 + minutes + seconds / 60
        
        return 0
    
    @staticmethod
    def _extract_best_practices(analyses: List[Dict]) -> List[str]:
        """Extract best practices from successful videos."""
        practices = []
        
        high_engagement_videos = [
            a for a in analyses 
            if float(a['engagement_metrics'].get('engagement_rate', '0').rstrip('%')) > 5
        ]
        
        if high_engagement_videos:
            avg_desc_len = sum(
                a['production_insights']['description_length']
                for a in high_engagement_videos
            ) / len(high_engagement_videos)
            
            if avg_desc_len > 500:
                practices.append("Use detailed descriptions (500+ characters)")
            
            if all(a['production_insights']['has_links'] for a in high_engagement_videos):
                practices.append("Include links in description (CTA)")
            
            avg_tags = sum(
                a['production_insights']['tag_count']
                for a in high_engagement_videos
            ) / len(high_engagement_videos)
            
            if avg_tags > 5:
                practices.append(f"Use {int(avg_tags)}+ relevant tags")
        
        if high_engagement_videos:
            durations = [
                a['production_insights']['duration_minutes']
                for a in high_engagement_videos
            ]
            avg_duration = sum(durations) / len(durations)
            practices.append(f"Optimal duration: {int(avg_duration)} minutes")
        
        return practices


class YouTubeVideoReference:
    """Fetch and analyze reference videos for production quality."""
    
    def __init__(self, youtube_service=None):
        self.analyzer = YouTubeVideoAnalyzer(youtube_service)
    
    def get_video_from_url(self, url: str) -> Optional[str]:
        """Extract video ID from YouTube URL."""
        import re
        
        patterns = [
            r'youtube\.com/watch\?v=([a-zA-Z0-9_-]{11})',
            r'youtu\.be/([a-zA-Z0-9_-]{11})',
            r'(?:youtube\.com/shorts/|youtube\.com/watch\?v=)([a-zA-Z0-9_-]{11})',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        
        return None
    
    def analyze_reference_video(self, url: str) -> Dict:
        """Analyze a reference video for production insights."""
        video_id = self.get_video_from_url(url)
        
        if not video_id:
            return {"error": "Invalid YouTube URL"}
        
        analysis = self.analyzer.analyze_video_quality(video_id)
        
        if not analysis:
            return {"error": "Could not fetch video (may need authentication)"}
        
        return {
            "reference_video": analysis['video_info'],
            "quality_score": "high" if analysis['quality_indicators']['high_engagement'] else "medium",
            "insights": {
                "optimal_duration": analysis['production_insights']['duration_minutes'],
                "engagement_rate": analysis['engagement_metrics']['engagement_rate'],
                "recommended_tags": analysis['video_info']['tags'][:10],
                "channel": analysis['video_info']['channel'],
            },
            "recommendations": [
                f"Match duration: ~{int(analysis['production_insights']['duration_minutes'])} min",
                f"Aim for {float(analysis['engagement_metrics']['engagement_rate'].rstrip('%')):.1f}%+ engagement",
                f"Use relevant tags like: {', '.join(analysis['video_info']['tags'][:5])}",
            ]
        }


# Export
__all__ = [
    "YouTubeAuthenticator",
    "YouTubeVideoAnalyzer",
    "YouTubeVideoReference",
]

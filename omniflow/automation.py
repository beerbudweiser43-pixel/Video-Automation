"""n8n and Make automation templates for video publishing and scheduling.

These templates can be imported into n8n or Make to automate:
- Video upload to YouTube
- Scheduling posts
- Cross-platform distribution (TikTok, Instagram, etc.)
- Analytics collection
"""
import json


def create_n8n_youtube_automation() -> Dict:
    """Return n8n workflow template for YouTube video upload and scheduling."""
    return {
        "name": "OmniFlow: Upload to YouTube",
        "nodes": [
            {
                "parameters": {
                    "resource": "video",
                    "operation": "upload",
                    "title": "{{ $json.videoTitle }}",
                    "description": "{{ $json.videoDescription }}",
                    "tags": "{{ $json.tags || 'AI, YouTube, Automation' }}",
                    "categoryId": "28",  # Science & Technology
                    "privacyStatus": "public",
                    "videoFile": "={{ $binary.videoFile }}",
                    "autoGenerate": True,
                },
                "name": "YouTube Upload",
                "type": "n8n-nodes-base.youtube",
                "typeVersion": 1,
                "position": [250, 300],
            },
            {
                "parameters": {
                    "operation": "upload",
                    "resource": "video",
                    "title": "{{ $json.videoTitle }}",
                    "description": "{{ $json.videoDescription }}",
                },
                "name": "Schedule Post",
                "type": "n8n-nodes-base.spreadsheetTrigger",
                "typeVersion": 1,
                "position": [500, 300],
            },
        ],
        "connections": {
            "YouTube Upload": {
                "main": [[{"node": "Schedule Post", "type": "main", "index": 0}]]
            }
        },
    }


def create_n8n_multi_platform_automation() -> Dict:
    """Return n8n workflow for cross-platform publishing."""
    return {
        "name": "OmniFlow: Multi-Platform Publishing",
        "nodes": [
            {
                "parameters": {
                    "display": "{{ $json.videoTitle }}",
                },
                "name": "Input",
                "type": "n8n-nodes-base.manualTrigger",
                "typeVersion": 1,
                "position": [100, 100],
            },
            {
                "parameters": {"platform": "youtube"},
                "name": "Upload to YouTube",
                "type": "n8n-nodes-base.youtube",
                "typeVersion": 1,
                "position": [250, 100],
            },
            {
                "parameters": {"platform": "tiktok"},
                "name": "Upload to TikTok",
                "type": "n8n-nodes-base.http",  # Custom TikTok API call
                "typeVersion": 1,
                "position": [250, 200],
            },
            {
                "parameters": {"platform": "instagram"},
                "name": "Upload to Instagram Reels",
                "type": "n8n-nodes-base.instagram",
                "typeVersion": 1,
                "position": [250, 300],
            },
            {
                "parameters": {
                    "message": "Video published! Check it out: {{ $json.youtubeUrl }}",
                },
                "name": "Notify",
                "type": "n8n-nodes-base.slack",
                "typeVersion": 1,
                "position": [400, 200],
            },
        ],
        "connections": {
            "Input": {
                "main": [
                    [
                        {"node": "Upload to YouTube", "type": "main", "index": 0},
                        {"node": "Upload to TikTok", "type": "main", "index": 0},
                        {"node": "Upload to Instagram Reels", "type": "main", "index": 0},
                    ]
                ]
            },
            "Upload to YouTube": {
                "main": [[{"node": "Notify", "type": "main", "index": 0}]]
            },
        },
    }


def create_make_automation() -> Dict:
    """Return Make.com workflow template for YouTube publishing."""
    return {
        "name": "OmniFlow: YouTube Auto-Publish via Make",
        "description": "Automatically upload and publish videos to YouTube with custom metadata.",
        "modules": [
            {
                "id": 1,
                "module": "builtin:BasicTrigger",
                "parameters": {
                    "label": "Trigger on video ready",
                },
            },
            {
                "id": 2,
                "module": "youtube:UploadVideo",
                "parameters": {
                    "title": "{{ 1.videoTitle }}",
                    "description": "{{ 1.videoDescription }}",
                    "videoFile": "{{ 1.videoFile }}",
                    "categoryId": "28",
                    "privacyStatus": "public",
                    "tags": "{{ 1.tags }}",
                },
            },
            {
                "id": 3,
                "module": "google-sheets:AppendRow",
                "parameters": {
                    "spreadsheetId": "{{ env.SHEET_ID }}",
                    "range": "Analytics!A:Z",
                    "values": [
                        "{{ 2.videoId }}",
                        "{{ 2.publishedAt }}",
                        "{{ 1.videoTitle }}",
                        "{{ env.CHANNEL_NAME }}",
                    ],
                },
            },
        ],
        "connections": [[1, 2], [2, 3]],
    }


def get_webhook_url_for_completion() -> str:
    """Return webhook URL pattern for triggering automation on video completion.
    
    Use this webhook URL in your Streamlit app to POST when video generation completes:
    - Content: { videoPath, videoTitle, videoDescription, tags }
    """
    return """
    # POST to your n8n/Make webhook with this payload:
    {
        "videoPath": "/path/to/video.mp4",
        "videoTitle": "My AI Video",
        "videoDescription": "Generated with OmniFlow",
        "tags": ["AI", "Video", "Automation"],
        "platform": ["youtube", "tiktok", "instagram"]
    }
    """


# Utility to save templates
def save_templates(output_dir: str = "automations/"):
    """Save n8n and Make templates to JSON files for import."""
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    with open(f"{output_dir}/n8n_youtube_automation.json", "w") as f:
        json.dump(create_n8n_youtube_automation(), f, indent=2)
    
    with open(f"{output_dir}/n8n_multi_platform.json", "w") as f:
        json.dump(create_n8n_multi_platform_automation(), f, indent=2)
    
    with open(f"{output_dir}/make_youtube_automation.json", "w") as f:
        json.dump(create_make_automation(), f, indent=2)
    
    print(f"Templates saved to {output_dir}/")

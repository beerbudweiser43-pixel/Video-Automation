"""End-to-end orchestration for professional video production.

Orchestrates:
1. Visuals generation (ComfyUI)
2. Voice synthesis (ElevenLabs)
3. Video composition (FFmpeg)
4. YouTube publishing (n8n/Make)
"""
import os
import json
from pathlib import Path
from typing import Dict, Optional, List
from datetime import datetime


class VideoProductionOrchestrator:
    """High-level orchestration for complete video production pipeline."""
    
    def __init__(
        self,
        project_name: str,
        output_dir: str = "projects/",
        comfyui_url: str = "http://localhost:8188",
    ):
        """
        Args:
            project_name: Name of the project (e.g., "daily_video_2026-02-07").
            output_dir: Base directory for all project outputs.
            comfyui_url: ComfyUI API endpoint.
        """
        self.project_name = project_name
        self.output_dir = Path(output_dir) / project_name
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.comfyui_url = comfyui_url
        
        self.log_file = self.output_dir / "production.log"
        self.metadata_file = self.output_dir / "metadata.json"
        
        self.metadata = {
            "project_name": project_name,
            "created_at": datetime.now().isoformat(),
            "stages": {},
        }

    def _log(self, stage: str, message: str, status: str = "INFO"):
        """Log production events."""
        log_entry = f"[{datetime.now().isoformat()}] [{stage}] {status}: {message}"
        print(log_entry)
        with open(self.log_file, "a") as f:
            f.write(log_entry + "\n")

    def _stage_script_enhancement(self, script: str, channel_template: str) -> str:
        """Enhance script using AI for maximum engagement."""
        try:
            from . import script_enhancer
            
            enhancer = script_enhancer.ScriptEnhancer()
            result = enhancer.enhance_script(
                script=script,
                target_duration_seconds=600,
                tone="professional",
                style="documentary",
                enhance_hook=True,
                enhance_cta=True,
            )
            
            enhanced = result.get("enhanced_script", script)
            self.metadata["stages"]["enhancement"] = {
                "status": "success",
                "improvements": result.get("improvements_made", []),
                "engagement_score": result.get("engagement_score", 0),
            }
            
            self._log("ENHANCE", f"Script enhanced - engagement score: {result.get('engagement_score', 0)}")
            return enhanced
        except Exception as e:
            self._log("ENHANCE", f"Enhancement failed: {e}", status="WARN")
            return script  # Return original if enhancement fails

    def produce_video(
        self,
        script: str,
        title: str,
        description: str,
        channel_template: str = "Deep Dive Analysis",
        visual_style: str = "Real Human Character (Consistent)",
        tags: List[str] = None,
        voice_id: str = "21m00Tcm4TlvDq8ikWAM",  # Rachel default
        schedule_publish_at: Optional[str] = None,
        publish_to_youtube: bool = True,
        enhance_script: bool = True,
    ) -> Dict:
        """Complete video production from script to YouTube publication.
        
        Args:
            script: Full video narration/script.
            title: Video title (max 100 chars).
            description: Video description (max 5000 chars).
            channel_template: Which channel template to use.
            visual_style: Which visual style to apply.
            tags: Custom YouTube tags.
            voice_id: ElevenLabs voice ID.
            schedule_publish_at: ISO 8601 timestamp to schedule publishing.
            publish_to_youtube: Whether to publish automatically.
            enhance_script: Whether to enhance script with AI optimization.
            
        Returns:
            Dict with paths and status of all generated files.
        """
        try:
            self._log("ORCHESTRATOR", f"Starting production for '{title}'")
            
            # Stage 0: Script Enhancement (Optional)
            enhanced_script = script
            if enhance_script:
                self._log("STAGE_0", "Enhancing script...")
                enhanced_script = self._stage_script_enhancement(script, channel_template)
            
            # Stage 1: Visual Generation
            self._log("STAGE_1", "Generating visuals...")
            visuals_result = self._stage_visuals(enhanced_script, channel_template, visual_style)
            
            # Stage 2: Voice Synthesis
            self._log("STAGE_2", "Synthesizing voice...")
            audio_result = self._stage_voice(enhanced_script, voice_id)
            
            # Stage 3: Video Composition
            self._log("STAGE_3", "Composing video...")
            video_result = self._stage_composition(
                visuals_result["frames"],
                audio_result["audio_path"],
                title=title,
            )
            
            # Stage 4: YouTube Publishing
            publish_result = {}
            if publish_to_youtube:
                self._log("STAGE_4", "Publishing to YouTube...")
                publish_result = self._stage_youtube_publish(
                    video_result["video_path"],
                    title=title,
                    description=description,
                    tags=tags,
                    schedule_publish_at=schedule_publish_at,
                )
            
            # Compile final result
            final_result = {
                "status": "success",
                "project_name": self.project_name,
                "visuals": visuals_result,
                "audio": audio_result,
                "video": video_result,
                "youtube": publish_result,
                "logs": str(self.log_file),
            }
            
            self._save_metadata(final_result)
            self._log("ORCHESTRATOR", f"✅ Production complete! Video: {video_result['video_path']}")
            
            return final_result
        
        except Exception as e:
            self._log("ORCHESTRATOR", f"❌ Production failed: {e}", status="ERROR")
            raise

    def _stage_visuals(self, script: str, template: str, style: str) -> Dict:
        """Generate visuals using ComfyUI."""
        from . import generator
        
        try:
            outputs = generator.generate_visuals(
                channel=template,
                style=style,
                prompt=script[:500],  # First 500 chars as visual prompt
                use_comfyui=True,
                comfy_url=self.comfyui_url,
            )
            
            # Save frames
            frames_dir = self.output_dir / "visuals"
            frames_dir.mkdir(exist_ok=True)
            frame_paths = []
            for i, img in enumerate(outputs):
                frame_path = frames_dir / f"frame_{i:04d}.png"
                img.save(frame_path)
                frame_paths.append(str(frame_path))
            
            self.metadata["stages"]["visuals"] = {
                "status": "success",
                "frame_count": len(frame_paths),
                "frames_dir": str(frames_dir),
            }
            
            return {
                "frames": frame_paths,
                "frames_dir": str(frames_dir),
                "count": len(frame_paths),
            }
        except Exception as e:
            self._log("VISUALS", f"Generation failed: {e}", status="WARN")
            # Return dummy frames on failure
            return {"frames": [], "frames_dir": "", "count": 0}

    def _stage_voice(self, script: str, voice_id: str) -> Dict:
        """Synthesize voice using ElevenLabs."""
        from . import tts
        
        try:
            audio_path = tts.synthesize_script(
                script=script,
                output_dir=str(self.output_dir / "audio"),
                voice_id=voice_id,
            )
            
            self.metadata["stages"]["voice"] = {
                "status": "success",
                "audio_path": audio_path,
                "voice_id": voice_id,
            }
            
            return {"audio_path": audio_path}
        except Exception as e:
            self._log("VOICE", f"Synthesis failed: {e}", status="ERROR")
            raise

    def _stage_composition(self, frames: List[str], audio_path: str, title: str = "") -> Dict:
        """Compose video from frames + audio."""
        from . import video_composer
        
        try:
            if not frames:
                raise ValueError("No frames generated")
            
            composer = video_composer.VideoComposer()
            
            # Create main video
            video_path = str(self.output_dir / "final_video.mp4")
            composer.create_simple_video(
                image_sequence=frames,
                audio_path=audio_path,
                output_path=video_path,
                fps=24,
                title=title,
            )
            
            # Add title overlay if provided
            if title:
                titled_path = str(self.output_dir / "final_video_titled.mp4")
                composer.add_overlay_text(
                    video_path=video_path,
                    text=title,
                    output_path=titled_path,
                    position="top_center",
                    duration=3.0,
                )
                video_path = titled_path
            
            # Export for YouTube
            youtube_path = str(self.output_dir / "final_video_youtube.mp4")
            composer.export_for_youtube(video_path, youtube_path)
            
            self.metadata["stages"]["composition"] = {
                "status": "success",
                "video_path": youtube_path,
            }
            
            return {"video_path": youtube_path}
        except Exception as e:
            self._log("COMPOSITION", f"Composition failed: {e}", status="ERROR")
            raise

    def _stage_youtube_publish(
        self,
        video_path: str,
        title: str,
        description: str,
        tags: List[str] = None,
        schedule_publish_at: Optional[str] = None,
    ) -> Dict:
        """Publish to YouTube via webhook."""
        from . import youtube_publisher
        
        try:
            publisher = youtube_publisher.YouTubePublisher()
            
            # Enhance metadata
            optimizer = youtube_publisher.YouTubeOptimizer()
            enhanced_description = optimizer.generate_description(
                description,
                keywords=tags,
            )
            
            suggested_tags = optimizer.suggest_tags(
                title,
                description,
                channel_niche="technology",
            )
            
            # Publish
            result = publisher.publish_via_webhook(
                video_path=video_path,
                title=title,
                description=enhanced_description,
                tags=tags or suggested_tags,
                schedule_publish_at=schedule_publish_at,
            )
            
            self.metadata["stages"]["youtube"] = {
                "status": "success",
                "webhook_response": result,
            }
            
            return result
        except Exception as e:
            self._log("YOUTUBE", f"Publishing failed: {e}", status="WARN")
            return {"status": "failed", "error": str(e)}

    def _save_metadata(self, result: Dict):
        """Save production metadata to JSON."""
        self.metadata["completed_at"] = datetime.now().isoformat()
        self.metadata["result"] = result
        
        with open(self.metadata_file, "w") as f:
            json.dump(self.metadata, f, indent=2)

    def get_production_status(self) -> Dict:
        """Get current production status and metadata."""
        if self.metadata_file.exists():
            with open(self.metadata_file) as f:
                return json.load(f)
        return self.metadata

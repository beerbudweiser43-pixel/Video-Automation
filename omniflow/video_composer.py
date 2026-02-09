"""Professional video composition using FFmpeg.

Handles:
- Syncing visuals with narration
- Adding titles, overlays, transitions
- Watermarks and branding
- Exporting for YouTube (optimal codec/bitrate)
"""
import subprocess
import os
from pathlib import Path
from typing import List, Optional, Dict
import json


class VideoComposer:
    """Compose professional videos from images, audio, and metadata."""
    
    def __init__(self, ffmpeg_path: str = "ffmpeg"):
        """
        Args:
            ffmpeg_path: Path to ffmpeg executable (assumes in PATH by default).
        """
        self.ffmpeg_path = ffmpeg_path
        self._check_ffmpeg()

    def _check_ffmpeg(self):
        """Verify ffmpeg is available."""
        try:
            subprocess.run([self.ffmpeg_path, "-version"], capture_output=True, check=True)
        except (FileNotFoundError, subprocess.CalledProcessError):
            raise RuntimeError(
                f"FFmpeg not found at '{self.ffmpeg_path}'. "
                "Install from https://ffmpeg.org/download.html and ensure it's in PATH."
            )

    def create_simple_video(
        self,
        image_sequence: List[str],
        audio_path: str,
        output_path: str,
        fps: int = 24,
        title: Optional[str] = None,
    ) -> str:
        """Create a simple video from image sequence + audio.
        
        Args:
            image_sequence: List of image file paths (in order).
            audio_path: Path to audio file (MP3/AAC).
            output_path: Where to save the output video.
            fps: Frames per second.
            title: Optional title to overlay on first frame.
            
        Returns:
            Path to generated video.
        """
        # Create a temporary image concatenation file
        concat_file = "/tmp/image_list.txt"
        self._create_image_list(image_sequence, concat_file)
        
        # FFmpeg command to create video from images + audio
        cmd = [
            self.ffmpeg_path,
            "-framerate", str(fps),
            "-i", image_sequence[0].replace("%d", "%0" + str(len(str(len(image_sequence)))) + "d"),
            "-i", audio_path,
            "-c:v", "libx264",
            "-profile:v", "high",
            "-level", "4.1",
            "-preset", "slow",  # Quality-focused
            "-crf", "18",  # Lower = better quality
            "-c:a", "aac",
            "-b:a", "128k",
            "-pix_fmt", "yuv420p",  # Ensure YouTube compatibility
            "-y",  # Overwrite output
            output_path,
        ]
        
        try:
            subprocess.run(cmd, check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"FFmpeg failed: {e.stderr.decode()}")
        
        return output_path

    def add_overlay_text(
        self,
        video_path: str,
        text: str,
        output_path: str,
        position: str = "top_center",
        duration: float = 5.0,
        font_size: int = 48,
    ) -> str:
        """Add text overlay to video.
        
        Args:
            video_path: Input video file.
            text: Text to overlay.
            output_path: Output file.
            position: top_center, top_left, center, bottom_center, etc.
            duration: How long to display the text (seconds).
            font_size: Font size.
            
        Returns:
            Path to output video.
        """
        position_map = {
            "top_center": "(w-text_w)/2, 50",
            "top_left": "50, 50",
            "center": "(w-text_w)/2, (h-text_h)/2",
            "bottom_center": "(w-text_w)/2, h-text_h-50",
        }
        
        xy = position_map.get(position, position_map["top_center"])
        
        filter_str = f"drawtext=text='{text}':fontfile=/Windows/Fonts/Arial.ttf:fontsize={font_size}:fontcolor=white:box=1:boxcolor=black@0.5:x={xy}:enable='lt(t,{duration})'"
        
        cmd = [
            self.ffmpeg_path,
            "-i", video_path,
            "-vf", filter_str,
            "-c:a", "copy",
            "-y",
            output_path,
        ]
        
        try:
            subprocess.run(cmd, check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"FFmpeg overlay failed: {e.stderr.decode()}")
        
        return output_path

    def concatenate_videos(
        self,
        video_paths: List[str],
        output_path: str,
    ) -> str:
        """Concatenate multiple videos into one.
        
        Args:
            video_paths: List of video file paths.
            output_path: Output file.
            
        Returns:
            Path to concatenated video.
        """
        # Create concat demux file
        concat_file = "/tmp/concat.txt"
        with open(concat_file, "w") as f:
            for vp in video_paths:
                f.write(f"file '{vp}'\n")
        
        cmd = [
            self.ffmpeg_path,
            "-f", "concat",
            "-safe", "0",
            "-i", concat_file,
            "-c", "copy",
            "-y",
            output_path,
        ]
        
        try:
            subprocess.run(cmd, check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"FFmpeg concat failed: {e.stderr.decode()}")
        
        return output_path

    def export_for_youtube(
        self,
        input_path: str,
        output_path: str,
    ) -> str:
        """Export video optimized for YouTube.
        
        Recommended by YouTube:
        - Container: MP4
        - Codec: H.264 (video), AAC (audio)
        - Bitrate: 15-25 Mbps for 1080p
        - Resolution: 1920x1080 (16:9)
        """
        cmd = [
            self.ffmpeg_path,
            "-i", input_path,
            "-c:v", "libx264",
            "-preset", "slow",
            "-crf", "18",
            "-profile:v", "high",
            "-level", "4.1",
            "-c:a", "aac",
            "-b:a", "128k",
            "-pix_fmt", "yuv420p",
            "-y",
            output_path,
        ]
        
        try:
            subprocess.run(cmd, check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"YouTube export failed: {e.stderr.decode()}")
        
        return output_path

    def _create_image_list(self, images: List[str], output_file: str):
        """Create ffmpeg concat demux file for images."""
        Path(output_file).parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w") as f:
            for img in images:
                f.write(f"file '{img}'\n")

    def get_video_info(self, video_path: str) -> Dict:
        """Get video metadata (duration, resolution, codec, etc.)."""
        cmd = [
            self.ffmpeg_path,
            "-i", video_path,
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stderr  # FFmpeg outputs to stderr
        
        # Parse duration
        import re
        duration_match = re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", output)
        duration = None
        if duration_match:
            h, m, s = duration_match.groups()
            duration = int(h) * 3600 + int(m) * 60 + float(s)
        
        return {
            "duration_seconds": duration,
            "raw_output": output,
        }

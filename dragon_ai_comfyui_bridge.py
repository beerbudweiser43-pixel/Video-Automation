#!/usr/bin/env python3
"""
Dragon Ai ↔ ComfyUI Integration Bridge
Handles communication and workflow conversion between systems
"""

import requests
import json
import time
import asyncio
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

class VideoQuality(Enum):
    """Video output quality options"""
    HD_1080P = ("1080p", 5)      # 5 min per video
    K2 = ("2K", 10)               # 10 min per video
    K4 = ("4K", 20)               # 20 min per video

@dataclass
class GeneratorConfig:
    """Configuration for content generation"""
    generator_type: str
    params: Dict
    quality: VideoQuality = VideoQuality.HD_1080P
    batch_size: int = 1
    effects: List[str] = None
    
    def __post_init__(self):
        if self.effects is None:
            self.effects = []

class DragonAiComfyUIBridge:
    """Bridge between Dragon Ai and ComfyUI"""
    
    def __init__(self, 
                 dragon_ai_url: str = "http://localhost:8501",
                 comfyui_url: str = "http://localhost:8188",
                 output_dir: str = "C:/workspace/outputs/"):
        """
        Initialize the bridge
        
        Args:
            dragon_ai_url: URL to Dragon Ai server
            comfyui_url: URL to ComfyUI server
            output_dir: Directory for output videos
        """
        self.dragon_ai_url = dragon_ai_url
        self.comfyui_url = comfyui_url
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.workflow_dir = self.output_dir / "workflows"
        self.workflow_dir.mkdir(exist_ok=True)
        
        self.session = requests.Session()
        self.processing_jobs = {}
    
    def health_check(self) -> Tuple[bool, bool]:
        """
        Check if both servers are running
        
        Returns:
            Tuple of (dragon_ai_alive, comfyui_alive)
        """
        dragon_ai_alive = False
        comfyui_alive = False
        
        try:
            r = self.session.get(f"{self.dragon_ai_url}/", timeout=2)
            dragon_ai_alive = r.status_code < 500
        except:
            pass
        
        try:
            # Try multiple endpoints as ComfyUI API varies by version
            r = self.session.get(f"{self.comfyui_url}/", timeout=2)
            comfyui_alive = r.status_code == 200
        except:
            try:
                r = self.session.get(f"{self.comfyui_url}/queue", timeout=2)
                comfyui_alive = r.status_code == 200
            except:
                pass
        
        return dragon_ai_alive, comfyui_alive
    
    def create_gospel_workflow(self, config: GeneratorConfig) -> Dict:
        """Create ComfyUI workflow for Gospel music video"""
        theme = config.params.get("theme", "worship")
        duration = config.params.get("duration", 6)
        
        width = 1920 if config.quality == VideoQuality.HD_1080P else 2560
        height = 1080 if config.quality == VideoQuality.HD_1080P else 1440
        
        workflow = {
            "1": {
                "class_type": "CheckpointLoaderSimple",
                "inputs": {"ckpt_name": "sd-v1-5-pruned-emaonly.safetensors"}
            },
            "2": {
                "class_type": "CLIPTextEncode",
                "inputs": {
                    "text": f"Gospel music video, theme: {theme}, duration: {duration}min, spiritual, uplifting",
                    "clip": ["1", 1]
                }
            },
            "3": {
                "class_type": "CLIPTextEncode",
                "inputs": {"text": "low quality, blurry", "clip": ["1", 1]}
            },
            "4": {
                "class_type": "EmptyLatentImage",
                "inputs": {
                    "width": width,
                    "height": height,
                    "batch_size": 1
                }
            },
            "5": {
                "class_type": "KSampler",
                "inputs": {
                    "seed": 12345,
                    "steps": 20,
                    "cfg": 7.0,
                    "sampler_name": "euler",
                    "scheduler": "normal",
                    "denoise": 1.0,
                    "model": ["1", 0],
                    "positive": ["2", 0],
                    "negative": ["3", 0],
                    "latent_image": ["4", 0]
                }
            },
            "6": {
                "class_type": "VAEDecode",
                "inputs": {"samples": ["5", 0], "vae": ["1", 2]}
            },
            "7": {
                "class_type": "SaveImage",
                "inputs": {
                    "filename_prefix": f"gospel_{theme}_{duration}min",
                    "images": ["6", 0]
                }
            }
        }
        return workflow
    
    def create_tech_workflow(self, config: GeneratorConfig) -> Dict:
        """Create ComfyUI workflow for Tech Explained video"""
        topic = config.params.get("topic", "ai_basics")
        complexity = config.params.get("complexity", "beginner")
        
        width = 1920 if config.quality == VideoQuality.HD_1080P else 2560
        height = 1080 if config.quality == VideoQuality.HD_1080P else 1440
        
        workflow = {
            "1": {
                "class_type": "CheckpointLoaderSimple",
                "inputs": {"ckpt_name": "sd-v1-5-pruned-emaonly.safetensors"}
            },
            "2": {
                "class_type": "CLIPTextEncode",
                "inputs": {
                    "text": f"Tech tutorial, topic: {topic}, complexity: {complexity}, educational, clear visuals",
                    "clip": ["1", 1]
                }
            },
            "3": {
                "class_type": "CLIPTextEncode",
                "inputs": {"text": "blurry, low quality, confusing", "clip": ["1", 1]}
            },
            "4": {
                "class_type": "EmptyLatentImage",
                "inputs": {"width": width, "height": height, "batch_size": 1}
            },
            "5": {
                "class_type": "KSampler",
                "inputs": {
                    "seed": 54321,
                    "steps": 20,
                    "cfg": 7.0,
                    "sampler_name": "euler",
                    "scheduler": "normal",
                    "denoise": 1.0,
                    "model": ["1", 0],
                    "positive": ["2", 0],
                    "negative": ["3", 0],
                    "latent_image": ["4", 0]
                }
            },
            "6": {
                "class_type": "VAEDecode",
                "inputs": {"samples": ["5", 0], "vae": ["1", 2]}
            },
            "7": {
                "class_type": "SaveImage",
                "inputs": {
                    "filename_prefix": f"tech_{topic}_{complexity}",
                    "images": ["6", 0]
                }
            }
        }
        return workflow
        
        workflow = {
            "1": {
                "class_type": "CheckpointLoaderSimple",
                "inputs": {"ckpt_name": "model.safetensors"}
            },
            "2": {
                "class_type": "CLIPTextEncode",
                "inputs": {
                    "text": f"Tech tutorial, topic: {topic}, complexity: {complexity}, educational, clear visuals",
                    "clip": ["1", 1]
                }
            },
            "3": {
                "class_type": "CLIPTextEncode",
                "inputs": {"text": "blurry, low quality, confusing", "clip": ["1", 1]}
            },
            "4": {
                "class_type": "EmptyLatentImage",
                "inputs": {"width": 1920, "height": 1080, "batch_size": 1}
            },
            "5": {
                "class_type": "KSampler",
                "inputs": {
                    "seed": 54321,
                    "steps": 20,
                    "cfg": 7.0,
                    "sampler_name": "euler",
                    "scheduler": "normal",
                    "denoise": 1.0,
                    "model": ["1", 0],
                    "positive": ["2", 0],
                    "negative": ["3", 0],
                    "latent_image": ["4", 0]
                }
            },
            "6": {
                "class_type": "VAEDecode",
                "inputs": {"samples": ["5", 0], "vae": ["1", 2]}
            },
            "7": {
                "class_type": "SaveImage",
                "inputs": {
                    "filename_prefix": f"tech_{topic}_{complexity}",
                    "images": ["6", 0]
                }
            }
        }
        return workflow
    
    def get_workflow(self, config: GeneratorConfig) -> Dict:
        """Get appropriate workflow for generator type"""
        if config.generator_type.lower() == "gospel":
            return self.create_gospel_workflow(config)
        elif config.generator_type.lower() == "tech":
            return self.create_tech_workflow(config)
        else:
            return self.create_tech_workflow(config)  # Default to tech
    
    def submit_workflow(self, workflow: Dict) -> Optional[str]:
        """
        Submit workflow to ComfyUI
        
        Returns:
            prompt_id if successful, None otherwise
        """
        try:
            # Convert string keys to integers and fix node references
            workflow_converted = {}
            for key, node in workflow.items():
                node_id = int(key)
                node_copy = node.copy()
                inputs_copy = {}
                
                # Fix node references in inputs
                for input_name, input_value in node.get("inputs", {}).items():
                    if isinstance(input_value, list) and len(input_value) >= 1:
                        # Check if first element is a node reference (string that looks like a number)
                        if isinstance(input_value[0], str) and input_value[0].isdigit():
                            inputs_copy[input_name] = [int(input_value[0])] + input_value[1:]
                        else:
                            inputs_copy[input_name] = input_value
                    else:
                        inputs_copy[input_name] = input_value
                
                node_copy["inputs"] = inputs_copy
                workflow_converted[node_id] = node_copy
            
            print(f"📋 Workflow structure (nodes): {list(workflow_converted.keys())}")
            
            # Prepare the request payload
            payload = {
                "prompt": workflow_converted,
                "client_id": "dragon-ai-bridge"
            }
            
            print(f"📤 Submitting workflow...")
            response = self.session.post(
                f"{self.comfyui_url}/api/prompt",
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                prompt_id = result.get("prompt_id")
                print(f"✅ Workflow submitted: {prompt_id}")
                return prompt_id
            else:
                print(f"❌ ComfyUI error: {response.status_code}")
                print(f"Response: {response.text}")
                return None
                
        except Exception as e:
            print(f"❌ Workflow submission failed: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def monitor_progress(self, prompt_id: str, timeout: int = 600) -> bool:
        """
        Monitor ComfyUI processing status
        
        Args:
            prompt_id: ID of the processing job
            timeout: Timeout in seconds
            
        Returns:
            True if completed successfully
        """
        start_time = time.time()
        last_status = None
        
        while time.time() - start_time < timeout:
            try:
                response = self.session.get(
                    f"{self.comfyui_url}/history/{prompt_id}",
                    timeout=10
                )
                
                history = response.json()
                
                if prompt_id in history:
                    status = history[prompt_id]
                    # Check for outputs
                    if "outputs" in status and len(status["outputs"]) > 0:
                        print(f"✅ Processing complete: {prompt_id}")
                        return True
                    
                    # Print status if changed
                    current_status = json.dumps(status, indent=2)
                    if current_status != last_status:
                        last_status = current_status
                        print(f"⏳ Processing... {prompt_id}")
                
                time.sleep(2)
                
            except Exception as e:
                print(f"⚠️  Monitoring error: {e}")
                time.sleep(2)
        
        print(f"❌ Processing timeout: {prompt_id}")
        return False
    
    def process_video(self, config: GeneratorConfig) -> Optional[Dict]:
        """
        Process single video through Dragon Ai + ComfyUI pipeline
        
        Returns:
            Result dict if successful
        """
        print(f"\n🚀 Starting {config.generator_type} video generation...")
        
        # Check servers
        dragon_ai_up, comfyui_up = self.health_check()
        if not dragon_ai_up:
            print("❌ Dragon Ai server not responding")
            return None
        if not comfyui_up:
            print("❌ ComfyUI server not responding")
            return None
        
        print("✅ Servers online")
        print("⚠️  IMPORTANT: This requires AI models to be installed in ComfyUI")
        print("   Models Directory: C:\\workspace\\ComfyUI\\models\\checkpoints\\")
        print("   Download a model like Stable Diffusion first!")
        
        # Step 1: Create workflow
        print("🔧 Creating workflow...")
        workflow = self.get_workflow(config)
        
        # Save workflow for reference
        workflow_file = self.workflow_dir / f"{config.generator_type}_{int(time.time())}.json"
        with open(workflow_file, 'w') as f:
            json.dump(workflow, f, indent=2)
        print(f"   Saved to: {workflow_file}")
        
        # Step 2: Submit to ComfyUI
        print("📤 Submitting workflow...")
        prompt_id = self.submit_workflow(workflow)
        if not prompt_id:
            print("\n⚠️  ERROR: Model not found or workflow validation failed")
            print("   This usually means:") 
            print("   1. No AI models installed (most common)")
            print("   2. Model file doesn't exist in checkpoints folder")
            print("   3. ComfyUI nodes are misconfigured")
            print("\n   To fix: Download and install a model file to:")
            print("   C:\\workspace\\ComfyUI\\models\\checkpoints\\")
            return None
        
        # Step 3: Monitor processing
        print(f"⏳ Processing (ID: {prompt_id})...")
        success = self.monitor_progress(prompt_id)
        
        if success:
            print("✅ Video generation complete!")
            return {
                "prompt_id": prompt_id,
                "generator_type": config.generator_type,
                "quality": config.quality.value[0],
                "status": "complete"
            }
        else:
            return None
    
    def process_batch(self, configs: List[GeneratorConfig]) -> List[Dict]:
        """
        Process batch of videos
        
        Returns:
            List of results
        """
        print(f"\n🎬 Starting batch processing ({len(configs)} videos)...")
        results = []
        
        for i, config in enumerate(configs, 1):
            print(f"\n[{i}/{len(configs)}] Processing {config.generator_type}...")
            result = self.process_video(config)
            if result:
                results.append(result)
        
        print(f"\n📊 Batch complete: {len(results)}/{len(configs)} successful")
        return results
    
    def get_system_info(self) -> Dict:
        """Get system information"""
        info = {
            "dragon_ai": "unknown",
            "comfyui": "unknown",
            "timestamp": time.time()
        }
        
        try:
            r = self.session.get(f"{self.comfyui_url}/api/systeminfo", timeout=2)
            if r.status_code == 200:
                info["comfyui"] = r.json()
        except:
            pass
        
        return info

# ============================================================================
# Example Usage
# ============================================================================

if __name__ == "__main__":
    # Initialize bridge
    bridge = DragonAiComfyUIBridge()
    
    # Check servers
    print("🔍 Checking servers...")
    dragon_up, comfyui_up = bridge.health_check()
    print(f"   Dragon Ai: {'✅ Online' if dragon_up else '❌ Offline'}")
    print(f"   ComfyUI: {'✅ Online' if comfyui_up else '❌ Offline'}")
    
    if not (dragon_up and comfyui_up):
        print("\n⚠️  Both servers needed to start processing")
        print("Terminal 1: cd C:\\workspace\\ComfyUI-OmniFlow && .\\start.bat")
        print("Terminal 2: cd C:\\workspace\\ComfyUI && python main.py")
        exit(1)
    
    # Single video example
    print("\n" + "="*60)
    print("EXAMPLE: Generate Gospel Music Video")
    print("="*60)
    
    gospel_config = GeneratorConfig(
        generator_type="gospel",
        params={"theme": "worship", "duration": 6},
        quality=VideoQuality.HD_1080P,
        effects=["color_grading", "transitions"]
    )
    
    result = bridge.process_video(gospel_config)
    if result:
        print(f"\n✅ Video ready: {result['prompt_id']}")
    
    # Batch example (commented out)
    # print("\n" + "="*60)
    # print("EXAMPLE: Batch Generate 3 Tech Videos")
    # print("="*60)
    #
    # batch_configs = [
    #     GeneratorConfig(
    #         generator_type="tech",
    #         params={"topic": "ai_basics", "complexity": "beginner"}
    #     ),
    #     GeneratorConfig(
    #         generator_type="tech",
    #         params={"topic": "neural_networks", "complexity": "intermediate"}
    #     ),
    #     GeneratorConfig(
    #         generator_type="tech",
    #         params={"topic": "cybersecurity", "complexity": "advanced"}
    #     ),
    # ]
    #
    # results = bridge.process_batch(batch_configs)
    # print(f"\nCompleted: {len(results)} videos")

"""
Gospel Music & Spiritual Content Generator
Specialized module for creating high-quality Gospel music videos with spiritual visuals

Features:
- Gospel music script templates
- Spiritual themes and narratives
- Optimal pacing for gospel content
- Spiritual color palettes
- Music recommendations
- Visual element suggestions
"""

import json
from typing import Dict, List, Optional

# Try to import AI modules, but make them optional
try:
    from omniflow import PoetryGenerator, ScriptDeveloper, YouTubeAnalyst
    HAS_AI_MODULES = True
except (ImportError, Exception) as e:
    HAS_AI_MODULES = False
    _import_error = str(e)


class GospelMusicScriptBuilder:
    """Creates authentic Gospel music video scripts"""
    
    GOSPEL_THEMES = {
        "faith": {
            "name": "Faith & Trust",
            "keywords": ["faith", "trust", "believe", "journey", "light"],
            "mood": "inspirational, uplifting",
            "duration_preference": "4-8 minutes"
        },
        "redemption": {
            "name": "Redemption & Grace",
            "keywords": ["redemption", "grace", "forgiveness", "restore", "hope"],
            "mood": "moving, emotional, powerful",
            "duration_preference": "6-10 minutes"
        },
        "worship": {
            "name": "Worship & Praise",
            "keywords": ["worship", "praise", "glory", "salvation", "almighty"],
            "mood": "passionate, joyful, energetic",
            "duration_preference": "3-7 minutes"
        },
        "spiritual_journey": {
            "name": "Spiritual Journey",
            "keywords": ["journey", "spiritual", "transformation", "growth", "awakening"],
            "mood": "reflective, inspirational, profound",
            "duration_preference": "7-10 minutes"
        },
        "praise_celebration": {
            "name": "Praise & Celebration",
            "keywords": ["praise", "celebrate", "joy", "blessing", "victorious"],
            "mood": "celebratory, joyful, upbeat",
            "duration_preference": "3-6 minutes"
        },
        "biblical_stories": {
            "name": "Biblical Stories",
            "keywords": ["bible", "story", "miracle", "testimony", "truth"],
            "mood": "narrative, inspiring, educational",
            "duration_preference": "8-10 minutes"
        }
    }
    
    SPIRITUAL_VISUALS = {
        "light_themes": [
            "Golden light rays breaking through clouds",
            "Sunrise over mountains (spiritual awakening)",
            "Candlelit hands raised in praise",
            "Glowing orbs of light floating upward",
            "Divine light illuminating church interior",
            "Star-filled night sky with spiritual elements",
            "Light reflections on water (purity)",
            "Ethereal light particles (Holy Spirit visualization)"
        ],
        "nature_themes": [
            "Majestic mountains (strength, faith)",
            "Flowing rivers (grace, abundance)",
            "Blooming flowers (growth, renewal)",
            "Peaceful forests (spiritual sanctuary)",
            "Ocean waves (eternal, overwhelming grace)",
            "Starry night sky (divine presence)",
            "Sunrise/sunset (spiritual transitions)",
            "Birds flying free (liberation, spirit)"
        ],
        "church_themes": [
            "Historical church architecture",
            "Stained glass windows with light",
            "Congregation in worship",
            "Gospel choir performing",
            "Hands raised in worship",
            "Candles lit in sanctuary",
            "Cross with dramatic lighting",
            "Baptismal waters (renewal)"
        ],
        "emotional_themes": [
            "People hugging (community, love)",
            "Tears of joy (emotional release)",
            "Families praying together",
            "Hands together (unity, strength)",
            "Faces of peace and joy",
            "Hands reaching toward sky",
            "People celebrating together",
            "Humble kneeling in prayer"
        ],
        "symbolic_themes": [
            "Dove flying (Holy Spirit, peace)",
            "Chains breaking (freedom)",
            "Phoenix rising (resurrection)",
            "Seeds growing (faith growth)",
            "Diamond sparkling (spiritual value)",
            "Crown (kingship, glory)",
            "Wings spreading (spiritual flight)",
            "Door opening (new beginnings)"
        ]
    }
    
    GOSPEL_MUSIC_STYLES = {
        "traditional_gospel": {
            "characteristics": ["church organ", "gospel choir", "hymn-like", "traditional"],
            "pacing": "moderate, rhythmic",
            "energy": "warm, comforting",
            "color_scheme": "rich golds, deep purples, warm whites"
        },
        "contemporary_gospel": {
            "characteristics": ["modern instruments", "contemporary sound", "upbeat", "energetic"],
            "pacing": "fast, dynamic",
            "energy": "high energy, celebratory",
            "color_scheme": "bright golds, electric blues, vibrant colors"
        },
        "soul_gospel": {
            "characteristics": ["soul singing", "emotional delivery", "powerful vocals", "deep feeling"],
            "pacing": "varied, emotional peaks",
            "energy": "intense, moving",
            "color_scheme": "warm oranges, deep reds, golden ambers"
        },
        "spiritual_ambient": {
            "characteristics": ["peaceful", "meditative", "ethereal", "instrumental"],
            "pacing": "slow, contemplative",
            "energy": "calm, reflective",
            "color_scheme": "soft whites, pale blues, ethereal purples"
        }
    }
    
    def __init__(self):
        """Initialize Gospel Music Script Builder
        
        AI modules are optional - full functionality available without
        external API keys
        """
        self.has_ai = HAS_AI_MODULES
        if self.has_ai:
            try:
                self.poetry_gen = PoetryGenerator()
                self.script_dev = ScriptDeveloper()
                self.analyst = YouTubeAnalyst()
            except Exception:
                self.has_ai = False
    
    def generate_gospel_script(
        self,
        theme: str,
        music_style: str = "contemporary_gospel",
        duration_minutes: int = 8,
        include_testimony: bool = False
    ) -> Dict:
        """
        Generate a complete Gospel music video script
        
        Args:
            theme: One of gospel_music_themes keys
            music_style: One of gospel_music_styles keys
            duration_minutes: 3-10 minutes
            include_testimony: Add personal testimony element
        
        Returns:
            Complete script with metadata
        """
        
        if theme not in self.GOSPEL_THEMES:
            return {"error": f"Theme must be one of: {list(self.GOSPEL_THEMES.keys())}"}
        
        if music_style not in self.GOSPEL_MUSIC_STYLES:
            return {"error": f"Music style must be one of: {list(self.GOSPEL_MUSIC_STYLES.keys())}"}
        
        theme_info = self.GOSPEL_THEMES[theme]
        style_info = self.GOSPEL_MUSIC_STYLES[music_style]
        
        # Generate script (with or without AI modules)
        if self.has_ai:
            print(f"📝 Creating poetic script for {theme_info['name']}...")
            try:
                poetic_script = self.poetry_gen.generate_poetic_narration(
                    topic=theme_info['name'],
                    style=theme_info['mood'].split(',')[0].strip()
                )
            except Exception:
                poetic_script = self._get_fallback_script(theme, duration_minutes)
        else:
            # Use template-based script generation
            poetic_script = self._get_fallback_script(theme, duration_minutes)
        
        # Add testimony if requested
        if include_testimony:
            testimony = self._get_fallback_testimony(theme)
            poetic_script += f"\n\n[PERSONAL TESTIMONY]\n{testimony}"
        
        # Refine script timing
        if self.has_ai:
            try:
                refined_script = self.script_dev.refine_script_professionally(
                    script=poetic_script,
                    target_duration_seconds=duration_minutes * 60
                )
                script_output = refined_script.get("refined_script", refined_script)
            except Exception:
                script_output = poetic_script
        else:
            script_output = poetic_script
        
        # Get viral potential
        if self.has_ai:
            try:
                viral_score = self.analyst.estimate_viral_score(
                    title=f"Gospel Music: {theme_info['name']}",
                    script=script_output,
                    niche="Gospel Music"
                )
            except Exception:
                viral_score = "High"
        else:
            viral_score = "High"
        
        return {
            "theme": theme_info['name'],
            "music_style": style_info['characteristics'],
            "script": {
                "narrative": script_output,
                "duration_seconds": duration_minutes * 60,
                "pacing": style_info['pacing']
            },
            "duration_minutes": duration_minutes,
            "color_palette": style_info['color_scheme'],
            "visual_suggestions": self._get_visual_suggestions(theme),
            "music_recommendations": self._get_music_recommendations(music_style),
            "pacing": style_info['pacing'],
            "energy_level": style_info['energy'],
            "viral_potential": viral_score,
            "tags": [
                "Gospel",
                "Music",
                "Spiritual",
                "Christian",
                "Worship",
                "Faith",
                theme_info['name'].replace(" & ", "").replace(" ", "")
            ]
        }
    
    def _get_visual_suggestions(self, theme: str) -> List[str]:
        """Get visual suggestions for the theme"""
        suggestions = []
        
        # Add theme-specific visuals
        if theme == "faith":
            suggestions.extend([
                self.SPIRITUAL_VISUALS["light_themes"][0],  # Golden light rays
                self.SPIRITUAL_VISUALS["nature_themes"][0],  # Mountains
                self.SPIRITUAL_VISUALS["symbolic_themes"][3], # Seeds growing
            ])
        elif theme == "redemption":
            suggestions.extend([
                self.SPIRITUAL_VISUALS["light_themes"][1],  # Sunrise
                self.SPIRITUAL_VISUALS["symbolic_themes"][1], # Chains breaking
                self.SPIRITUAL_VISUALS["emotional_themes"][1], # Tears of joy
            ])
        elif theme == "worship":
            suggestions.extend([
                self.SPIRITUAL_VISUALS["church_themes"][1],  # Stained glass
                self.SPIRITUAL_VISUALS["church_themes"][4],  # Hands raised
                self.SPIRITUAL_VISUALS["nature_themes"][6],  # Sunrise
            ])
        elif theme == "spiritual_journey":
            suggestions.extend([
                self.SPIRITUAL_VISUALS["symbolic_themes"][4], # Phoenix rising
                self.SPIRITUAL_VISUALS["nature_themes"][2],  # Blooming flowers
                self.SPIRITUAL_VISUALS["emotional_themes"][0], # People hugging
            ])
        elif theme == "praise_celebration":
            suggestions.extend([
                self.SPIRITUAL_VISUALS["light_themes"][3],  # Glowing orbs
                self.SPIRITUAL_VISUALS["church_themes"][1],  # Stained glass
                self.SPIRITUAL_VISUALS["emotional_themes"][4], # Faces of joy
            ])
        elif theme == "biblical_stories":
            suggestions.extend([
                self.SPIRITUAL_VISUALS["church_themes"][0],  # Church architecture
                self.SPIRITUAL_VISUALS["nature_themes"][0],  # Mountains
                self.SPIRITUAL_VISUALS["symbolic_themes"][2], # Phoenix
            ])
        
        return suggestions
    
    def _get_music_recommendations(self, music_style: str) -> Dict:
        """Get music recommendations for the style"""
        recommendations = {
            "traditional_gospel": {
                "primary_instruments": ["church organ", "piano", "gospel choir"],
                "mood": "warm, comforting, traditional",
                "tempo": "80-100 BPM",
                "suggested_artists": ["Mahalia Jackson style", "Traditional hymns with arrangement"],
                "production_tips": ["Rich reverb", "Organ prominent", "Choir harmonies emphasized"]
            },
            "contemporary_gospel": {
                "primary_instruments": ["electric drums", "bass guitar", "synth keys", "vocals"],
                "mood": "upbeat, modern, energetic",
                "tempo": "100-130 BPM",
                "suggested_artists": ["Kirk Franklin style", "Modern gospel beats"],
                "production_tips": ["Clean drums", "Driving bass", "Contemporary production"]
            },
            "soul_gospel": {
                "primary_instruments": ["powerful vocals", "strings", "piano", "light percussion"],
                "mood": "emotional, soulful, powerful",
                "tempo": "90-110 BPM",
                "suggested_artists": ["Aretha Franklin style", "Soul gospel classics"],
                "production_tips": ["Vocal layering", "String arrangements", "Emotional dynamics"]
            },
            "spiritual_ambient": {
                "primary_instruments": ["ambient pads", "strings", "light bells", "vocal layers"],
                "mood": "peaceful, meditative, spiritual",
                "tempo": "60-80 BPM",
                "suggested_artists": ["Peaceful gospel", "Spiritual instrumental"],
                "production_tips": ["Ethereal pads", "String layering", "Minimalist approach"]
            }
        }
        return recommendations.get(music_style, recommendations["contemporary_gospel"])
    
    def _get_fallback_script(self, theme: str, duration_minutes: int) -> str:
        """Generate a template script when AI modules aren't available"""
        
        theme_scripts = {
            "faith": f"""
FAITH & TRUST - A Journey of Belief
Duration: ~{duration_minutes} minutes

[OPENING]
In the quiet moments of our lives, when doubt whispers louder than hope,
When the path ahead seems unclear and darkness feels endless...
We discover an eternal truth: Faith is not the absence of fear, but trust in what we cannot see.

[THEME DEVELOPMENT]
Faith begins in the heart. Not as certainty, but as a choice.
A choice to believe when evidence feels thin.
A choice to move forward when every step feels uncertain.
Through history, through generations, faith has been the bridge between despair and deliverance.

[REFLECTION]
What is faith if not the willingness to believe?
What is trust if not the courage to let go and let God lead?
In every challenge overcome, in every prayer answered,
We find renewed faith that carries us through tomorrows troubled and troubled times.

[CLOSING]
So hold fast to your faith. Let it be the anchor for your soul.
For with faith, mountains move. With faith, the impossible becomes possible.
With faith, you are never truly alone.

--- Duration: approximately {duration_minutes} minutes of narration ---
""",
            "redemption": f"""
REDEMPTION & GRACE - A Story of Restoration
Duration: ~{duration_minutes} minutes

[OPENING]
We are all broken. Perhaps not in body, but in spirit.
We carry the weight of mistakes, of failures, of moments we wish we could rewrite.
But there is a hope greater than our brokenness: the power of redemption.

[TRANSFORMATION]
Redemption is not earned - it is given. It is grace extending beyond what we deserve.
When we confess our failures, we discover freedom waiting on the other side.
When we accept forgiveness, we begin the journey home.

[VOICES OF REDEMPTION]
Mighty is the call of grace that reaches us in our darkest hour.
Powerful is the love that says: "You are worth redeeming."
Life-changing is the moment we realize we are less defined by our past than we think.

[HOPE RISING]
From ashes, new growth emerges. From endings, new beginnings.
This is the redemption we celebrate - not just for ourselves, but for all humanity.
For grace has no limits. Mercy has no boundaries.

[CLOSING]
You are not your mistakes. You are not your failures.
You are redeemed. You are restored. You are free.

--- Duration: approximately {duration_minutes} minutes of narration ---
""",
            "worship": f"""
WORSHIP & PRAISE - Celebrating the Divine
Duration: ~{duration_minutes} minutes

[OPENING]
There is power in raising our voices together.
There is healing in bowing our hearts in reverence.
Worship connects us to something greater than ourselves.

[CELEBRATION]
With every note of praise, we proclaim our faith.
With every word of worship, we express our gratitude.
With every heartbeat raised in devotion, we honor the presence of the divine.

[GLORY & MAJESTY]
Almighty God deserves our praise. Holy and worthy of all our adoration.
In worship, we find peace. In worship, we find belonging.
In worship, the world's troubles fade away, and we experience divine presence.

[COMMUNITY MOMENT]
When we worship together, we become one voice crying out in harmony.
Our individual struggles fade as we unite in a chorus of faith.
This is the power of worship - to transform hearts and minds.

[CLOSING]
Let praise flow from your lips. Let worship fill your heart.
For in giving glory, we receive blessings immeasurable.

--- Duration: approximately {duration_minutes} minutes of narration ---
""",
            "spiritual_journey": f"""
SPIRITUAL JOURNEY - A Path of Discovery and Growth
Duration: ~{duration_minutes} minutes

[OPENING]
Every life is a journey. Every soul is on a path of discovery.
Some paths are straight, others wind through valleys deep and mountains high.
But all paths that lead to the divine are worthy and sacred.

[THE AWAKENING]
It begins with a question. A yearning. A sense that something greater exists.
Then comes the seeking - looking beyond the visible for the invisible truth.
This is the beginning of spiritual awakening.

[CHALLENGES & GROWTH]
The journey is not always easy. Faith is tested. Resolve is questioned.
But with each obstacle overcome comes wisdom. With each trial endured comes strength.
We grow not in comfortable moments, but through transformation.

[COMMUNITY & CONNECTION]
No journey is walked alone. Others have walked this path before us.
We find ourselves in the stories of the faithful, the brave, the devoted.
And we carry hope for those who follow.

[TRANSFORMATION]
A spiritual journey changes us. It transforms how we see. How we love. How we live.
We discover that the destination was never the goal - the journey itself is the blessing.

[CLOSING]
Continue your journey with faith. The path ahead is bright with possibility.

--- Duration: approximately {duration_minutes} minutes of narration ---
""",
            "praise_celebration": f"""
PRAISE & CELEBRATION - Joy in the Divine
Duration: ~{duration_minutes} minutes

[OPENING]
Joy! Let it ring through the heavens!
Celebration! Let it echo in every heart!
Today we gather to proclaim the goodness of God!

[JUBILATION]
This is a day for rejoicing! A moment for raising voices in exultation!
Feel the energy, the power, the overwhelming joy of collective praise!
When we celebrate together, heaven itself joins our chorus!

[BLESSINGS COUNTED]
What blessings have you received? What miracles have you witnessed?
Every joy, every answered prayer, every moment of grace - worthy of celebration!
God's goodness is endless. Our reasons for praise are infinite.

[MOVEMENT & ENERGY]
Rise up! Lift your hands! Let your whole being proclaim victory!
This is not reserved worship - this is passionate, energetic, joyful celebration!
When your spirit is free, your praise knows no bounds!

[UNITY IN JOY]
Our celebration becomes contagious. Others see our joy and desire it.
In sharing our happiness, we offer others a pathway to their own celebration.
This is the beauty of praise - it multiplies when shared.

[CLOSING]
Celebrate with all your heart! Praise with your whole being!
For joy is our birthright, and celebration is our calling!

--- Duration: approximately {duration_minutes} minutes of narration ---
""",
            "biblical_stories": f"""
BIBLICAL STORIES - Timeless Lessons of Faith
Duration: ~{duration_minutes} minutes

[OPENING]
The Bible is filled with stories - of ordinary people discovering extraordinary faith.
Stories of transformation. Stories of courage. Stories that echo through millennia.
Today we honor these timeless tales.

[THE STORIES]
From redemption tales of grace working through willing hearts,
To stories of faith conquering impossible odds,
To narratives of transformation that still inspire today.
These stories are not ancient history - they are alive in our present.

[LESSONS FROM THE PAST]
What can we learn from those who came before?
That faith is simple yet powerful. That trust is revolutionary.
That one person, dedicated to their calling, can change history.

[RELEVANCE TODAY]
These biblical narratives address our modern struggles.
They speak to the fear, the doubt, the hope that lives in our contemporary hearts.
The messages are timeless. Truth never grows old.

[OUR STORY]
We are part of this biblical legacy. Our choices matter. Our faith counts.
We are writing new chapters in an ancient story of God's faithfulness.

[CLOSING]
Learn from the stories of old. Live out new stories of faith.
For you are part of biblical history in the making.

--- Duration: approximately {duration_minutes} minutes of narration ---
"""
        }
        
        return theme_scripts.get(theme, "A Gospel message of faith, hope, and love.")
    
    def _get_fallback_testimony(self, theme: str) -> str:
        """Generate a template testimony when AI modules aren't available"""
        
        return f"""
In my own journey with {self.GOSPEL_THEMES[theme]['name']}, I have discovered:

The struggle was real. There were moments of deep doubt and endless questions.
But in that valley, I met grace. In that darkness, I found light.

My turning point came when I realized I was not meant to walk this path alone.
When I surrendered my need to understand everything, I found peace in trust.
When I stopped fighting, I found freedom.

This faith has changed everything - how I see myself, how I see others, how I see God.
And my deepest desire is that you would experience this transformation too.

Whatever your struggle, whatever your question - faith is still available to you.
Grace is waiting. Hope is available. Peace is possible.

This is not just my story. This is the story of every person who has ever encountered the divine.
And it can be your story too."""
    
    def create_gospel_music_video_plan(
        self,
        title: str,
        theme: str = "worship",
        music_style: str = "contemporary_gospel",
        duration_minutes: int = 8,
        artist_name: Optional[str] = None
    ) -> Dict:
        """
        Create a complete production plan for Gospel music video
        
        Returns everything needed to produce the video
        """
        
        # Generate script
        script_data = self.generate_gospel_script(
            theme=theme,
            music_style=music_style,
            duration_minutes=duration_minutes,
            include_testimony=False
        )
        
        if "error" in script_data:
            return script_data
        
        # Create complete production plan
        plan = {
            "title": title,
            "artist": artist_name or "Gospel Artist",
            "video_metadata": {
                "duration_minutes": duration_minutes,
                "channel_template": "gospel_music",
                "video_style": "cinematic_storytelling",
                "voice_id": "21m00Tcm4TlvDq8ikWAM",  # Bella - soulful voice
            },
            "script": {
                "narrative": script_data["script"]["narrative"],
                "duration_seconds": duration_minutes * 60,
                "pacing": script_data['pacing']
            },
            "visual_production": {
                "color_palette": script_data['color_palette'],
                "primary_visuals": script_data['visual_suggestions'],
                "transitions": [
                    "Gentle fade between scenes",
                    "Light effects at spiritual moments",
                    "Slow motion for emotional peaks",
                    "Cross-fade at music changes"
                ],
                "lighting": [
                    "Warm golden lighting throughout",
                    "Bright light rays for spiritual moments",
                    "Backlit silhouettes for contrast",
                    "Soft glowing highlights"
                ]
            },
            "audio_production": {
                "music_style": music_style,
                "characteristics": script_data['music_recommendations']['primary_instruments'],
                "tempo_bpm": script_data['music_recommendations']['tempo'],
                "mood": script_data['music_recommendations']['mood'],
                "production_tips": script_data['music_recommendations']['production_tips']
            },
            "youtube_optimization": {
                "title": title,
                "tags": script_data['tags'],
                "description_elements": [
                    f"Divine music celebrating {script_data['theme']}",
                    f"Artist: {artist_name or 'Gospel Artist'}",
                    f"Duration: {duration_minutes} minutes",
                    "Subscribe for more Gospel music",
                    "Lyrics and message of faith in every note"
                ]
            },
            "quality_metrics": {
                "viral_potential": script_data.get('viral_potential', 'High'),
                "engagement_factors": [
                    "Emotional spiritual message",
                    "Professional production quality",
                    "Authentic Gospel music style",
                    "Compelling visual storytelling"
                ]
            }
        }
        
        return plan


class GospelMusicVideoGenerator:
    """
    End-to-end Gospel music video generation
    Handles script, visuals, audio, and YouTube publishing
    """
    
    def __init__(self):
        self.script_builder = GospelMusicScriptBuilder()
    
    def generate_gospel_music_video(
        self,
        title: str,
        theme: str = "worship",
        music_style: str = "contemporary_gospel",
        duration_minutes: int = 8,
        artist_name: Optional[str] = None
    ) -> Dict:
        """
        Generate complete Gospel music video production
        
        Returns:
            Complete production plan ready for video generation
        """
        
        print(f"🎵 Generating Gospel Music Video: {title}")
        print(f"📖 Theme: {theme}")
        print(f"🎶 Style: {music_style}")
        print(f"⏱️  Duration: {duration_minutes} minutes\n")
        
        # Create production plan
        plan = self.script_builder.create_gospel_music_video_plan(
            title=title,
            theme=theme,
            music_style=music_style,
            duration_minutes=duration_minutes,
            artist_name=artist_name
        )
        
        if "error" in plan:
            return plan
        
        print("✅ Production plan created!")
        print(f"📝 Script: {len(plan['script']['narrative'])} characters")
        print(f"🎨 Visuals: {len(plan['visual_production']['primary_visuals'])} visual elements")
        print(f"🎵 Audio: {music_style} composition")
        print(f"📺 YouTube ready: {len(plan['youtube_optimization']['tags'])} tags\n")
        
        return plan


# Example themes for Gospel content creation
GOSPEL_MUSIC_EXAMPLES = {
    "fast_paced_praise": {
        "title": "Joy in the Morning",
        "theme": "praise_celebration",
        "music_style": "contemporary_gospel",
        "duration_minutes": 5,
        "description": "High-energy celebration of faith"
    },
    "slow_worship": {
        "title": "Grace Abounds",
        "theme": "redemption",
        "music_style": "spiritual_ambient",
        "duration_minutes": 8,
        "description": "Contemplative worship experience"
    },
    "testimony_story": {
        "title": "From Darkness to Light",
        "theme": "spiritual_journey",
        "music_style": "soul_gospel",
        "duration_minutes": 9,
        "description": "Personal faith journey narrative"
    },
    "traditional_hymn": {
        "title": "Amazing Grace Reimagined",
        "theme": "faith",
        "music_style": "traditional_gospel",
        "duration_minutes": 6,
        "description": "Traditional hymn with spiritual visuals"
    },
    "biblical_story": {
        "title": "The Prodigal's Return",
        "theme": "redemption",
        "music_style": "soul_gospel",
        "duration_minutes": 10,
        "description": "Biblical narrative with gospel music"
    }
}

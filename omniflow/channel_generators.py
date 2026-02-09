"""
Specialized Content Generators for All Channel Types
Applies the Gospel approach to all major OmniFlow channel templates

Structure:
- TechExplainedGenerator - Tech & AI education
- TutorialGenerator - How-to & step-by-step guides
- FinanceAnalysisGenerator - Finance & investment content
- TrendingCommentaryGenerator - News & trending topics
- WellnessLifestyleGenerator - Health & wellness content
- SpiritualDocumentaryGenerator - Inspirational & spiritual content
- BusinessInsightsGenerator - Business & entrepreneurship
"""

import json
from typing import Dict, List, Optional


class TechExplainedGenerator:
    """Generate tech education & AI explanation videos"""
    
    TECH_TOPICS = {
        "ai_basics": {
            "name": "AI Basics & Introduction",
            "keywords": ["artificial intelligence", "machine learning", "basics", "explained"],
            "complexity": "beginner",
            "duration": "8-12 minutes"
        },
        "neural_networks": {
            "name": "Neural Networks & Deep Learning",
            "keywords": ["neural networks", "deep learning", "AI", "training"],
            "complexity": "intermediate",
            "duration": "10-15 minutes"
        },
        "python_programming": {
            "name": "Python Programming Tutorials",
            "keywords": ["python", "programming", "coding", "tutorial"],
            "complexity": "beginner",
            "duration": "8-15 minutes"
        },
        "data_science": {
            "name": "Data Science & Analytics",
            "keywords": ["data science", "analytics", "visualization", "datasets"],
            "complexity": "intermediate",
            "duration": "10-15 minutes"
        },
        "cybersecurity": {
            "name": "Cybersecurity & Online Safety",
            "keywords": ["security", "hacking", "protection", "privacy"],
            "complexity": "intermediate",
            "duration": "10-12 minutes"
        }
    }
    
    def __init__(self):
        self.topics = self.TECH_TOPICS
    
    def generate_tech_script(
        self,
        topic: str,
        complexity: str = "beginner",
        duration_minutes: int = 10
    ) -> Dict:
        """Generate tech education script"""
        
        if topic not in self.TECH_TOPICS:
            return {"error": f"Topic must be one of: {list(self.TECH_TOPICS.keys())}"}
        
        topic_info = self.TECH_TOPICS[topic]
        
        # Generate template script
        script = self._get_tech_template(topic, complexity, duration_minutes)
        
        return {
            "topic": topic_info["name"],
            "complexity": complexity,
            "script": {
                "narrative": script,
                "duration_seconds": duration_minutes * 60
            },
            "visual_suggestions": self._get_tech_visuals(topic),
            "key_points": self._get_key_points(topic),
            "tags": self._get_tech_tags(topic),
            "color_palette": "tech_modern_bright",
            "pacing": "step_by_step_detailed"
        }
    
    def _get_tech_template(self, topic: str, complexity: str, duration_minutes: int) -> str:
        templates = {
            "ai_basics": f"""
ARTIFICIAL INTELLIGENCE BASICS - A Beginner's Guide
Duration: ~{duration_minutes} minutes

[OPENING]
What is Artificial Intelligence? It sounds complex, but at its core, AI is simply machines learning from data to make decisions.
Think of it as teaching a computer to learn, just like you learn from experience.

[THE CONCEPT]
Artificial Intelligence started as a dream: can machines think? The answer is more nuanced than yes or no.
What we really mean is: can machines recognize patterns? Can they predict outcomes? Can they make useful decisions?
The answer to all three is yes.

[HOW IT WORKS]
AI learns through examples. You show it thousands of pictures of cats, and it learns to recognize cats.
You show it thousands of medical images, and it learns to detect diseases.
This process is called machine learning, and it's the foundation of modern AI.

[REAL-WORLD APPLICATIONS]
ChatGPT writes essays. Self-driving cars navigate traffic. Medical AI diagnoses diseases.
Recommendation systems suggest what you should watch next.
These aren't magic - they're all examples of AI learning from data and finding patterns.

[THE FUTURE]
AI is advancing faster than ever. But remember: AI is a tool. Like any tool, its impact depends on how we use it.
The future of AI isn't about replacing humans - it's about humans and AI working together.

[CLOSING]
AI might seem intimidating, but at its heart, it's about learning. And learning is something humans have been doing forever.

--- Duration: approximately {duration_minutes} minutes of narration ---
""",
            "neural_networks": f"""
UNDERSTANDING NEURAL NETWORKS
Duration: ~{duration_minutes} minutes

[OPENING]
Neural networks are inspired by how your brain works. Your brain has billions of neurons communicating with each other.
Artificial neural networks mimic this structure, creating powerful systems that can learn incredibly complex patterns.

[THE BIOLOGY CONNECTION]
Your brain learns through experience. Every time you learn something new, neural connections strengthen.
Artificial neural networks work similarly - they adjust internal parameters based on data, getting better with practice.

[ARCHITECTURE]
A neural network has layers: input layer (receives data), hidden layers (process information), output layer (gives results).
Data flows through these layers, getting transformed at each step.
The magic happens in the hidden layers - they automatically discover what features matter.

[TRAINING PROCESS]
Training is iterative. We show the network examples. It makes predictions. We correct it when it's wrong.
Over thousands of iterations, the network learns to map inputs to outputs accurately.

[DEEP LEARNING]
Deep learning uses many hidden layers - hence "deep" neural networks.
More layers mean the network can learn more complex patterns.
This is why deep learning has revolutionized AI in recent years.

[APPLICATIONS & IMPACT]
Neural networks power image recognition, language processing, game-playing AIs, and much more.
They've achieved superhuman performance in many domains.

[CLOSING]
Neural networks are powerful, but they're not magic. They're mathematical models that learn patterns from data.

--- Duration: approximately {duration_minutes} minutes of narration ---
"""
        }
        return templates.get(topic, "Educational content about the topic")
    
    def _get_tech_visuals(self, topic: str) -> List[str]:
        return [
            "Code on screen (syntax highlighting)",
            "Data flow diagrams",
            "Neural network visualizations",
            "Examples and demonstrations",
            "Graphs and statistics",
            "Real-world applications",
        ]
    
    def _get_key_points(self, topic: str) -> List[str]:
        return [
            f"Definition of {self.TECH_TOPICS[topic]['name']}",
            "How it works in practice",
            "Real-world examples",
            "Why it matters",
            "Getting started guide"
        ]
    
    def _get_tech_tags(self, topic: str) -> List[str]:
        return [
            "Technology", "Explained", "Tutorial", "Learning",
            "AI", "Coding", "Education", "Tech Tutorial"
        ] + self.TECH_TOPICS[topic]["keywords"]


class TutorialGenerator:
    """Generate how-to and tutorial videos"""
    
    TUTORIAL_CATEGORIES = {
        "diy_project": {
            "name": "DIY & Crafts",
            "keywords": ["DIY", "craft", "project", "build"],
            "duration": "8-20 minutes"
        },
        "cooking": {
            "name": "Cooking & Recipes",
            "keywords": ["recipe", "cooking", "food", "preparation"],
            "duration": "5-15 minutes"
        },
        "fitness": {
            "name": "Fitness & Exercise",
            "keywords": ["fitness", "workout", "exercise", "training"],
            "duration": "5-20 minutes"
        },
        "photography": {
            "name": "Photography & Videography",
            "keywords": ["photography", "camera", "technique", "lighting"],
            "duration": "10-15 minutes"
        },
        "software": {
            "name": "Software & Tech Setup",
            "keywords": ["tutorial", "software", "setup", "how-to"],
            "duration": "5-20 minutes"
        }
    }
    
    def generate_tutorial_script(
        self,
        category: str,
        title: str,
        num_steps: int = 5,
        duration_minutes: int = 12
    ) -> Dict:
        """Generate tutorial script with numbered steps"""
        
        if category not in self.TUTORIAL_CATEGORIES:
            return {"error": f"Category must be one of: {list(self.TUTORIAL_CATEGORIES.keys())}"}
        
        category_info = self.TUTORIAL_CATEGORIES[category]
        
        script = f"""
{title.upper()}
Duration: ~{duration_minutes} minutes

[OPENING]
Today I'm going to show you exactly how to {title.lower()}. This is a step-by-step guide, so follow along.
By the end of this video, you'll have completed the entire process.

[WHAT YOU'LL NEED]
Before we start, here's what you'll need:
(List of materials/tools)

[STEPS BEGIN]
"""
        
        # Add numbered steps
        for i in range(1, min(num_steps + 1, 10)):
            script += f"\n[STEP {i}]\nDescription of step {i}.\nHere's how to do it correctly.\n"
        
        script += f"""

[TIPS & TRICKS]
Here are some pro tips to make this easier:
- Tip 1 for better results
- Tip 2 for efficiency
- Tip 3 to avoid common mistakes

[FINAL RESULT]
Here's what you should have at the end. If yours looks different, check step X.

[CLOSING]
Congratulations! You've completed {title}. Now practice several times to master it.
Subscribe for more step-by-step tutorials.

--- Duration: approximately {duration_minutes} minutes of narration ---
"""
        
        return {
            "category": category_info["name"],
            "title": title,
            "script": {
                "narrative": script,
                "duration_seconds": duration_minutes * 60,
                "steps": num_steps
            },
            "structure": "step_by_step",
            "pacing": "instructional_moderate",
            "visual_suggestions": [
                "Close-up of hands doing the action",
                "Wide shot of full workspace",
                "Before/after comparison",
                "Slow motion for detailed steps",
                "Text overlay for key points",
                "Highlight important details",
            ],
            "tags": ["Tutorial", "How-To", "DIY", "Learning", "Steps"] + category_info["keywords"]
        }


class FinanceAnalysisGenerator:
    """Generate finance and investment analysis videos"""
    
    FINANCE_TOPICS = {
        "stock_analysis": {
            "name": "Stock Market Analysis",
            "keywords": ["stocks", "trading", "market", "analysis"],
            "complexity": "intermediate"
        },
        "investing_basics": {
            "name": "Investing for Beginners",
            "keywords": ["investing", "portfolio", "stocks", "bonds"],
            "complexity": "beginner"
        },
        "crypto_explained": {
            "name": "Cryptocurrency Explained",
            "keywords": ["crypto", "blockchain", "bitcoin", "ethereum"],
            "complexity": "intermediate"
        },
        "financial_planning": {
            "name": "Personal Financial Planning",
            "keywords": ["finance", "budgeting", "planning", "money"],
            "complexity": "beginner"
        }
    }
    
    def generate_finance_script(
        self,
        topic: str,
        market_data: Optional[Dict] = None,
        duration_minutes: int = 12
    ) -> Dict:
        """Generate finance analysis script"""
        
        if topic not in self.FINANCE_TOPICS:
            return {"error": f"Topic must be one of: {list(self.FINANCE_TOPICS.keys())}"}
        
        topic_info = self.FINANCE_TOPICS[topic]
        
        script = f"""
{topic_info['name'].upper()} - ANALYSIS & INSIGHTS
Duration: ~{duration_minutes} minutes

[OPENING]
In this video, we're analyzing {topic_info['name'].lower()}. This is based on current market data and research.
If you're looking to understand {topic_info['name'].lower()}, this video is for you.

[MARKET OVERVIEW]
Let's look at the current state of the market. 
(Present relevant data and trends)

[KEY INSIGHTS]
Here are the important takeaways:
1. Understanding the fundamentals
2. Analyzing the current situation
3. What experts are saying
4. Future outlook and predictions

[ANALYSIS]
Looking deeper:
- Technical analysis of current trends
- Fundamental factors affecting the market
- Comparison with historical data
- Expert opinions

[ACTIONABLE ADVICE]
What should you do with this information?
1. Consider your personal situation
2. Do your own research
3. Consult with financial advisors
4. Make informed decisions

[DISCLAIMER]
I'm not a financial advisor. This is for educational purposes only.
Always do your own research before making financial decisions.

[CLOSING]
That's the analysis for this period. Subscribe for regular market updates.

--- Duration: approximately {duration_minutes} minutes of narration ---
"""
        
        return {
            "topic": topic_info["name"],
            "complexity": topic_info["complexity"],
            "script": {
                "narrative": script,
                "duration_seconds": duration_minutes * 60
            },
            "visual_suggestions": [
                "Stock charts and graphs",
                "Market data overlays",
                "Professional analytics",
                "Timeline visualizations",
                "Comparison charts",
                "Key metric highlights"
            ],
            "tags": ["Finance", "Investment", "Analysis", "Trading"] + topic_info["keywords"],
            "color_palette": "professional_golds_grays",
            "pacing": "analytical_detailed"
        }


class TrendingCommentaryGenerator:
    """Generate trending news and commentary videos"""
    
    COMMENTARY_STYLES = {
        "news_breakdown": {
            "name": "News Breakdown",
            "keywords": ["news", "breaking", "update", "current"],
            "tone": "informative"
        },
        "viral_reaction": {
            "name": "Viral Reaction & Commentary",
            "keywords": ["reaction", "viral", "trending", "commentary"],
            "tone": "engaging"
        },
        "deep_analysis": {
            "name": "Deep Dive Analysis",
            "keywords": ["analysis", "deep-dive", "investigation"],
            "tone": "serious"
        },
        "cultural_commentary": {
            "name": "Cultural & Social Commentary",
            "keywords": ["culture", "social", "society", "commentary"],
            "tone": "opinionated"
        }
    }
    
    def generate_commentary_script(
        self,
        style: str,
        topic: str,
        duration_minutes: int = 10
    ) -> Dict:
        """Generate commentary script based on trending topic"""
        
        if style not in self.COMMENTARY_STYLES:
            return {"error": f"Style must be one of: {list(self.COMMENTARY_STYLES.keys())}"}
        
        style_info = self.COMMENTARY_STYLES[style]
        
        script = f"""
{topic.upper()} - {style_info['name'].upper()}
Duration: ~{duration_minutes} minutes

[OPENING]
So this is trending right now, and here's what everyone should know about it.
Let me break down {topic} for you.

[THE CONTEXT]
Here's the background:
- What happened
- When it happened
- Who's involved
- Why it matters

[CURRENT SITUATION]
This is where we are now:
- Latest developments
- Key facts
- Recent updates
- What changed

[ANALYSIS & PERSPECTIVE]
Here's what I think about this:
- The important details people miss
- The bigger picture
- Different perspectives
- Expert opinions

[SOCIAL IMPACT]
Why people are reacting this way:
- Emotional responses
- Community reactions
- Cultural significance
- Long-term implications

[CLOSING]
That's the situation. What do you think? Comment below.
Subscribe for more commentary on trending topics.

--- Duration: approximately {duration_minutes} minutes of narration ---
"""
        
        return {
            "style": style_info["name"],
            "topic": topic,
            "script": {
                "narrative": script,
                "duration_seconds": duration_minutes * 60
            },
            "visual_suggestions": [
                "Fast cuts between scenes",
                "B-roll supporting footage",
                "Text overlays for emphasis",
                "Screenshot annotations",
                "Reaction graphics",
                "Timeline of events"
            ],
            "tags": ["Trending", "News", "Commentary", "Opinion", "Culture"] + style_info["keywords"],
            "pacing": "fast_energetic",
            "color_palette": "vibrant_trendy"
        }


class WellnessLifestyleGenerator:
    """Generate wellness and lifestyle videos"""
    
    WELLNESS_TOPICS = {
        "fitness_routine": {
            "name": "Fitness Routines & Workouts",
            "keywords": ["fitness", "workout", "exercise", "health"],
            "duration": "10-25 minutes"
        },
        "meditation": {
            "name": "Meditation & Mindfulness",
            "keywords": ["meditation", "mindfulness", "mental health", "peace"],
            "duration": "5-20 minutes"
        },
        "nutrition": {
            "name": "Nutrition & Diet Planning",
            "keywords": ["nutrition", "diet", "healthy eating", "food"],
            "duration": "8-15 minutes"
        },
        "sleep_wellness": {
            "name": "Sleep & Rest Optimization",
            "keywords": ["sleep", "rest", "wellness", "recovery"],
            "duration": "10-20 minutes"
        },
        "self_care": {
            "name": "Self-Care & Mental Health",
            "keywords": ["self-care", "mental health", "wellness", "lifestyle"],
            "duration": "8-20 minutes"
        }
    }
    
    def generate_wellness_script(
        self,
        topic: str,
        tips_count: int = 5,
        duration_minutes: int = 15
    ) -> Dict:
        """Generate wellness content script"""
        
        if topic not in self.WELLNESS_TOPICS:
            return {"error": f"Topic must be one of: {list(self.WELLNESS_TOPICS.keys())}"}
        
        topic_info = self.WELLNESS_TOPICS[topic]
        
        script = f"""
{topic_info['name'].upper()} - YOUR GUIDE TO BETTER WELLNESS
Duration: ~{duration_minutes} minutes

[OPENING]
Taking care of your {topic} is essential for a balanced life. In this video, I'll share {tips_count} practical tips you can start today.

[WHY IT MATTERS]
Understanding the importance:
- Scientific benefits
- How it affects your life
- Long-term impact
- Your personal health

[TIP BREAKDOWN]
"""
        
        for i in range(1, tips_count + 1):
            script += f"""

[TIP {i}]
Here's tip number {i}:
- What it is
- How to do it
- Why it works
- Common mistakes to avoid
"""
        
        script += f"""

[IMPLEMENTATION]
How to start today:
- Small, manageable changes
- Building the habit
- Tracking progress
- Staying motivated

[YOUR WELLNESS JOURNEY]
Remember:
- This is personal
- Start where you are
- Progress over perfection
- Celebrate small wins

[CLOSING]
Your wellness is worth investing in. Start with one tip today.
Subscribe for more wellness guidance on your journey.

--- Duration: approximately {duration_minutes} minutes of narration ---
"""
        
        return {
            "topic": topic_info["name"],
            "script": {
                "narrative": script,
                "duration_seconds": duration_minutes * 60,
                "tips": tips_count
            },
            "visual_suggestions": [
                "Serene natural settings",
                "Demonstration footage",
                "Before/after examples",
                "Calming transitions",
                "Infographics & data",
                "Lifestyle imagery"
            ],
            "tags": ["Wellness", "Health", "Lifestyle", "Tips", "Self-Care"] + topic_info["keywords"],
            "pacing": "relaxed_mindful",
            "color_palette": "calm_wellness_greens"
        }


class SpiritualDocumentaryGenerator:
    """Generate spiritual & inspirational documentary content"""
    
    SPIRITUAL_TOPICS = {
        "wisdom_teachings": {
            "name": "Wisdom & Teachings",
            "keywords": ["wisdom", "teachings", "enlightenment", "spiritual"],
            "duration": "10-20 minutes"
        },
        "daily_affirmations": {
            "name": "Daily Affirmations & Motivation",
            "keywords": ["affirmations", "motivation", "inspiration", "mindset"],
            "duration": "5-10 minutes"
        },
        "life_lessons": {
            "name": "Life Lessons & Growth",
            "keywords": ["lessons", "growth", "personal development", "wisdom"],
            "duration": "8-18 minutes"
        },
        "ancient_wisdom": {
            "name": "Ancient Wisdom & Philosophy",
            "keywords": ["philosophy", "ancient wisdom", "teachings"],
            "duration": "10-20 minutes"
        }
    }
    
    def generate_spiritual_script(
        self,
        topic: str,
        duration_minutes: int = 15
    ) -> Dict:
        """Generate inspirational & spiritual script"""
        
        if topic not in self.SPIRITUAL_TOPICS:
            return {"error": f"Topic must be one of: {list(self.SPIRITUAL_TOPICS.keys())}"}
        
        topic_info = self.SPIRITUAL_TOPICS[topic]
        
        script = f"""
{topic_info['name'].upper()} - A JOURNEY INWARD
Duration: ~{duration_minutes} minutes

[OPENING]
Today, let's explore {topic_info['name'].lower()}. This is about discovering deeper meaning in your life.
Take a moment. Breathe. Let's begin.

[THE FOUNDATION]
Understanding the basics:
- What it means
- Why it matters
- How it affects you
- Your personal connection

[THE TEACHING]
The core message:
- The main idea
- How it applies to life
- Practical wisdom
- Timeless truths

[REFLECTION]
Let's go deeper:
- What resonates with you
- How to apply it
- Personal discoveries
- Your own wisdom

[THE PATH FORWARD]
Taking this into your life:
- Small daily practices
- Building awareness
- Deepening understanding
- Your spiritual journey

[CLOSING]
Remember this wisdom. Let it guide your path.
In the comments, share what resonates with you.
Subscribe for more spiritual guidance.

--- Duration: approximately {duration_minutes} minutes of narration ---
"""
        
        return {
            "topic": topic_info["name"],
            "script": {
                "narrative": script,
                "duration_seconds": duration_minutes * 60
            },
            "visual_suggestions": [
                "Nature scenery (mountains, water)",
                "Peaceful interiors (temples, studios)",
                "Sunrise/sunset moments",
                "Meditation imagery",
                "Symbolic elements",
                "Light effects"
            ],
            "tags": ["Spiritual", "Inspirational", "Wisdom", "Growth", "Mindfulness"] + topic_info["keywords"],
            "pacing": "slow_meditative",
            "color_palette": "calm_earth_tones"
        }


class BusinessInsightsGenerator:
    """Generate business and entrepreneurship content"""
    
    BUSINESS_TOPICS = {
        "startup_advice": {
            "name": "Startup & Entrepreneurship",
            "keywords": ["startup", "entrepreneurship", "business", "launch"],
            "expertise": "intermediate"
        },
        "leadership": {
            "name": "Leadership & Management",
            "keywords": ["leadership", "management", "team", "business"],
            "expertise": "advanced"
        },
        "marketing": {
            "name": "Marketing & Growth Strategies",
            "keywords": ["marketing", "growth", "strategy", "business"],
            "expertise": "intermediate"
        },
        "success_stories": {
            "name": "Success Stories & Case Studies",
            "keywords": ["success", "case study", "inspiration", "business"],
            "expertise": "intermediate"
        },
        "business_fundamentals": {
            "name": "Business Fundamentals",
            "keywords": ["business", "fundamentals", "learning", "basics"],
            "expertise": "beginner"
        }
    }
    
    def generate_business_script(
        self,
        topic: str,
        insights_count: int = 5,
        duration_minutes: int = 18
    ) -> Dict:
        """Generate business insight script"""
        
        if topic not in self.BUSINESS_TOPICS:
            return {"error": f"Topic must be one of: {list(self.BUSINESS_TOPICS.keys())}"}
        
        topic_info = self.BUSINESS_TOPICS[topic]
        
        script = f"""
{topic_info['name'].upper()} - EXPERT INSIGHTS
Duration: ~{duration_minutes} minutes

[OPENING]
If you want to succeed in business, you need to understand {topic_info['name'].lower()}.
I'm going to share {insights_count} key insights that will transform your approach.

[THE LANDSCAPE]
Current state of {topic}:
- Market overview
- Trends & opportunities
- Challenges & solutions
- What's changing

[INSIGHT BREAKDOWN]
"""
        
        for i in range(1, insights_count + 1):
            script += f"""

[INSIGHT {i}]
Key insight number {i}:
- What successful people do
- Why it works
- How to apply it
- Common pitfalls
"""
        
        script += f"""

[REAL-WORLD APPLICATION]
How to use these insights:
- In your business
- In your role
- Starting today
- Building momentum

[ACTIONABLE STEPS]
Here's your action plan:
1. First step to take
2. Build on that
3. Create momentum
4. Scale your results

[CLOSING]
Business success comes from applying these principles consistently.
What insight resonates most with you? Share in the comments.
Subscribe for 更多 business insights and strategies.

--- Duration: approximately {duration_minutes} minutes of narration ---
"""
        
        return {
            "topic": topic_info["name"],
            "script": {
                "narrative": script,
                "duration_seconds": duration_minutes * 60,
                "insights": insights_count
            },
            "visual_suggestions": [
                "Professional office settings",
                "Business graphics & charts",
                "Real people & interviews",
                "Key points overlays",
                "Data visualizations",
                "Success imagery"
            ],
            "tags": ["Business", "Entrepreneurship", "Strategy", "Success", "Growth"] + topic_info["keywords"],
            "pacing": "expert_paced",
            "color_palette": "professional_power_colors"
        }


# Export all generators
ALL_GENERATORS = {
    "tech_explained_animated": TechExplainedGenerator,
    "how_to_tutorial": TutorialGenerator,
    "financial_analysis": FinanceAnalysisGenerator,
    "trending_commentary": TrendingCommentaryGenerator,
    "wellness_lifestyle": WellnessLifestyleGenerator,
    "spiritual_documentary": SpiritualDocumentaryGenerator,
    "business_insights": BusinessInsightsGenerator,
}

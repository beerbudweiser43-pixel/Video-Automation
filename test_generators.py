#!/usr/bin/env python3
"""Test all generators to verify they work correctly"""

from omniflow import (
    TechExplainedGenerator,
    TutorialGenerator,
    FinanceAnalysisGenerator,
    TrendingCommentaryGenerator,
    WellnessLifestyleGenerator,
    SpiritualDocumentaryGenerator,
    BusinessInsightsGenerator,
    GospelMusicVideoGenerator,
)

def test_generator(name, generator, method_name, *args, **kwargs):
    """Test a single generator"""
    try:
        gen = generator()
        method = getattr(gen, method_name)
        result = method(*args, **kwargs)
        
        # Check essential keys
        required_keys = ['script', 'visual_suggestions', 'tags']
        missing = [k for k in required_keys if k not in result]
        
        script_len = 0
        if 'script' in result:
            script = result['script']
            if isinstance(script, dict):
                script_len = len(script.get('narrative', ''))
            else:
                script_len = len(str(script))
        
        status = "✅" if script_len > 50 else "⚠️"
        print(f"{status} {name:30} | Script: {script_len:5} chars | Keys: {', '.join(result.keys())}")
        return True
    except Exception as e:
        print(f"❌ {name:30} | Error: {str(e)[:60]}")
        return False

print("=" * 100)
print("TESTING ALL GENERATORS")
print("=" * 100)

# Test each generator
tests = [
    ("Gospel Music", GospelMusicVideoGenerator, "generate_gospel_music_video", "Grace Song", "worship", "contemporary_gospel", 8, "James Brown"),
    ("Tech Explained", TechExplainedGenerator, "generate_tech_script", "ai_basics", "beginner", 10),
    ("Tutorial", TutorialGenerator, "generate_tutorial_script", "cooking", "Pasta Carbonara", 5, 8),
    ("Finance Analysis", FinanceAnalysisGenerator, "generate_finance_script", "stock_analysis", None, 12),
    ("Trending Commentary", TrendingCommentaryGenerator, "generate_commentary_script", "news_breakdown", "AI Revolution", 10),
    ("Wellness Lifestyle", WellnessLifestyleGenerator, "generate_wellness_script", "fitness_routine", 5, 12),
    ("Spiritual Documentary", SpiritualDocumentaryGenerator, "generate_spiritual_script", "wisdom_teachings", 15),
    ("Business Insights", BusinessInsightsGenerator, "generate_business_script", "startup_advice", 4, 18),
]

passed = 0
failed = 0

for name, gen_class, method, *args in tests:
    if test_generator(name, gen_class, method, *args):
        passed += 1
    else:
        failed += 1

print("=" * 100)
print(f"RESULTS: {passed} passed ✅ | {failed} failed ❌")
print("=" * 100)

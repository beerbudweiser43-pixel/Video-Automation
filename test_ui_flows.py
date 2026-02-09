#!/usr/bin/env python3
"""
Targeted UI Test Suite
Simulates each content type generation through the Streamlit app workflow
Tests: Gospel, Tech, Tutorial, Finance, Trending, Wellness, Spiritual, Business
"""

from omniflow import (
    GospelMusicVideoGenerator,
    TechExplainedGenerator,
    TutorialGenerator,
    FinanceAnalysisGenerator,
    TrendingCommentaryGenerator,
    WellnessLifestyleGenerator,
    SpiritualDocumentaryGenerator,
    BusinessInsightsGenerator,
)

def test_gospel_flow():
    """Test Gospel Music Video Generation (simulating Sidebar + Tab workflow)"""
    print("\n" + "="*80)
    print("TEST 1: GOSPEL MUSIC GENERATION")
    print("="*80)
    
    # Sidebar Config (simulated)
    gospel_theme = "worship"
    gospel_style = "contemporary_gospel"
    gospel_duration = 6
    gospel_artist = "Grace Ministries"
    
    print(f"Sidebar Config: Theme={gospel_theme}, Style={gospel_style}, Duration={gospel_duration}min, Artist={gospel_artist}")
    
    # Tab: Generate button clicked
    gen = GospelMusicVideoGenerator()
    result = gen.generate_gospel_music_video(
        title=gospel_artist or "Gospel Music Video",
        theme=gospel_theme,
        music_style=gospel_style,
        duration_minutes=gospel_duration,
        artist_name=gospel_artist
    )
    
    # Validate result
    assert 'script' in result, "Missing 'script' key"
    assert 'visual_production' in result, "Missing 'visual_production' key"
    assert 'youtube_optimization' in result, "Missing 'youtube_optimization' key"
    
    script_len = len(result.get('script', {}).get('narrative', ''))
    print(f"✅ PASS | Script: {script_len} chars | Tags: {len(result.get('youtube_optimization', {}).get('tags', []))} tags")
    return True

def test_tech_flow():
    """Test Tech Explained Generation"""
    print("\n" + "="*80)
    print("TEST 2: TECH EXPLAINED GENERATION")
    print("="*80)
    
    # Sidebar Config
    tech_topic = "ai_basics"
    tech_complexity = "beginner"
    tech_duration = 10
    
    print(f"Sidebar Config: Topic={tech_topic}, Complexity={tech_complexity}, Duration={tech_duration}min")
    
    # Tab: Generate button clicked
    gen = TechExplainedGenerator()
    result = gen.generate_tech_script(tech_topic, tech_complexity, tech_duration)
    
    # Validate
    assert 'script' in result, "Missing 'script' key"
    assert 'visual_suggestions' in result, "Missing 'visual_suggestions' key"
    assert 'key_points' in result, "Missing 'key_points' key"
    
    script_len = len(result.get('script', ''))
    print(f"✅ PASS | Script: {script_len} chars | Visuals: {len(result.get('visual_suggestions', []))} items | Key Points: {len(result.get('key_points', []))}")
    return True

def test_tutorial_flow():
    """Test Tutorial Generation"""
    print("\n" + "="*80)
    print("TEST 3: TUTORIAL GENERATION")
    print("="*80)
    
    # Sidebar Config
    tutorial_category = "cooking"
    tutorial_title = "Simple Pasta Carbonara"
    tutorial_steps = 5
    tutorial_duration = 8
    
    print(f"Sidebar Config: Category={tutorial_category}, Title={tutorial_title}, Steps={tutorial_steps}, Duration={tutorial_duration}min")
    
    # Tab: Generate button clicked
    gen = TutorialGenerator()
    result = gen.generate_tutorial_script(tutorial_category, tutorial_title, tutorial_steps, tutorial_duration)
    
    # Validate
    assert 'script' in result, "Missing 'script' key"
    assert 'structure' in result, "Missing 'structure' key"
    assert 'visual_suggestions' in result, "Missing 'visual_suggestions' key"
    
    script_len = len(result.get('script', ''))
    print(f"✅ PASS | Script: {script_len} chars | Structure sections: {len(result.get('structure', []))} | Visuals: {len(result.get('visual_suggestions', []))}")
    return True

def test_finance_flow():
    """Test Finance Analysis Generation"""
    print("\n" + "="*80)
    print("TEST 4: FINANCE ANALYSIS GENERATION")
    print("="*80)
    
    # Sidebar Config
    finance_topic = "stock_analysis"
    finance_duration = 12
    
    print(f"Sidebar Config: Topic={finance_topic}, Duration={finance_duration}min")
    
    # Tab: Generate button clicked
    gen = FinanceAnalysisGenerator()
    result = gen.generate_finance_script(finance_topic, None, finance_duration)
    
    # Validate
    assert 'script' in result, "Missing 'script' key"
    assert 'visual_suggestions' in result, "Missing 'visual_suggestions' key"
    assert 'tags' in result, "Missing 'tags' key"
    
    script_len = len(result.get('script', ''))
    print(f"✅ PASS | Script: {script_len} chars | Visuals: {len(result.get('visual_suggestions', []))} | Tags: {len(result.get('tags', []))}")
    return True

def test_trending_flow():
    """Test Trending Commentary Generation"""
    print("\n" + "="*80)
    print("TEST 5: TRENDING COMMENTARY GENERATION")
    print("="*80)
    
    # Sidebar Config
    trending_style = "news_breakdown"
    trending_topic = "AI breakthroughs in 2026"
    trending_duration = 10
    
    print(f"Sidebar Config: Style={trending_style}, Topic={trending_topic}, Duration={trending_duration}min")
    
    # Tab: Generate button clicked
    gen = TrendingCommentaryGenerator()
    result = gen.generate_commentary_script(trending_style, trending_topic, trending_duration)
    
    # Validate
    assert 'script' in result, "Missing 'script' key"
    assert 'visual_suggestions' in result, "Missing 'visual_suggestions' key"
    assert 'pacing' in result, "Missing 'pacing' key"
    
    script_len = len(result.get('script', ''))
    print(f"✅ PASS | Script: {script_len} chars | Visuals: {len(result.get('visual_suggestions', []))} | Pacing: {result.get('pacing', 'N/A')}")
    return True

def test_wellness_flow():
    """Test Wellness Lifestyle Generation"""
    print("\n" + "="*80)
    print("TEST 6: WELLNESS LIFESTYLE GENERATION")
    print("="*80)
    
    # Sidebar Config
    wellness_topic = "fitness_routine"
    wellness_tips = 5
    wellness_duration = 12
    
    print(f"Sidebar Config: Topic={wellness_topic}, Tips={wellness_tips}, Duration={wellness_duration}min")
    
    # Tab: Generate button clicked
    gen = WellnessLifestyleGenerator()
    result = gen.generate_wellness_script(wellness_topic, wellness_tips, wellness_duration)
    
    # Validate
    assert 'script' in result, "Missing 'script' key"
    assert 'visual_suggestions' in result, "Missing 'visual_suggestions' key"
    assert 'tags' in result, "Missing 'tags' key"
    
    script_len = len(result.get('script', ''))
    print(f"✅ PASS | Script: {script_len} chars | Visuals: {len(result.get('visual_suggestions', []))} | Tags: {len(result.get('tags', []))}")
    return True

def test_spiritual_flow():
    """Test Spiritual Documentary Generation"""
    print("\n" + "="*80)
    print("TEST 7: SPIRITUAL DOCUMENTARY GENERATION")
    print("="*80)
    
    # Sidebar Config
    spiritual_topic = "wisdom_teachings"
    spiritual_duration = 15
    
    print(f"Sidebar Config: Topic={spiritual_topic}, Duration={spiritual_duration}min")
    
    # Tab: Generate button clicked
    gen = SpiritualDocumentaryGenerator()
    result = gen.generate_spiritual_script(spiritual_topic, spiritual_duration)
    
    # Validate
    assert 'script' in result, "Missing 'script' key"
    assert 'visual_suggestions' in result, "Missing 'visual_suggestions' key"
    assert 'color_palette' in result, "Missing 'color_palette' key"
    
    script_len = len(result.get('script', ''))
    print(f"✅ PASS | Script: {script_len} chars | Visuals: {len(result.get('visual_suggestions', []))} | Colors: {result.get('color_palette', 'N/A')}")
    return True

def test_business_flow():
    """Test Business Insights Generation"""
    print("\n" + "="*80)
    print("TEST 8: BUSINESS INSIGHTS GENERATION")
    print("="*80)
    
    # Sidebar Config
    business_topic = "startup_advice"
    business_insights = 4
    business_duration = 18
    
    print(f"Sidebar Config: Topic={business_topic}, Insights={business_insights}, Duration={business_duration}min")
    
    # Tab: Generate button clicked
    gen = BusinessInsightsGenerator()
    result = gen.generate_business_script(business_topic, business_insights, business_duration)
    
    # Validate
    assert 'script' in result, "Missing 'script' key"
    assert 'visual_suggestions' in result, "Missing 'visual_suggestions' key"
    assert 'tags' in result, "Missing 'tags' key"
    
    script_len = len(result.get('script', ''))
    print(f"✅ PASS | Script: {script_len} chars | Visuals: {len(result.get('visual_suggestions', []))} | Tags: {len(result.get('tags', []))}")
    return True

def main():
    """Run all UI flow tests"""
    print("\n╔═══════════════════════════════════════════════════════════════════════════════╗")
    print("║                  OMNIFLOW UI FLOW TEST SUITE                                 ║")
    print("║              Testing all 8 content generators end-to-end                     ║")
    print("╚═══════════════════════════════════════════════════════════════════════════════╝")
    
    tests = [
        ("Gospel Music", test_gospel_flow),
        ("Tech Explained", test_tech_flow),
        ("Tutorial", test_tutorial_flow),
        ("Finance Analysis", test_finance_flow),
        ("Trending Commentary", test_trending_flow),
        ("Wellness Lifestyle", test_wellness_flow),
        ("Spiritual Documentary", test_spiritual_flow),
        ("Business Insights", test_business_flow),
    ]
    
    passed = 0
    failed = 0
    errors = []
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
        except Exception as e:
            failed += 1
            errors.append((test_name, str(e)))
            print(f"❌ FAIL | {test_name}: {e}")
    
    # Summary
    print("\n" + "="*80)
    print("TEST SUMMARY")
    print("="*80)
    print(f"Total Tests: {len(tests)}")
    print(f"Passed: {passed} ✅")
    print(f"Failed: {failed} ❌")
    
    if errors:
        print("\nFailures:")
        for test_name, error in errors:
            print(f"  - {test_name}: {error}")
    else:
        print("\n🎉 ALL TESTS PASSED!")
    
    print("="*80)
    
    return failed == 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)

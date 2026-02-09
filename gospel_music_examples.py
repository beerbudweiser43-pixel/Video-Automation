"""
Gospel Music Video Examples
Ready-to-use templates for creating instant Gospel music videos

These examples show common Gospel music video configurations that perform well on YouTube
"""

from omniflow import GospelMusicVideoGenerator

# Initialize the generator
generator = GospelMusicVideoGenerator()

# ============================================================================
# EXAMPLE 1: HIGH-ENERGY PRAISE & CELEBRATION
# ============================================================================
def example_praise_celebration():
    """
    HIGH-ENERGY PRAISE VIDEO (5 minutes)
    Perfect for: Events, celebrations, joy-focused content
    Target audience: General audience, all ages
    Expected performance: High engagement, shares
    """
    return generator.generate_gospel_music_video(
        title="Joy Unspeakable - Gospel Celebration",
        theme="praise_celebration",
        music_style="contemporary_gospel",
        duration_minutes=5,
        artist_name="Joy Gospel Ministry"
    )

# ============================================================================
# EXAMPLE 2: EMOTIONAL REDEMPTION STORY
# ============================================================================
def example_redemption_deep():
    """
    EMOTIONAL REDEMPTION VIDEO (9 minutes)
    Perfect for: Testimonies, transformation stories, emotional content
    Target audience: Spiritual seekers, people in struggle
    Expected performance: High watch time, comments
    """
    return generator.generate_gospel_music_video(
        title="From Darkness to Light - A Redemption Story",
        theme="redemption",
        music_style="soul_gospel",
        duration_minutes=9,
        artist_name="Grace Redemption Ministry"
    )

# ============================================================================
# EXAMPLE 3: PEACEFUL WORSHIP MEDITATION
# ============================================================================
def example_worship_meditation():
    """
    PEACEFUL WORSHIP VIDEO (8 minutes)
    Perfect for: Meditation, prayer, bedtime content
    Target audience: Spiritual seekers, prayer warriors
    Expected performance: High retention, watch till end
    """
    return generator.generate_gospel_music_video(
        title="Still My Soul - Peaceful Gospel Worship",
        theme="worship",
        music_style="spiritual_ambient",
        duration_minutes=8,
        artist_name="Stillness Gospel"
    )

# ============================================================================
# EXAMPLE 4: TRADITIONAL HYMN ARRANGEMENT
# ============================================================================
def example_traditional_hymn():
    """
    TRADITIONAL HYMN VIDEO (6 minutes)
    Perfect for: Church content, hymn arrangements, traditional audience
    Target audience: Mature Christians, church community
    Expected performance: Community building, loyalty
    """
    return generator.generate_gospel_music_video(
        title="Amazing Grace - Traditional Gospel Arrangement",
        theme="faith",
        music_style="traditional_gospel",
        duration_minutes=6,
        artist_name="Traditional Gospel Choir"
    )

# ============================================================================
# EXAMPLE 5: SPIRITUAL JOURNEY DOCUMENTARY
# ============================================================================
def example_spiritual_journey():
    """
    SPIRITUAL JOURNEY VIDEO (10 minutes)
    Perfect for: Life stories, documentary content, transformation arcs
    Target audience: Spiritual seekers, people on journeys
    Expected performance: High engagement, shares, comments
    """
    return generator.generate_gospel_music_video(
        title="My Spiritual Journey - From Seeker to Believer",
        theme="spiritual_journey",
        music_style="soul_gospel",
        duration_minutes=10,
        artist_name="Spiritual Journey Productions"
    )

# ============================================================================
# EXAMPLE 6: QUICK FAITH ENCOURAGEMENT
# ============================================================================
def example_faith_short():
    """
    QUICK FAITH ENCOURAGEMENT (4 minutes)
    Perfect for: Daily encouragement, shorts series, viral potential
    Target audience: Busy people, social media users
    Expected performance: Very high shares, viral potential
    """
    return generator.generate_gospel_music_video(
        title="Daily Faith: Trust the Process",
        theme="faith",
        music_style="contemporary_gospel",
        duration_minutes=4,
        artist_name="Daily Faith Ministries"
    )

# ============================================================================
# EXAMPLE 7: BIBLICAL STORY WITH DRAMA
# ============================================================================
def example_biblical_story():
    """
    BIBLICAL STORY VIDEO (10 minutes)
    Perfect for: Bible teaching, story-based content, educational
    Target audience: Christians, Bible students, families
    Expected performance: Long watch time, subscriptions
    """
    return generator.generate_gospel_music_video(
        title="The Prodigal's Return - Biblical Narrative",
        theme="biblical_stories",
        music_style="soul_gospel",
        duration_minutes=10,
        artist_name="Bible Stories Gospel"
    )

# ============================================================================
# EXAMPLE 8: MODERN GOSPEL WITH ENERGY
# ============================================================================
def example_modern_worship():
    """
    MODERN GOSPEL VIDEO (7 minutes)
    Perfect for: Younger audience, contemporary churches, music videos
    Target audience: Gen Z, Millennials, contemporary worshippers
    Expected performance: High engagement, social shares
    """
    return generator.generate_gospel_music_video(
        title="Modern Gospel Worship - What You've Done",
        theme="worship",
        music_style="contemporary_gospel",
        duration_minutes=7,
        artist_name="Modern Gospel Movement"
    )

# ============================================================================
# EXAMPLE 9: PRAYER & FAITH MEDITATION
# ============================================================================
def example_prayer_faith():
    """
    PRAYER & FAITH VIDEO (9 minutes)
    Perfect for: Prayer warriors, meditation, spiritual practice
    Target audience: Prayer warriors, contemplatives
    Expected performance: High completion rate, repeat views
    """
    return generator.generate_gospel_music_video(
        title="Prayer & Faith - Deep Spiritual Practice",
        theme="faith",
        music_style="spiritual_ambient",
        duration_minutes=9,
        artist_name="Prayer & Faith Ministry"
    )

# ============================================================================
# EXAMPLE 10: CELEBRATORY VICTORY ANTHEM
# ============================================================================
def example_victory_anthem():
    """
    VICTORY ANTHEM VIDEO (6 minutes)
    Perfect for: Celebrations, victories, announcements
    Target audience: Community members, celebration seekers
    Expected performance: Community engagement, comments
    """
    return generator.generate_gospel_music_video(
        title="Victory in Jesus - Celebratory Gospel Anthem",
        theme="praise_celebration",
        music_style="soul_gospel",
        duration_minutes=6,
        artist_name="Victory Gospel Ministries"
    )

# ============================================================================
# EXAMPLE 11: GRACE HYMN SERIES
# ============================================================================
def example_grace_hymn_series():
    """
    GRACE HYMN VIDEO (7 minutes)
    Perfect for: Hymn series, traditional + spiritual fusion
    Target audience: All-age audience, hymn lovers
    Expected performance: Steady views, build series
    """
    return generator.generate_gospel_music_video(
        title="Grace Hymns - Grace That Saves",
        theme="redemption",
        music_style="traditional_gospel",
        duration_minutes=7,
        artist_name="Grace Hymns Collection"
    )

# ============================================================================
# EXAMPLE 12: YOUTH GOSPEL VIBES
# ============================================================================
def example_youth_gospel():
    """
    YOUTH GOSPEL VIDEO (5 minutes)
    Perfect for: Youth ministry, Gen Z engagement, trending content
    Target audience: Teenagers, young adults, youth groups
    Expected performance: High engagement, shares
    """
    return generator.generate_gospel_music_video(
        title="Youth Gospel - Faith for Gen Z",
        theme="faith",
        music_style="contemporary_gospel",
        duration_minutes=5,
        artist_name="Youth Gospel Movement"
    )

# ============================================================================
# USAGE INSTRUCTIONS
# ============================================================================
"""
HOW TO USE THESE EXAMPLES:

1. DIRECT GENERATION:
   
   from gospel_music_examples import example_praise_celebration
   
   plan = example_praise_celebration()
   script = plan['script']['narrative']
   tags = plan['youtube_optimization']['tags']
   
2. MODIFY ANY EXAMPLE:
   
   plan = example_redemption_deep()
   
   # Change artist name
   plan['artist'] = "Your Ministry Name"
   
   # Change title
   plan['title'] = "Your Custom Title"
   
3. CREATE ALL EXAMPLES:
   
   from gospel_music_examples import (
       example_praise_celebration,
       example_redemption_deep,
       example_worship_meditation,
       # ... etc
   )
   
   examples = [
       example_praise_celebration(),
       example_redemption_deep(),
       example_worship_meditation(),
       # ... etc
   ]
   
   for example in examples:
       print(f"Generated: {example['title']}")

4. USE IN STREAMLIT:
   
   import streamlit as st
   from gospel_music_examples import *
   
   if st.button("Load Example"):
       plan = example_praise_celebration()
       st.session_state.gospel_plan = plan

RECOMMENDATIONS:

For Building a Channel:
- Monday: example_praise_celebration (to start week high-energy)
- Wednesday: example_redemption_deep (mid-week deep connection)
- Friday: example_worship_meditation (weekend peace)

For Quick Viral Content:
- Use example_faith_short (4 min, high shares)
- Use example_victory_anthem (6 min, celebratory)

For Series Building:
- Use example_biblical_story (episodic content)
- Use example_grace_hymn_series (hymn series)
- Use example_spiritual_journey (documentary series)

For Growing Fast:
- Mix themes weekly
- Rotate music styles
- Consistent upload schedule
- Reply to comments
- Use trending Gospel songs

"""

# ============================================================================
# QUICK REFERENCE TABLE
# ============================================================================
EXAMPLE_SUMMARY = {
    "praise_celebration": {
        "title": "Joy Unspeakable",
        "duration": 5,
        "energy": "⚡⚡⚡ Very High",
        "emotion": "🎉 Celebratory",
        "audience": "Everyone",
        "viral_potential": "Very High",
        "best_day": "Monday/Friday",
        "function": "example_praise_celebration"
    },
    "redemption_deep": {
        "title": "From Darkness to Light",
        "duration": 9,
        "energy": "⚡ Medium",
        "emotion": "💔 Emotional",
        "audience": "Seekers",
        "viral_potential": "High",
        "best_day": "Wednesday/Thursday",
        "function": "example_redemption_deep"
    },
    "worship_meditation": {
        "title": "Still My Soul",
        "duration": 8,
        "energy": "🕯️ Calm",
        "emotion": "🙏 Peaceful",
        "audience": "Spiritual Seekers",
        "viral_potential": "Medium-High",
        "best_day": "Anytime",
        "function": "example_worship_meditation"
    },
    "traditional_hymn": {
        "title": "Amazing Grace",
        "duration": 6,
        "energy": "⚡⚡ Moderate",
        "emotion": "💙 Classic",
        "audience": "Mature Christians",
        "viral_potential": "Medium",
        "best_day": "Sunday",
        "function": "example_traditional_hymn"
    },
    "spiritual_journey": {
        "title": "My Spiritual Journey",
        "duration": 10,
        "energy": "⚡⚡ Moderate-High",
        "emotion": "✨ Inspiring",
        "audience": "Everyone",
        "viral_potential": "Very High",
        "best_day": "Any",
        "function": "example_spiritual_journey"
    },
    "faith_short": {
        "title": "Daily Faith: Trust",
        "duration": 4,
        "energy": "⚡⚡⚡ High",
        "emotion": "💪 Empowering",
        "audience": "Everyone",
        "viral_potential": "Very High (Shorts/Reels)",
        "best_day": "Daily",
        "function": "example_faith_short"
    },
    "biblical_story": {
        "title": "The Prodigal's Return",
        "duration": 10,
        "energy": "⚡⚡ Moderate",
        "emotion": "📖 Narrative",
        "audience": "Christians/Students",
        "viral_potential": "High",
        "best_day": "Sunday/Monday",
        "function": "example_biblical_story"
    },
    "modern_worship": {
        "title": "Modern Gospel Worship",
        "duration": 7,
        "energy": "⚡⚡⚡ High",
        "emotion": "🎸 Contemporary",
        "audience": "Gen Z/Millennials",
        "viral_potential": "Very High",
        "best_day": "Any",
        "function": "example_modern_worship"
    },
    "prayer_faith": {
        "title": "Prayer & Faith",
        "duration": 9,
        "energy": "🕯️ Calm-Moderate",
        "emotion": "🙏 Contemplative",
        "audience": "Prayer Warriors",
        "viral_potential": "Medium-High",
        "best_day": "Anytime",
        "function": "example_prayer_faith"
    },
    "victory_anthem": {
        "title": "Victory in Jesus",
        "duration": 6,
        "energy": "⚡⚡⚡ Very High",
        "emotion": "🏆 Victorious",
        "audience": "Community",
        "viral_potential": "Very High",
        "best_day": "Any",
        "function": "example_victory_anthem"
    }
}

if __name__ == "__main__":
    print("🎵 Gospel Music Video Examples")
    print("=" * 50)
    print("\nQuick Summary:")
    print("-" * 50)
    
    for key, info in EXAMPLE_SUMMARY.items():
        print(f"\n{info['title']}")
        print(f"  Duration: {info['duration']} min")
        print(f"  Energy: {info['energy']}")
        print(f"  Viral Potential: {info['viral_potential']}")
        print(f"  Function: {info['function']}")
    
    print("\n" + "=" * 50)
    print("To use examples:")
    print("from gospel_music_examples import example_praise_celebration")
    print("plan = example_praise_celebration()")

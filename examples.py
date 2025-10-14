#!/usr/bin/env python3
"""
Example script demonstrating how to use the CS Learning Agent programmatically.

This script shows different ways to use the learning agent in your own applications.
"""

from learning_agent import CSLearningAgent, CSTopicInfo
from datetime import datetime


def example_basic_usage():
    """Example 1: Basic usage - discover topics and generate lectures."""
    print("🔥 Example 1: Basic Usage")
    print("=" * 50)
    
    # Initialize the learning agent
    agent = CSLearningAgent()
    
    # Discover trending topics
    print("📋 Discovering trending topics...")
    topics = agent.discover_topics(limit=3)
    
    # Generate a lecture for the first topic
    if topics:
        print(f"\n🎓 Generating lecture for: {topics[0].title}")
        lecture = agent.generate_lecture_for_topic(topics[0])
        
        # Export as markdown
        markdown_content = agent.export_lecture(lecture, "markdown")
        
        # Save to file
        filename = f"example_lecture_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"✅ Lecture saved to: {filename}")
    
    print("\n" + "=" * 50 + "\n")


def example_custom_topic():
    """Example 2: Generate lecture for a custom topic."""
    print("🔥 Example 2: Custom Topic")
    print("=" * 50)
    
    agent = CSLearningAgent()
    
    # Create a custom topic
    custom_topic = CSTopicInfo(
        title="Quantum Computing Fundamentals",
        description="Introduction to quantum computing principles, qubits, and quantum algorithms",
        category="Emerging Technologies",
        source="Custom Example",
        relevance_score=0.95,
        date_found=datetime.now().strftime("%Y-%m-%d")
    )
    
    print(f"🎓 Generating lecture for custom topic: {custom_topic.title}")
    
    # Generate lecture
    lecture = agent.generate_lecture_for_topic(custom_topic)
    
    # Display lecture info
    print(f"📖 Topic: {lecture.topic}")
    print(f"⏱️ Duration: {lecture.estimated_duration}")
    print(f"📊 Difficulty: {lecture.difficulty_level}")
    print(f"🎯 Key Concepts: {len(lecture.key_concepts)}")
    print(f"💡 Examples: {len(lecture.examples)}")
    
    print("\n" + "=" * 50 + "\n")


def example_full_session():
    """Example 3: Run a complete learning session."""
    print("🔥 Example 3: Full Learning Session")
    print("=" * 50)
    
    agent = CSLearningAgent()
    
    # Run complete session
    print("🚀 Running full learning session...")
    results = agent.run_full_session(num_topics=2)
    
    # Display results
    print(f"📊 Session Results:")
    print(f"   - Topics discovered: {results.get('topics_discovered', 0)}")
    print(f"   - Lectures generated: {results.get('lectures_generated', 0)}")
    print(f"   - Session date: {results.get('session_date', 'N/A')}")
    
    # Export all lectures
    if 'lectures' in results:
        print(f"\n💾 Exporting {len(results['lectures'])} lectures...")
        for title, lecture in results['lectures'].items():
            # Clean title for filename
            safe_title = "".join(c if c.isalnum() or c in (' ', '-', '_') else '' for c in title)
            safe_title = safe_title.replace(' ', '_').lower()
            filename = f"session_lecture_{safe_title}.md"
            
            content = agent.export_lecture(lecture, "markdown")
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"   ✅ Exported: {filename}")
    
    print("\n" + "=" * 50 + "\n")


def example_multiple_formats():
    """Example 4: Export lectures in multiple formats."""
    print("🔥 Example 4: Multiple Export Formats")
    print("=" * 50)
    
    agent = CSLearningAgent()
    
    # Get a topic and generate lecture
    topics = agent.discover_topics(limit=1)
    if not topics:
        print("❌ No topics found for this example")
        return
    
    topic = topics[0]
    print(f"🎓 Generating lecture for: {topic.title}")
    lecture = agent.generate_lecture_for_topic(topic)
    
    # Export in multiple formats
    formats = ['markdown', 'txt', 'html']
    
    for fmt in formats:
        print(f"💾 Exporting as {fmt.upper()}...")
        content = agent.export_lecture(lecture, fmt)
        
        # Save to file
        filename = f"multi_format_lecture.{fmt}"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"   ✅ Saved: {filename}")
    
    print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    print("🤖 CS Learning Agent - Examples")
    print("=" * 60)
    print()
    
    # Run all examples
    try:
        example_basic_usage()
        example_custom_topic()
        example_full_session()
        example_multiple_formats()
        
        print("🎉 All examples completed successfully!")
        print("\nGenerated files:")
        print("- Various lecture files in markdown, txt, and html formats")
        print("- Check the current directory for exported lectures")
        
    except Exception as e:
        print(f"❌ Error running examples: {e}")
        import traceback
        traceback.print_exc()
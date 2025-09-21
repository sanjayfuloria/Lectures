#!/usr/bin/env python3
"""
Student Agent Examples
======================

This script demonstrates various ways to use the Student Agent
for different learning scenarios.
"""

import os
from student_agent import StudentAgent


def example_basic_questions():
    """Example of asking basic subject questions."""
    print("📚 Example 1: Basic Subject Questions")
    print("=" * 40)
    
    agent = StudentAgent()
    
    questions = [
        "What is the difference between mitosis and meiosis?",
        "Can you explain Newton's first law of motion?",
        "How do I solve quadratic equations?",
        "What caused World War I?"
    ]
    
    for question in questions:
        print(f"Q: {question}")
        response = agent.ask(question)
        print(f"A: {response}\n")


def example_study_help():
    """Example of getting study tips and techniques."""
    print("📖 Example 2: Study Tips and Techniques")
    print("=" * 40)
    
    agent = StudentAgent()
    
    # Get general study tips
    tips = agent.get_study_tips("mathematics")
    print(f"Math Study Tips:\n{tips}\n")
    
    # Get concept explanation
    explanation = agent.explain_concept("photosynthesis", "beginner")
    print(f"Photosynthesis Explanation:\n{explanation}\n")


def example_homework_guidance():
    """Example of getting homework guidance (not direct answers)."""
    print("✏️ Example 3: Homework Guidance")
    print("=" * 40)
    
    agent = StudentAgent()
    
    homework_questions = [
        "I need to write an essay about climate change. Can you help me get started?",
        "I'm stuck on this algebra problem: 2x + 5 = 15. Can you guide me through the steps?",
        "I have to memorize the periodic table. What's the best approach?"
    ]
    
    for question in homework_questions:
        print(f"Student: {question}")
        response = agent.ask(question)
        print(f"Agent: {response}\n")


def example_conversation_flow():
    """Example of a flowing conversation with follow-up questions."""
    print("💭 Example 4: Conversation Flow")
    print("=" * 40)
    
    agent = StudentAgent()
    
    # Start with a topic
    response1 = agent.ask("I'm having trouble understanding fractions")
    print(f"Student: I'm having trouble understanding fractions")
    print(f"Agent: {response1}\n")
    
    # Follow up with more specific question
    response2 = agent.ask("Can you show me how to add fractions with different denominators?")
    print(f"Student: Can you show me how to add fractions with different denominators?")
    print(f"Agent: {response2}\n")
    
    # Ask for practice
    response3 = agent.ask("Can you give me a practice problem?")
    print(f"Student: Can you give me a practice problem?")
    print(f"Agent: {response3}\n")


def main():
    """Run all examples."""
    # Check for API key first
    if not os.getenv('OPENAI_API_KEY'):
        print("⚠️  Please set your OPENAI_API_KEY environment variable")
        print("   Example: export OPENAI_API_KEY='your-api-key-here'")
        print("   You can get an API key from: https://platform.openai.com/api-keys")
        return
    
    print("🎓 Student Agent Examples")
    print("This demo shows how the agent can help students learn!\n")
    
    try:
        # Run examples
        example_basic_questions()
        input("Press Enter to continue to the next example...")
        
        example_study_help()
        input("Press Enter to continue to the next example...")
        
        example_homework_guidance()
        input("Press Enter to continue to the next example...")
        
        example_conversation_flow()
        
        print("✨ Demo complete! The agent is ready to help students learn.")
        
    except Exception as e:
        print(f"❌ Error running examples: {e}")
        print("Make sure your OpenAI API key is valid and you have internet connection.")


if __name__ == "__main__":
    main()
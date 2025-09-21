#!/usr/bin/env python3
"""
Simple Student Learning Agent
=============================

A neat and simple agent that demonstrates how easy it is to build an AI agent
for educational purposes using the OpenAI API.

This agent can help students with:
- Answering questions about various subjects
- Explaining concepts in simple terms
- Providing study tips
- Helping with homework (guidance, not direct answers)
"""

import os
import openai
from typing import List, Dict
import json


class StudentAgent:
    """
    A simple AI agent designed to help students learn effectively.
    
    This agent uses OpenAI's API to provide educational assistance while
    maintaining a helpful and encouraging tone suitable for students.
    """
    
    def __init__(self, api_key: str = None):
        """
        Initialize the Student Agent.
        
        Args:
            api_key (str): OpenAI API key. If not provided, will look for
                          OPENAI_API_KEY environment variable.
        """
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass it directly.")
        
        # Set up OpenAI client
        openai.api_key = self.api_key
        
        # Agent personality and behavior
        self.system_prompt = """You are a helpful, patient, and encouraging AI tutor for students. 
        Your goal is to help students learn and understand concepts rather than just providing direct answers.
        
        Guidelines:
        - Be encouraging and positive
        - Explain concepts clearly and simply
        - Ask follow-up questions to check understanding
        - Provide hints and guidance rather than direct homework answers
        - Suggest study techniques when appropriate
        - Keep responses concise but thorough
        """
        
        # Store conversation history
        self.conversation_history: List[Dict[str, str]] = []
    
    def ask(self, question: str) -> str:
        """
        Ask the agent a question and get a helpful response.
        
        Args:
            question (str): The student's question
            
        Returns:
            str: The agent's response
        """
        try:
            # Add user question to conversation history
            self.conversation_history.append({"role": "user", "content": question})
            
            # Prepare messages for API call
            messages = [{"role": "system", "content": self.system_prompt}]
            messages.extend(self.conversation_history[-10:])  # Keep last 10 messages for context
            
            # Call OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )
            
            # Extract and store the response
            agent_response = response.choices[0].message.content.strip()
            self.conversation_history.append({"role": "assistant", "content": agent_response})
            
            return agent_response
            
        except Exception as e:
            return f"I'm sorry, I encountered an error: {str(e)}. Please try again."
    
    def get_study_tips(self, subject: str = "general") -> str:
        """
        Get study tips for a specific subject or general study advice.
        
        Args:
            subject (str): The subject to get study tips for
            
        Returns:
            str: Study tips and advice
        """
        question = f"Can you give me some effective study tips for {subject}?"
        return self.ask(question)
    
    def explain_concept(self, concept: str, level: str = "beginner") -> str:
        """
        Ask the agent to explain a concept at a specific level.
        
        Args:
            concept (str): The concept to explain
            level (str): The level of explanation (beginner, intermediate, advanced)
            
        Returns:
            str: Explanation of the concept
        """
        question = f"Can you explain {concept} at a {level} level? Please use simple examples."
        return self.ask(question)
    
    def clear_history(self):
        """Clear the conversation history to start fresh."""
        self.conversation_history = []
    
    def save_conversation(self, filename: str):
        """
        Save the current conversation to a file.
        
        Args:
            filename (str): The filename to save to
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.conversation_history, f, indent=2)
            print(f"Conversation saved to {filename}")
        except Exception as e:
            print(f"Error saving conversation: {e}")


def main():
    """
    Demo function showing how to use the Student Agent.
    """
    print("🎓 Student Learning Agent Demo")
    print("=" * 40)
    
    # Check for API key
    if not os.getenv('OPENAI_API_KEY'):
        print("⚠️  Please set your OPENAI_API_KEY environment variable")
        print("   Example: export OPENAI_API_KEY='your-api-key-here'")
        return
    
    try:
        # Create the agent
        agent = StudentAgent()
        print("✅ Agent initialized successfully!")
        print()
        
        # Demo interactions
        demo_questions = [
            "What is photosynthesis?",
            "How can I remember the order of operations in math?",
            "What are some good study techniques for preparing for exams?"
        ]
        
        for i, question in enumerate(demo_questions, 1):
            print(f"Demo Question {i}: {question}")
            response = agent.ask(question)
            print(f"Agent Response: {response}")
            print("-" * 40)
        
        # Interactive mode
        print("\n🎯 Interactive Mode - Ask me anything! (type 'quit' to exit)")
        while True:
            user_input = input("\nYour question: ").strip()
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("👋 Thanks for using the Student Agent! Keep learning!")
                break
            elif user_input:
                response = agent.ask(user_input)
                print(f"Agent: {response}")
    
    except ValueError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
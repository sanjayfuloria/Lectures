#!/usr/bin/env python3
"""
Simple tests for Student Agent
===============================

Basic tests to verify the agent structure and functionality.
"""

import os
import sys
import tempfile
import json

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_agent_initialization():
    """Test that the agent can be initialized with proper error handling."""
    from student_agent import StudentAgent
    
    # Test without API key (should raise ValueError)
    try:
        agent = StudentAgent()
        print("❌ Should have raised ValueError for missing API key")
        return False
    except ValueError as e:
        if "API key is required" in str(e):
            print("✅ Proper error handling for missing API key")
        else:
            print(f"❌ Unexpected error message: {e}")
            return False
    
    # Test with dummy API key (should initialize)
    try:
        agent = StudentAgent(api_key="dummy-key-for-testing")
        print("✅ Agent initializes with API key")
        return True
    except Exception as e:
        print(f"❌ Failed to initialize with API key: {e}")
        return False

def test_conversation_history():
    """Test conversation history functionality."""
    from student_agent import StudentAgent
    
    try:
        agent = StudentAgent(api_key="dummy-key")
        
        # Test initial state
        if len(agent.conversation_history) == 0:
            print("✅ Initial conversation history is empty")
        else:
            print("❌ Initial conversation history should be empty")
            return False
        
        # Test clear history
        agent.conversation_history.append({"role": "user", "content": "test"})
        agent.clear_history()
        if len(agent.conversation_history) == 0:
            print("✅ Clear history works")
        else:
            print("❌ Clear history failed")
            return False
        
        return True
    except Exception as e:
        print(f"❌ Conversation history test failed: {e}")
        return False

def test_save_conversation():
    """Test saving conversation functionality."""
    from student_agent import StudentAgent
    
    try:
        agent = StudentAgent(api_key="dummy-key")
        agent.conversation_history = [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there!"}
        ]
        
        # Test saving to temporary file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            temp_filename = f.name
        
        agent.save_conversation(temp_filename)
        
        # Verify file contents
        with open(temp_filename, 'r') as f:
            saved_data = json.load(f)
        
        if saved_data == agent.conversation_history:
            print("✅ Save conversation works")
            os.unlink(temp_filename)  # Clean up
            return True
        else:
            print("❌ Saved conversation doesn't match")
            os.unlink(temp_filename)
            return False
    
    except Exception as e:
        print(f"❌ Save conversation test failed: {e}")
        return False

def test_examples_import():
    """Test that examples module imports correctly."""
    try:
        import examples
        print("✅ Examples module imports successfully")
        return True
    except Exception as e:
        print(f"❌ Examples import failed: {e}")
        return False

def test_setup_import():
    """Test that setup module imports correctly."""
    try:
        import setup
        print("✅ Setup module imports successfully")
        return True
    except Exception as e:
        print(f"❌ Setup import failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🧪 Running Student Agent Tests")
    print("=" * 40)
    
    tests = [
        test_agent_initialization,
        test_conversation_history, 
        test_save_conversation,
        test_examples_import,
        test_setup_import
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        print(f"\nRunning {test.__name__}...")
        if test():
            passed += 1
        else:
            print(f"❌ {test.__name__} failed")
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The agent structure is working correctly.")
        return True
    else:
        print("⚠️  Some tests failed. Please check the implementation.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
#!/usr/bin/env python3
"""
Setup Script for Student Agent
===============================

This script helps students set up the Student Agent environment.
"""

import os
import subprocess
import sys


def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required.")
        print(f"   Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True


def install_requirements():
    """Install required packages."""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages. Please check your internet connection.")
        return False


def setup_environment():
    """Help user set up environment variables."""
    print("\n🔑 Setting up environment variables...")
    
    if os.path.exists('.env'):
        print("✅ .env file already exists")
    else:
        if os.path.exists('.env.example'):
            # Copy example file
            with open('.env.example', 'r') as f:
                content = f.read()
            with open('.env', 'w') as f:
                f.write(content)
            print("✅ Created .env file from template")
        else:
            # Create basic .env file
            with open('.env', 'w') as f:
                f.write("OPENAI_API_KEY=your_openai_api_key_here\n")
            print("✅ Created basic .env file")
    
    # Check if API key is set
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key or api_key == 'your_openai_api_key_here':
        print("\n⚠️  Please set your OpenAI API key:")
        print("   1. Get an API key from: https://platform.openai.com/api-keys")
        print("   2. Edit the .env file and replace 'your_openai_api_key_here' with your actual key")
        print("   OR")
        print("   3. Set environment variable: export OPENAI_API_KEY='your-key-here'")
        return False
    else:
        print("✅ OpenAI API key is set")
        return True


def run_quick_test():
    """Run a quick test of the agent."""
    print("\n🧪 Running quick test...")
    try:
        from student_agent import StudentAgent
        agent = StudentAgent()
        response = agent.ask("Hello! Can you introduce yourself?")
        print(f"✅ Test successful! Agent response: {response[:100]}...")
        return True
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False


def main():
    """Main setup function."""
    print("🎓 Student Agent Setup")
    print("=" * 30)
    
    # Check Python version
    if not check_python_version():
        return
    
    # Install requirements
    if not install_requirements():
        return
    
    # Setup environment
    env_ok = setup_environment()
    
    # Run test if environment is ready
    if env_ok:
        if run_quick_test():
            print("\n🎉 Setup complete! You're ready to use the Student Agent.")
            print("\nNext steps:")
            print("1. Run: python student_agent.py (for interactive mode)")
            print("2. Run: python examples.py (to see examples)")
        else:
            print("\n⚠️  Setup completed but test failed. Please check your API key.")
    else:
        print("\n⚠️  Setup completed but API key needs to be configured.")
    
    print("\nFor help, check the README.md file!")


if __name__ == "__main__":
    main()
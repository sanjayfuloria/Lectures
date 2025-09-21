# Lectures
This repository will have my lecture demos

## 🎓 Student Learning Agent

A simple and neat AI agent that demonstrates how easy it is to build an educational agent for students using the OpenAI API. This agent helps students learn by providing explanations, study tips, and guidance rather than direct answers.

### ✨ Features

- **Educational Focus**: Designed specifically to help students learn and understand concepts
- **Encouraging Tone**: Provides positive, patient responses that motivate learning
- **Study Guidance**: Offers study tips and techniques tailored to different subjects
- **Concept Explanations**: Breaks down complex topics into understandable explanations
- **Homework Help**: Provides guidance and hints rather than direct answers
- **Conversation Memory**: Maintains context throughout the conversation
- **Easy to Use**: Simple API with clear examples

### 🚀 Quick Start

1. **Setup the environment:**
   ```bash
   python setup.py
   ```

2. **Get your OpenAI API key:**
   - Visit [OpenAI API Keys](https://platform.openai.com/api-keys)
   - Create a new API key
   - Set it in your `.env` file or environment variable

3. **Run the agent:**
   ```bash
   # Interactive mode
   python student_agent.py
   
   # See examples
   python examples.py
   ```

### 📖 Usage Examples

#### Basic Usage
```python
from student_agent import StudentAgent

# Create an agent
agent = StudentAgent()

# Ask questions
response = agent.ask("What is photosynthesis?")
print(response)

# Get study tips
tips = agent.get_study_tips("mathematics")
print(tips)

# Explain concepts
explanation = agent.explain_concept("gravity", "beginner")
print(explanation)
```

#### Interactive Conversation
```python
agent = StudentAgent()

# The agent remembers context
agent.ask("I'm learning about fractions")
agent.ask("How do I add them?")
agent.ask("Can you give me a practice problem?")
```

### 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sanjayfuloria/Lectures.git
   cd Lectures
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key:**
   ```bash
   # Option 1: Environment variable
   export OPENAI_API_KEY='your-api-key-here'
   
   # Option 2: Create .env file
   cp .env.example .env
   # Edit .env file with your API key
   ```

### 📁 Project Structure

```
Lectures/
├── student_agent.py      # Main agent class
├── examples.py           # Usage examples
├── setup.py             # Setup script
├── requirements.txt     # Python dependencies
├── .env.example        # Environment template
└── README.md           # This file
```

### 🎯 Educational Philosophy

This agent is designed with educational best practices in mind:

- **Socratic Method**: Asks follow-up questions to encourage thinking
- **Scaffolding**: Provides hints and guidance rather than direct answers
- **Positive Reinforcement**: Uses encouraging language to build confidence
- **Differentiated Learning**: Adapts explanations to different skill levels
- **Active Learning**: Encourages students to engage with the material

### 🔧 Configuration

You can customize the agent behavior by modifying the environment variables:

```bash
OPENAI_API_KEY=your_api_key_here
AGENT_MODEL=gpt-3.5-turbo          # OpenAI model to use
AGENT_MAX_TOKENS=500               # Maximum response length
AGENT_TEMPERATURE=0.7              # Response creativity (0-1)
```

### 🎓 For Educators

This project serves as an excellent example for students learning about:

- **AI Integration**: How to use AI APIs in practical applications
- **Clean Code**: Well-structured, documented Python code
- **User Experience**: Designing AI interactions for specific audiences
- **Educational Technology**: Building tools that enhance learning

### 🤝 Contributing

This is a lecture demonstration repository. Feel free to:

- Fork the project for your own learning
- Suggest improvements via issues
- Share your own educational agent variations

### 📝 License

This project is intended for educational purposes. Please ensure you comply with OpenAI's usage policies when using their API.

### 🆘 Troubleshooting

**Common Issues:**

1. **API Key Error**: Make sure your OpenAI API key is correctly set
2. **Import Error**: Run `pip install -r requirements.txt`
3. **Connection Error**: Check your internet connection
4. **Rate Limits**: OpenAI has rate limits; wait a moment and try again

**Need Help?**
- Check the examples in `examples.py`
- Run the setup script: `python setup.py`
- Review OpenAI's documentation: [https://platform.openai.com/docs](https://platform.openai.com/docs)

---

*This project demonstrates how simple it is to build powerful educational tools with AI. The focus is on clean, understandable code that students can learn from and build upon.*

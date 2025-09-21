# CS Learning Agent 🤖📚

An intelligent learning agent for Computer Science Engineering courses that automatically discovers trending CS topics and generates comprehensive, detailed lectures on those topics.

## 🌟 Features

- **🔍 Topic Discovery**: Automatically searches for the latest and most relevant Computer Science topics
- **🎓 Lecture Generation**: Creates detailed, structured lectures with:
  - Comprehensive introductions
  - Main content sections with explanations
  - Practical code examples
  - Key concepts summary
  - Real-world applications
  - Further reading recommendations
- **📊 Multiple Difficulty Levels**: Adapts content complexity based on topic
- **💾 Export Options**: Save lectures in Markdown, HTML, or plain text formats
- **🖥️ CLI Interface**: Easy-to-use command-line interface
- **🎯 Interactive Mode**: Step-by-step guided experience

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/sanjayfuloria/Lectures.git
cd Lectures
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Set up environment variables for enhanced features:
```bash
cp .env.example .env
# Edit .env file with your API keys if needed
```

### Quick Usage

#### 🔍 Discover Trending Topics
```bash
python cli.py discover --topics 5
```

#### 🎓 Run Complete Learning Session
```bash
python cli.py session --topics 3 --export-all
```

#### 🤖 Interactive Mode
```bash
python cli.py interactive
```

## 📖 Detailed Usage

### Command Line Interface

The CLI provides several commands to interact with the learning agent:

#### 1. Topic Discovery
Discover trending Computer Science topics:
```bash
python cli.py discover --topics 10
```

#### 2. Learning Session
Run a complete session that discovers topics and generates lectures:
```bash
# Basic session
python cli.py session --topics 5

# Export all lectures as Markdown files
python cli.py session --topics 3 --export-all --format markdown

# Export as HTML
python cli.py session --topics 2 --export-all --format html
```

#### 3. Interactive Mode
Launch interactive mode for guided experience:
```bash
python cli.py interactive
```

### Programmatic Usage

You can also use the learning agent directly in your Python code:

```python
from learning_agent import CSLearningAgent

# Initialize the agent
agent = CSLearningAgent()

# Discover trending topics
topics = agent.discover_topics(limit=5)

# Generate a lecture for a specific topic
if topics:
    lecture = agent.generate_lecture_for_topic(topics[0])
    
    # Export the lecture
    markdown_content = agent.export_lecture(lecture, format="markdown")
    
    # Save to file
    with open("my_lecture.md", "w") as f:
        f.write(markdown_content)

# Run a complete session
results = agent.run_full_session(num_topics=3)
print(f"Generated {results['lectures_generated']} lectures!")
```

## 📚 Example Topics Covered

The learning agent covers a wide range of current Computer Science topics:

- **🤖 Artificial Intelligence & Machine Learning**
  - Neural Networks and Deep Learning
  - Natural Language Processing
  - Computer Vision
  - Reinforcement Learning

- **☁️ Cloud Computing & Systems**
  - Microservices Architecture
  - Container Orchestration (Docker, Kubernetes)
  - Distributed Systems Design
  - DevOps and CI/CD

- **🔒 Cybersecurity**
  - Network Security
  - Ethical Hacking
  - Cryptography
  - Security Best Practices

- **💻 Software Engineering**
  - Design Patterns
  - Software Architecture
  - Code Quality and Testing
  - Agile Methodologies

- **📊 Data Science & Analytics**
  - Big Data Processing
  - Database Design
  - Data Visualization
  - Statistical Analysis

## 📁 Output Structure

Generated lectures are saved in the `lectures/` directory with the following structure:

```
lectures/
├── lecture_machine_learning_fundamentals_20241201_143022.md
├── lecture_cloud_computing_systems_20241201_143045.md
└── lecture_cybersecurity_basics_20241201_143108.md
```

Each lecture file contains:
- **Introduction**: Engaging overview of the topic
- **Main Content**: Detailed sections with explanations
- **Code Examples**: Practical, runnable code snippets
- **Key Concepts**: Important points to remember
- **Applications**: Real-world use cases
- **Further Reading**: Additional resources

## 🛠️ Configuration

### Environment Variables

You can enhance the learning agent with optional API keys:

```bash
# .env file
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_SEARCH_API_KEY=your_google_api_key_here
GOOGLE_SEARCH_ENGINE_ID=your_custom_search_engine_id
```

### Customization

The learning agent is designed to be easily customizable:

- **Add new topic sources**: Modify the `TopicSearcher` class
- **Customize lecture templates**: Update the `LectureGenerator` class
- **Add new export formats**: Extend the export methods
- **Modify difficulty assessment**: Update the difficulty determination logic

## 🧪 Examples

### Example 1: Generated Lecture Structure

```markdown
# Machine Learning and Deep Learning Fundamentals

**Duration:** 90-120 minutes  
**Difficulty Level:** Advanced

## Introduction to Machine Learning and Deep Learning Fundamentals

Welcome to today's lecture on Machine Learning and Deep Learning Fundamentals! 
In our rapidly evolving digital world, artificial intelligence has become one of 
the most transformative forces in technology...

## 1. Fundamentals of Machine Learning

### What is Machine Learning?
Machine Learning is a subset of artificial intelligence that enables computers 
to learn and improve from experience without being explicitly programmed...

## 💻 Practical Examples

### Example 1: Simple Linear Regression
```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Create and train model
model = LinearRegression()
model.fit(X, y)
```

## 🎯 Key Concepts to Remember
- Supervised vs Unsupervised Learning
- Neural Network Architecture
- Gradient Descent Optimization
...
```

### Example 2: Topic Discovery Output

```
🔥 Trending CS Topics
┏━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Rank ┃ Topic                                       ┃ Category             ┃ Relevance  ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ 1    │ Machine Learning and Deep Learning          │ Artificial           │ 0.9/1.0    │
│      │ Fundamentals                                │ Intelligence         │            │
│ 2    │ Cloud Computing and Distributed Systems     │ Systems Engineering  │ 0.9/1.0    │
│ 3    │ Cybersecurity and Ethical Hacking          │ Security             │ 0.9/1.0    │
└──────┴─────────────────────────────────────────────┴──────────────────────┴────────────┘
```

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

1. **Add new topic sources**: Implement additional web scrapers or API integrations
2. **Improve lecture templates**: Enhance the content generation algorithms
3. **Add new export formats**: Support for LaTeX, PDF, or presentation formats
4. **Enhance CLI**: Add more interactive features and options
5. **Add tests**: Write unit tests for better reliability

### Development Setup

1. Fork the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install development dependencies:
```bash
pip install -r requirements.txt
```
4. Make your changes and test them
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/sanjayfuloria/Lectures/issues) page
2. Create a new issue with detailed description
3. Contact the maintainer

## 🙏 Acknowledgments

- Built with Python and Rich for beautiful CLI output
- Inspired by the need for up-to-date CS education
- Thanks to the open-source community for excellent libraries

---

**Happy Learning! 🎓✨**

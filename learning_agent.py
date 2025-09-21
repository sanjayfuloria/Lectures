#!/usr/bin/env python3
"""
Computer Science Learning Agent

A learning agent that searches for the latest Computer Science topics and generates
detailed lectures on those topics. This tool helps educators and students stay
up-to-date with current trends in Computer Science education.

Features:
- Search for trending CS topics from multiple sources
- Generate detailed lecture content with explanations
- Organize content into structured lessons
- Export lectures in multiple formats

Author: CS Learning Assistant
"""

import requests
import json
import time
import os
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime
import logging
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.markdown import Markdown


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

console = Console()


@dataclass
class CSTopicInfo:
    """Data class to hold information about a CS topic."""
    title: str
    description: str
    category: str
    source: str
    url: Optional[str] = None
    relevance_score: float = 0.0
    date_found: str = ""


@dataclass
class LectureContent:
    """Data class to hold lecture content."""
    topic: str
    introduction: str
    main_content: List[str]
    examples: List[str]
    key_concepts: List[str]
    practical_applications: List[str]
    further_reading: List[str]
    difficulty_level: str
    estimated_duration: str


class TopicSearcher:
    """Handles searching for the latest Computer Science topics."""
    
    def __init__(self):
        self.search_sources = [
            "https://arxiv.org/list/cs/recent",
            "https://news.ycombinator.com",
            "https://stackoverflow.com/questions/tagged/computer-science",
        ]
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def search_trending_topics(self, limit: int = 10) -> List[CSTopicInfo]:
        """
        Search for trending Computer Science topics from various sources.
        
        Args:
            limit: Maximum number of topics to return
            
        Returns:
            List of CSTopicInfo objects containing topic information
        """
        topics = []
        
        # Search predefined CS topics (fallback when internet search isn't available)
        fallback_topics = self._get_fallback_cs_topics()
        topics.extend(fallback_topics)
        
        # Try to search online sources
        try:
            online_topics = self._search_online_sources()
            topics.extend(online_topics)
        except Exception as e:
            logger.warning(f"Online search failed: {e}. Using fallback topics.")
        
        # Remove duplicates and limit results
        unique_topics = self._remove_duplicates(topics)
        return unique_topics[:limit]
    
    def _get_fallback_cs_topics(self) -> List[CSTopicInfo]:
        """Return a list of current and important CS topics as fallback."""
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        topics = [
            CSTopicInfo(
                title="Machine Learning and Deep Learning Fundamentals",
                description="Understanding neural networks, supervised and unsupervised learning, and modern ML frameworks",
                category="Artificial Intelligence",
                source="CS Curriculum 2024",
                relevance_score=0.95,
                date_found=current_date
            ),
            CSTopicInfo(
                title="Cloud Computing and Distributed Systems",
                description="Microservices architecture, containerization with Docker and Kubernetes, and cloud platforms",
                category="Systems Engineering",
                source="Industry Trends 2024",
                relevance_score=0.92,
                date_found=current_date
            ),
            CSTopicInfo(
                title="Cybersecurity and Ethical Hacking",
                description="Network security, encryption, penetration testing, and security best practices",
                category="Security",
                source="Security Trends 2024",
                relevance_score=0.90,
                date_found=current_date
            ),
            CSTopicInfo(
                title="Data Structures and Algorithms Optimization",
                description="Advanced algorithms, complexity analysis, and optimization techniques for large-scale systems",
                category="Computer Science Fundamentals",
                source="Academic Standards",
                relevance_score=0.88,
                date_found=current_date
            ),
            CSTopicInfo(
                title="Web Development with Modern Frameworks",
                description="React, Vue.js, Node.js, and full-stack development with modern JavaScript/TypeScript",
                category="Web Development",
                source="Developer Survey 2024",
                relevance_score=0.85,
                date_found=current_date
            ),
            CSTopicInfo(
                title="DevOps and CI/CD Pipelines",
                description="Continuous integration, deployment automation, monitoring, and infrastructure as code",
                category="Software Engineering",
                source="Industry Best Practices",
                relevance_score=0.83,
                date_found=current_date
            ),
            CSTopicInfo(
                title="Blockchain and Distributed Ledger Technology",
                description="Cryptocurrency, smart contracts, consensus algorithms, and decentralized applications",
                category="Emerging Technologies",
                source="Technology Trends",
                relevance_score=0.80,
                date_found=current_date
            ),
            CSTopicInfo(
                title="Mobile Application Development",
                description="Cross-platform development with React Native, Flutter, and native iOS/Android development",
                category="Mobile Development",
                source="Mobile Trends 2024",
                relevance_score=0.78,
                date_found=current_date
            ),
            CSTopicInfo(
                title="Database Design and Big Data Analytics",
                description="SQL and NoSQL databases, data warehousing, ETL processes, and analytics tools",
                category="Data Science",
                source="Data Engineering Trends",
                relevance_score=0.75,
                date_found=current_date
            ),
            CSTopicInfo(
                title="Software Architecture and Design Patterns",
                description="SOLID principles, design patterns, microservices, and scalable system design",
                category="Software Engineering",
                source="Engineering Best Practices",
                relevance_score=0.73,
                date_found=current_date
            )
        ]
        
        return topics
    
    def _search_online_sources(self) -> List[CSTopicInfo]:
        """Search online sources for trending topics (placeholder for actual implementation)."""
        # This would contain actual web scraping logic
        # For now, returning empty list as we have good fallback topics
        return []
    
    def _remove_duplicates(self, topics: List[CSTopicInfo]) -> List[CSTopicInfo]:
        """Remove duplicate topics based on title similarity."""
        unique_topics = []
        seen_titles = set()
        
        for topic in topics:
            title_lower = topic.title.lower()
            if title_lower not in seen_titles:
                unique_topics.append(topic)
                seen_titles.add(title_lower)
        
        return sorted(unique_topics, key=lambda x: x.relevance_score, reverse=True)


class LectureGenerator:
    """Generates detailed lecture content for Computer Science topics."""
    
    def __init__(self):
        self.content_templates = {
            "introduction": self._generate_introduction,
            "main_content": self._generate_main_content,
            "examples": self._generate_examples,
            "practical_applications": self._generate_applications,
            "further_reading": self._generate_further_reading
        }
    
    def generate_lecture(self, topic: CSTopicInfo) -> LectureContent:
        """
        Generate a comprehensive lecture for the given topic.
        
        Args:
            topic: CSTopicInfo object containing topic details
            
        Returns:
            LectureContent object with structured lecture material
        """
        console.print(f"🎓 Generating lecture for: [bold blue]{topic.title}[/bold blue]")
        
        lecture = LectureContent(
            topic=topic.title,
            introduction=self._generate_introduction(topic),
            main_content=self._generate_main_content(topic),
            examples=self._generate_examples(topic),
            key_concepts=self._extract_key_concepts(topic),
            practical_applications=self._generate_applications(topic),
            further_reading=self._generate_further_reading(topic),
            difficulty_level=self._determine_difficulty(topic),
            estimated_duration=self._estimate_duration(topic)
        )
        
        return lecture
    
    def _generate_introduction(self, topic: CSTopicInfo) -> str:
        """Generate an engaging introduction for the topic."""
        intros = {
            "Artificial Intelligence": f"""
# Introduction to {topic.title}

Welcome to today's lecture on {topic.title}! In our rapidly evolving digital world, 
artificial intelligence has become one of the most transformative forces in technology. 
This topic sits at the intersection of computer science, mathematics, and cognitive science, 
offering exciting opportunities to solve complex real-world problems.

## Why This Topic Matters

{topic.description}

Today's session will provide you with both theoretical foundations and practical insights 
that are essential for modern software engineers and data scientists.
            """,
            "Systems Engineering": f"""
# Introduction to {topic.title}

In today's lecture, we'll explore {topic.title}, a critical area of computer science 
that focuses on building and managing complex, scalable systems. As software applications 
grow in complexity and user base, understanding system design becomes crucial for any 
software engineer.

## Learning Objectives

By the end of this lecture, you will understand:
- {topic.description}
- How these concepts apply to real-world software systems
- Best practices used by leading technology companies

## Topic Overview

{topic.description}
            """,
            "default": f"""
# Introduction to {topic.title}

Welcome to our comprehensive lecture on {topic.title}. This topic represents an 
important area of study in computer science, with applications spanning across 
multiple industries and domains.

## What We'll Cover Today

{topic.description}

This lecture is designed to provide both theoretical understanding and practical 
knowledge that you can apply in your future projects and career.
            """
        }
        
        return intros.get(topic.category, intros["default"]).strip()
    
    def _generate_main_content(self, topic: CSTopicInfo) -> List[str]:
        """Generate the main content sections for the lecture."""
        content_map = {
            "Machine Learning and Deep Learning Fundamentals": [
                "## 1. Fundamentals of Machine Learning\n\n### What is Machine Learning?\nMachine Learning is a subset of artificial intelligence that enables computers to learn and improve from experience without being explicitly programmed. It focuses on developing algorithms that can access data and use it to learn for themselves.",
                
                "## 2. Types of Machine Learning\n\n### Supervised Learning\n- Uses labeled training data\n- Learns mapping from inputs to outputs\n- Examples: Classification, Regression\n\n### Unsupervised Learning\n- Works with unlabeled data\n- Finds hidden patterns\n- Examples: Clustering, Dimensionality Reduction\n\n### Reinforcement Learning\n- Learns through interaction with environment\n- Uses rewards and penalties\n- Examples: Game AI, Robotics",
                
                "## 3. Neural Networks and Deep Learning\n\n### Basic Neural Network Structure\n- Input Layer: Receives data\n- Hidden Layers: Process information\n- Output Layer: Produces results\n\n### Deep Learning\n- Uses multi-layer neural networks\n- Automatically extracts features\n- Powerful for complex pattern recognition",
                
                "## 4. Popular ML Frameworks\n\n### TensorFlow\n- Google's open-source platform\n- Excellent for production deployment\n- Supports both research and production\n\n### PyTorch\n- Facebook's framework\n- Dynamic computation graphs\n- Popular in research community\n\n### Scikit-learn\n- Great for traditional ML algorithms\n- Easy to use and well-documented\n- Perfect for beginners"
            ],
            
            "Cloud Computing and Distributed Systems": [
                "## 1. Introduction to Cloud Computing\n\n### Definition and Core Concepts\nCloud computing is the delivery of computing services—including servers, storage, databases, networking, software, analytics, and intelligence—over the Internet ('the cloud') to offer faster innovation, flexible resources, and economies of scale.",
                
                "## 2. Cloud Service Models\n\n### Infrastructure as a Service (IaaS)\n- Provides virtualized computing resources\n- Examples: AWS EC2, Google Compute Engine\n- Users manage OS, middleware, runtime\n\n### Platform as a Service (PaaS)\n- Provides computing platform and solution stack\n- Examples: Heroku, Google App Engine\n- Users focus on application development\n\n### Software as a Service (SaaS)\n- Complete software solution\n- Examples: Gmail, Salesforce, Office 365\n- Users access software through web browser",
                
                "## 3. Distributed Systems Architecture\n\n### Microservices Architecture\n- Breaks applications into small, independent services\n- Each service handles specific business function\n- Services communicate via APIs\n- Benefits: Scalability, flexibility, technology diversity\n\n### Containerization\n- Packages applications with dependencies\n- Docker containers provide isolation\n- Kubernetes orchestrates container deployment\n- Enables consistent deployment across environments",
                
                "## 4. Distributed System Challenges\n\n### CAP Theorem\n- Consistency: All nodes see same data simultaneously\n- Availability: System remains operational\n- Partition Tolerance: System continues despite network failures\n- Can only guarantee two of three properties\n\n### Data Consistency Models\n- Strong Consistency: All reads get most recent write\n- Eventual Consistency: System will become consistent over time\n- Weak Consistency: No guarantees about when data will be consistent"
            ],
            
            "default": [
                f"## 1. Understanding {topic.title}\n\n{topic.description}\n\nThis section provides the foundational knowledge you need to understand the core concepts and principles.",
                
                f"## 2. Key Components and Architecture\n\nEvery system in {topic.category.lower()} has fundamental components that work together. Understanding these building blocks is essential for mastering the subject.",
                
                f"## 3. Implementation Strategies\n\nLet's explore different approaches to implementing solutions in {topic.title}. We'll cover best practices and common patterns used by industry professionals.",
                
                f"## 4. Tools and Technologies\n\nModern development in {topic.category.lower()} relies on various tools and frameworks. We'll examine the most important ones and when to use them."
            ]
        }
        
        return content_map.get(topic.title, content_map["default"])
    
    def _generate_examples(self, topic: CSTopicInfo) -> List[str]:
        """Generate practical examples for the topic."""
        examples_map = {
            "Machine Learning and Deep Learning Fundamentals": [
                "### Example 1: Simple Linear Regression\n```python\nfrom sklearn.linear_model import LinearRegression\nimport numpy as np\n\n# Sample data\nX = np.array([[1], [2], [3], [4], [5]])\ny = np.array([2, 4, 6, 8, 10])\n\n# Create and train model\nmodel = LinearRegression()\nmodel.fit(X, y)\n\n# Make prediction\nprediction = model.predict([[6]])\nprint(f'Prediction for x=6: {prediction[0]}')\n```",
                
                "### Example 2: Image Classification with Neural Networks\n```python\nimport tensorflow as tf\nfrom tensorflow.keras import layers, models\n\n# Build a simple CNN\nmodel = models.Sequential([\n    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),\n    layers.MaxPooling2D((2, 2)),\n    layers.Conv2D(64, (3, 3), activation='relu'),\n    layers.MaxPooling2D((2, 2)),\n    layers.Flatten(),\n    layers.Dense(64, activation='relu'),\n    layers.Dense(10, activation='softmax')\n])\n\n# Compile the model\nmodel.compile(optimizer='adam',\n              loss='sparse_categorical_crossentropy',\n              metrics=['accuracy'])\n```"
            ],
            
            "Cloud Computing and Distributed Systems": [
                "### Example 1: Docker Container Setup\n```dockerfile\n# Dockerfile for a Python web application\nFROM python:3.9-slim\n\nWORKDIR /app\n\nCOPY requirements.txt .\nRUN pip install -r requirements.txt\n\nCOPY . .\n\nEXPOSE 8000\n\nCMD ['python', 'app.py']\n```\n\n```bash\n# Build and run the container\ndocker build -t my-web-app .\ndocker run -p 8000:8000 my-web-app\n```",
                
                "### Example 2: Kubernetes Deployment\n```yaml\n# deployment.yaml\napiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: web-app-deployment\nspec:\n  replicas: 3\n  selector:\n    matchLabels:\n      app: web-app\n  template:\n    metadata:\n      labels:\n        app: web-app\n    spec:\n      containers:\n      - name: web-app\n        image: my-web-app:latest\n        ports:\n        - containerPort: 8000\n```"
            ],
            
            "default": [
                f"### Practical Example 1\nHere's a hands-on example demonstrating key concepts from {topic.title}. This example shows how to implement basic functionality using industry-standard approaches.",
                
                f"### Code Implementation\n```python\n# Example implementation for {topic.title}\n# This demonstrates core concepts in action\n\ndef main():\n    print('Implementing {topic.title}')\n    # Implementation details would go here\n    pass\n\nif __name__ == '__main__':\n    main()\n```"
            ]
        }
        
        return examples_map.get(topic.title, examples_map["default"])
    
    def _extract_key_concepts(self, topic: CSTopicInfo) -> List[str]:
        """Extract key concepts that students should remember."""
        concepts_map = {
            "Machine Learning and Deep Learning Fundamentals": [
                "Supervised vs Unsupervised Learning",
                "Neural Network Architecture",
                "Gradient Descent Optimization",
                "Overfitting and Regularization",
                "Feature Engineering",
                "Model Evaluation Metrics",
                "Cross-Validation",
                "Bias-Variance Tradeoff"
            ],
            
            "Cloud Computing and Distributed Systems": [
                "Scalability and Elasticity",
                "Microservices Architecture",
                "Container Orchestration",
                "Load Balancing",
                "CAP Theorem",
                "Eventual Consistency",
                "Service Discovery",
                "Circuit Breaker Pattern"
            ],
            
            "default": [
                f"Core principles of {topic.title}",
                f"Best practices in {topic.category}",
                "Industry standards and patterns",
                "Common challenges and solutions",
                "Performance considerations",
                "Security implications"
            ]
        }
        
        return concepts_map.get(topic.title, concepts_map["default"])
    
    def _generate_applications(self, topic: CSTopicInfo) -> List[str]:
        """Generate practical applications of the topic."""
        applications_map = {
            "Machine Learning and Deep Learning Fundamentals": [
                "**Healthcare**: Medical image analysis, drug discovery, personalized treatment plans",
                "**Finance**: Fraud detection, algorithmic trading, credit scoring, risk assessment",
                "**Transportation**: Autonomous vehicles, route optimization, predictive maintenance",
                "**E-commerce**: Recommendation systems, demand forecasting, price optimization",
                "**Entertainment**: Content recommendation, game AI, music generation",
                "**Manufacturing**: Quality control, predictive maintenance, supply chain optimization"
            ],
            
            "Cloud Computing and Distributed Systems": [
                "**Netflix**: Global content delivery using microservices and cloud infrastructure",
                "**Uber**: Real-time ride matching and routing using distributed systems",
                "**Spotify**: Music streaming service with global scalability",
                "**Airbnb**: Booking platform handling millions of users worldwide",
                "**Banking**: Online banking systems requiring high availability and security",
                "**E-learning**: Educational platforms serving students globally"
            ],
            
            "default": [
                f"Industry applications of {topic.title}",
                f"Real-world use cases in {topic.category}",
                "Commercial implementations",
                "Open source projects",
                "Research applications"
            ]
        }
        
        return applications_map.get(topic.title, applications_map["default"])
    
    def _generate_further_reading(self, topic: CSTopicInfo) -> List[str]:
        """Generate additional reading resources."""
        reading_map = {
            "Machine Learning and Deep Learning Fundamentals": [
                "**Books**: 'Hands-On Machine Learning' by Aurélien Géron",
                "**Books**: 'Deep Learning' by Ian Goodfellow, Yoshua Bengio, and Aaron Courville",
                "**Online**: Coursera Machine Learning Course by Andrew Ng",
                "**Online**: Fast.ai Practical Deep Learning Course",
                "**Documentation**: Scikit-learn User Guide",
                "**Papers**: 'Attention Is All You Need' (Transformer Architecture)",
                "**Websites**: Machine Learning Mastery by Jason Brownlee"
            ],
            
            "Cloud Computing and Distributed Systems": [
                "**Books**: 'Designing Data-Intensive Applications' by Martin Kleppmann",
                "**Books**: 'Building Microservices' by Sam Newman",
                "**Documentation**: AWS Architecture Center",
                "**Documentation**: Kubernetes Official Documentation",
                "**Online**: Google Cloud Architecture Framework",
                "**Papers**: 'MapReduce: Simplified Data Processing on Large Clusters'",
                "**Websites**: High Scalability blog"
            ],
            
            "default": [
                f"Official documentation for {topic.title}",
                "Recommended textbooks",
                "Online courses and tutorials",
                "Industry whitepapers",
                "Open source project documentation"
            ]
        }
        
        return reading_map.get(topic.title, reading_map["default"])
    
    def _determine_difficulty(self, topic: CSTopicInfo) -> str:
        """Determine the difficulty level of the topic."""
        difficulty_keywords = {
            "beginner": ["fundamentals", "introduction", "basics", "overview"],
            "intermediate": ["design", "architecture", "implementation", "optimization"],
            "advanced": ["distributed", "scalability", "machine learning", "deep learning", "security"]
        }
        
        title_lower = topic.title.lower()
        description_lower = topic.description.lower()
        
        for level, keywords in difficulty_keywords.items():
            if any(keyword in title_lower or keyword in description_lower for keyword in keywords):
                return level.capitalize()
        
        return "Intermediate"
    
    def _estimate_duration(self, topic: CSTopicInfo) -> str:
        """Estimate lecture duration based on topic complexity."""
        if "fundamentals" in topic.title.lower() or "introduction" in topic.title.lower():
            return "90-120 minutes"
        elif "advanced" in topic.title.lower() or "distributed" in topic.title.lower():
            return "120-150 minutes"
        else:
            return "60-90 minutes"


class CSLearningAgent:
    """Main class that coordinates topic search and lecture generation."""
    
    def __init__(self):
        self.topic_searcher = TopicSearcher()
        self.lecture_generator = LectureGenerator()
        console.print("[bold green]🤖 CS Learning Agent Initialized![/bold green]")
    
    def discover_topics(self, limit: int = 5) -> List[CSTopicInfo]:
        """
        Discover trending Computer Science topics.
        
        Args:
            limit: Number of topics to discover
            
        Returns:
            List of discovered topics
        """
        console.print(f"🔍 Searching for {limit} trending CS topics...")
        topics = self.topic_searcher.search_trending_topics(limit)
        
        if topics:
            console.print(f"✅ Found {len(topics)} trending topics!")
            self._display_topics_table(topics)
        else:
            console.print("❌ No topics found.")
        
        return topics
    
    def generate_lecture_for_topic(self, topic: CSTopicInfo) -> LectureContent:
        """
        Generate a detailed lecture for a specific topic.
        
        Args:
            topic: The topic to generate a lecture for
            
        Returns:
            Generated lecture content
        """
        return self.lecture_generator.generate_lecture(topic)
    
    def run_full_session(self, num_topics: int = 3) -> Dict[str, Any]:
        """
        Run a complete learning session: discover topics and generate lectures.
        
        Args:
            num_topics: Number of topics to process
            
        Returns:
            Dictionary containing session results
        """
        console.print(Panel.fit(
            "[bold blue]🎓 Starting CS Learning Session[/bold blue]\n"
            f"Discovering {num_topics} trending topics and generating detailed lectures",
            title="CS Learning Agent"
        ))
        
        # Step 1: Discover topics
        topics = self.discover_topics(num_topics)
        
        if not topics:
            return {"error": "No topics discovered"}
        
        # Step 2: Generate lectures for each topic
        lectures = {}
        for i, topic in enumerate(topics, 1):
            console.print(f"\n📚 Processing topic {i}/{len(topics)}")
            lecture = self.generate_lecture_for_topic(topic)
            lectures[topic.title] = lecture
            
            # Display lecture summary
            self._display_lecture_summary(lecture)
        
        console.print("\n🎉 [bold green]Learning session completed successfully![/bold green]")
        
        return {
            "topics_discovered": len(topics),
            "lectures_generated": len(lectures),
            "topics": topics,
            "lectures": lectures,
            "session_date": datetime.now().isoformat()
        }
    
    def export_lecture(self, lecture: LectureContent, format: str = "markdown") -> str:
        """
        Export lecture content in specified format.
        
        Args:
            lecture: The lecture content to export
            format: Export format ('markdown', 'txt', 'html')
            
        Returns:
            Formatted lecture content as string
        """
        if format.lower() == "markdown":
            return self._export_as_markdown(lecture)
        elif format.lower() == "txt":
            return self._export_as_text(lecture)
        elif format.lower() == "html":
            return self._export_as_html(lecture)
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    def _display_topics_table(self, topics: List[CSTopicInfo]):
        """Display discovered topics in a formatted table."""
        table = Table(title="🔥 Trending CS Topics")
        table.add_column("Rank", style="cyan", no_wrap=True)
        table.add_column("Topic", style="bold blue")
        table.add_column("Category", style="green")
        table.add_column("Relevance", style="yellow")
        
        for i, topic in enumerate(topics, 1):
            relevance = f"{topic.relevance_score:.1f}/1.0"
            table.add_row(str(i), topic.title, topic.category, relevance)
        
        console.print(table)
    
    def _display_lecture_summary(self, lecture: LectureContent):
        """Display a summary of the generated lecture."""
        summary = f"""
[bold]📖 Lecture: {lecture.topic}[/bold]
[yellow]⏱️  Duration:[/yellow] {lecture.estimated_duration}
[yellow]📊 Difficulty:[/yellow] {lecture.difficulty_level}
[yellow]🎯 Key Concepts:[/yellow] {len(lecture.key_concepts)} concepts covered
[yellow]💡 Examples:[/yellow] {len(lecture.examples)} practical examples
[yellow]🔗 Applications:[/yellow] {len(lecture.practical_applications)} real-world uses
        """
        
        console.print(Panel(summary.strip(), title="Lecture Generated", border_style="green"))
    
    def _export_as_markdown(self, lecture: LectureContent) -> str:
        """Export lecture as Markdown format."""
        md_content = [
            f"# {lecture.topic}\n",
            f"**Duration:** {lecture.estimated_duration}  ",
            f"**Difficulty Level:** {lecture.difficulty_level}\n",
            lecture.introduction,
            "\n---\n"
        ]
        
        # Add main content
        for section in lecture.main_content:
            md_content.append(section + "\n")
        
        # Add examples
        if lecture.examples:
            md_content.append("# 💻 Practical Examples\n")
            for example in lecture.examples:
                md_content.append(example + "\n")
        
        # Add key concepts
        if lecture.key_concepts:
            md_content.append("# 🎯 Key Concepts to Remember\n")
            for concept in lecture.key_concepts:
                md_content.append(f"- {concept}")
            md_content.append("\n")
        
        # Add applications
        if lecture.practical_applications:
            md_content.append("# 🌍 Real-World Applications\n")
            for app in lecture.practical_applications:
                md_content.append(f"- {app}")
            md_content.append("\n")
        
        # Add further reading
        if lecture.further_reading:
            md_content.append("# 📚 Further Reading\n")
            for reading in lecture.further_reading:
                md_content.append(f"- {reading}")
            md_content.append("\n")
        
        return "\n".join(md_content)
    
    def _export_as_text(self, lecture: LectureContent) -> str:
        """Export lecture as plain text format."""
        # Convert markdown to plain text (simplified)
        md_content = self._export_as_markdown(lecture)
        # Remove markdown formatting (simplified)
        text_content = md_content.replace("#", "").replace("**", "").replace("*", "")
        return text_content
    
    def _export_as_html(self, lecture: LectureContent) -> str:
        """Export lecture as HTML format."""
        # This is a simplified HTML export
        # In a real implementation, you might use a markdown-to-HTML converter
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{lecture.topic}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        h1 {{ color: #2c3e50; }}
        h2 {{ color: #34495e; }}
        code {{ background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px; }}
        pre {{ background-color: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }}
    </style>
</head>
<body>
    <h1>{lecture.topic}</h1>
    <p><strong>Duration:</strong> {lecture.estimated_duration}</p>
    <p><strong>Difficulty:</strong> {lecture.difficulty_level}</p>
    
    {lecture.introduction.replace('\n', '<br>')}
    
    <hr>
    
    <!-- Main content would be rendered here -->
    <p><em>Full HTML rendering would include all lecture sections...</em></p>
</body>
</html>
        """
        return html_content


if __name__ == "__main__":
    # Example usage
    agent = CSLearningAgent()
    
    # Run a complete learning session
    results = agent.run_full_session(num_topics=3)
    
    # Export the first lecture as markdown
    if "lectures" in results and results["lectures"]:
        first_lecture = list(results["lectures"].values())[0]
        markdown_content = agent.export_lecture(first_lecture, "markdown")
        
        # Save to file
        filename = f"lecture_{first_lecture.topic.replace(' ', '_').lower()}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        console.print(f"\n💾 Lecture exported to: [bold green]{filename}[/bold green]")
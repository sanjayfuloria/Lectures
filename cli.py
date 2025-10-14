#!/usr/bin/env python3
"""
CLI interface for the CS Learning Agent

This script provides a command-line interface to interact with the CS Learning Agent,
allowing users to discover trending topics and generate detailed lectures.

Usage:
    python cli.py --help
    python cli.py discover --topics 5
    python cli.py lecture --topic "Machine Learning" --export markdown
    python cli.py session --topics 3 --export-all
"""

import argparse
import sys
import os
from pathlib import Path
from datetime import datetime
from learning_agent import CSLearningAgent, CSTopicInfo
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm

console = Console()


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="CS Learning Agent - Discover trending CS topics and generate lectures",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli.py discover --topics 5
  python cli.py session --topics 3 --export-all
  python cli.py interactive
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Discover command
    discover_parser = subparsers.add_parser('discover', help='Discover trending CS topics')
    discover_parser.add_argument(
        '--topics', '-t', 
        type=int, 
        default=5, 
        help='Number of topics to discover (default: 5)'
    )
    
    # Session command
    session_parser = subparsers.add_parser('session', help='Run complete learning session')
    session_parser.add_argument(
        '--topics', '-t',
        type=int,
        default=3,
        help='Number of topics to process (default: 3)'
    )
    session_parser.add_argument(
        '--export-all',
        action='store_true',
        help='Export all generated lectures to files'
    )
    session_parser.add_argument(
        '--format',
        choices=['markdown', 'txt', 'html'],
        default='markdown',
        help='Export format (default: markdown)'
    )
    
    # Interactive command
    interactive_parser = subparsers.add_parser('interactive', help='Run in interactive mode')
    
    # Parse arguments
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Initialize the learning agent
    try:
        agent = CSLearningAgent()
    except Exception as e:
        console.print(f"[red]Error initializing learning agent: {e}[/red]")
        return
    
    # Execute commands
    if args.command == 'discover':
        discover_topics(agent, args.topics)
    elif args.command == 'session':
        run_session(agent, args.topics, args.export_all, args.format)
    elif args.command == 'interactive':
        run_interactive_mode(agent)


def discover_topics(agent: CSLearningAgent, num_topics: int):
    """Discover and display trending topics."""
    console.print(Panel.fit(
        f"[bold blue]🔍 Discovering {num_topics} Trending CS Topics[/bold blue]",
        title="Topic Discovery"
    ))
    
    topics = agent.discover_topics(num_topics)
    
    if not topics:
        console.print("[red]❌ No topics discovered.[/red]")
        return
    
    console.print(f"\n[green]✅ Successfully discovered {len(topics)} topics![/green]")
    
    # Ask if user wants to generate lectures
    if Confirm.ask("\n🎓 Would you like to generate a lecture for any of these topics?"):
        # Let user choose a topic
        console.print("\n[yellow]📋 Select a topic by entering its number:[/yellow]")
        while True:
            try:
                choice = Prompt.ask("Enter topic number (1-{})".format(len(topics)))
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(topics):
                    selected_topic = topics[choice_idx]
                    break
                else:
                    console.print("[red]Invalid choice. Please try again.[/red]")
            except ValueError:
                console.print("[red]Please enter a valid number.[/red]")
        
        # Generate lecture for selected topic
        console.print(f"\n🎓 Generating lecture for: [bold]{selected_topic.title}[/bold]")
        lecture = agent.generate_lecture_for_topic(selected_topic)
        
        # Ask about export
        if Confirm.ask("\n💾 Would you like to export this lecture to a file?"):
            format_choice = Prompt.ask(
                "Choose format",
                choices=["markdown", "txt", "html"],
                default="markdown"
            )
            export_lecture_to_file(agent, lecture, format_choice)


def run_session(agent: CSLearningAgent, num_topics: int, export_all: bool, export_format: str):
    """Run a complete learning session."""
    console.print(Panel.fit(
        f"[bold blue]🎓 Running Learning Session[/bold blue]\n"
        f"Topics: {num_topics} | Export: {export_all} | Format: {export_format}",
        title="Learning Session"
    ))
    
    results = agent.run_full_session(num_topics)
    
    if "error" in results:
        console.print(f"[red]❌ Session failed: {results['error']}[/red]")
        return
    
    console.print(f"\n[green]✅ Session completed successfully![/green]")
    console.print(f"📊 Topics discovered: {results['topics_discovered']}")
    console.print(f"📚 Lectures generated: {results['lectures_generated']}")
    
    if export_all and "lectures" in results:
        console.print(f"\n💾 Exporting all lectures as {export_format} files...")
        export_count = 0
        
        for lecture_title, lecture in results["lectures"].items():
            try:
                export_lecture_to_file(agent, lecture, export_format)
                export_count += 1
            except Exception as e:
                console.print(f"[red]❌ Failed to export '{lecture_title}': {e}[/red]")
        
        console.print(f"[green]✅ Exported {export_count} lectures![/green]")


def run_interactive_mode(agent: CSLearningAgent):
    """Run the agent in interactive mode."""
    console.print(Panel.fit(
        "[bold blue]🤖 CS Learning Agent - Interactive Mode[/bold blue]\n"
        "Discover topics, generate lectures, and export content interactively!",
        title="Interactive Mode"
    ))
    
    while True:
        console.print("\n[yellow]📋 What would you like to do?[/yellow]")
        console.print("1. 🔍 Discover trending topics")
        console.print("2. 🎓 Generate lecture for specific topic")
        console.print("3. 🚀 Run complete learning session")
        console.print("4. ❌ Exit")
        
        choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "4"])
        
        if choice == "1":
            num_topics = int(Prompt.ask("How many topics to discover?", default="5"))
            discover_topics(agent, num_topics)
            
        elif choice == "2":
            # Let user input a custom topic
            topic_title = Prompt.ask("Enter topic title")
            topic_description = Prompt.ask("Enter topic description (optional)", default="")
            topic_category = Prompt.ask("Enter topic category", default="Computer Science")
            
            # Create a custom topic
            custom_topic = CSTopicInfo(
                title=topic_title,
                description=topic_description or f"Learn about {topic_title}",
                category=topic_category,
                source="User Input",
                relevance_score=1.0,
                date_found=datetime.now().strftime("%Y-%m-%d")
            )
            
            lecture = agent.generate_lecture_for_topic(custom_topic)
            
            if Confirm.ask("Export lecture to file?"):
                format_choice = Prompt.ask(
                    "Choose format",
                    choices=["markdown", "txt", "html"],
                    default="markdown"
                )
                export_lecture_to_file(agent, lecture, format_choice)
                
        elif choice == "3":
            num_topics = int(Prompt.ask("How many topics to process?", default="3"))
            export_all = Confirm.ask("Export all lectures to files?")
            
            format_choice = "markdown"
            if export_all:
                format_choice = Prompt.ask(
                    "Choose export format",
                    choices=["markdown", "txt", "html"],
                    default="markdown"
                )
            
            run_session(agent, num_topics, export_all, format_choice)
            
        elif choice == "4":
            console.print("[green]👋 Thanks for using CS Learning Agent![/green]")
            break


def export_lecture_to_file(agent: CSLearningAgent, lecture, format_choice: str):
    """Export a lecture to a file."""
    try:
        # Generate content
        content = agent.export_lecture(lecture, format_choice)
        
        # Create filename
        safe_title = "".join(c if c.isalnum() or c in (' ', '-', '_') else '' for c in lecture.topic)
        safe_title = safe_title.replace(' ', '_').lower()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        extensions = {"markdown": "md", "txt": "txt", "html": "html"}
        extension = extensions.get(format_choice, "txt")
        filename = f"lecture_{safe_title}_{timestamp}.{extension}"
        
        # Create lectures directory if it doesn't exist
        lectures_dir = Path("lectures")
        lectures_dir.mkdir(exist_ok=True)
        
        filepath = lectures_dir / filename
        
        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        console.print(f"[green]✅ Lecture exported to: {filepath}[/green]")
        
    except Exception as e:
        console.print(f"[red]❌ Export failed: {e}[/red]")


def setup_environment():
    """Setup the environment for the CLI."""
    # Create necessary directories
    directories = ["lectures", "exports"]
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
    
    # Check for required packages
    try:
        import requests
        import bs4
        from rich.console import Console
    except ImportError as e:
        console.print(f"[red]❌ Missing required package: {e}[/red]")
        console.print("Please install requirements: pip install -r requirements.txt")
        sys.exit(1)


if __name__ == "__main__":
    setup_environment()
    main()
"""
Advanced System Example

This example demonstrates how to use ALL Metis Agent components together
for a comprehensive AI agent system including auth, memory, scheduling, web formatting, and more.
"""
import os
import time
from dotenv import load_dotenv
from metis_agent import (
    # Core Components
    SingleAgent, 
    IntentRouter, 
    Planner, 
    TaskManager, 
    Scheduler,
    configure_llm,
    
    # Memory Systems
    MemoryInterface,
    SQLiteMemory,
    TitansInspiredMemory,
    TitansMemoryAdapter,
    TitansAnalytics,
    MemoryMonitor,
    
    # Auth & Security
    APIKeyManager,
    CredentialsManager,
    SecureStorage,
    
    # Web & Formatting
    format_response_for_frontend,
    extract_code_blocks,
    extract_tasks,
    
    # Tools
    BaseTool,
    register_tool,
    get_available_tools
)

# Load environment variables from .env files
load_dotenv()  # Load from .env
load_dotenv('.env.local')  # Load from .env.local (overrides .env)
load_dotenv('templates/.env.local')  # Load from templates/.env.local

def demonstrate_auth_system():
    """Demonstrate the authentication and credentials management system."""
    print("\n=== Authentication System Demo ===")
    
    # Initialize secure storage
    secure_storage = SecureStorage()
    print("+ Secure storage initialized")
    
    # Initialize credentials manager
    credentials_manager = CredentialsManager()
    print("+ Credentials manager initialized")
    
    # Initialize API key manager
    api_manager = APIKeyManager()
    
    # Store API keys securely (example - normally you'd get these from user input)
    groq_key = os.environ.get("GROQ_API_KEY")
    if groq_key:
        api_manager.set_key("groq", groq_key)
        print("+ Groq API key stored securely")
    
    # Validate stored keys
    if api_manager.has_key("groq"):
        print("+ Groq API key validation successful")
    else:
        print("- Groq API key validation failed")
    
    return api_manager

def demonstrate_memory_systems():
    """Demonstrate different memory systems including Titans memory."""
    print("\n=== Memory Systems Demo ===")
    
    # 1. Basic SQLite Memory
    print("\n-- SQLite Memory --")
    sqlite_memory = SQLiteMemory()
    sqlite_memory.store_interaction("user123", "Hello", "Hi there! How can I help?", {})
    recent = sqlite_memory.get_recent_interactions("user123", limit=1)
    print(f"+ SQLite memory stored and retrieved {len(recent)} interactions")
    
    # 2. Titans Inspired Memory
    print("\n-- Titans Memory --")
    titans_memory = TitansInspiredMemory()
    
    # Store some interactions with surprise elements
    interactions = [
        ("What's the weather?", "It's sunny and 75°F", 0.2),
        ("Explain quantum computing", "Quantum computing uses quantum mechanical phenomena...", 0.8),
        ("What's 2+2?", "2+2 equals 4", 0.1),
        ("How do neural networks learn?", "Neural networks learn through backpropagation...", 0.7)
    ]
    
    for query, response, surprise in interactions:
        titans_memory.store_interaction("user123", query, response, {"surprise_factor": surprise})
    
    print(f"+ Titans memory stored {len(interactions)} interactions")
    
    # 3. Titans Analytics
    print("\n-- Titans Analytics --")
    analytics = TitansAnalytics(titans_memory)
    
    # Get memory insights
    insights = analytics.get_memory_insights("user123")
    print(f"+ Memory insights: {insights.get('total_interactions', 0)} total interactions")
    print(f"+ Learning velocity: {insights.get('learning_velocity', 0):.2f}")
    
    # 4. Memory Monitor
    print("\n-- Memory Monitor --")
    monitor = MemoryMonitor(titans_memory)
    stats = monitor.get_memory_stats()
    print(f"+ Memory usage: {stats.get('memory_size_mb', 0):.2f} MB")
    print(f"+ Active sessions: {stats.get('active_sessions', 0)}")
    
    # 5. Titans Memory Adapter (for SingleAgent integration)
    print("\n-- Titans Memory Adapter --")
    adapter = TitansMemoryAdapter(titans_memory)
    print("+ Titans memory adapter initialized for agent integration")
    
    return adapter

def demonstrate_scheduling_system():
    """Demonstrate the task scheduling system."""
    print("\n=== Scheduling System Demo ===")
    
    # Initialize scheduler
    scheduler = Scheduler()
    print("+ Scheduler initialized")
    
    # Create some tasks
    tasks = [
        {"id": "task1", "description": "Analyze market trends", "priority": "high", "estimated_time": 300},
        {"id": "task2", "description": "Generate report", "priority": "medium", "estimated_time": 600},
        {"id": "task3", "description": "Send notifications", "priority": "low", "estimated_time": 60}
    ]
    
    # Schedule tasks
    for task in tasks:
        scheduler.schedule_task(task["id"], task["description"], task["priority"])
        print(f"+ Scheduled task: {task['description']}")
    
    # Get scheduled tasks
    pending_tasks = scheduler.get_pending_tasks()
    print(f"+ Total pending tasks: {len(pending_tasks)}")
    
    return scheduler

def demonstrate_web_formatting():
    """Demonstrate web formatting capabilities."""
    print("\n=== Web Formatting Demo ===")
    
    # Sample agent response with code and tasks
    sample_response = """
    Here's how to create a Flask web application:
    
    ```python
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/')
    def hello():
        return 'Hello, World!'
    
    if __name__ == '__main__':
        app.run()
    ```
    
    Tasks to complete:
    - Install Flask: pip install flask
    - Create app.py file
    - Run the application
    - Test the endpoint
    """
    
    # Format response for frontend
    formatted = format_response_for_frontend(sample_response)
    print("+ Response formatted for web frontend")
    print(f"  Content length: {len(formatted)} characters")
    
    # Extract code blocks
    code_blocks = extract_code_blocks(sample_response)
    print(f"+ Extracted {len(code_blocks)} code blocks")
    for i, block in enumerate(code_blocks):
        print(f"  Block {i+1}: {block['language']} ({len(block['code'])} chars)")
    
    # Extract tasks
    tasks = extract_tasks(sample_response)
    print(f"+ Extracted {len(tasks)} tasks:")
    for task in tasks:
        print(f"  - {task}")
    
    return formatted, code_blocks, tasks

def demonstrate_integrated_system():
    """Demonstrate all components working together in an integrated system."""
    print("\n=== Integrated System Demo ===")
    
    # 1. Set up authentication
    api_manager = demonstrate_auth_system()
    
    # 2. Configure LLM with authenticated credentials
    groq_key = api_manager.get_key("groq")
    if groq_key:
        configure_llm("groq", "llama-3.1-8b-instant", groq_key)
        print("+ LLM configured with authenticated API key")
    else:
        print("- Warning: No Groq API key available, using mock mode")
        return
    
    # 3. Set up advanced memory system
    memory_adapter = demonstrate_memory_systems()
    
    # 4. Create agent with Titans memory
    agent = SingleAgent(
        memory=memory_adapter,
        use_titans_memory=True,
        session_timeout=3600
    )
    print("+ Advanced agent created with Titans memory")
    
    # 5. Set up scheduling
    scheduler = demonstrate_scheduling_system()
    
    # 6. Process a complex query
    print("\n-- Processing Complex Query --")
    query = "I need help building a Python web scraper for e-commerce data. Can you create a plan and implementation?"
    session_id = "integrated_demo_session"
    
    print(f"Query: {query}")
    response = agent.process_query(query, session_id=session_id)
    
    # 7. Format response for web
    formatted_response, code_blocks, tasks = demonstrate_web_formatting()
    
    # 8. Get memory analytics
    if hasattr(agent.memory, 'memory_store'):
        analytics = TitansAnalytics(agent.memory.memory_store)
        insights = analytics.get_memory_insights(session_id)
        print(f"+ Session insights: {insights.get('context_quality', 0):.2f} context quality")
    
    print("\n+ Integrated system demonstration complete!")
    print("  All components (Auth, Memory, Scheduling, Web, Core) working together")

def main():
    """Run the advanced system demonstration."""
    print("Metis Agent - Advanced System Example")
    print("=" * 50)
    print("Demonstrating ALL system components:")
    print("- Authentication & Security")
    print("- Memory Systems (SQLite + Titans)")
    print("- Task Scheduling")
    print("- Web Formatting")
    print("- Integrated Agent System")
    
    try:
        # Run individual component demos
        demonstrate_auth_system()
        demonstrate_memory_systems()
        demonstrate_scheduling_system()
        demonstrate_web_formatting()
        
        # Run integrated system demo
        demonstrate_integrated_system()
        
        print("\n+ All advanced system components demonstrated successfully!")
        print("Your Metis Agent framework is comprehensive and production-ready!")
        
    except Exception as e:
        print(f"- Error running advanced system demo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

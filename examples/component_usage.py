"""
Component Usage Example

This example demonstrates how to use individual Metis Agent components
for advanced use cases where you need more control over the agent behavior.
"""
import os
from dotenv import load_dotenv
from metis_agent import (
    SingleAgent, 
    IntentRouter, 
    Planner, 
    TaskManager,
    Scheduler,
    configure_llm,
    # Memory components
    SQLiteMemory
)

# Try to import additional components that may not be available in all versions
try:
    from metis_agent import TitansMemoryAdapter, TitansAnalytics
    TITANS_AVAILABLE = True
except ImportError:
    TITANS_AVAILABLE = False
    print("Note: Titans memory components not available in this version")

try:
    from metis_agent import APIKeyManager
    AUTH_AVAILABLE = True
except ImportError:
    AUTH_AVAILABLE = False
    print("Note: Auth components not available in this version")

try:
    from metis_agent import format_response_for_frontend, extract_code_blocks
    WEB_AVAILABLE = True
except ImportError:
    WEB_AVAILABLE = False
    print("Note: Web components not available in this version")

# Load environment variables from .env files
load_dotenv()  # Load from .env
load_dotenv('.env.local')  # Load from .env.local (overrides .env)
load_dotenv('templates/.env.local')  # Load from templates/.env.local

def demonstrate_intent_router():
    """Show how to use the IntentRouter independently."""
    print("\n=== Intent Router Example ===")
    
    # Configure LLM first - using Groq
    groq_api_key = os.environ.get("GROQ_API_KEY")
    configure_llm("groq", "llama-3.1-8b-instant", groq_api_key)
    
    # Create an intent router
    router = IntentRouter()
    
    # Test different queries
    queries = [
        "What is machine learning?",  # Question
        "Write a Python function to sort a list",  # Task
        "How does photosynthesis work?",  # Question
        "Create a REST API for user management"  # Task
    ]
    
    for query in queries:
        intent = router.classify(query)
        print(f"Query: {query}")
        print(f"Intent: {intent}")
        print()

def demonstrate_planner():
    """Show how to use the Planner independently."""
    print("\n=== Planner Example ===")
    
    # Create a planner (requires task_file parameter)
    task_file = "demo_tasks.md"
    planner = Planner(task_file)
    
    # Create a complex task
    complex_task = "Build a web application with user authentication and a dashboard"
    
    # Generate a plan
    plan = planner.create_plan(complex_task)
    print(f"Task: {complex_task}")
    print("Generated Plan:")
    for i, step in enumerate(plan, 1):
        print(f"{i}. {step}")
    print()

def demonstrate_task_manager():
    """Show how to use the TaskManager independently."""
    print("\n=== Task Manager Example ===")
    
    # Create a task manager (requires task_file parameter)
    task_file = "demo_tasks.md"
    task_manager = TaskManager(task_file)
    
    # Add some tasks
    tasks_to_add = [
        "Set up development environment",
        "Create user authentication system", 
        "Build dashboard UI",
        "Implement data persistence"
    ]
    
    print("Adding tasks:")
    # Add all tasks at once (TaskManager.add_tasks takes a list)
    task_manager.add_tasks(tasks_to_add, "Demo web application project")
    for task in tasks_to_add:
        print(f"  + Added: {task}")
    
    # Show all tasks
    all_tasks = task_manager.get_all_tasks()
    pending_tasks = all_tasks["pending"]
    completed_tasks = all_tasks["completed"]
    total_count = len(pending_tasks) + len(completed_tasks)
    print(f"\nTotal tasks: {total_count}")
    print(f"Pending: {len(pending_tasks)}, Completed: {len(completed_tasks)}")
    
    # Complete the first pending task
    if pending_tasks:
        first_task = pending_tasks[0]
        print(f"\nCompleting task: {first_task}")
        task_manager.mark_complete(first_task)
        print("  + Task completed!")
    
    print()

def demonstrate_integrated_approach():
    """Show how components work together in SingleAgent."""
    print("\n=== Integrated Approach (Recommended) ===")
    
    # Configure LLM for SingleAgent to use Groq
    groq_api_key = os.environ.get("GROQ_API_KEY")
    
    # For most use cases, use SingleAgent which orchestrates all components
    # Configure it to use Groq instead of the default OpenAI
    agent = SingleAgent(
        llm_provider="groq",
        llm_model="llama-3.1-8b-instant"
    )
    
    # Make sure the LLM is configured globally as well
    configure_llm("groq", "llama-3.1-8b-instant", groq_api_key)
    
    # The agent automatically uses IntentRouter, Planner, and TaskManager internally
    query = "Create a Python script that processes CSV files and generates reports"
    
    print(f"Processing: {query}")
    response = agent.process_query(query)
    print(f"Response:\n{response}")

def demonstrate_scheduler():
    """Show how to use the Scheduler component."""
    print("\n=== Scheduler Component ===\n")
    
    scheduler = Scheduler()
    print("+ Scheduler initialized")
    
    # Create some tasks to prioritize
    tasks = [
        "Send notification emails",
        "Analyze customer data", 
        "Generate monthly report",
        "Update documentation",
        "Review code changes"
    ]
    
    print("Original tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"  {i}. {task}")
    
    # Prioritize tasks using the scheduler
    print("\n+ Prioritizing tasks using LLM...")
    try:
        prioritized = scheduler.prioritize_tasks(tasks)
        print("\n+ Prioritized task order:")
        for i, task in enumerate(prioritized, 1):
            print(f"  {i}. {task}")
    except Exception as e:
        print(f"- Error prioritizing tasks: {e}")
        print("- Using original order as fallback")

def demonstrate_memory_components():
    """Show how to use memory components."""
    print("\n=== Memory Components ===\n")
    
    # SQLite Memory
    print("-- SQLite Memory --")
    db_path = "./data/demo_memory.db"
    try:
        sqlite_memory = SQLiteMemory(db_path)
        print(f"+ SQLite memory initialized (db: {db_path})")
    except Exception as e:
        print(f"- Error initializing SQLite memory: {e}")
        print("- Trying with current directory...")
        try:
            import os
            db_path = os.path.join(os.getcwd(), "demo_memory.db")
            sqlite_memory = SQLiteMemory(db_path)
            print(f"+ SQLite memory initialized (db: {db_path})")
        except Exception as e2:
            print(f"- SQLite memory initialization failed: {e2}")
            return
    
    # Store input and output
    sqlite_memory.store_input("demo_user", "What is machine learning?")
    sqlite_memory.store_output("demo_user", "Machine learning is a type of AI...")
    print("+ Interaction stored")
    
    # Store a task
    sqlite_memory.store_task("Learn about neural networks", "pending")
    print("+ Task stored")
    
    # Retrieve context
    context = sqlite_memory.get_context("demo_user", limit=3)
    print(f"+ Retrieved context (length: {len(context)} chars)")
    
    # Update task status
    sqlite_memory.update_task_status("Learn about neural networks", "completed")
    print("+ Task updated")
    
    # Titans Memory Adapter (for advanced memory)
    print("\n-- Titans Memory Adapter --")
    if TITANS_AVAILABLE:
        try:
            from metis_agent.memory.titans import TitansInspiredMemory
            titans_memory = TitansInspiredMemory()
            adapter = TitansMemoryAdapter(titans_memory)
            print("+ Titans memory adapter initialized")
            
            # Analytics
            analytics = TitansAnalytics(titans_memory)
            print("+ Titans analytics initialized")
            
        except Exception as e:
            print(f"- Note: Titans memory requires additional setup: {e}")
    else:
        print("- Titans memory components not available in this version")

def demonstrate_auth_components():
    """Show how to use authentication components."""
    print("\n=== Authentication Components ===\n")
    
    if AUTH_AVAILABLE:
        # API Key Manager
        api_manager = APIKeyManager()
        print("+ API Key Manager initialized")
        
        # Store and validate API key
        groq_key = os.environ.get("GROQ_API_KEY")
        if groq_key:
            api_manager.set_key("groq", groq_key)
            print("+ API key stored securely")
            
            if api_manager.has_key("groq"):
                print("+ API key found and verified")
            else:
                print("- API key not found")
        else:
            print("- No GROQ_API_KEY found in environment")
        
        # List stored services
        stored_services = api_manager.list_services()
        print(f"+ Stored services: {stored_services}")
    else:
        print("- Authentication components not available in this version")

def demonstrate_web_components():
    """Show how to use web formatting components."""
    print("\n=== Web Components ===\n")
    
    if WEB_AVAILABLE:
        # Sample response with code
        sample_response = """
        Here's a Python example:
        
        ```python
        def hello_world():
            print("Hello, World!")
        
        hello_world()
        ```
        
        This code demonstrates basic function definition and calling.
        """
        
        # Format for frontend
        formatted = format_response_for_frontend(sample_response)
        print("+ Response formatted for web frontend")
        print(f"  Formatted length: {len(formatted)} characters")
        
        # Extract code blocks
        code_blocks = extract_code_blocks(sample_response)
        print(f"+ Extracted {len(code_blocks)} code blocks:")
        for i, block in enumerate(code_blocks):
            print(f"  Block {i+1}: {block.get('language', 'unknown')} ({len(block.get('code', ''))} chars)")
    else:
        print("- Web components not available in this version")
        print("- This is a basic text formatting demonstration:")
        sample_text = "Hello, World! This is sample text."
        print(f"  Sample text: {sample_text}")
        print(f"  Length: {len(sample_text)} characters")
        print(f"  Words: {len(sample_text.split())} words")

def main():
    """Run all component demonstrations."""
    print("Metis Agent - Component Usage Examples")
    print("=" * 50)
    
    # Check for Groq API key
    groq_api_key = os.environ.get("GROQ_API_KEY")
    if not groq_api_key:
        print("Warning: GROQ_API_KEY not found. Some examples may not work.")
        print("Set your API key: set GROQ_API_KEY=your-key-here")
        print("Or you can set it temporarily in this session.")
        return
    
    # Run core component demonstrations
    demonstrate_intent_router()
    demonstrate_planner()
    demonstrate_task_manager()
    
    # Run additional component demonstrations
    demonstrate_scheduler()
    demonstrate_memory_components()
    demonstrate_auth_components()
    demonstrate_web_components()
    
    # Run integrated approach
    demonstrate_integrated_approach()
    
    print("\n+ All available Metis Agent components demonstrated!")
    print("\nRecommendation: For most use cases, use SingleAgent which")
    print("automatically orchestrates all components for optimal performance.")
    print("\nAvailable Components:")
    print("- Core: IntentRouter, Planner, TaskManager, Scheduler")
    print("- Memory: SQLiteMemory" + (" + Titans components" if TITANS_AVAILABLE else " (Titans not available)"))
    print("- Auth: " + ("APIKeyManager + others" if AUTH_AVAILABLE else "Not available in this version"))
    print("- Web: " + ("format_response_for_frontend + extract_code_blocks" if WEB_AVAILABLE else "Basic formatting only"))
    print("- Integration: SingleAgent (recommended for most use cases)")

if __name__ == "__main__":
    main()

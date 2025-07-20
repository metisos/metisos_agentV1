"""
Best Practices Example

This example demonstrates the recommended patterns for using Metis Agent
in production applications.
"""
import os
from dotenv import load_dotenv
from metis_agent import (
    SingleAgent, 
    configure_llm, 
    BaseTool, 
    register_tool,
    get_available_tools
)

# Load environment variables from .env files
load_dotenv()  # Load from .env
load_dotenv('.env.local')  # Load from .env.local (overrides .env)
load_dotenv('templates/.env.local')  # Load from templates/.env.local

def setup_environment():
    """Set up the agent environment following best practices."""
    # 1. Always check for required API keys
    groq_api_key = os.environ.get("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY environment variable is required")
    
    # 2. Configure LLM explicitly for production
    configure_llm(
        provider="groq",
        model="llama-3.1-8b-instant",  # Use specific model versions in production
        api_key=groq_api_key
    )
    
    print("+ Environment configured successfully")

def create_production_agent():
    """Create an agent configured for production use."""
    # 1. Use Titans memory for better context retention
    agent = SingleAgent(
        use_titans_memory=True,  # Better for production
        session_timeout=3600,    # 1 hour session timeout
    )
    
    # 2. Initialize tools (automatically done, but shown for clarity)
    available_tools = get_available_tools()
    print(f"+ Agent created with {len(available_tools)} available tools")
    
    return agent

def demonstrate_session_management():
    """Show proper session management."""
    agent = create_production_agent()
    
    # Always use meaningful session IDs
    user_id = "user_123"
    session_id = f"{user_id}_session_{os.getpid()}"
    
    print(f"\n=== Session Management Example ===")
    print(f"Session ID: {session_id}")
    
    # First interaction
    query1 = "I'm working on a Python web application using Flask"
    response1 = agent.process_query(query1, session_id=session_id)
    print(f"Query 1: {query1}")
    print(f"Response 1: {response1[:100]}...")
    
    # Follow-up that uses context
    query2 = "What's the best way to handle user authentication in this setup?"
    response2 = agent.process_query(query2, session_id=session_id)
    print(f"Query 2: {query2}")
    print(f"Response 2: {response2[:100]}...")

def demonstrate_error_handling():
    """Show proper error handling patterns."""
    print(f"\n=== Error Handling Example ===")
    
    try:
        agent = create_production_agent()
        
        # Simulate a problematic query
        problematic_query = ""  # Empty query
        
        if not problematic_query.strip():
            print("- Empty query detected, handling gracefully")
            return "Please provide a valid query."
        
        response = agent.process_query(problematic_query)
        return response
        
    except ValueError as e:
        print(f"- Configuration error: {e}")
        return None
    except Exception as e:
        print(f"- Unexpected error: {e}")
        return None

def demonstrate_custom_tool_best_practices():
    """Show how to properly create and register custom tools."""
    
    class ValidatedTool(BaseTool):
        """A custom tool that demonstrates best practices."""
        
        name = "validated_tool"
        description = "A tool that validates input before processing"
        
        def can_handle(self, task):
            """Implement robust task detection."""
            if not isinstance(task, str):
                return False
            
            # Use specific keywords for better matching
            keywords = ["validate", "check", "verify"]
            return any(keyword in task.lower() for keyword in keywords)
        
        def execute(self, task):
            """Execute with proper error handling."""
            try:
                # Validate input
                if not task or not task.strip():
                    return "Error: Empty task provided"
                
                # Process the task
                result = f"Validated and processed: {task}"
                return result
                
            except Exception as e:
                # Always handle exceptions in tools
                return f"Error processing task: {str(e)}"
    
    # Register the tool
    register_tool("ValidatedTool", ValidatedTool)
    print("+ Custom tool registered successfully")
    
    # Test the tool
    agent = create_production_agent()
    test_query = "Please validate this data format"
    response = agent.process_query(test_query)
    print(f"Custom tool test: {response[:100]}...")

def demonstrate_monitoring_and_logging():
    """Show how to add monitoring to your agent."""
    import time
    import logging
    
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger("metis_agent_app")
    
    print(f"\n=== Monitoring and Logging Example ===")
    
    agent = create_production_agent()
    session_id = "monitoring_session"
    
    # Log the interaction
    query = "Explain the concept of machine learning"
    start_time = time.time()
    
    logger.info(f"Processing query: {query[:50]}...")
    
    try:
        response = agent.process_query(query, session_id=session_id)
        processing_time = time.time() - start_time
        
        logger.info(f"Query processed successfully in {processing_time:.2f}s")
        print(f"+ Query processed in {processing_time:.2f} seconds")
        
        return response
        
    except Exception as e:
        processing_time = time.time() - start_time
        logger.error(f"Query failed after {processing_time:.2f}s: {e}")
        print(f"- Query failed after {processing_time:.2f} seconds")
        return None

def main():
    """Run all best practices demonstrations."""
    print("Metis Agent - Best Practices Examples")
    print("=" * 50)
    
    try:
        # 1. Set up environment
        setup_environment()
        
        # 2. Demonstrate session management
        demonstrate_session_management()
        
        # 3. Show error handling
        demonstrate_error_handling()
        
        # 4. Custom tool best practices
        demonstrate_custom_tool_best_practices()
        
        # 5. Monitoring and logging
        demonstrate_monitoring_and_logging()
        
        print("\n+ All best practices demonstrated successfully!")
        
    except Exception as e:
        print(f"- Failed to run examples: {e}")

if __name__ == "__main__":
    main()

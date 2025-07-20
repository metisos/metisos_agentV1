"""
API Key Management Example

This example demonstrates how to use the APIKeyManager to securely store 
and retrieve API keys for various services used by Metis Agent.
"""
import os
from dotenv import load_dotenv
from metis_agent import SingleAgent, APIKeyManager, configure_llm

# Load environment variables from .env files
load_dotenv()  # Load from .env
load_dotenv('.env.local')  # Load from .env.local (overrides .env)
load_dotenv('templates/.env.local')  # Load from templates/.env.local

def setup_api_keys():
    """Demonstrate how to set up API keys using APIKeyManager."""
    print("=== API Key Management Setup ===")
    
    # Initialize the API Key Manager
    key_manager = APIKeyManager()
    
    # Example 1: Setting up API keys programmatically
    print("\n1. Setting up API keys programmatically:")
    
    # You can set API keys directly (for demonstration - don't hardcode real keys!)
    # key_manager.set_key("groq", "your-groq-api-key-here")
    # key_manager.set_key("openai", "your-openai-api-key-here")
    # key_manager.set_key("google", "your-google-api-key-here")
    # key_manager.set_key("firecrawl", "your-firecrawl-api-key-here")
    
    print("+ API keys can be set using: key_manager.set_key('service', 'key')")
    
    # Example 2: Check if keys exist
    print("\n2. Checking for existing API keys:")
    services = ["groq", "openai", "google", "firecrawl"]
    
    for service in services:
        has_key = key_manager.has_key(service)
        status = "+" if has_key else "-"
        source = ""
        
        if has_key:
            # Check if key comes from environment or storage
            env_key = os.environ.get(f"{service.upper()}_API_KEY")
            if env_key:
                source = " (from environment variable)"
            else:
                source = " (from secure storage)"
        
        print(f"{status} {service.upper()}_API_KEY: {'Available' if has_key else 'Not found'}{source}")
    
    # Example 3: List all stored services
    stored_services = key_manager.list_services()
    if stored_services:
        print(f"\n3. Services with stored keys: {', '.join(stored_services)}")
    else:
        print("\n3. No API keys currently stored in secure storage")
    
    return key_manager

def demonstrate_environment_priority():
    """Show how environment variables take priority over stored keys."""
    print("\n=== Environment Variable Priority ===")
    
    key_manager = APIKeyManager()
    
    # Check GROQ_API_KEY specifically
    groq_key = key_manager.get_key("groq")
    if groq_key:
        env_key = os.environ.get("GROQ_API_KEY")
        if env_key:
            print("+ GROQ_API_KEY found in environment variables (takes priority)")
        else:
            print("+ GROQ_API_KEY found in secure storage")
    else:
        print("- GROQ_API_KEY not found in environment or storage")
    
    print("\nNOTE: Environment variables always take priority over stored keys")
    print("Set environment variables like: GROQ_API_KEY=your-key-here")

def setup_api_keys_interactively():
    """Interactive setup for API keys (commented for demo)."""
    print("\n=== Interactive API Key Setup (Demo) ===")
    
    # This is what you could do for interactive setup
    print("""
For interactive setup, you could prompt users like this:

```python
key_manager = APIKeyManager()

# Prompt for API keys
services = {
    'groq': 'Groq API Key (for LLM)',
    'openai': 'OpenAI API Key (alternative LLM)',
    'google': 'Google API Key (for web search)',
    'firecrawl': 'Firecrawl API Key (for web scraping)'
}

for service, description in services.items():
    if not key_manager.has_key(service):
        api_key = input(f"Enter {description} (or press Enter to skip): ")
        if api_key.strip():
            key_manager.set_key(service, api_key.strip())
            print(f"+ Saved {service} API key")
```
""")

def demonstrate_agent_with_keys():
    """Show how to use the agent after setting up API keys."""
    print("\n=== Using Agent with API Keys ===")
    
    key_manager = APIKeyManager()
    
    # Configure LLM with available key
    groq_key = key_manager.get_key("groq") or os.environ.get("GROQ_API_KEY")
    
    if groq_key:
        print("+ Configuring agent with Groq LLM")
        configure_llm("groq", "llama-3.1-8b-instant", groq_key)
    else:
        print("- No LLM API key found, using mock mode")
    
    # Create agent
    agent = SingleAgent()
    
    # Test a simple query
    print("\nTesting agent with a simple query:")
    response = agent.process_query("What are the benefits of using API key management?")
    print(f"Response: {response}")

def show_best_practices():
    """Show best practices for API key management."""
    print("\n=== API Key Management Best Practices ===")
    
    practices = [
        "1. Use environment variables for development (.env files)",
        "2. Use APIKeyManager.set_key() for programmatic setup",
        "3. Never hardcode API keys in source code",
        "4. Keys are encrypted when stored by APIKeyManager",
        "5. Environment variables take priority over stored keys",
        "6. Use different keys for different environments (dev/prod)",
        "7. Regularly rotate your API keys",
        "8. Store production keys in secure environment systems"
    ]
    
    for practice in practices:
        print(f"+ {practice}")

def show_file_structure():
    """Show where API keys are stored."""
    print("\n=== Storage Location ===")
    
    key_manager = APIKeyManager()
    config_dir = key_manager.config_dir
    
    print(f"API keys are stored in: {config_dir}")
    print("Files created:")
    print("  .key          - Encryption key (keep secure!)")
    print("  api_keys.enc  - Encrypted API keys")
    print("  credentials.enc - Other encrypted credentials")
    print("\nThese files are automatically created when you store keys.")

def main():
    """Run the API key management example."""
    print("Metis Agent - API Key Management Example")
    print("=" * 50)
    
    # Setup and demonstrate API key management
    key_manager = setup_api_keys()
    
    # Show environment variable priority
    demonstrate_environment_priority()
    
    # Show interactive setup example
    setup_api_keys_interactively()
    
    # Show file storage info
    show_file_structure()
    
    # Show best practices
    show_best_practices()
    
    # Demonstrate agent usage
    demonstrate_agent_with_keys()
    
    print("\n=== Example Complete ===")
    print("To set up your API keys:")
    print("1. Set environment variables in .env file")
    print("2. Or use key_manager.set_key('service', 'your-key')")
    print("3. Keys are automatically used by tools")

if __name__ == "__main__":
    main()

"""
Interactive API Key Setup Script

This script helps users set up their API keys for Metis Agent in a secure way.
Keys are encrypted and stored locally using the APIKeyManager.
"""
import os
import getpass
from metis_agent import APIKeyManager

def setup_api_keys():
    """Interactive setup for API keys."""
    print("Metis Agent - API Key Setup")
    print("=" * 40)
    print("This script will help you securely store API keys for various services.")
    print("Keys are encrypted and stored locally in ~/.metis_agent/")
    print()
    
    # Initialize API Key Manager
    key_manager = APIKeyManager()
    
    # Define services and their descriptions
    services = {
        'groq': {
            'name': 'Groq API Key',
            'description': 'Required for LLM functionality (recommended)',
            'signup': 'Get your key at: https://console.groq.com/',
            'required': True
        },
        'openai': {
            'name': 'OpenAI API Key',
            'description': 'Alternative LLM provider (optional)',
            'signup': 'Get your key at: https://platform.openai.com/',
            'required': False
        },
        'google': {
            'name': 'Google Custom Search API Key',
            'description': 'For web search functionality (optional)',
            'signup': 'Get your key at: https://developers.google.com/custom-search/',
            'required': False
        },
        'firecrawl': {
            'name': 'Firecrawl API Key',
            'description': 'For advanced web scraping (optional)',
            'signup': 'Get your key at: https://firecrawl.dev/',
            'required': False
        }
    }
    
    keys_set = 0
    
    for service_id, service_info in services.items():
        print(f"\n{'='*50}")
        print(f"{service_info['name']}")
        print(f"Description: {service_info['description']}")
        print(f"Sign up: {service_info['signup']}")
        
        # Check if key already exists
        if key_manager.has_key(service_id):
            env_key = os.environ.get(f"{service_id.upper()}_API_KEY")
            if env_key:
                print(f"+ Key already set via environment variable")
            else:
                print(f"+ Key already stored securely")
            
            update = input("Update existing key? (y/N): ").strip().lower()
            if update != 'y':
                print("+ Keeping existing key")
                keys_set += 1
                continue
        
        # Prompt for API key
        if service_info['required']:
            api_key = getpass.getpass(f"Enter {service_info['name']} (required): ").strip()
        else:
            api_key = getpass.getpass(f"Enter {service_info['name']} (optional, press Enter to skip): ").strip()
        
        if api_key:
            try:
                key_manager.set_key(service_id, api_key)
                print(f"+ {service_info['name']} saved securely")
                keys_set += 1
            except Exception as e:
                print(f"- Error saving key: {e}")
        else:
            if service_info['required']:
                print(f"- Warning: {service_info['name']} is required for full functionality")
            else:
                print(f"- Skipped {service_info['name']}")
    
    print(f"\n{'='*50}")
    print("Setup Complete!")
    print(f"+ {keys_set} API keys configured")
    
    # Show summary
    print("\nCurrent API key status:")
    for service_id, service_info in services.items():
        has_key = key_manager.has_key(service_id)
        env_key = os.environ.get(f"{service_id.upper()}_API_KEY")
        
        if has_key:
            source = " (environment)" if env_key else " (secure storage)"
            print(f"+ {service_info['name']}: Available{source}")
        else:
            print(f"- {service_info['name']}: Not set")
    
    print(f"\nKeys are stored in: {key_manager.config_dir}")
    print("You can now run other examples without API key warnings!")
    
    return keys_set > 0

def show_current_status():
    """Show current API key status."""
    print("Current API Key Status")
    print("=" * 30)
    
    key_manager = APIKeyManager()
    services = ['groq', 'openai', 'google', 'firecrawl']
    
    for service in services:
        has_key = key_manager.has_key(service)
        env_key = os.environ.get(f"{service.upper()}_API_KEY")
        
        if has_key:
            source = " (from environment)" if env_key else " (from secure storage)"
            print(f"+ {service.upper()}: Available{source}")
        else:
            print(f"- {service.upper()}: Not found")

def remove_keys():
    """Remove stored API keys."""
    print("Remove API Keys")
    print("=" * 20)
    
    key_manager = APIKeyManager()
    stored_services = key_manager.list_services()
    
    if not stored_services:
        print("No API keys currently stored.")
        return
    
    print("Stored services:", ", ".join(stored_services))
    
    service = input("Enter service name to remove (or 'all' for all): ").strip().lower()
    
    if service == 'all':
        confirm = input("Remove ALL stored API keys? (y/N): ").strip().lower()
        if confirm == 'y':
            for svc in stored_services:
                key_manager.remove_key(svc)
                print(f"+ Removed {svc}")
        else:
            print("+ Cancelled")
    elif service in stored_services:
        key_manager.remove_key(service)
        print(f"+ Removed {service}")
    else:
        print(f"- Service '{service}' not found")

def main():
    """Main menu for API key management."""
    while True:
        print("\n" + "="*50)
        print("Metis Agent - API Key Management")
        print("="*50)
        print("1. Setup API keys (interactive)")
        print("2. Show current status")
        print("3. Remove stored keys")
        print("4. Exit")
        print()
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            setup_api_keys()
        elif choice == '2':
            show_current_status()
        elif choice == '3':
            remove_keys()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()

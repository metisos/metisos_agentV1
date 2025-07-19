"""
CLI Application Example

This example demonstrates how to build a command-line interface for your Metis Agent.
"""
import os
import sys
import argparse
from metis_agent import SingleAgent, configure_llm

class MetisAgentCLI:
    """Command-line interface for Metis Agent."""
    
    def __init__(self):
        """Initialize the CLI."""
        self.agent = None
        self.session_id = None
        self.api_key = os.environ.get("OPENAI_API_KEY")
        self.llm_provider = "openai"
        self.llm_model = "gpt-4o"
        
    def initialize_agent(self):
        """Initialize the agent with configuration."""
        # Configure LLM
        configure_llm(self.llm_provider, self.llm_model, self.api_key)
        
        # Create agent
        self.agent = SingleAgent(use_titans_memory=True)
        
        print(f"Agent initialized with {self.llm_provider} ({self.llm_model})")
        
    def process_query(self, query, session_id=None, tool_name=None):
        """Process a query using the agent."""
        if not self.agent:
            self.initialize_agent()
            
        # Use provided session ID or default
        session_id = session_id or self.session_id or "cli_session"
        self.session_id = session_id
        
        # Process the query
        response = self.agent.process_query(query, session_id=session_id, tool_name=tool_name)
        
        return response
        
    def interactive_mode(self):
        """Run in interactive mode."""
        print("=== Metis Agent Interactive Mode ===")
        print("Type 'exit' or 'quit' to end the session.")
        print("Type 'session <name>' to change the session ID.")
        print("Type 'tool <name>' to specify a tool for the next query.")
        print("Type 'provider <name>' to change the LLM provider.")
        print("Type 'model <name>' to change the LLM model.")
        print()
        
        # Initialize agent
        self.initialize_agent()
        
        # Set default session ID
        self.session_id = "interactive_session"
        
        # Tool for next query
        next_tool = None
        
        while True:
            # Show prompt with session info
            prompt = f"[Session: {self.session_id}"
            if next_tool:
                prompt += f", Tool: {next_tool}"
            prompt += "] > "
            
            # Get user input
            user_input = input(prompt)
            
            # Check for exit command
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
                
            # Check for session command
            if user_input.lower().startswith('session '):
                self.session_id = user_input[8:].strip()
                print(f"Session ID changed to: {self.session_id}")
                continue
                
            # Check for tool command
            if user_input.lower().startswith('tool '):
                next_tool = user_input[5:].strip()
                print(f"Next query will use tool: {next_tool}")
                continue
                
            # Check for provider command
            if user_input.lower().startswith('provider '):
                self.llm_provider = user_input[9:].strip()
                print(f"LLM provider changed to: {self.llm_provider}")
                self.initialize_agent()
                continue
                
            # Check for model command
            if user_input.lower().startswith('model '):
                self.llm_model = user_input[6:].strip()
                print(f"LLM model changed to: {self.llm_model}")
                self.initialize_agent()
                continue
                
            # Process the query
            try:
                response = self.process_query(user_input, tool_name=next_tool)
                print("\n" + response + "\n")
            except Exception as e:
                print(f"Error: {e}")
                
            # Reset next tool
            next_tool = None
            
    def run_command(self, args):
        """Run the CLI with the given arguments."""
        # Check for interactive mode
        if args.interactive:
            self.interactive_mode()
            return
            
        # Set configuration
        if args.provider:
            self.llm_provider = args.provider
        if args.model:
            self.llm_model = args.model
        if args.session:
            self.session_id = args.session
        if args.api_key:
            self.api_key = args.api_key
            
        # Initialize agent
        self.initialize_agent()
        
        # Process the query
        response = self.process_query(args.query, tool_name=args.tool)
        
        # Print the response
        print(response)

def main():
    """Run the CLI application."""
    # Create argument parser
    parser = argparse.ArgumentParser(description="Metis Agent CLI")
    
    # Add arguments
    parser.add_argument("query", nargs="?", help="Query to process")
    parser.add_argument("-i", "--interactive", action="store_true", help="Run in interactive mode")
    parser.add_argument("-s", "--session", help="Session ID")
    parser.add_argument("-t", "--tool", help="Tool to use")
    parser.add_argument("-p", "--provider", help="LLM provider")
    parser.add_argument("-m", "--model", help="LLM model")
    parser.add_argument("-k", "--api-key", help="API key")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Check for required arguments
    if not args.interactive and not args.query:
        parser.print_help()
        sys.exit(1)
        
    # Create and run CLI
    cli = MetisAgentCLI()
    cli.run_command(args)

if __name__ == "__main__":
    main()
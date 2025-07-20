"""
Research Agent Template

This template provides a specialized agent for research tasks.
It leverages the built-in tools from the Metis Agent framework.
"""
import os
from metis_agent import SingleAgent
from metis_agent.tools.google_search import GoogleSearchTool
from metis_agent.tools.content_generation import ContentGenerationTool
from metis_agent.tools.firecrawl import FirecrawlTool

class ResearchAgent:
    """Specialized agent for research tasks."""
    
    def __init__(self, llm_provider=None, use_titans_memory=True):
        """Initialize the research agent."""
        # Create the agent - will auto-detect LLM provider from environment
        self.agent = SingleAgent(
            use_titans_memory=use_titans_memory,
            llm_provider=llm_provider  # Optional: specify provider, otherwise auto-detects
        )
        
        # Set up Google Search API key if available
        google_api_key = os.environ.get("GOOGLE_API_KEY")
        if google_api_key:
            from metis_agent.auth.api_key_manager import APIKeyManager
            key_manager = APIKeyManager()
            key_manager.set_key("google_search", google_api_key)
            
        # Set up Firecrawl API key if available
        firecrawl_api_key = os.environ.get("FIRECRAWL_API_KEY")
        if firecrawl_api_key:
            from metis_agent.auth.api_key_manager import APIKeyManager
            key_manager = APIKeyManager()
            key_manager.set_key("firecrawl", firecrawl_api_key)
        
        print("Research Agent initialized")
    
    def research(self, query, session_id=None):
        """Perform research on the given query."""
        # Format the research query
        research_query = f"Research the following topic thoroughly: {query}"
        
        # Process the query, preferring the GoogleSearchTool if available
        response = self.agent.process_query(
            research_query, 
            session_id=session_id,
            tool_name="GoogleSearchTool" if "GOOGLE_API_KEY" in os.environ else None
        )
        
        return response
    
    def follow_up(self, query, session_id):
        """Ask a follow-up question about previous research."""
        # Process the follow-up query
        response = self.agent.process_query(query, session_id=session_id)
        
        return response
    
    def summarize(self, url, session_id=None):
        """Summarize content from a specific URL."""
        # Use Firecrawl tool if available, otherwise use ContentGenerationTool
        if "FIRECRAWL_API_KEY" in os.environ:
            tool_name = "FirecrawlTool"
            query = f"Summarize the content from this URL: {url}"
        else:
            tool_name = "ContentGenerationTool"
            query = f"Summarize the content that might be found at this URL (without actually visiting it): {url}"
        
        # Process the query
        response = self.agent.process_query(
            query,
            session_id=session_id,
            tool_name=tool_name
        )
        
        return response
    
    def generate_report(self, topic, research_data=None, session_id=None):
        """Generate a structured research report."""
        if research_data:
            query = f"Generate a comprehensive research report on {topic} based on this data: {research_data}"
        else:
            query = f"Generate a comprehensive research report on {topic}"
        
        # Use ContentGenerationTool for report generation
        response = self.agent.process_query(
            query,
            session_id=session_id,
            tool_name="ContentGenerationTool"
        )
        
        return response


def main():
    """Run a demonstration of the research agent."""
    # Create the research agent (will auto-detect LLM provider from environment)
    agent = ResearchAgent()
    
    # Define a session ID
    session_id = "research_session"
    
    # Perform initial research
    research_query = "Research the impact of artificial intelligence on healthcare"
    print(f"Research Query: {research_query}")
    
    research_result = agent.research(research_query, session_id=session_id)
    print(f"Research Result:\n{research_result}")
    
    # Ask a follow-up question
    follow_up_query = "What are the ethical concerns related to this topic?"
    print(f"\nFollow-up Query: {follow_up_query}")
    
    follow_up_result = agent.follow_up(follow_up_query, session_id=session_id)
    print(f"Follow-up Result:\n{follow_up_result}")
    
    # Generate a report
    print("\nGenerating Research Report...")
    report = agent.generate_report("Artificial Intelligence in Healthcare", session_id=session_id)
    print(f"Research Report:\n{report}")

if __name__ == "__main__":
    main()
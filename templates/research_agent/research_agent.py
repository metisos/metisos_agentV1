"""
Research Agent Template

This template provides a specialized agent for research tasks.
"""
import os
from metis_agent import SingleAgent, BaseTool, register_tool

class ResearchTool(BaseTool):
    """Tool for research-specific tasks."""
    
    name = "research_tool"
    description = "Performs research tasks with structured output"
    
    def can_handle(self, task):
        """Determine if this tool can handle the task."""
        research_keywords = [
            "research", "investigate", "analyze", "study", "examine",
            "explore", "review", "survey", "find information", "gather data"
        ]
        return any(keyword in task.lower() for keyword in research_keywords)
        
    def execute(self, task):
        """Execute the research task."""
        # In a real implementation, you might:
        # 1. Use web search tools to gather information
        # 2. Extract key points from search results
        # 3. Synthesize information into a structured format
        
        # For this template, we'll simulate the process
        
        # Parse the research topic
        topic = self._extract_topic(task)
        
        # Generate a structured research report
        report = self._generate_research_report(topic, task)
        
        return report
    
    def _extract_topic(self, task):
        """Extract the main research topic from the task."""
        # This is a simplified implementation
        # In a real tool, you would use NLP or the LLM to extract the topic
        
        task_lower = task.lower()
        
        # Look for common patterns
        patterns = [
            "research on ",
            "research about ",
            "information on ",
            "information about ",
            "investigate ",
            "analyze "
        ]
        
        for pattern in patterns:
            if pattern in task_lower:
                parts = task_lower.split(pattern, 1)
                if len(parts) > 1:
                    return parts[1].strip().split()[0].capitalize()
        
        # Default topic if we can't extract one
        return "Topic"
    
    def _generate_research_report(self, topic, task):
        """Generate a structured research report."""
        # In a real implementation, this would use actual research data
        
        report = f"# Research Report: {topic}\n\n"
        report += "## Summary\n\n"
        report += f"This report provides an overview of {topic} based on the latest available information.\n\n"
        
        report += "## Key Findings\n\n"
        report += "1. Finding one\n"
        report += "2. Finding two\n"
        report += "3. Finding three\n\n"
        
        report += "## Analysis\n\n"
        report += f"The analysis of {topic} reveals several important aspects...\n\n"
        
        report += "## Conclusions\n\n"
        report += "Based on the research, we can conclude that...\n\n"
        
        report += "## References\n\n"
        report += "1. Reference one\n"
        report += "2. Reference two\n"
        
        return report


class ResearchAgent:
    """Specialized agent for research tasks."""
    
    def __init__(self, api_key=None, use_titans_memory=True):
        """Initialize the research agent."""
        # Register the research tool
        register_tool("research_tool", ResearchTool)
        
        # Create the agent
        self.agent = SingleAgent(
            use_titans_memory=use_titans_memory,
            llm_provider="openai",
            llm_model="gpt-4o"
        )
        
        print("Research Agent initialized")
    
    def research(self, query, session_id=None):
        """Perform research on the given query."""
        # Process the query
        response = self.agent.process_query(query, session_id=session_id)
        
        return response
    
    def follow_up(self, query, session_id):
        """Ask a follow-up question about previous research."""
        # Process the follow-up query
        response = self.agent.process_query(query, session_id=session_id)
        
        return response


def main():
    """Run a demonstration of the research agent."""
    # Get API key from environment variable
    api_key = os.environ.get("OPENAI_API_KEY")
    
    # Create the research agent
    agent = ResearchAgent(api_key=api_key)
    
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

if __name__ == "__main__":
    main()
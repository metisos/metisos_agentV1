# Research Agent Template

This template provides a specialized agent for research tasks. It includes a custom research tool that structures research output in a professional format.

## Features

- Specialized for research tasks
- Structured research reports
- Follow-up question handling
- Memory for context retention

## Usage

```python
from research_agent import ResearchAgent

# Create the research agent
agent = ResearchAgent(api_key="your_api_key")

# Define a session ID
session_id = "research_session"

# Perform initial research
research_query = "Research the impact of artificial intelligence on healthcare"
research_result = agent.research(research_query, session_id=session_id)

# Ask a follow-up question
follow_up_query = "What are the ethical concerns related to this topic?"
follow_up_result = agent.follow_up(follow_up_query, session_id=session_id)
```

## Customization

You can customize the research agent by:

1. Modifying the `ResearchTool` class to change how research is conducted
2. Adjusting the report format in the `_generate_research_report` method
3. Adding additional tools for specific research tasks

## Example

See the `research_agent.py` file for a complete example of how to use this template.
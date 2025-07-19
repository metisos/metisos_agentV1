# Metis Agent Starter Kit

![Metis Agent](https://img.shields.io/badge/Metis-Agent-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-Apache%202.0-blue)

A starter kit for building intelligent AI agents with the Metis Agent framework. This repository provides examples, templates, and best practices to help you get started quickly.

## What is Metis Agent?

Metis Agent is a powerful, modular framework for building AI agents with minimal boilerplate code. It provides:

- **Modular Architecture**: Clean separation of concerns with specialized components
- **Multiple LLM Providers**: Seamless integration with OpenAI, Groq, Anthropic, and HuggingFace
- **Advanced Memory Systems**: Both simple and adaptive memory options
- **Specialized Tools**: Ready-to-use tools for common tasks
- **Task Planning and Execution**: Break down complex tasks into manageable subtasks

## Installation

```bash
pip install metis-agent
```

## Quick Start

### Basic Agent

```python
from metis_agent import SingleAgent

# Create an agent
agent = SingleAgent()

# Process a query
response = agent.process_query("Write a Python function to calculate Fibonacci numbers")
print(response)
```

### Using Different LLM Providers

```python
from metis_agent import SingleAgent, configure_llm

# Configure LLM (OpenAI, Groq, Anthropic, or HuggingFace)
configure_llm("groq", "llama-3.1-8b-instant", "your-api-key")

# Create an agent
agent = SingleAgent()

# Process a query
response = agent.process_query("Explain quantum computing in simple terms")
print(response)
```

## Examples

This repository contains several examples to help you get started:

- [Simple Agent](examples/simple_agent.py): Basic agent setup and usage
- [Custom Tool](examples/custom_tool.py): Creating and using custom tools
- [Memory Usage](examples/memory_usage.py): Working with different memory systems
- [Web Server](examples/web_server.py): Setting up a web API for your agent
- [CLI Application](examples/cli_app.py): Building a command-line interface

## Templates

Ready-to-use templates for common agent types:

- [Research Agent](templates/research_agent/): Agent specialized for research tasks
- [Coding Assistant](templates/coding_assistant/): Agent for code generation and explanation
- [Content Creator](templates/content_creator/): Agent for creating various types of content
- [Customer Support](templates/customer_support/): Agent for handling customer inquiries

## Building Custom Tools

Metis Agent allows you to create custom tools for specialized tasks:

```python
from metis_agent import BaseTool, register_tool

class MyCustomTool(BaseTool):
    name = "custom_tool"
    description = "A custom tool for specialized tasks"
    
    def can_handle(self, task):
        return "custom task" in task.lower()
        
    def execute(self, task):
        return f"Executed custom tool on: {task}"

# Register the tool
register_tool("custom_tool", MyCustomTool)
```

## Working with Memory

Metis Agent provides different memory systems:

```python
# Using SQLite memory
agent = SingleAgent()

# Using Titans-inspired adaptive memory
agent = SingleAgent(use_titans_memory=True)

# Process queries with memory
result1 = agent.process_query("What is machine learning?", session_id="user123")
result2 = agent.process_query("How does it relate to AI?", session_id="user123")
```

## Deployment Options

- **Local Development**: Run agents locally for development and testing
- **Web API**: Deploy as a web service using the built-in Flask server
- **CLI Application**: Build command-line tools with the Metis CLI framework
- **Integration**: Embed agents in existing applications

## Best Practices

- **API Key Management**: Use environment variables or the secure storage system
- **Error Handling**: Implement proper error handling for LLM calls and tool execution
- **Testing**: Write tests for your agents and tools
- **Monitoring**: Log agent activities and performance metrics
- **Scaling**: Consider using async patterns for handling multiple requests

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Resources

- [Metis Agent Documentation](https://pypi.org/project/metis-agent/)
- [PyPI Package](https://pypi.org/project/metis-agent/)
- [Issue Tracker](https://github.com/metisos/metisos_agentV1/issues)

---

<p align="center">
  <strong>Metis Agent - Building Intelligent AI Systems</strong>
</p>
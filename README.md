# Metis Agent Starter Kit

![Metis Agent](https://img.shields.io/badge/Metis-Agent-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-Apache%202.0-blue)

A starter kit for building intelligent AI agents with the Metis Agent framework. This repository provides examples, templates, and best practices to help you get started quickly.

## What is Metis Agent?

Metis Agent is a powerful, modular framework for building AI agents with minimal boilerplate code. It provides:

- **Modular Architecture**: Clean separation of concerns with specialized components
- **Multiple LLM Providers**: Seamless integration with Groq, Anthropic, HuggingFace, and OpenAI
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

### Environment Setup

1. Copy the environment template:
```bash
cp .env.example .env
```

2. Add your API keys to `.env`:
```bash
# Primary LLM Provider (Groq is recommended)
GROQ_API_KEY=your_groq_api_key_here

# Optional: Other LLM providers
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key

# Optional: Additional tool API keys
GOOGLE_API_KEY=your_google_api_key
FIRECRAWL_API_KEY=your_firecrawl_api_key
```

### Using Different LLM Providers

```python
from metis_agent import SingleAgent

# Agent will auto-detect available LLM providers from environment
agent = SingleAgent()

# Or explicitly specify a provider
agent = SingleAgent(llm_provider="groq")

# Process queries
response = agent.process_query("Explain quantum computing in simple terms")
print(response)
```

## Using Pre-built Templates

This starter kit includes several pre-built templates that you can use right away:

### Research Agent

```python
from templates.research_agent import ResearchAgent

# Create a research agent
agent = ResearchAgent(api_key="your-api-key")

# Perform research on a topic
result = agent.research("The impact of artificial intelligence on healthcare", session_id="research_session")
print(result)

# Ask a follow-up question
follow_up = agent.follow_up("What are the ethical concerns?", session_id="research_session")
print(follow_up)
```

### Coding Assistant

```python
from templates.coding_assistant import CodingAssistant

# Create a coding assistant
assistant = CodingAssistant(api_key="your-api-key")

# Generate code
code = assistant.generate_code("Write a Python function to find the nth Fibonacci number")
print(code)

# Analyze code
analysis = assistant.analyze_code("def bubble_sort(arr):\n    for i in range(len(arr)):\n        for j in range(len(arr)-1):\n            if arr[j] > arr[j+1]:\n                arr[j], arr[j+1] = arr[j+1], arr[j]")
print(analysis)
```

### Content Creator

```python
from templates.content_creator import ContentCreator

# Create a content creator
creator = ContentCreator(api_key="your-api-key")

# Create a blog post
blog_post = creator.create_blog_post("Artificial Intelligence in Healthcare", tone="professional")
print(blog_post)

# Create social media content
tweet = creator.create_social_media_post("twitter", "Artificial Intelligence in Healthcare")
print(tweet)
```

### Customer Support Agent

```python
from templates.customer_support import CustomerSupportAgent

# Create a customer support agent
support = CustomerSupportAgent(api_key="your-api-key")

# Answer an FAQ
faq_response = support.answer_faq("What are your business hours?")
print(faq_response)

# Create a support ticket
ticket = support.create_ticket("I'm having trouble logging into my account")
print(ticket)
```

## Using Built-in Tools

Metis Agent comes with several built-in tools that you can use:

```python
from metis_agent import SingleAgent
from metis_agent.tools.code_generation import CodeGenerationTool
from metis_agent.tools.content_generation import ContentGenerationTool
from metis_agent.tools.google_search import GoogleSearchTool
from metis_agent.tools.firecrawl import FirecrawlTool

# Create an agent with specific tools
agent = SingleAgent()

# Use a specific tool for a query
code_response = agent.process_query(
    "Write a Python function to calculate the factorial of a number",
    tool_name="CodeGenerationTool"
)

content_response = agent.process_query(
    "Write a blog post about machine learning",
    tool_name="ContentGenerationTool"
)

# Note: GoogleSearchTool and FirecrawlTool require API keys
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

## Command-Line Interface (CLI)

Metis Agent includes a built-in command-line interface that's available immediately after installation. No need to download this repository!

### Installation and Quick Start

```bash
# Install the package
pip install metis-agent

# Run a quick query
metis run "What is artificial intelligence?"

# Start interactive mode
metis run -i
```

### Basic Usage

**Direct Query Mode:**
```bash
metis run "Your query here"
```

**Interactive Mode:**
```bash
metis run -i
# or without any query:
metis run
```

### CLI Commands

#### Main Commands
```bash
metis run [QUERY]         # Run a query or start interactive mode
metis serve              # Start web server
metis tools list         # List available tools
metis auth set-key       # Set API keys
metis memory stats       # View memory statistics
```

#### Options for `metis run`
```bash
metis run [OPTIONS] [QUERY]

Options:
  -i, --interactive     Start interactive mode
  --tool TEXT          Specify a tool to use
  --session-id TEXT    Session ID for context
  --memory             Enable Titans memory
  --llm TEXT           LLM provider to use (default: groq)
  --model TEXT         LLM model to use
  --help               Show help message
```

### Examples

**Research and Web Search:**
```bash
metis run "Search for the latest developments in quantum computing"
```

**Code Generation with Specific Tool:**
```bash
metis run --tool CodeGenerationTool "Write a Python function to sort a list using quicksort"
```

**Interactive Session with Memory:**
```bash
metis run -i --memory --session-id my_project
[my_project] > Tell me about machine learning
[my_project] > What are its main applications?
[my_project] > session new_session  # Switch sessions
[new_session] > tools  # List available tools
[new_session] > exit
```

**Custom LLM Configuration:**
```bash
# Use a different provider
metis run --llm anthropic --model claude-3-sonnet "Explain quantum entanglement"

# Use OpenAI
metis run --llm openai "Generate a poem about technology"
```

**API Key Management:**
```bash
# Set API keys
metis auth set-key groq your-groq-api-key
metis auth set-key google your-google-api-key

# List configured keys
metis auth list-keys

# Remove a key
metis auth remove-key groq
```

### Interactive Commands

When running in interactive mode (`-i`), you can use special commands:

- `session <session_id>`: Switch to a different session for memory isolation
- `tool <tool_name>`: Set a specific tool to use for the next query
- `exit` or `quit`: Exit the CLI

### Features

- **Memory Persistence**: Sessions maintain context across queries
- **Tool Integration**: Access to Google Search, code generation, content creation, and more
- **Flexible Configuration**: Support for multiple LLM providers and models
- **Error Handling**: Graceful handling of missing API keys and network issues
- **Professional Output**: Clean, formatted responses without distracting elements

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
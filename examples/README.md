# Metis Agent Examples

This directory contains examples demonstrating how to use the Metis Agent framework for various use cases.

## Available Examples

- **simple_agent.py**: Basic agent setup and usage
- **custom_tool.py**: Creating and using custom tools
- **memory_usage.py**: Working with different memory systems
- **web_server.py**: Setting up a web API for your agent
- **cli_app.py**: Building a command-line interface

## Running the Examples

To run an example, make sure you have installed the Metis Agent package:

```bash
pip install metis-agent
```

Then, you can run an example with:

```bash
python examples/simple_agent.py
```

## API Keys

Most examples require an API key for the LLM provider. You can set this as an environment variable:

```bash
# For OpenAI
export OPENAI_API_KEY=your_api_key

# For Groq
export GROQ_API_KEY=your_api_key

# For Anthropic
export ANTHROPIC_API_KEY=your_api_key
```

Alternatively, you can create a `.env` file in the root directory with these variables (see `.env.example` for a template).
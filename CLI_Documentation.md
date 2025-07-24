# Metis Agent CLI Documentation

The Metis Agent provides a comprehensive command-line interface (CLI) for interacting with AI agents, managing configurations, and handling authentication. This documentation covers all available commands and their usage.

## Installation

First, install the Metis Agent package:

```bash
pip install metis-agent
```

## Quick Start

After installation, you can immediately start using the CLI:

```bash
# Start interactive chat mode
metis chat

# Process a single query
metis chat "Create a Python web app with FastAPI"

# Show help for all commands
metis --help
```

## Main Commands Overview

The Metis CLI is organized into three main command groups:

1. **`chat`** - Interactive AI assistant and query processing
2. **`config`** - Configuration and agent identity management
3. **`auth`** - API key and authentication management

---

## Chat Commands

### `metis chat`

Start interactive chat mode with the AI agent.

**Usage:**
```bash
metis chat [QUERY] [OPTIONS]
```

**Arguments:**
- `QUERY` (optional) - Process a single query instead of entering interactive mode

**Options:**
- `--session, -s TEXT` - Session ID for maintaining conversation context

**Examples:**

```bash
# Start interactive chat mode
metis chat

# Process a single query
metis chat "Analyze the code in this directory"

# Use a specific session for context
metis chat --session "project-work" "Continue working on the API"
```

**Interactive Mode Features:**

When you run `metis chat` without a query, you enter interactive mode with these features:

- **Natural Language Interface**: Just type your requests in plain English
- **Project Context**: Automatically detects and shows current project information
- **Session Management**: Maintains conversation context across interactions
- **Special Commands**:
  - `exit` or `quit` - Exit chat mode
  - `session <name>` - Switch to a different session
  - `clear` - Clear the screen
  - `help` - Show help information

**Example Interactive Session:**
```
$ metis chat
Metis Agent - Interactive Mode
Directory: /home/user/my-project
Session: main
Project: MyWebApp (Python, Flask, 25 files)

Just type your request in natural language!
Examples:
  - 'Create a Python web app with FastAPI'
  - 'Analyze the code in this project'
  - 'Search for information about quantum computing'
  - 'Help me debug this error'

[main] > Create a new API endpoint for user authentication
[Agent processes request and provides response]

[main] > session auth-work
Switched to session: auth-work

[auth-work] > exit
Goodbye!
```

---

## Configuration Commands

### `metis config`

Manage agent configuration and settings.

**Usage:**
```bash
metis config COMMAND [OPTIONS]
```

**Available Subcommands:**
- `show` - Display current configuration
- `set` - Set configuration values
- `reset` - Reset configuration to defaults
- `system-message` - Manage agent system messages
- `show-identity` - Display agent identity information
- `set-name` - Set the agent's name
- `set-personality` - Set the agent's personality
- `regenerate-identity` - Generate new agent identity

### `metis config show`

Display the current agent configuration.

**Usage:**
```bash
metis config show
```

**Example Output:**
```
Current Configuration:
  LLM Provider: groq
  LLM Model: llama3-70b-8192
  Memory System: titans
  Enhanced Processing: enabled
  Agent ID: metis-12345
  Agent Name: Assistant
```

### `metis config set KEY VALUE`

Set a configuration value.

**Usage:**
```bash
metis config set KEY VALUE
```

**Available Configuration Keys:**
- `llm_provider` - LLM provider (openai, groq, anthropic, huggingface)
- `llm_model` - Model name for the selected provider
- `memory_system` - Memory system (sqlite, titans)
- `enhanced_processing` - Enable/disable enhanced processing (true/false)

**Examples:**
```bash
# Set LLM provider to OpenAI
metis config set llm_provider openai

# Set model to GPT-4
metis config set llm_model gpt-4

# Enable Titans memory
metis config set memory_system titans

# Disable enhanced processing
metis config set enhanced_processing false
```

### `metis config system-message`

Manage the agent's system message (base instructions).

**Usage:**
```bash
metis config system-message [OPTIONS]
```

**Options:**
- `--file PATH` - Load system message from a file
- `--interactive` - Enter system message interactively
- `--layer TEXT` - Specify layer (base or custom) [default: base]

**Examples:**
```bash
# Set system message from file
metis config system-message --file system_prompt.txt

# Enter system message interactively
metis config system-message --interactive

# Set custom layer system message
metis config system-message --interactive --layer custom
```

### `metis config show-identity`

Display agent identity information.

**Usage:**
```bash
metis config show-identity
```

**Example Output:**
```
Agent Identity:
  ID: metis-12345
  Name: Assistant
  Custom Personality: You are a helpful coding assistant specialized in Python development...
```

### `metis config set-name NAME`

Set the agent's display name.

**Usage:**
```bash
metis config set-name NAME
```

**Example:**
```bash
metis config set-name "CodeHelper"
```

### `metis config set-personality`

Set the agent's personality (custom system message).

**Usage:**
```bash
metis config set-personality [OPTIONS]
```

**Options:**
- `--file PATH` - Load personality from a file
- `--interactive` - Enter personality interactively

**Examples:**
```bash
# Set personality from file
metis config set-personality --file personality.txt

# Enter personality interactively
metis config set-personality --interactive
```

### `metis config reset`

Reset all configuration to default values.

**Usage:**
```bash
metis config reset
```

**Note:** This will reset all settings but preserve your API keys and agent identity.

### `metis config regenerate-identity`

Generate a new agent identity (ID and name).

**Usage:**
```bash
metis config regenerate-identity
```

**Note:** This creates a new agent ID and generates a new random name while preserving your custom personality settings.

---

## Authentication Commands

### `metis auth`

Manage API keys and authentication for various LLM providers.

**Usage:**
```bash
metis auth COMMAND [OPTIONS]
```

**Available Subcommands:**
- `set` - Set an API key for a service
- `list` - List configured API keys
- `remove` - Remove an API key
- `test` - Test API key connectivity

### `metis auth set SERVICE [KEY]`

Set an API key for a specific service.

**Usage:**
```bash
metis auth set SERVICE [KEY]
```

**Supported Services:**
- `openai` - OpenAI API
- `groq` - Groq API (recommended for free usage)
- `anthropic` - Anthropic Claude API
- `huggingface` - HuggingFace API
- `google` - Google AI API

**Examples:**
```bash
# Set API key with prompt (secure input)
metis auth set openai

# Set API key directly (less secure)
metis auth set groq your-api-key-here
```

**Security Note:** When you don't provide the key as an argument, you'll be prompted to enter it securely (hidden input).

### `metis auth list`

List all configured API keys (shows service names only, not the actual keys).

**Usage:**
```bash
metis auth list
```

**Example Output:**
```
Configured API keys:
  openai
  groq
  anthropic
```

### `metis auth remove SERVICE`

Remove an API key for a specific service.

**Usage:**
```bash
metis auth remove SERVICE
```

**Example:**
```bash
metis auth remove openai
```

### `metis auth test [SERVICE]`

Test API key connectivity for one or all services.

**Usage:**
```bash
metis auth test [SERVICE]
```

**Examples:**
```bash
# Test all configured API keys
metis auth test

# Test specific service
metis auth test openai
```

---

## Common Workflows

### Initial Setup

1. **Install the package:**
   ```bash
   pip install metis-agent
   ```

2. **Set up your API key (Groq is recommended for free usage):**
   ```bash
   metis auth set groq
   ```

3. **Configure the agent to use Groq:**
   ```bash
   metis config set llm_provider groq
   metis config set llm_model llama3-70b-8192
   ```

4. **Start chatting:**
   ```bash
   metis chat
   ```

### Switching Between Providers

```bash
# Switch to OpenAI
metis auth set openai
metis config set llm_provider openai
metis config set llm_model gpt-4

# Switch to Anthropic
metis auth set anthropic
metis config set llm_provider anthropic
metis config set llm_model claude-3-sonnet-20240229
```

### Customizing Your Agent

```bash
# Set a custom name
metis config set-name "DevAssistant"

# Set a custom personality
metis config set-personality --interactive
# Then enter: "You are a senior software engineer specializing in Python and web development..."

# View your customizations
metis config show-identity
```

### Project-Specific Sessions

```bash
# Work on different projects with separate contexts
metis chat --session "webapp-project" "Help me design the database schema"
metis chat --session "ml-project" "Explain this neural network architecture"
```

---

## Environment Variables

You can also set configuration through environment variables:

- `METIS_LLM_PROVIDER` - Default LLM provider
- `METIS_LLM_MODEL` - Default LLM model
- `METIS_MEMORY_SYSTEM` - Default memory system
- `OPENAI_API_KEY` - OpenAI API key
- `GROQ_API_KEY` - Groq API key
- `ANTHROPIC_API_KEY` - Anthropic API key
- `HUGGINGFACE_API_KEY` - HuggingFace API key

**Example:**
```bash
export GROQ_API_KEY="your-groq-api-key"
export METIS_LLM_PROVIDER="groq"
metis chat "Hello!"
```

---

## Troubleshooting

### Common Issues

**1. "No API key configured" error:**
```bash
# Solution: Set up an API key
metis auth set groq
```

**2. "Invalid API key" error:**
```bash
# Solution: Test and reset your API key
metis auth test groq
metis auth set groq
```

**3. "Command not found: metis":**
```bash
# Solution: Reinstall or check your PATH
pip install --upgrade metis-agent
```

**4. Configuration issues:**
```bash
# Solution: Reset configuration
metis config reset
```

### Getting Help

- Use `metis --help` for general help
- Use `metis COMMAND --help` for command-specific help
- Use `metis config show` to check current settings
- Use `metis auth list` to check configured API keys

---

## Advanced Usage

### Batch Processing

Process multiple queries from a file:
```bash
# Create a file with queries
echo "Explain Python decorators" > queries.txt
echo "Create a REST API example" >> queries.txt

# Process each query
while read query; do
  metis chat "$query" --session "batch-$(date +%s)"
done < queries.txt
```

### Integration with Scripts

Use Metis in shell scripts:
```bash
#!/bin/bash
# analyze_project.sh

echo "Analyzing project structure..."
result=$(metis chat "Analyze the code structure in this directory and suggest improvements")
echo "$result" > analysis_report.txt
echo "Analysis complete. Report saved to analysis_report.txt"
```

### Custom System Messages

Create reusable personality files:
```bash
# Create a specialist personality
cat > python_expert.txt << EOF
You are a Python expert with 10+ years of experience. You specialize in:
- Clean, Pythonic code
- Performance optimization
- Best practices and design patterns
- Testing and debugging
Always provide practical, production-ready solutions.
EOF

# Apply the personality
metis config set-personality --file python_expert.txt
```

---

## API Integration

The CLI commands can be integrated into larger workflows and automation systems. All commands return appropriate exit codes for script integration:

- `0` - Success
- `1` - General error
- `2` - Invalid arguments

This makes it easy to use Metis CLI in CI/CD pipelines, automation scripts, and other development workflows.

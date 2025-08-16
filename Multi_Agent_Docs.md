# Multi-Agent @Mentions System & Custom Agent Profiles

> **Transform your AI workflow with collaborative multi-agent conversations and unlimited custom agent profiles**

The Metis Agent framework supports a powerful @mention system that allows you to seamlessly collaborate with multiple specialized AI agents in a single conversation. Create unlimited custom agent profiles tailored to your specific needs and get different perspectives, expertise, and approaches to solve complex problems more effectively.

## 🎯 Quick Start

```bash
# Create specialized agents
metis agents create frontend-dev --profile developer
metis agents create backend-dev --profile developer  
metis agents create security-expert --profile research

# Start chat and use @mentions
metis chat
> @frontend-dev @backend-dev How should we build a user dashboard?

# Or in code interface
metis code
> @security-expert @backend-dev Review this authentication function
```

## 🚀 Features

### ✨ **Intelligent @Mention Parsing**
- **Single Agent**: `@agent-id your question` - Get response from specific agent
- **Multiple Agents**: `@agent1 @agent2 question` - Get responses from multiple agents
- **All Agents**: `@all your question` - Query every available agent
- **Context Aware**: Each agent knows other agents are also responding

### 🎨 **Beautiful Multi-Agent Responses**
- **Rich Formatting**: Each agent's response is clearly identified and formatted
- **Profile Information**: Shows agent ID and profile type (developer, research, etc.)
- **Seamless Integration**: Works in both `metis chat` and `metis code` interfaces
- **Streaming Support**: Real-time responses maintain the interactive experience

### 🔧 **Full CLI Integration**
- **Slash Commands**: Use alongside existing `/agent`, `/agents`, `/current` commands
- **Help System**: Updated help with @mention examples and usage
- **Backward Compatible**: Zero breaking changes to existing functionality
- **Error Handling**: Graceful handling of missing or invalid agent mentions

## 📖 Usage Guide

### Basic @Mention Syntax

```bash
# Single agent consultation
@agent-name your question here

# Multiple agent collaboration  
@agent1 @agent2 @agent3 your question here

# Query all available agents
@all your question here
```

### Advanced Usage Patterns

#### 🏗️ **Architecture Discussions**
```bash
> @architect @devops @database-expert How should we design a scalable microservices system?

# Each agent provides their specialized perspective:
# 🤖 architect: System design patterns and architectural principles
# 🤖 devops: Deployment, scaling, and infrastructure considerations  
# 🤖 database-expert: Data architecture and persistence strategies
```

#### 🔒 **Security Reviews**
```bash
> @security-expert @backend-dev @frontend-dev Review this authentication implementation

# Multi-faceted security analysis:
# 🤖 security-expert: Security vulnerabilities and best practices
# 🤖 backend-dev: Server-side implementation review
# 🤖 frontend-dev: Client-side security considerations
```

#### 💻 **Code Implementation**
```bash
> @python-expert @javascript-expert @go-expert Implement rate limiting in your language

# Language-specific implementations:
# 🤖 python-expert: Python/Django rate limiting with Redis
# 🤖 javascript-expert: Node.js/Express middleware implementation
# 🤖 go-expert: Go rate limiting with time windows
```

#### 🎨 **Design & UX**
```bash
> @ui-designer @ux-researcher @frontend-dev Design a modern user onboarding flow

# Comprehensive design approach:
# 🤖 ui-designer: Visual design and interface elements
# 🤖 ux-researcher: User research insights and flow optimization
# 🤖 frontend-dev: Technical implementation considerations
```

## 🔧 Interface Examples

### Chat Interface (`metis chat`)

```bash
metis chat

[session] > @backend-dev @database-expert How should we handle user sessions?

🤖 Processing with 2 agents: backend-dev, database-expert

┌─────────────────────────────────────────────────────────────┐
│ 🤖 backend-dev (developer)                                 │
├─────────────────────────────────────────────────────────────┤
│ For session management, I recommend:                       │
│                                                             │
│ **Backend Implementation:**                                 │
│ - JWT tokens with refresh token rotation                   │
│ - Redis for session storage                                │
│ - Secure httpOnly cookies                                  │
│ - Session timeout and cleanup                              │
│                                                             │
│ **Code Example:**                                          │
│ ```javascript                                              │
│ const session = {                                          │
│   create: async (userId) => {                             │
│     const sessionId = generateSecureId();                 │
│     await redis.setex(`session:${sessionId}`, 3600, userId);│
│     return sessionId;                                      │
│   }                                                        │
│ };                                                         │
│ ```                                                        │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 🤖 database-expert (database)                              │
├─────────────────────────────────────────────────────────────┤
│ From a database perspective:                               │
│                                                             │
│ **Session Table Design:**                                  │
│ ```sql                                                     │
│ CREATE TABLE user_sessions (                               │
│   id UUID PRIMARY KEY,                                     │
│   user_id UUID NOT NULL REFERENCES users(id),             │
│   session_token VARCHAR(255) UNIQUE NOT NULL,              │
│   expires_at TIMESTAMP NOT NULL,                           │
│   created_at TIMESTAMP DEFAULT NOW(),                      │
│   last_accessed TIMESTAMP DEFAULT NOW(),                   │
│   ip_address INET,                                         │
│   user_agent TEXT                                          │
│ );                                                         │
│ ```                                                        │
│                                                             │
│ **Key Considerations:**                                    │
│ - Index on user_id and expires_at                         │
│ - Automatic cleanup of expired sessions                    │
│ - Track session metadata for security                      │
└─────────────────────────────────────────────────────────────┘
```

### Code Interface (`metis code`)

```bash
metis code

You > @python-expert @rust-expert Implement a fast JSON parser

🤖 Processing with 2 agents: python-expert, rust-expert

🤖 python-expert (developer)
─────────────────────────────
Here's a high-performance JSON parser in Python using C extensions:

```python
import json
import ujson  # Ultra-fast JSON library
from typing import Any, Dict, List, Union

class FastJSONParser:
    def __init__(self, use_ujson: bool = True):
        self.parser = ujson if use_ujson else json
    
    def parse(self, json_string: str) -> Union[Dict, List, Any]:
        """Parse JSON string with error handling."""
        try:
            return self.parser.loads(json_string)
        except (ValueError, ujson.JSONDecodeError) as e:
            raise JSONParseError(f"Invalid JSON: {e}")
    
    def parse_streaming(self, json_stream):
        """Parse JSON from a stream for large files."""
        for line in json_stream:
            if line.strip():
                yield self.parse(line)

# Benchmarks show 2-3x faster than standard library
parser = FastJSONParser()
data = parser.parse('{"key": "value", "numbers": [1,2,3]}')
```

🤖 rust-expert (developer)  
───────────────────────────
Here's a blazingly fast JSON parser in Rust using serde:

```rust
use serde_json::{Result, Value};
use serde::{Deserialize, Serialize};
use std::collections::HashMap;

#[derive(Serialize, Deserialize, Debug)]
pub struct FastJsonParser {
    strict_mode: bool,
}

impl FastJsonParser {
    pub fn new(strict: bool) -> Self {
        Self { strict_mode: strict }
    }
    
    pub fn parse(&self, json_str: &str) -> Result<Value> {
        if self.strict_mode {
            serde_json::from_str(json_str)
        } else {
            // More permissive parsing
            serde_json::from_str(json_str)
                .or_else(|_| self.try_repair_and_parse(json_str))
        }
    }
    
    pub fn parse_to_map(&self, json_str: &str) -> Result<HashMap<String, Value>> {
        serde_json::from_str(json_str)
    }
    
    fn try_repair_and_parse(&self, json_str: &str) -> Result<Value> {
        // Attempt to fix common JSON issues
        let repaired = json_str
            .replace("'", "\"")  // Single to double quotes
            .replace(",}", "}")   // Trailing commas
            .replace(",]", "]");
        
        serde_json::from_str(&repaired)
    }
}

// Usage - typically 5-10x faster than Python
fn main() -> Result<()> {
    let parser = FastJsonParser::new(true);
    let data = parser.parse(r#"{"key": "value", "numbers": [1,2,3]}"#)?;
    println!("Parsed: {:#}", data);
    Ok(())
}
```
```

## 🎮 Interactive Commands

### Slash Commands (work alongside @mentions)

| Command | Description | Example |
|---------|-------------|---------|
| `/agents` | List all available agents | Shows agent IDs and profiles |
| `/agent <id>` | Switch to specific agent | `/agent frontend-dev` |
| `/current` | Show current agent info | Display active agent details |
| `/help` | Show help with @mention examples | Updated help system |

### @Mention Commands

| Pattern | Description | Example |
|---------|-------------|---------|
| `@agent-id question` | Single agent response | `@security-expert Review this code` |
| `@agent1 @agent2 question` | Multiple agent collaboration | `@dev @designer Create a login page` |
| `@all question` | Query all available agents | `@all What are best practices for APIs?` |

### Mixed Usage Workflow

```bash
# 1. List available agents
> /agents
Available agents: frontend-dev, backend-dev, security-expert, ui-designer

# 2. Multi-agent consultation
> @frontend-dev @backend-dev @security-expert How should we implement OAuth?
[All three agents provide their perspectives]

# 3. Follow up with specific agent
> /agent security-expert  
Switched to agent: security-expert (research)

> Can you elaborate on the JWT security concerns you mentioned?
[Single agent deep-dive response]

# 4. Return to multi-agent mode
> @frontend-dev @ui-designer Now help me design the OAuth login flow
[UI and frontend implementation guidance]
```

## 🏗️ Agent Profiles & Specializations

### Creating Specialized Agents

```bash
# Development team
metis agents create frontend-dev --profile developer
metis agents create backend-dev --profile developer
metis agents create fullstack-dev --profile developer

# Research & analysis team  
metis agents create security-expert --profile research
metis agents create performance-analyst --profile research
metis agents create market-researcher --profile research

# Data & science team
metis agents create data-scientist --profile data_science
metis agents create ml-engineer --profile data_science
metis agents create analyst --profile data_science

# Design & UX team
metis agents create ui-designer --profile developer
metis agents create ux-researcher --profile research
metis agents create brand-strategist --profile research
```

### Profile Capabilities

| Profile | Strengths | Best For |
|---------|-----------|----------|
| `developer` | Code generation, debugging, architecture | Technical implementation |
| `research` | Analysis, investigation, best practices | Research and strategy |
| `data_science` | Analytics, ML, data processing | Data-driven insights |

## 🎯 Use Cases & Examples

### 🏢 **Enterprise Development Team**

```bash
# Architecture planning
> @senior-architect @tech-lead @devops-expert 
  Plan the migration from monolith to microservices

# Security audit
> @security-architect @penetration-tester @compliance-expert
  Audit our authentication and authorization systems

# Performance optimization
> @performance-engineer @database-expert @infrastructure-expert
  Our API response times are slow, help optimize
```

### 🚀 **Startup MVP Development**

```bash
# Quick MVP planning
> @fullstack-dev @product-manager @ui-designer
  Design and plan a social media MVP in 2 weeks

# Technology stack decisions
> @backend-dev @frontend-dev @devops-expert
  Choose the best tech stack for rapid development

# Launch preparation
> @marketing-expert @seo-specialist @analytics-expert
  Prepare go-to-market strategy and tracking
```

### 🎓 **Learning & Education**

```bash
# Concept explanation from multiple angles
> @all Explain machine learning concepts for beginners

# Language comparison
> @python-expert @javascript-expert @rust-expert
  Compare these languages for web backend development

# Best practices learning
> @senior-dev @architect @security-expert
  Teach me about secure coding practices
```

### 🔬 **Research & Analysis**

```bash
# Market analysis
> @market-researcher @competitive-analyst @trend-forecaster
  Analyze the AI tools market for 2024

# Technical research
> @algorithm-expert @performance-researcher @academic-researcher
  Research state-of-the-art in graph neural networks

# Comparative studies
> @framework-expert @benchmark-specialist @adoption-analyst
  Compare React vs Vue vs Angular for our use case
```

## ⚡ Performance & Tips

### Best Practices

1. **Strategic Agent Selection**: Choose agents whose expertise complements each other
2. **Clear Questions**: Be specific about what you want from each agent
3. **Follow-up Effectively**: Use single-agent mode for deep dives after multi-agent overview
4. **Agent Naming**: Use descriptive agent IDs that reflect their expertise

### Performance Notes

- **Parallel Processing**: Multiple agents process queries simultaneously
- **Context Sharing**: Each agent knows others are responding (reduces redundancy)
- **Streaming**: Responses stream in real-time for better user experience
- **Memory Isolation**: Each agent maintains separate memory and context

### Advanced Tips

```bash
# Use descriptive agent names
metis agents create react-specialist --profile developer
metis agents create nodejs-backend --profile developer
metis agents create aws-devops --profile developer

# Combine specialists strategically
> @react-specialist @nodejs-backend @aws-devops
  Build and deploy a scalable React application

# Use @all for brainstorming, specific agents for implementation
> @all What are innovative approaches to user onboarding?
[Broad ideation from all agents]

> @ux-researcher @ui-designer 
  Now design the onboarding flow based on those ideas
[Focused implementation]
```

## 🤝 Integration with Existing Workflows

### Seamless Compatibility

- **Zero Breaking Changes**: Existing single-agent workflows work unchanged
- **Gradual Adoption**: Add @mentions to existing conversations naturally
- **Tool Integration**: Works with all existing Metis tools and features
- **Session Continuity**: Switch between single and multi-agent modes seamlessly

### Migration Path

1. **Start with existing workflow**: Use Metis as usual
2. **Create specialized agents**: Add agents for specific expertise areas
3. **Experiment with @mentions**: Try multi-agent queries for complex problems
4. **Develop team workflows**: Create agent teams for recurring tasks
5. **Advanced collaboration**: Use mixed single/multi-agent workflows

## 🚀 Getting Started

### 1. Setup Multi-Agent Environment

```bash
# Install/update Metis Agent
pip install -e metis_agent/

# Create your first agent team
metis agents create frontend --profile developer
metis agents create backend --profile developer
metis agents create researcher --profile research
```

### 2. Try Your First @Mention

```bash
metis chat
> @frontend @backend How should we structure a modern web application?
```

### 3. Explore Advanced Features

```bash
# List your agents
> /agents

# Get help with examples
> /help

# Try different combinations
> @all What are the latest trends in software development?
> @researcher @backend What's the best database for our use case?
```

---

# 📋 Custom Agent Profiles Guide

## Overview

While Metis provides 3 built-in profiles (`general`, `developer`, `research`), you can create **unlimited custom profiles** tailored to your specific needs. Custom profiles allow you to define specialized agents with unique tool configurations, LLM settings, and expertise areas.

## Table of Contents

- [Default Profiles](#default-profiles)
- [Creating Custom Profiles](#creating-custom-profiles)
- [Profile Configuration Reference](#profile-configuration-reference)
- [Advanced Features](#advanced-features)
- [Profile Examples](#profile-examples)
- [Best Practices](#best-practices)

## Default Profiles

### 1. **General** (`general`)
**Purpose**: Versatile agent for general tasks and conversations

**Configuration**:
- **LLM**: Groq Llama-3.1-70b-versatile, temp=0.1
- **Tools**: Calculator, Search, Content Generation, Data Analysis
- **Memory**: SQLite, 4K context, 30-day retention
- **Use Cases**: General Q&A, content creation, basic analysis

```bash
metis agents create assistant --profile general
```

### 2. **Developer** (`developer`)
**Purpose**: Optimized for software development tasks

**Configuration**:
- **LLM**: Groq Llama-3.1-70b-versatile, temp=0.1  
- **Tools**: Python Code, Git, Edit, Search, Unit Tests, E2B Sandbox
- **Memory**: SQLite, 8K context, 30-day retention
- **File Access**: `./src/`, `./tests/`, `./docs/`, `./scripts/`
- **Commands**: `git`, `pytest`, `black`, `isort`, `flake8`, `mypy`
- **Use Cases**: Code writing, debugging, testing, Git operations

```bash
metis agents create coder --profile developer
```

### 3. **Research** (`research`)
**Purpose**: Specialized for research and information gathering

**Configuration**:
- **LLM**: OpenAI GPT-4, temp=0.3
- **Tools**: Google Search, Web Scraper, Deep Research, Content Gen, Data Analysis
- **Memory**: Titans (advanced), 12K context, 90-day retention
- **File Access**: `./research/`, `./data/`, `./reports/`, `./sources/`
- **Network**: Full internet access enabled
- **Use Cases**: Information gathering, academic research, market analysis

```bash
metis agents create researcher --profile research
```

## Creating Custom Profiles

### Method 1: CLI with Overrides

Create agents with profile overrides:

```bash
# Override LLM provider
metis agents create ai-analyst --profile research --provider anthropic

# Create with custom configuration
metis agents create data-scientist --profile developer \
  --provider openai \
  --model gpt-4o \
  --temperature 0.2
```

### Method 2: YAML Profile Files

Create custom profiles as YAML files in the `profiles/` directory:

#### Example: `profiles/data-scientist.yaml`
```yaml
agent_profile:
  name: "Data Scientist Agent"
  description: "Specialized for data science and machine learning tasks"
  agent_id: "ds_001"
  version: "1.0"
  
  # Inherit from base profile
  base_profile: "developer"
  
  # LLM Configuration
  llm_config:
    provider: "openai"
    model: "gpt-4o"
    temperature: 0.2
    max_tokens: 6000
    timeout: 45
  
  # Tools Configuration
  tools:
    enabled:
      - "PythonCodeTool"
      - "DataAnalysisTool" 
      - "CalculatorTool"
      - "EnhancedSearchTool"
      - "E2BCodeSandboxTool"
      - "GoogleSearchTool"
    disabled:
      - "GitIntegrationTool"
    config:
      DataAnalysisTool:
        visualization_enabled: true
        statistical_analysis: true
        max_dataset_size_mb: 500
      E2BCodeSandboxTool:
        timeout: 120
        language: "python"
        packages: ["pandas", "numpy", "matplotlib", "seaborn", "scikit-learn"]
  
  # Memory Configuration  
  memory_config:
    type: "titans"
    max_context_tokens: 10000
    retention_days: 60
    specialized_memory: "data_science_focused"
    backup_enabled: true
  
  # Performance Settings
  performance:
    cache_enabled: true
    cache_ttl: 3600
    max_parallel_tools: 4
    timeout_seconds: 60
    retry_attempts: 3
  
  # Permissions
  permissions:
    file_access:
      - "./data/"
      - "./notebooks/"
      - "./models/"
      - "./reports/"
    network_access: true
    system_commands:
      - "python"
      - "pip"
      - "jupyter"
      - "git"
    max_file_size_mb: 1000
  
  # Shared Resources
  shared_resources:
    knowledge_base: true
    tool_registry: true
    cache_layer: true
    memory_sharing: false
  
  # Custom Configuration
  custom_config:
    specialization: "machine_learning"
    preferred_frameworks: ["scikit-learn", "pandas", "matplotlib"]
    data_formats: ["csv", "json", "parquet", "xlsx"]
    analysis_types: ["descriptive", "predictive", "clustering"]
```

Then use the custom profile:
```bash
metis agents create ml-expert --profile data-scientist
```

### Method 3: Programmatic Creation

```python
from metis_core_package.config.agent_profiles import ProfileManager, LLMConfig, ToolConfig

manager = ProfileManager()

# Create custom profile
custom_profile = manager.create_profile({
    'name': 'DevOps Engineer',
    'description': 'Specialized for DevOps and infrastructure tasks',
    'llm_config': {
        'provider': 'anthropic',
        'model': 'claude-3-sonnet-20240229',
        'temperature': 0.1
    },
    'tools': {
        'enabled': [
            'BashTool', 'GitIntegrationTool', 'FileOperationsTool',
            'ProjectManagementTool', 'EnhancedSearchTool'
        ],
        'config': {
            'BashTool': {
                'allowed_commands': ['docker', 'kubectl', 'terraform', 'ansible'],
                'timeout': 300
            }
        }
    },
    'permissions': {
        'system_commands': ['docker', 'kubectl', 'terraform', 'ansible', 'git'],
        'file_access': ['./infrastructure/', './deployments/', './scripts/'],
        'network_access': True
    }
})
```

## Profile Configuration Reference

### Core Profile Structure

```yaml
agent_profile:
  name: string                    # Display name
  description: string             # Agent description
  agent_id: string               # Unique identifier
  version: string                # Profile version
  base_profile: string           # Inherit from existing profile
  
  llm_config: { }                # LLM settings
  tools: { }                     # Tool configuration
  memory_config: { }             # Memory settings
  performance: { }               # Performance tuning
  permissions: { }               # Security & access
  shared_resources: { }          # Resource sharing
  custom_config: { }             # Custom fields
```

### LLM Configuration

```yaml
llm_config:
  provider: string               # openai, anthropic, groq, huggingface, ollama
  model: string                  # Model name
  temperature: float             # 0.0-2.0, creativity level
  max_tokens: int               # Response length limit
  timeout: int                  # Request timeout (seconds)
  api_key: string               # Optional: custom API key
  base_url: string              # Optional: custom endpoint
  custom_config: { }            # Provider-specific settings
```

**Supported Providers & Models**:

| Provider | Example Models |
|----------|----------------|
| `openai` | `gpt-4o`, `gpt-4-turbo`, `gpt-3.5-turbo` |
| `anthropic` | `claude-3-sonnet-20240229`, `claude-3-haiku-20240307` |
| `groq` | `llama-3.1-70b-versatile`, `mixtral-8x7b-32768` |
| `ollama` | `llama2`, `codellama`, `mistral` (local) |

### Tools Configuration

```yaml
tools:
  enabled:                      # List of enabled tools
    - "ToolName1"
    - "ToolName2"
  disabled:                     # List of disabled tools
    - "UnwantedTool"
  config:                       # Tool-specific settings
    ToolName1:
      setting1: value
      setting2: value
```

**Available Tools**:

| Category | Tools |
|----------|-------|
| **Code** | `PythonCodeTool`, `E2BCodeSandboxTool`, `GitIntegrationTool`, `UnitTestGeneratorTool` |
| **Files** | `EditTool`, `FileOperationsTool`, `ReadTool`, `WriteTool` |
| **Search** | `EnhancedSearchTool`, `GoogleSearchTool`, `GrepTool` |
| **Web** | `WebScraperTool`, `FirecrawlTool` |
| **Analysis** | `DataAnalysisTool`, `TextAnalyzerTool`, `DependencyAnalyzerTool` |
| **System** | `BashTool`, `ProjectManagementTool`, `CalculatorTool` |

### Memory Configuration

```yaml
memory_config:
  type: string                  # sqlite, titans, redis, memory
  path: string                  # Custom memory path
  max_context_tokens: int       # Context window size
  retention_days: int           # How long to keep memories
  isolation: boolean            # Isolate from other agents
  cache_size: int              # Memory cache size
  specialized_memory: string    # Domain-specific memory type
  backup_enabled: boolean       # Enable memory backups
```

### Performance Configuration

```yaml
performance:
  cache_enabled: boolean        # Enable response caching
  cache_ttl: int               # Cache time-to-live (seconds)
  memory_monitoring: boolean    # Monitor memory usage
  max_parallel_tools: int      # Concurrent tool execution
  timeout_seconds: int         # Operation timeout
  retry_attempts: int          # Retry failed operations
  lazy_loading: boolean        # Load tools on demand
```

### Permissions Configuration

```yaml
permissions:
  file_access:                 # Allowed file paths
    - "./src/"
    - "./data/"
  network_access: boolean      # Internet access allowed
  system_commands:             # Allowed shell commands
    - "git"
    - "python"
  restricted_paths:            # Blocked file paths  
    - "/etc/"
    - "/sys/"
  max_file_size_mb: int       # File size limit
```

### Shared Resources Configuration

```yaml
shared_resources:
  knowledge_base: boolean      # Access shared knowledge
  tool_registry: boolean      # Access shared tools
  cache_layer: boolean        # Share response cache
  memory_sharing: boolean     # Share memories between agents
  config_sharing: boolean     # Share configuration data
```

## Advanced Features

### Profile Inheritance

Create specialized profiles that inherit from base profiles:

```yaml
# profiles/senior-developer.yaml
agent_profile:
  name: "Senior Developer"
  base_profile: "developer"    # Inherit everything from developer
  
  # Override specific settings
  llm_config:
    provider: "anthropic"      # Use Claude instead of Llama
    model: "claude-3-sonnet-20240229"
    temperature: 0.05          # More conservative
  
  tools:
    enabled:                   # Add specialized tools
      - "AdvancedMathTool" 
      - "DeepResearchTool"
    
  permissions:
    system_commands:           # Additional permissions
      - "docker"
      - "kubectl"
```

### Provider Override at Runtime

Override the LLM provider when creating agents:

```bash
# Use OpenAI instead of default Groq
metis agents create smart-dev --profile developer --provider openai

# Use local Ollama model
metis agents create local-dev --profile developer --provider ollama --model codellama
```

### Custom Tool Configurations

Configure tools with specific settings:

```yaml
tools:
  config:
    E2BCodeSandboxTool:
      timeout: 120
      language: "python"
      packages: ["requests", "pandas", "numpy"]
      environment_variables:
        PYTHONPATH: "/workspace"
    
    GoogleSearchTool:
      max_results: 20
      search_depth: "comprehensive"
      safe_search: true
    
    DataAnalysisTool:
      visualization_enabled: true
      max_dataset_size_mb: 100
      supported_formats: ["csv", "json", "xlsx"]
```

### Memory Specialization

Use specialized memory types for different domains:

```yaml
memory_config:
  type: "titans"
  specialized_memory: "code_focused"     # For development tasks
  # OR
  specialized_memory: "research_focused" # For research tasks
  # OR  
  specialized_memory: "data_science_focused" # For ML/data tasks
```

## Profile Examples

### Example 1: Full-Stack Developer Agent

```yaml
# profiles/fullstack-dev.yaml
agent_profile:
  name: "Full-Stack Developer"
  description: "Expert in both frontend and backend development"
  base_profile: "developer"
  
  llm_config:
    provider: "openai"
    model: "gpt-4o"
    temperature: 0.1
  
  tools:
    enabled:
      - "PythonCodeTool"
      - "GitIntegrationTool"
      - "E2BCodeSandboxTool"
      - "WebScraperTool"
      - "EditTool"
      - "BashTool"
    config:
      E2BCodeSandboxTool:
        timeout: 180
        packages: ["flask", "react", "express", "django"]
  
  permissions:
    file_access:
      - "./frontend/"
      - "./backend/"
      - "./api/"
      - "./tests/"
    system_commands:
      - "npm"
      - "yarn"
      - "pip"
      - "docker"
      - "git"
  
  custom_config:
    specializations: ["react", "python", "nodejs", "docker"]
    deployment_platforms: ["vercel", "heroku", "aws"]
```

### Example 2: DevOps Pipeline Agent

```yaml
# profiles/devops.yaml
agent_profile:
  name: "DevOps Engineer"
  description: "Infrastructure automation and deployment specialist"
  
  llm_config:
    provider: "anthropic"
    model: "claude-3-sonnet-20240229"
    temperature: 0.1
  
  tools:
    enabled:
      - "BashTool"
      - "GitIntegrationTool"
      - "FileOperationsTool"
      - "EnhancedSearchTool"
      - "EditTool"
    config:
      BashTool:
        timeout: 600
        allowed_commands: ["docker", "kubectl", "terraform", "ansible"]
  
  permissions:
    system_commands:
      - "docker"
      - "kubectl" 
      - "terraform"
      - "ansible"
      - "helm"
      - "git"
    file_access:
      - "./infrastructure/"
      - "./k8s/"
      - "./terraform/"
      - "./ansible/"
    network_access: true
  
  custom_config:
    platforms: ["kubernetes", "docker", "aws", "gcp"]
    tools: ["terraform", "ansible", "helm", "prometheus"]
```

### Example 3: Security Audit Agent

```yaml
# profiles/security-auditor.yaml
agent_profile:
  name: "Security Auditor"
  description: "Code security analysis and vulnerability assessment"
  base_profile: "developer"
  
  llm_config:
    provider: "anthropic"
    model: "claude-3-sonnet-20240229"
    temperature: 0.05  # Very conservative for security
  
  tools:
    enabled:
      - "EnhancedSearchTool"
      - "GrepTool"
      - "ReadTool"
      - "DataAnalysisTool"
      - "DependencyAnalyzerTool"
      - "TextAnalyzerTool"
    disabled:
      - "BashTool"        # Restrict system access
      - "EditTool"        # Read-only access
  
  permissions:
    file_access:
      - "./src/"
      - "./tests/"
      - "./config/"
    network_access: true   # For vulnerability databases
    system_commands: []    # No system commands allowed
    max_file_size_mb: 50
  
  custom_config:
    focus_areas: ["injection", "authentication", "authorization", "encryption"]
    compliance_standards: ["OWASP", "NIST", "ISO27001"]
```

### Example 4: UI/UX Design Agent

```yaml
# profiles/ui-designer.yaml
agent_profile:
  name: "UI/UX Designer"
  description: "User interface and experience design specialist"
  base_profile: "general"
  
  llm_config:
    provider: "openai"
    model: "gpt-4o"
    temperature: 0.3  # More creative for design
  
  tools:
    enabled:
      - "ContentGenerationTool"
      - "WebScraperTool"
      - "GoogleSearchTool"
      - "DataAnalysisTool"
      - "EnhancedSearchTool"
    config:
      ContentGenerationTool:
        style: "creative"
        formats: ["markdown", "html", "css"]
      GoogleSearchTool:
        focus_domains: ["dribbble.com", "behance.net", "uxplanet.org"]
  
  custom_config:
    design_systems: ["material-ui", "ant-design", "chakra-ui"]
    tools: ["figma", "sketch", "adobe-xd"]
    methodologies: ["design-thinking", "user-centered-design", "atomic-design"]
    research_methods: ["user-interviews", "usability-testing", "a-b-testing"]
```

### Example 5: Content Marketing Agent

```yaml
# profiles/content-marketer.yaml
agent_profile:
  name: "Content Marketing Specialist"
  description: "SEO-optimized content creation and marketing strategy"
  base_profile: "research"
  
  llm_config:
    provider: "openai"
    model: "gpt-4o"
    temperature: 0.4  # Creative but focused
  
  tools:
    enabled:
      - "ContentGenerationTool"
      - "GoogleSearchTool"
      - "WebScraperTool"
      - "DataAnalysisTool"
      - "TextAnalyzerTool"
    config:
      ContentGenerationTool:
        seo_optimization: true
        readability_target: "general_audience"
        tone_options: ["professional", "conversational", "authoritative"]
      GoogleSearchTool:
        include_trends: true
        competitor_analysis: true
  
  permissions:
    file_access:
      - "./content/"
      - "./blog/"
      - "./marketing/"
    network_access: true
  
  custom_config:
    content_types: ["blog-posts", "social-media", "email-campaigns", "whitepapers"]
    seo_tools: ["keyword-research", "competitor-analysis", "trending-topics"]
    platforms: ["linkedin", "twitter", "medium", "wordpress"]
```

## Best Practices

### 1. Profile Organization
- Use descriptive names: `senior-python-dev` vs `dev1`
- Group related profiles in subdirectories
- Version your profiles: include `version` field
- Document custom configurations

### 2. Tool Selection
- Enable only necessary tools for performance
- Configure tool-specific settings for optimal behavior
- Consider security implications of enabled tools

### 3. Memory Management
- Use appropriate memory types for use cases
- Set reasonable retention periods
- Enable isolation for sensitive agents

### 4. Security
- Restrict file access to necessary paths only
- Limit system commands to required operations
- Use read-only access when possible
- Review shared resource settings

### 5. Performance
- Tune cache settings based on usage patterns
- Adjust timeout values for tool complexity
- Monitor resource usage and adjust limits

### 6. Multi-Agent Teams

Create complementary agent teams:

```bash
# Development Team
metis agents create frontend-dev --profile fullstack-dev
metis agents create backend-dev --profile fullstack-dev
metis agents create devops-eng --profile devops

# Design Team  
metis agents create ui-designer --profile ui-designer
metis agents create ux-researcher --profile research
metis agents create content-creator --profile content-marketer

# Security Team
metis agents create security-auditor --profile security-auditor
metis agents create penetration-tester --profile security-auditor
metis agents create compliance-expert --profile research

# Use them together
metis chat "@frontend-dev @ui-designer @ux-researcher design a modern dashboard"
```

## Troubleshooting

### Common Issues

#### 1. Profile Not Found
```bash
❌ Profile 'custom-profile' not found
```
**Solutions**:
- Check `profiles/` directory for YAML files
- Use built-in profiles: `general`, `developer`, `research`
- Create the profile first

#### 2. Tool Loading Errors
```bash
❌ Failed to load tool: ToolName
```
**Solutions**:
- Check tool name spelling in `enabled` list
- Verify tool dependencies are installed
- Check tool configuration parameters

#### 3. Permission Denied
```bash
❌ Permission denied accessing /path/
```
**Solutions**:
- Add path to `permissions.file_access` in profile
- Check `restricted_paths` for conflicts
- Verify file permissions on system

#### 4. Provider/Model Errors
```bash
❌ Provider 'xyz' not supported
```
**Solutions**:
- Check supported providers: `openai`, `anthropic`, `groq`, `ollama`
- Verify API keys are configured: `metis auth test`
- Check model names match provider's available models

### Debug Commands

```bash
# Check system status
metis agents system

# Test provider connectivity  
metis agents providers

# Get agent details
metis agents status agent-name

# Clear agent cache
metis agents cleanup
```

---

## 📚 Additional Resources

- **[GitHub Repository](https://github.com/metisos/metisos_agentV1)**: Source code and examples
- **[PyPI Package](https://pypi.org/project/metis-agent/)**: Installation and updates
- **[Documentation](DOCUMENTATION.md)**: Complete system documentation
- **[CLI Reference](CLI_REFERENCE.md)**: Complete command reference

---

## 🎉 Transform Your AI Workflow

The @mention system combined with unlimited custom profiles transforms Metis from a single-agent tool into a **collaborative AI ecosystem**. Create specialized agents for any domain, get multiple expert perspectives, and build comprehensive solutions to complex problems.

**Key Benefits**:
- ✅ **Unlimited Customization**: Create agents for any specialization
- ✅ **Profile Inheritance**: Build on existing profiles efficiently  
- ✅ **Multi-Agent Collaboration**: Get diverse perspectives with @mentions
- ✅ **Enterprise Ready**: Advanced security, permissions, and resource control
- ✅ **Provider Flexibility**: Use any LLM provider (OpenAI, Anthropic, Groq, local models)

**Ready to revolutionize your AI workflow? Start creating custom agents and mentioning! 🚀**

---

*Generated for metis-agent v0.16.3+ - Multi-Agent @Mentions & Custom Profiles System*
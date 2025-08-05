#!/usr/bin/env python3
"""
Custom Metis Agent Template - v0.6.0

This template demonstrates advanced customization features in Metis Agent v0.6.0:
- Custom agent identities and specialized personalities
- Multi-provider LLM configuration (OpenAI, Groq, Anthropic, HuggingFace)
- Advanced tool selection and configuration
- Enhanced memory management with Titans memory
- E2B Code Sandbox integration for secure execution
- Role-specific agent factories
- Smart orchestrator configuration
- Session management and context preservation

Perfect for:
- Creating specialized AI assistants
- Role-specific agent deployments
- Enterprise multi-agent systems
- Advanced customization scenarios

Usage:
    python custom_agent_template.py

Prerequisites:
    - pip install metis-agent
    - Configure API keys for desired providers
    - Optional: E2B API key for code execution
"""

from metis_agent import SingleAgent
from metis_agent.core.agent_config import AgentConfig
from metis_agent.auth.api_key_manager import APIKeyManager
from dotenv import load_dotenv
import os
import sys
from metis_agent.tools.registry import get_available_tools
from typing import Dict, List, Optional

def create_custom_agent(
    agent_name: str = "CodeMentor",
    personality: str = "You are a senior software engineer and coding mentor with access to advanced tools including secure code execution, research capabilities, and project management. You specialize in helping developers write clean, efficient code and solve complex programming problems with hands-on examples.",
    llm_provider: str = "groq",
    llm_model: Optional[str] = None,
    enable_memory: bool = True,
    enable_titans: bool = True,
    custom_tools: Optional[List[str]] = None,
    enable_e2b: bool = True,
    session_id: Optional[str] = None
) -> SingleAgent:
    """
    Create a customized Metis Agent with v0.6.0 advanced features.
    
    Args:
        agent_name: Custom name for the agent
        personality: Custom personality/role for the agent
        llm_provider: LLM provider ('groq', 'openai', 'anthropic', 'huggingface')
        llm_model: Specific model to use (auto-selected if None)
        enable_memory: Enable conversation memory
        enable_titans: Enable Titans memory enhancement
        custom_tools: List of specific tools to enable (None = all tools)
        enable_e2b: Enable E2B Code Sandbox for secure execution
        session_id: Optional session ID for context management
    
    Returns:
        SingleAgent: Configured custom agent with v0.6.0 capabilities
    """
    print(f"Creating custom agent '{agent_name}' with {llm_provider} provider...")
    
    # Initialize configuration
    config = AgentConfig()
    
    # Configure agent with custom personality
    config.set_personality(personality)
    config.set_llm_provider(llm_provider)
    
    if not llm_model:
        # Auto-select optimal models for each provider
        optimal_models = {
            "groq": "llama-3.1-8b-instant",  # Fast and free
            "openai": "gpt-4o-mini",         # Cost-effective
            "anthropic": "claude-3-haiku-20240307",  # Fast and efficient
            "huggingface": "mistralai/Mixtral-8x7B-Instruct-v0.1"  # Open source
        }
        llm_model = optimal_models.get(llm_provider, "llama-3.1-8b-instant")
    
    config.set_llm_model(llm_model)
    print(f"Using model: {llm_model}")
    
    # Configure enhanced memory management
    config.set_memory_enabled(enable_memory)
    config.set_titans_memory(enable_titans)
    
    # Set custom agent identity
    config.set_agent_name(agent_name)
    
    # Configure custom personality with v0.6.0 context
    enhanced_personality = f"""{personality}

You have access to Metis Agent v0.6.0's advanced capabilities including:
- 36+ specialized tools for development, research, and analysis
- E2B Code Sandbox for secure Python code execution
- Advanced research tools with citation management
- Git integration for complete workflow management
- Data analysis with pandas, numpy, and visualization
- Project management and validation tools
- Enhanced memory system for context preservation

Always leverage these tools when appropriate to provide comprehensive, actionable assistance."""
    
    # Set the enhanced personality
    config.set_personality(enhanced_personality)
    
    # Check for E2B API key if E2B is enabled
    if enable_e2b and not os.getenv('E2B_API_KEY'):
        print("[WARNING] E2B Code Sandbox requested but E2B_API_KEY not found")
        print("   Code execution will fall back to other available tools")
    
    # Create the agent with enhanced v0.6.0 capabilities
    agent = SingleAgent(
        config=config,
        use_titans_memory=enable_titans,
        tools=custom_tools  # None means use all available tools
    )
    
    # Set session ID if provided
    if session_id:
        agent.session_id = session_id
    
    print(f"[OK] Agent '{agent_name}' created successfully!")
    
    # Display available tools
    try:
        available_tools = get_available_tools()
        print(f"[TOOLS] Available tools: {len(available_tools)}")
        if enable_e2b and os.getenv('E2B_API_KEY'):
            print("[E2B] Code Sandbox: Enabled")
    except Exception as e:
        print(f"Tool info not available: {e}")
    
    return agent

def create_specialized_agents() -> Dict[str, SingleAgent]:
    """
    Create multiple specialized agents for different use cases using v0.6.0 capabilities.
    
    Returns:
        Dict[str, SingleAgent]: Dictionary of specialized agents with enhanced capabilities
    """
    print("[TEAM] Creating specialized agent team...")
    agents = {}
    
    # 1. Advanced Code Assistant with E2B Integration
    print("Creating CodeWizard...")
    agents['code_wizard'] = create_custom_agent(
        agent_name="CodeWizard",
        personality="You are an elite software architect and full-stack developer with expertise in Python, JavaScript, TypeScript, Go, and system design. You excel at code generation, debugging, optimization, and architectural decisions. You use E2B Code Sandbox for secure code execution and testing.",
        llm_provider="groq",
        enable_e2b=True,
        custom_tools=["E2BCodeSandboxTool", "GitIntegrationTool", "CodeGenerationTool", "UnitTestGeneratorTool", "DependencyAnalyzerTool"],
        session_id="code_wizard_session"
    )
    
    # 2. Data Science & Analytics Expert
    print("Creating DataSage...")
    agents['data_sage'] = create_custom_agent(
        agent_name="DataSage",
        personality="You are a senior data scientist with expertise in machine learning, statistical analysis, and data visualization. You excel at data preprocessing, model building, and deriving actionable insights. You use advanced analytics tools and secure code execution for data analysis.",
        llm_provider="groq",
        enable_e2b=True,
        custom_tools=["E2BCodeSandboxTool", "DataAnalysisTool", "AdvancedMathTool", "DeepResearchTool"],
        session_id="data_sage_session"
    )
    
    # 3. Research & Content Specialist
    print("Creating Scholar...")
    agents['scholar'] = create_custom_agent(
        agent_name="Scholar",
        personality="You are a research specialist and academic expert with access to advanced research tools. You excel at gathering information from multiple sources, fact-checking, citation management, and synthesizing complex information into clear, actionable insights.",
        llm_provider="groq",
        enable_titans=True,  # Enhanced memory for research context
        custom_tools=["DeepResearchTool", "GoogleSearchTool", "FirecrawlTool", "ContentGenerationTool", "TextAnalyzerTool"],
        session_id="scholar_session"
    )
    
    # 4. DevOps & Project Management Expert
    print("Creating DevOpsMaster...")
    agents['devops_master'] = create_custom_agent(
        agent_name="DevOpsMaster",
        personality="You are a DevOps engineer and project management expert specializing in CI/CD, infrastructure automation, and project lifecycle management. You excel at Git workflows, project validation, and deployment strategies.",
        llm_provider="groq",
        custom_tools=["GitIntegrationTool", "ProjectManagementTool", "ProjectValidationTool", "BashTool", "BlueprintExecutionTool"],
        session_id="devops_session"
    )
    
    # 5. Content Creation & Communication Expert
    print("Creating WordSmith...")
    agents['word_smith'] = create_custom_agent(
        agent_name="WordSmith",
        personality="You are a professional content creator, technical writer, and communication expert. You excel at creating engaging content, documentation, marketing materials, and improving writing clarity and style.",
        llm_provider="groq",
        custom_tools=["ContentGenerationTool", "TextAnalyzerTool", "DeepResearchTool", "GoogleSearchTool"],
        session_id="wordsmith_session"
    )
    
    # 6. Security & Code Analysis Specialist
    print("Creating SecurityGuard...")
    agents['security_guard'] = create_custom_agent(
        agent_name="SecurityGuard",
        personality="You are a cybersecurity expert and code security analyst. You specialize in secure coding practices, vulnerability assessment, dependency analysis, and security best practices. You use secure sandboxes for code analysis.",
        llm_provider="groq",
        enable_e2b=True,
        custom_tools=["E2BCodeSandboxTool", "DependencyAnalyzerTool", "CodeGenerationTool", "ProjectValidationTool"],
        session_id="security_session"
    )
    
    print(f"[OK] Created {len(agents)} specialized agents!")
    return agents

def demonstrate_custom_agent():
    """
    Demonstrate custom agent capabilities.
    """
    print("=== Custom Metis Agent Template ===")
    print()
    
    # Create a custom coding assistant
    print("Creating custom coding assistant...")
    agent = create_custom_agent(
        agent_name="PythonMentor",
        personality="You are a Python expert and mentor. You help developers learn Python best practices, debug code, and build efficient applications. You always provide working code examples.",
        llm_provider="groq",
        llm_model="llama-3.1-8b-instant"
    )
    
    # Display agent info
    identity = agent.get_agent_identity()
    print(f"Agent Name: {identity.get('name')}")
    print(f"Agent ID: {identity.get('agent_id')}")
    print(f"LLM Provider: {agent.config.get_llm_provider()}")
    print(f"Memory Enabled: {agent.config.is_memory_enabled()}")
    print()
    
    # Test the custom agent
    queries = [
        "What's your name and what do you specialize in?",
        "Can you help me write a Python function to calculate fibonacci numbers?",
        "What are some Python best practices for error handling?"
    ]
    
    print("Testing custom agent...")
    print("-" * 60)
    
    for query in queries:
        print(f"User: {query}")
        try:
            response = agent.process_query(query)
            print(f"Agent: {response}")
        except Exception as e:
            print(f"Error: {e}")
            print("Make sure you have configured your API keys!")
        print()

def demonstrate_specialized_agents():
    """
    Demonstrate multiple specialized agents.
    """
    print("=== Specialized Agents Demo ===")
    print()
    
    # Create specialized agents
    print("Creating specialized agents...")
    agents = create_specialized_agents()
    
    # Display all agents
    for role, agent in agents.items():
        identity = agent.get_agent_identity()
        print(f"{role.title()}: {identity.get('name')} ({identity.get('agent_id')})")
    print()
    
    # Test each agent with role-specific queries
    test_cases = {
        'code_assistant': "Can you help me optimize this Python code for better performance?",
        'data_analyst': "How would you approach analyzing customer churn data?",
        'writer': "Can you help me improve the clarity of this technical documentation?",
        'researcher': "What are the latest trends in artificial intelligence research?"
    }
    
    print("Testing specialized agents...")
    print("-" * 60)
    
    for role, query in test_cases.items():
        if role in agents:
            agent = agents[role]
            identity = agent.get_agent_identity()
            print(f"Testing {identity.get('name')} ({role}):")
            print(f"Query: {query}")
            try:
                response = agent.process_query(query)
                print(f"Response: {response[:200]}...")  # Truncate for demo
            except Exception as e:
                print(f"Error: {e}")
            print()

def demonstrate_v6_features():
    """
    Demonstrate advanced v0.6.0 features with custom agents.
    """
    print("\n[DEMO] Demonstrating v0.6.0 Advanced Features")
    print("=" * 50)
    
    # Create a specialized agent for code execution
    print("\n1. [E2B] Secure Code Execution with Custom Agent")
    print("-" * 40)
    
    code_agent = create_custom_agent(
        agent_name="CodeExecutor",
        personality="You are a code execution specialist. You excel at running Python code securely and analyzing results.",
        enable_e2b=True,
        custom_tools=["E2BCodeSandboxTool", "DataAnalysisTool"]
    )
    
    code_query = """
Execute this data analysis code:
```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Generate sample sales data
np.random.seed(42)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = np.random.randint(1000, 5000, 6)

df = pd.DataFrame({'Month': months, 'Sales': sales})
print("Sales Data:")
print(df)

# Calculate statistics
print(f"\nTotal Sales: ${df['Sales'].sum():,}")
print(f"Average Monthly Sales: ${df['Sales'].mean():.2f}")
print(f"Best Month: {df.loc[df['Sales'].idxmax(), 'Month']} (${df['Sales'].max():,})")
```
"""
    
    try:
        print(f"Query: Execute sales data analysis...")
        response = code_agent.process_query(code_query)
        print(f"Response: {response[:500]}..." if len(response) > 500 else f"Response: {response}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Demonstrate multi-agent collaboration
    print("\n\n2. [COLLAB] Multi-Agent Collaboration")
    print("-" * 40)
    
    # Create research agent
    research_agent = create_custom_agent(
        agent_name="ResearchBot",
        personality="You are a research specialist focused on gathering and analyzing information.",
        custom_tools=["DeepResearchTool", "GoogleSearchTool"],
        session_id="research_session"
    )
    
    # Create content agent
    content_agent = create_custom_agent(
        agent_name="ContentBot",
        personality="You are a content creation expert who transforms research into engaging content.",
        custom_tools=["ContentGenerationTool", "TextAnalyzerTool"],
        session_id="content_session"
    )
    
    research_query = "Research the latest trends in artificial intelligence for 2024"
    print(f"Research Agent Query: {research_query}")
    
    try:
        research_result = research_agent.process_query(research_query)
        print(f"Research Result: {research_result[:300]}...")
        
        # Use research result for content creation
        content_query = f"Create a blog post summary based on this research: {research_result[:500]}"
        content_result = content_agent.process_query(content_query)
        print(f"\nContent Result: {content_result[:300]}...")
    except Exception as e:
        print(f"Error in multi-agent workflow: {e}")

def check_api_keys():
    """
    Check and display API key configuration status.
    """
    print("[CONFIG] API Key Configuration Status")
    print("=" * 40)
    
    required_keys = {
        'GROQ_API_KEY': 'Groq (recommended - fast and free)',
        'OPENAI_API_KEY': 'OpenAI (GPT models)',
        'ANTHROPIC_API_KEY': 'Anthropic (Claude models)',
    }
    
    optional_keys = {
        'E2B_API_KEY': 'E2B Code Sandbox (secure code execution)',
        'FIRECRAWL_API_KEY': 'Firecrawl (advanced web scraping)',
        'GOOGLE_API_KEY': 'Google Search API',
    }
    
    # Check required keys
    missing_required = []
    for key, description in required_keys.items():
        if os.getenv(key):
            print(f"[OK] {key}: Configured ({description})")
        else:
            print(f"[MISSING] {key}: Missing ({description})")
            missing_required.append(key)
    
    # Check optional keys
    print("\nOptional API keys:")
    for key, description in optional_keys.items():
        if os.getenv(key):
            print(f"[OK] {key}: Configured ({description})")
        else:
            print(f"[NOT SET] {key}: Not set ({description})")
    
    if missing_required:
        print(f"\n[WARNING] {len(missing_required)} required API key(s) missing!")
        print("\nQuick setup (choose one):")
        print("export GROQ_API_KEY='your_groq_api_key'  # Recommended")
        print("export OPENAI_API_KEY='your_openai_api_key'")
        print("export ANTHROPIC_API_KEY='your_anthropic_api_key'")
        return False
    
    return True

def main():
    """
    Main function demonstrating Metis Agent v0.6.0 custom agent capabilities.
    """
    # Load environment variables from .env.local file
    env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env.local')
    if os.path.exists(env_path):
        load_dotenv(env_path)
        print(f"[ENV] Loaded environment variables from {env_path}")
    else:
        print(f"[ENV] No .env.local file found at {env_path}")
    
    print("[METIS] Agent v0.6.0 - Custom Agent Template")
    print("Advanced Agent Customization & Specialization")
    print("=" * 60)
    
    # Check API key configuration
    if not check_api_keys():
        print("\n[ERROR] Please configure at least one LLM provider API key to continue.")
        print("\nGet API keys:")
        print("- Groq: https://console.groq.com/keys (recommended - fast & free)")
        print("- OpenAI: https://platform.openai.com/api-keys")
        print("- Anthropic: https://console.anthropic.com/")
        sys.exit(1)
    
    print("\n[OK] API keys configured! Proceeding with demonstrations...")
    
    try:
        # Demonstrate single custom agent
        print("\n\n[DEMO] Single Custom Agent Demo")
        print("=" * 40)
        demonstrate_custom_agent()
        
        # Demonstrate specialized agent team
        print("\n\n[TEAM] Specialized Agent Team Demo")
        print("=" * 40)
        demonstrate_specialized_agents()
        
        # Demonstrate advanced v0.6.0 features
        demonstrate_v6_features()
        
        print("\n\n[COMPLETE] Custom Agent Template Complete!")
        print("\n[INFO] Next Steps:")
        print("- Modify agent personalities for your specific use cases")
        print("- Experiment with different tool combinations")
        print("- Create domain-specific agent teams")
        print("- Explore the web_app_template.py for web integration")
        print("- Check advanced_integration_template.py for enterprise patterns")
        
    except Exception as e:
        print(f"\n[ERROR] Error in demonstration: {e}")
        print("\nTroubleshooting:")
        print("1. Verify API keys are correctly set")
        print("2. Check internet connectivity")
        print("3. Ensure metis-agent is up to date: pip install --upgrade metis-agent")
        sys.exit(1)

if __name__ == "__main__":
    main()

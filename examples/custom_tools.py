#!/usr/bin/env python3
"""
Custom Tools & Agent - Metis Agent

Shows how to create custom tools and build a specialized agent 
with custom configuration, identity, and tool integration.
"""

import os
import io
import json
from pathlib import Path
from typing import Dict, Any
from contextlib import redirect_stderr, redirect_stdout

def main():
    # Load environment variables
    try:
        from dotenv import load_dotenv
        if Path('.env').exists():
            load_dotenv()
    except ImportError:
        pass
    
    from metis_agent import SingleAgent, BaseTool
    from metis_agent.tools.registry import register_tool
    from metis_agent.core.agent_config import AgentConfig
    from metis_agent.memory.enhanced_memory_manager import MemoryConfig
    
    print("Custom Tools & Specialized Agent")
    print("=" * 35)
    
    # 1. Define Custom Tools
    print("\n1. Creating Custom Tools")
    
    class WeatherAnalyzerTool(BaseTool):
        """Advanced weather analysis and recommendations tool"""
        
        def get_description(self) -> str:
            return "Analyze weather conditions and provide detailed recommendations for activities, clothing, and planning"
        
        def get_parameters(self) -> dict:
            return {
                "location": {
                    "type": "string",
                    "required": True,
                    "description": "City name or coordinates"
                },
                "activity_type": {
                    "type": "string",
                    "required": False,
                    "default": "general",
                    "description": "Type of activity (outdoor, sports, travel, etc.)"
                }
            }
        
        def can_handle(self, query: str) -> bool:
            weather_keywords = ['weather', 'forecast', 'temperature', 'rain', 'sunny', 'climate']
            return any(keyword in query.lower() for keyword in weather_keywords)
        
        def execute(self, **kwargs) -> dict:
            location = kwargs.get('location', 'Unknown')
            activity = kwargs.get('activity_type', 'general')
            
            # Simulate advanced weather analysis
            analysis = {
                "current_conditions": {
                    "location": location,
                    "temperature": "22°C (72°F)",
                    "conditions": "Partly cloudy with light breeze",
                    "humidity": "65%",
                    "wind": "12 km/h NW",
                    "uv_index": "Moderate (5/10)"
                },
                "recommendations": {
                    "clothing": "Light jacket recommended, comfortable shoes",
                    "activities": "Perfect for outdoor activities, avoid prolonged sun exposure",
                    "travel_tips": "Great conditions for sightseeing, bring light rain gear just in case"
                },
                "hourly_forecast": [
                    {"time": "12:00", "temp": "24°C", "conditions": "Sunny"},
                    {"time": "15:00", "temp": "26°C", "conditions": "Partly cloudy"},
                    {"time": "18:00", "temp": "23°C", "conditions": "Overcast"}
                ]
            }
            
            return {
                "success": True,
                "data": analysis,
                "message": f"Comprehensive weather analysis completed for {location}",
                "tool": "WeatherAnalyzerTool"
            }
    
    class ProjectManagerTool(BaseTool):
        """Project management and task organization tool"""
        
        def get_description(self) -> str:
            return "Create project plans, manage tasks, estimate timelines, and track progress"
        
        def get_parameters(self) -> dict:
            return {
                "project_type": {
                    "type": "string",
                    "required": True,
                    "description": "Type of project (web, mobile, data science, etc.)"
                },
                "complexity": {
                    "type": "string",
                    "required": False,
                    "default": "medium",
                    "description": "Project complexity (simple, medium, complex)"
                },
                "timeline": {
                    "type": "string",
                    "required": False,
                    "default": "4 weeks",
                    "description": "Desired project timeline"
                }
            }
        
        def can_handle(self, query: str) -> bool:
            project_keywords = ['project', 'plan', 'task', 'timeline', 'milestone', 'manage', 'organize']
            return any(keyword in query.lower() for keyword in project_keywords)
        
        def execute(self, **kwargs) -> dict:
            project_type = kwargs.get('project_type', 'web')
            complexity = kwargs.get('complexity', 'medium')
            timeline = kwargs.get('timeline', '4 weeks')
            
            # Generate project structure
            phases = {
                "Phase 1: Planning & Design": {
                    "duration": "1 week",
                    "tasks": [
                        "Requirements gathering",
                        "System design",
                        "UI/UX mockups",
                        "Technology stack selection"
                    ]
                },
                "Phase 2: Core Development": {
                    "duration": "2 weeks", 
                    "tasks": [
                        "Backend API development",
                        "Database schema implementation",
                        "Frontend components",
                        "Integration testing"
                    ]
                },
                "Phase 3: Testing & Deployment": {
                    "duration": "1 week",
                    "tasks": [
                        "Unit and integration testing",
                        "Performance optimization",
                        "Deployment setup",
                        "Documentation"
                    ]
                }
            }
            
            return {
                "success": True,
                "data": {
                    "project_type": project_type,
                    "complexity": complexity,
                    "timeline": timeline,
                    "phases": phases,
                    "total_tasks": sum(len(phase["tasks"]) for phase in phases.values()),
                    "estimated_hours": {"simple": 80, "medium": 160, "complex": 240}[complexity]
                },
                "message": f"Project plan created for {project_type} project ({complexity} complexity)",
                "tool": "ProjectManagerTool"
            }
    
    print("   > WeatherAnalyzerTool: Advanced weather analysis")
    print("   > ProjectManagerTool: Project planning and management")
    
    # 2. Register Custom Tools
    print("\n2. Registering Custom Tools")
    register_tool("weather_analyzer", WeatherAnalyzerTool)
    register_tool("project_manager", ProjectManagerTool)
    print("   > Tools registered with the system")
    
    # 3. Create Specialized Agent Configuration
    print("\n3. Creating Specialized Agent")
    config = AgentConfig()
    
    # Configure agent identity for project management specialty
    config.set_agent_name("ProjectMaster")
    config.set_llm_provider("groq")
    config.set_llm_model("llama-3.1-8b-instant")
    
    # Set specialized personality
    specialist_personality = """
    You are ProjectMaster, a specialized AI assistant focusing on:
    - Project planning and management
    - Weather-aware activity planning
    - Task organization and timeline estimation
    - Resource allocation and risk assessment
    
    You excel at:
    - Breaking down complex projects into manageable phases
    - Providing weather-conscious recommendations
    - Creating realistic timelines and milestones
    - Identifying potential project risks and solutions
    
    Always use your specialized tools when relevant and provide
    practical, actionable advice with specific examples.
    """
    
    config.set_personality(specialist_personality)
    
    # Configure memory for project tracking
    memory_config = MemoryConfig(
        max_context_tokens=3000,
        max_interactions_per_session=30,
        enable_cost_tracking=True
    )
    
    print(f"   > Agent Name: {config.get_agent_name()}")
    print(f"   > Agent ID: {config.get_agent_id()}")
    print("   > Specialized for project management and planning")
    
    # 4. Create Agent with Custom Tools
    print("\n4. Initializing Specialized Agent")
    with redirect_stderr(io.StringIO()), redirect_stdout(io.StringIO()):
        agent = SingleAgent(
            config=config,
            memory_config=memory_config,
            enhanced_processing=True,
            memory_path="./project_agent_memory"
        )
    
    print("   > Agent initialized with custom tools")
    
    # 5. Test Agent Identity
    print("\n5. Testing Agent Identity")
    response = agent.process_query("What's your name and what do you specialize in?")
    if isinstance(response, dict):
        print(f"   Identity: {response['response'][:120]}...")
    
    # 6. Test Custom Weather Tool
    print("\n6. Testing Weather Analysis Tool")
    weather_query = "What's the weather like in Paris for outdoor activities?"
    print(f"   Query: {weather_query}")
    
    weather_response = agent.process_query(weather_query)
    if isinstance(weather_response, dict):
        print(f"   Response: Used weather tool with {len(weather_response['response'])} character response")
    
    # 7. Test Project Management Tool
    print("\n7. Testing Project Management Tool")
    project_query = "Help me plan a web application project with medium complexity over 6 weeks"
    print(f"   Query: {project_query}")
    
    project_response = agent.process_query(project_query)
    if isinstance(project_response, dict):
        print(f"   Response: Created project plan with {len(project_response['response'])} character response")
    
    # 8. Test Combined Tool Usage
    print("\n8. Testing Multi-Tool Integration")
    complex_query = """
    I'm planning an outdoor team-building event in San Francisco next month.
    I need a project plan and weather considerations for the event.
    """
    print("   Query: Multi-tool outdoor event planning")
    
    complex_response = agent.process_query(complex_query)
    if isinstance(complex_response, dict):
        response_text = complex_response['response']
        print(f"   Response: {len(response_text)} characters")
        if 'weather' in response_text.lower() and ('plan' in response_text.lower() or 'project' in response_text.lower()):
            print("   > Successfully integrated both weather and project planning")
        else:
            print("   > Generated comprehensive response")
    
    # 9. Configuration Summary
    print("\n9. Agent & Tools Summary")
    print("=" * 35)
    print(f"Agent Name: {config.get_agent_name()}")
    print(f"Agent ID: {config.get_agent_id()}")
    print(f"Specialization: Project Management & Weather Planning")
    print(f"Custom Tools: 2 registered")
    print(f"LLM: {config.get_llm_provider()} ({config.get_llm_model()})")
    print(f"Memory: {memory_config.max_context_tokens} tokens, {memory_config.max_interactions_per_session} interactions")
    
    print("\n> Custom agent with specialized tools ready!")
    print("\nCapabilities added:")
    print("- Advanced weather analysis with recommendations")
    print("- Comprehensive project planning and management")
    print("- Specialized agent identity and personality")
    print("- Integration between multiple custom tools")
    print("- Persistent memory for project tracking")

if __name__ == "__main__":
    try:
        main()
    except ImportError:
        print("Install: pip install metis-agent python-dotenv")
    except Exception as e:
        print(f"Error: {e}")
        print("Ensure GROQ_API_KEY is set in environment")

#!/usr/bin/env python3
"""
Custom Tools Template - Metis Agent Framework

This template demonstrates how users can create and register their own custom tools
to extend agent capabilities for specific use cases.

Features:
- Custom tool creation following Metis standards
- Tool registration and integration
- Agent configuration with custom tools
- Example usage scenarios

Author: Metis Agent Framework
Version: 1.0.0
"""

import os
import sys
import json
import requests
from typing import Dict, Any, List, Optional
from datetime import datetime

# Add the metis_agent directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'metis_agent'))

from metis_agent.core.agent import SingleAgent
from metis_agent.core.agent_config import AgentConfig
from metis_agent.tools.base import BaseTool


# ============================================================
# CUSTOM TOOL EXAMPLES
# ============================================================

class WeatherTool(BaseTool):
    """Custom tool for weather information"""
    
    def __init__(self):
        super().__init__()
        self.name = "WeatherTool"
        self.description = "Get current weather information for any city"
        self.version = "1.0.0"
    
    def can_handle(self, task: str) -> bool:
        """Check if this tool can handle the given task"""
        weather_keywords = [
            'weather', 'temperature', 'forecast', 'climate',
            'rain', 'sunny', 'cloudy', 'humidity', 'wind'
        ]
        task_lower = task.lower()
        return any(keyword in task_lower for keyword in weather_keywords)
    
    def execute(self, task: str, **kwargs) -> Dict[str, Any]:
        """Execute weather lookup"""
        try:
            # Extract city from task
            city = self._extract_city(task)
            if not city:
                return {
                    "success": False,
                    "error": "Could not identify city in request",
                    "suggestion": "Please specify a city name"
                }
            
            # Get weather data (using a free weather API)
            weather_data = self._get_weather_data(city)
            
            return {
                "success": True,
                "data": weather_data,
                "tool_used": self.name,
                "city": city
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Weather lookup failed: {str(e)}",
                "tool_used": self.name
            }
    
    def _extract_city(self, task: str) -> Optional[str]:
        """Extract city name from task description"""
        # Simple city extraction - in production, use NLP
        words = task.split()
        
        # Look for common patterns
        for i, word in enumerate(words):
            if word.lower() in ['in', 'for', 'at']:
                if i + 1 < len(words):
                    return words[i + 1].strip('.,!?')
        
        # Look for capitalized words (likely city names)
        for word in words:
            if word[0].isupper() and len(word) > 2:
                return word.strip('.,!?')
        
        return None
    
    def _get_weather_data(self, city: str) -> Dict[str, Any]:
        """Get weather data for city (mock implementation)"""
        # In production, use actual weather API like OpenWeatherMap
        # This is a mock response for demonstration
        return {
            "city": city,
            "temperature": "22°C",
            "condition": "Partly Cloudy",
            "humidity": "65%",
            "wind": "10 km/h",
            "description": f"Current weather in {city} is partly cloudy with a temperature of 22°C"
        }


class DatabaseTool(BaseTool):
    """Custom tool for database operations"""
    
    def __init__(self, db_config: Dict[str, Any] = None):
        super().__init__()
        self.name = "DatabaseTool"
        self.description = "Execute database queries and operations"
        self.version = "1.0.0"
        self.db_config = db_config or {}
    
    def can_handle(self, task: str) -> bool:
        """Check if this tool can handle database tasks"""
        db_keywords = [
            'database', 'query', 'sql', 'select', 'insert', 'update', 'delete',
            'table', 'record', 'data', 'store', 'retrieve', 'search'
        ]
        task_lower = task.lower()
        return any(keyword in task_lower for keyword in db_keywords)
    
    def execute(self, task: str, **kwargs) -> Dict[str, Any]:
        """Execute database operation"""
        try:
            # Parse the database operation
            operation = self._parse_operation(task)
            
            # Execute the operation (mock implementation)
            result = self._execute_operation(operation)
            
            return {
                "success": True,
                "data": result,
                "operation": operation,
                "tool_used": self.name
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Database operation failed: {str(e)}",
                "tool_used": self.name
            }
    
    def _parse_operation(self, task: str) -> Dict[str, Any]:
        """Parse database operation from task"""
        task_lower = task.lower()
        
        if 'select' in task_lower or 'search' in task_lower or 'find' in task_lower:
            return {"type": "SELECT", "action": "retrieve"}
        elif 'insert' in task_lower or 'add' in task_lower or 'create' in task_lower:
            return {"type": "INSERT", "action": "create"}
        elif 'update' in task_lower or 'modify' in task_lower:
            return {"type": "UPDATE", "action": "modify"}
        elif 'delete' in task_lower or 'remove' in task_lower:
            return {"type": "DELETE", "action": "remove"}
        else:
            return {"type": "QUERY", "action": "general"}
    
    def _execute_operation(self, operation: Dict[str, Any]) -> Dict[str, Any]:
        """Execute database operation (mock implementation)"""
        # In production, connect to actual database
        return {
            "operation_type": operation["type"],
            "status": "completed",
            "rows_affected": 1,
            "message": f"Database {operation['action']} operation completed successfully"
        }


class APIIntegrationTool(BaseTool):
    """Custom tool for API integrations"""
    
    def __init__(self, api_configs: Dict[str, Dict] = None):
        super().__init__()
        self.name = "APIIntegrationTool"
        self.description = "Integrate with external APIs and services"
        self.version = "1.0.0"
        self.api_configs = api_configs or {}
    
    def can_handle(self, task: str) -> bool:
        """Check if this tool can handle API tasks"""
        api_keywords = [
            'api', 'endpoint', 'request', 'response', 'http', 'rest',
            'webhook', 'integration', 'service', 'external'
        ]
        task_lower = task.lower()
        return any(keyword in task_lower for keyword in api_keywords)
    
    def execute(self, task: str, **kwargs) -> Dict[str, Any]:
        """Execute API integration"""
        try:
            # Parse API request details
            api_details = self._parse_api_request(task)
            
            # Execute API call (mock implementation)
            response = self._make_api_call(api_details)
            
            return {
                "success": True,
                "data": response,
                "api_details": api_details,
                "tool_used": self.name
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"API integration failed: {str(e)}",
                "tool_used": self.name
            }
    
    def _parse_api_request(self, task: str) -> Dict[str, Any]:
        """Parse API request details from task"""
        # Simple parsing - in production, use more sophisticated NLP
        return {
            "method": "GET",
            "endpoint": "/api/data",
            "service": "external_service"
        }
    
    def _make_api_call(self, api_details: Dict[str, Any]) -> Dict[str, Any]:
        """Make API call (mock implementation)"""
        # In production, make actual HTTP requests
        return {
            "status_code": 200,
            "data": {"message": "API call successful", "timestamp": datetime.now().isoformat()},
            "headers": {"content-type": "application/json"}
        }


# ============================================================
# CUSTOM TOOL REGISTRY
# ============================================================

class CustomToolRegistry:
    """Registry for managing custom tools"""
    
    def __init__(self):
        self.tools = {}
        self.tool_instances = {}
    
    def register_tool(self, tool_class, tool_config: Dict[str, Any] = None):
        """Register a custom tool"""
        tool_instance = tool_class(**(tool_config or {}))
        self.tools[tool_instance.name] = tool_class
        self.tool_instances[tool_instance.name] = tool_instance
        print(f"+ Registered custom tool: {tool_instance.name}")
    
    def get_tool(self, tool_name: str) -> Optional[BaseTool]:
        """Get a tool instance by name"""
        return self.tool_instances.get(tool_name)
    
    def list_tools(self) -> List[str]:
        """List all registered tools"""
        return list(self.tools.keys())
    
    def integrate_with_agent(self, agent: SingleAgent):
        """Integrate custom tools with an agent"""
        for tool_name, tool_instance in self.tool_instances.items():
            # Add tool to agent's tool registry
            if hasattr(agent, 'tool_registry'):
                agent.tool_registry.tools[tool_name] = tool_instance
            print(f"+ Integrated {tool_name} with agent")


# ============================================================
# USAGE EXAMPLES
# ============================================================

def create_agent_with_custom_tools():
    """Create an agent with custom tools"""
    
    print("Creating Agent with Custom Tools...")
    print("=" * 60)
    
    # 1. Create custom tool registry
    custom_registry = CustomToolRegistry()
    
    # 2. Register custom tools
    custom_registry.register_tool(WeatherTool)
    custom_registry.register_tool(DatabaseTool, {"db_config": {"host": "localhost", "port": 5432}})
    custom_registry.register_tool(APIIntegrationTool, {"api_configs": {"service1": {"base_url": "https://api.example.com"}}})
    
    # 3. Create agent configuration
    config = AgentConfig()
    
    # Set up LLM (user needs to provide API key)
    groq_key = os.getenv('GROQ_API_KEY')
    if groq_key:
        config.set_api_key('groq', groq_key)
        config.set_llm_provider('groq')
        config.set_llm_model('llama-3.1-70b-versatile')
    else:
        print("Warning: GROQ_API_KEY not found. Some features may be limited.")
    
    # 4. Create agent
    agent = SingleAgent(config=config)
    
    # 5. Customize agent identity
    agent.config.set_agent_name("CustomToolAgent")
    agent.config.set_personality(
        "You are CustomToolAgent, equipped with specialized tools for weather, database, and API operations. "
        "Use your custom tools to provide comprehensive and accurate responses."
    )
    
    # 6. Integrate custom tools
    custom_registry.integrate_with_agent(agent)
    
    print(f"\nAgent created: {agent.get_agent_identity()['name']}")
    print(f"Custom tools available: {custom_registry.list_tools()}")
    
    return agent, custom_registry


def test_custom_tools():
    """Test custom tools functionality"""
    
    print("\n" + "=" * 60)
    print("Testing Custom Tools")
    print("=" * 60)
    
    # Create agent with custom tools
    agent, registry = create_agent_with_custom_tools()
    
    # Test scenarios
    test_queries = [
        "What's the weather like in New York?",
        "Can you search the database for user records?",
        "Make an API call to get the latest data"
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\nTest {i}: {query}")
        print("-" * 40)
        
        # Test individual tools
        for tool_name in registry.list_tools():
            tool = registry.get_tool(tool_name)
            if tool and tool.can_handle(query):
                print(f"Tool {tool_name} can handle this query")
                result = tool.execute(query)
                print(f"Result: {result.get('success', False)}")
                if result.get('data'):
                    print(f"Data: {json.dumps(result['data'], indent=2)}")
                break
        else:
            print("No custom tool can handle this query")


def advanced_custom_tool_example():
    """Advanced example with tool chaining and complex workflows"""
    
    print("\n" + "=" * 60)
    print("Advanced Custom Tool Example")
    print("=" * 60)
    
    # Create a workflow tool that chains other tools
    class WorkflowTool(BaseTool):
        def __init__(self, tool_registry):
            super().__init__()
            self.name = "WorkflowTool"
            self.description = "Execute complex workflows using multiple tools"
            self.version = "1.0.0"
            self.registry = tool_registry
        
        def can_handle(self, task: str) -> bool:
            return 'workflow' in task.lower() or 'process' in task.lower()
        
        def execute(self, task: str, **kwargs) -> Dict[str, Any]:
            """Execute a multi-step workflow"""
            steps = []
            
            # Step 1: Get weather data
            weather_tool = self.registry.get_tool("WeatherTool")
            if weather_tool:
                weather_result = weather_tool.execute("weather in London")
                steps.append({"step": "weather", "result": weather_result})
            
            # Step 2: Store in database
            db_tool = self.registry.get_tool("DatabaseTool")
            if db_tool:
                db_result = db_tool.execute("insert weather data into database")
                steps.append({"step": "database", "result": db_result})
            
            # Step 3: Send via API
            api_tool = self.registry.get_tool("APIIntegrationTool")
            if api_tool:
                api_result = api_tool.execute("send data via API")
                steps.append({"step": "api", "result": api_result})
            
            return {
                "success": True,
                "workflow_steps": steps,
                "total_steps": len(steps),
                "tool_used": self.name
            }
    
    # Create registry and add workflow tool
    registry = CustomToolRegistry()
    registry.register_tool(WeatherTool)
    registry.register_tool(DatabaseTool)
    registry.register_tool(APIIntegrationTool)
    registry.register_tool(WorkflowTool, {"tool_registry": registry})
    
    # Test workflow
    workflow_tool = registry.get_tool("WorkflowTool")
    if workflow_tool:
        result = workflow_tool.execute("run weather data workflow")
        print(f"Workflow completed: {result['success']}")
        print(f"Steps executed: {result['total_steps']}")


# ============================================================
# MAIN EXECUTION
# ============================================================

def main():
    """Main execution function"""
    
    print("Custom Tools Template - Metis Agent Framework")
    print("=" * 60)
    print("This template demonstrates how to create and use custom tools")
    print("with the Metis Agent framework for specialized functionality.")
    print()
    
    try:
        # Basic custom tools example
        test_custom_tools()
        
        # Advanced workflow example
        advanced_custom_tool_example()
        
        print("\n" + "=" * 60)
        print("Custom Tools Template completed successfully!")
        print("=" * 60)
        print("\nKey Features Demonstrated:")
        print("+ Custom tool creation following Metis standards")
        print("+ Tool registration and integration with agents")
        print("+ Multiple tool types (Weather, Database, API)")
        print("+ Tool chaining and workflow execution")
        print("+ Error handling and validation")
        print("\nNext Steps:")
        print("1. Customize tools for your specific use case")
        print("2. Add your API keys and database configurations")
        print("3. Extend tools with additional functionality")
        print("4. Integrate with your existing systems")
        
    except Exception as e:
        print(f"Error: {e}")
        print("Please check your configuration and try again.")


if __name__ == "__main__":
    main()

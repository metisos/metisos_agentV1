#!/usr/bin/env python3
"""
Advanced Metis Agent Integration Template

This template demonstrates advanced integration patterns including:
- Custom tool integration
- Memory management and persistence
- Multi-agent coordination
- Event-driven processing
- Custom LLM provider integration

Usage:
    python advanced_integration_template.py
"""

from metis_agent import SingleAgent
from metis_agent.core.agent_config import AgentConfig
from metis_agent.tools.base import BaseTool
from metis_agent.core.models import ToolResult
import asyncio
import json
import time
from typing import Dict, List, Any, Optional
from datetime import datetime

class CustomAnalyticsTool(BaseTool):
    """
    Custom tool for data analytics integration.
    """
    
    def __init__(self):
        super().__init__(
            name="analytics_tool",
            description="Performs data analysis and generates insights from datasets"
        )
    
    def execute(self, query: str, context: Dict = None) -> ToolResult:
        """
        Execute analytics operations.
        """
        # Simulate data analysis
        analysis_result = {
            "dataset_size": 1000,
            "key_metrics": {
                "average": 42.5,
                "median": 40.0,
                "std_dev": 12.3
            },
            "insights": [
                "Data shows normal distribution",
                "No significant outliers detected",
                "Trend is stable over time period"
            ],
            "timestamp": datetime.now().isoformat()
        }
        
        return ToolResult(
            success=True,
            result=analysis_result,
            message="Analytics completed successfully"
        )

class CustomDatabaseTool(BaseTool):
    """
    Custom tool for database operations.
    """
    
    def __init__(self):
        super().__init__(
            name="database_tool",
            description="Performs database queries and data retrieval operations"
        )
    
    def execute(self, query: str, context: Dict = None) -> ToolResult:
        """
        Execute database operations.
        """
        # Simulate database query
        db_result = {
            "query": query,
            "rows_affected": 15,
            "execution_time_ms": 45,
            "data": [
                {"id": 1, "name": "Sample Record 1", "value": 100},
                {"id": 2, "name": "Sample Record 2", "value": 200},
                {"id": 3, "name": "Sample Record 3", "value": 150}
            ]
        }
        
        return ToolResult(
            success=True,
            result=db_result,
            message=f"Database query executed successfully, {db_result['rows_affected']} rows returned"
        )

class AgentOrchestrator:
    """
    Orchestrates multiple specialized agents for complex workflows.
    """
    
    def __init__(self):
        self.agents = {}
        self.workflow_history = []
    
    def create_specialized_agents(self):
        """
        Create multiple specialized agents for different tasks.
        """
        # Data Analysis Agent
        data_config = AgentConfig()
        data_config.set_llm_provider("groq")
        data_agent = SingleAgent(data_config)
        data_agent.config.agent_identity.update_agent_name("DataAnalyst")
        data_agent.config.agent_identity.set_custom_system_message(
            "You are a data analysis specialist. You interpret data, create visualizations, and provide statistical insights."
        )
        self.agents['data_analyst'] = data_agent
        
        # Code Generation Agent
        code_config = AgentConfig()
        code_config.set_llm_provider("groq")
        code_agent = SingleAgent(code_config)
        code_agent.config.agent_identity.update_agent_name("CodeGenerator")
        code_agent.config.agent_identity.set_custom_system_message(
            "You are a code generation specialist. You write clean, efficient code and provide technical solutions."
        )
        self.agents['code_generator'] = code_agent
        
        # Report Writer Agent
        report_config = AgentConfig()
        report_config.set_llm_provider("groq")
        report_agent = SingleAgent(report_config)
        report_agent.config.agent_identity.update_agent_name("ReportWriter")
        report_agent.config.agent_identity.set_custom_system_message(
            "You are a technical report writer. You create comprehensive, well-structured reports from technical data and analysis."
        )
        self.agents['report_writer'] = report_agent
    
    def execute_workflow(self, task: str, workflow_type: str = "sequential") -> Dict:
        """
        Execute a multi-agent workflow.
        """
        workflow_id = f"workflow_{int(time.time())}"
        workflow_start = time.time()
        
        results = {
            "workflow_id": workflow_id,
            "task": task,
            "type": workflow_type,
            "start_time": workflow_start,
            "agent_results": {},
            "final_result": None
        }
        
        try:
            if workflow_type == "sequential":
                results = self._execute_sequential_workflow(task, results)
            elif workflow_type == "parallel":
                results = self._execute_parallel_workflow(task, results)
            else:
                raise ValueError(f"Unknown workflow type: {workflow_type}")
            
            results["end_time"] = time.time()
            results["duration"] = results["end_time"] - results["start_time"]
            results["success"] = True
            
        except Exception as e:
            results["error"] = str(e)
            results["success"] = False
        
        self.workflow_history.append(results)
        return results
    
    def _execute_sequential_workflow(self, task: str, results: Dict) -> Dict:
        """
        Execute agents in sequence, passing results between them.
        """
        # Step 1: Data Analysis
        data_query = f"Analyze the requirements for this task: {task}"
        data_result = self.agents['data_analyst'].process_query(data_query)
        results["agent_results"]["data_analyst"] = data_result
        
        # Step 2: Code Generation (using data analysis results)
        code_query = f"Based on this analysis: {data_result[:500]}..., generate code for: {task}"
        code_result = self.agents['code_generator'].process_query(code_query)
        results["agent_results"]["code_generator"] = code_result
        
        # Step 3: Report Writing (using both previous results)
        report_query = f"Create a comprehensive report for task '{task}' using this analysis: {data_result[:300]}... and this code: {code_result[:300]}..."
        report_result = self.agents['report_writer'].process_query(report_query)
        results["agent_results"]["report_writer"] = report_result
        
        results["final_result"] = report_result
        return results
    
    def _execute_parallel_workflow(self, task: str, results: Dict) -> Dict:
        """
        Execute agents in parallel for independent tasks.
        """
        # All agents work on the task simultaneously
        queries = {
            'data_analyst': f"Provide data analysis perspective on: {task}",
            'code_generator': f"Provide code implementation for: {task}",
            'report_writer': f"Provide documentation perspective on: {task}"
        }
        
        # Execute all queries
        for agent_name, query in queries.items():
            result = self.agents[agent_name].process_query(query)
            results["agent_results"][agent_name] = result
        
        # Combine results
        combined_result = "MULTI-AGENT ANALYSIS REPORT\n\n"
        combined_result += f"Task: {task}\n\n"
        
        for agent_name, result in results["agent_results"].items():
            combined_result += f"=== {agent_name.upper()} PERSPECTIVE ===\n"
            combined_result += f"{result}\n\n"
        
        results["final_result"] = combined_result
        return results

class AdvancedAgentManager:
    """
    Advanced agent management with custom tools and memory persistence.
    """
    
    def __init__(self):
        self.agent = None
        self.custom_tools = {}
        self.memory_store = {}
        self.event_handlers = {}
    
    def initialize_agent_with_custom_tools(self):
        """
        Initialize agent with custom tools integrated.
        """
        # Create agent configuration
        config = AgentConfig()
        config.set_memory_enabled(True)
        config.set_titans_memory(True)
        
        # Create agent
        self.agent = SingleAgent(config)
        
        # Create and register custom tools
        analytics_tool = CustomAnalyticsTool()
        database_tool = CustomDatabaseTool()
        
        self.custom_tools[analytics_tool.name] = analytics_tool
        self.custom_tools[database_tool.name] = database_tool
        
        # Register tools with agent's tool registry
        for tool_name, tool in self.custom_tools.items():
            self.agent.tools_registry.register_tool(tool)
        
        # Set specialized personality
        self.agent.config.agent_identity.update_agent_name("AdvancedAssistant")
        self.agent.config.agent_identity.set_custom_system_message(
            "You are an advanced AI assistant with specialized tools for analytics and database operations. "
            "You can perform complex data analysis, execute database queries, and provide comprehensive insights. "
            "Always use the appropriate tools when available to provide accurate, data-driven responses."
        )
    
    def process_with_memory_persistence(self, query: str, session_id: str = None) -> Dict:
        """
        Process query with enhanced memory persistence.
        """
        if not session_id:
            session_id = f"session_{int(time.time())}"
        
        # Store query context
        context = {
            "timestamp": datetime.now().isoformat(),
            "session_id": session_id,
            "query": query,
            "available_tools": list(self.custom_tools.keys())
        }
        
        # Process with agent
        response = self.agent.process_query(query, session_id=session_id)
        
        # Store in memory
        if session_id not in self.memory_store:
            self.memory_store[session_id] = []
        
        self.memory_store[session_id].append({
            "context": context,
            "response": response,
            "agent_identity": self.agent.get_agent_identity()
        })
        
        return {
            "session_id": session_id,
            "response": response,
            "context": context,
            "memory_entries": len(self.memory_store[session_id])
        }
    
    def get_session_history(self, session_id: str) -> List[Dict]:
        """
        Retrieve session history.
        """
        return self.memory_store.get(session_id, [])
    
    def export_session_data(self, session_id: str, format: str = "json") -> str:
        """
        Export session data in specified format.
        """
        history = self.get_session_history(session_id)
        
        if format == "json":
            return json.dumps(history, indent=2)
        elif format == "text":
            text_output = f"SESSION HISTORY: {session_id}\n"
            text_output += "=" * 50 + "\n\n"
            
            for i, entry in enumerate(history, 1):
                text_output += f"INTERACTION {i}\n"
                text_output += f"Time: {entry['context']['timestamp']}\n"
                text_output += f"Query: {entry['context']['query']}\n"
                text_output += f"Response: {entry['response']}\n\n"
            
            return text_output
        else:
            raise ValueError(f"Unsupported format: {format}")

def demonstrate_basic_integration():
    """
    Demonstrate basic advanced integration features.
    """
    print("=== Basic Advanced Integration ===")
    
    manager = AdvancedAgentManager()
    manager.initialize_agent_with_custom_tools()
    
    # Test custom tools integration
    queries = [
        "Can you analyze some sample data for me?",
        "Please run a database query to get user information",
        "What tools do you have available?"
    ]
    
    session_id = "demo_session_1"
    
    for query in queries:
        print(f"\nUser: {query}")
        result = manager.process_with_memory_persistence(query, session_id)
        print(f"Agent: {result['response']}")
    
    # Export session history
    print("\n=== Session History ===")
    history = manager.export_session_data(session_id, "text")
    print(history[:500] + "..." if len(history) > 500 else history)

def demonstrate_multi_agent_workflow():
    """
    Demonstrate multi-agent orchestration.
    """
    print("\n=== Multi-Agent Workflow Demo ===")
    
    orchestrator = AgentOrchestrator()
    orchestrator.create_specialized_agents()
    
    # Test sequential workflow
    task = "Create a Python web scraping tool for e-commerce price monitoring"
    
    print(f"\nExecuting sequential workflow for: {task}")
    result = orchestrator.execute_workflow(task, "sequential")
    
    print(f"Workflow completed in {result['duration']:.2f} seconds")
    print(f"Final result: {result['final_result'][:300]}...")
    
    # Test parallel workflow
    print(f"\nExecuting parallel workflow for: {task}")
    result = orchestrator.execute_workflow(task, "parallel")
    
    print(f"Workflow completed in {result['duration']:.2f} seconds")
    print(f"Final result: {result['final_result'][:300]}...")

def main():
    """
    Main function demonstrating advanced integration patterns.
    """
    print("=== Advanced Metis Agent Integration Template ===")
    print()
    
    # Check API keys
    import os
    if not any(os.getenv(key) for key in ['GROQ_API_KEY', 'OPENAI_API_KEY', 'ANTHROPIC_API_KEY']):
        print("WARNING: No API keys found. Please set environment variables:")
        print("- GROQ_API_KEY, OPENAI_API_KEY, or ANTHROPIC_API_KEY")
        print()
    
    try:
        # Demonstrate basic advanced integration
        demonstrate_basic_integration()
        
        print("\n" + "="*60)
        
        # Demonstrate multi-agent workflows
        demonstrate_multi_agent_workflow()
        
    except Exception as e:
        print(f"Error during demonstration: {e}")
        print("Make sure you have configured your API keys!")

if __name__ == "__main__":
    main()

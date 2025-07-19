"""
Web Server Example

This example demonstrates how to set up a web API for your Metis Agent.
"""
import os
from flask import Flask, request, jsonify
from metis_agent import SingleAgent, configure_llm

# Create Flask app
app = Flask(__name__)

# Create a global agent instance
agent = None

def initialize_agent():
    """Initialize the agent with configuration."""
    global agent
    
    # Get API key from environment variable
    api_key = os.environ.get("OPENAI_API_KEY")
    
    # Configure LLM
    configure_llm("openai", "gpt-4o", api_key)
    
    # Create agent with Titans memory
    agent = SingleAgent(use_titans_memory=True)
    
    print("Agent initialized successfully!")

@app.route('/')
def index():
    """Root endpoint."""
    return jsonify({
        "status": "ok",
        "message": "Metis Agent API is running",
        "endpoints": [
            "/api/query",
            "/api/agent-info",
            "/api/memory-insights"
        ]
    })

@app.route('/api/query', methods=['POST'])
def process_query():
    """Process a query from the user."""
    try:
        # Get the query from the request
        data = request.json
        
        if not data or 'query' not in data:
            return jsonify({'error': 'Missing query parameter'}), 400
            
        query = data['query']
        session_id = data.get('session_id', 'default_session')
        tool_name = data.get('tool_name')
        
        # Process the query
        response = agent.process_query(query, session_id=session_id, tool_name=tool_name)
        
        # Return the response
        return jsonify({
            'response': response,
            'session_id': session_id
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/api/agent-info', methods=['GET'])
def get_agent_info():
    """Return information about the agent."""
    try:
        # Get agent identity
        identity = agent.get_agent_identity()
        
        return jsonify(identity)
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/api/memory-insights', methods=['GET'])
def get_memory_insights():
    """Return memory insights."""
    try:
        # Get memory insights
        insights = agent.get_memory_insights()
        
        return jsonify(insights)
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

def main():
    """Run the web server."""
    # Initialize the agent
    initialize_agent()
    
    # Set host and port
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    
    # Run the app
    print(f"Starting web server on {host}:{port}...")
    app.run(host=host, port=port, debug=True)

if __name__ == "__main__":
    main()
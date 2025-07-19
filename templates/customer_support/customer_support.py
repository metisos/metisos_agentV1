"""
Customer Support Template

This template provides a specialized agent for handling customer inquiries.
It leverages the built-in tools from the Metis Agent framework.
"""
import os
import json
from metis_agent import SingleAgent
from metis_agent.tools.content_generation import ContentGenerationTool

class CustomerSupportAgent:
    """Specialized agent for handling customer inquiries."""
    
    def __init__(self, api_key=None, faq_file=None, use_titans_memory=True):
        """Initialize the customer support agent."""
        # Create the agent
        self.agent = SingleAgent(
            use_titans_memory=use_titans_memory,
            llm_provider="openai",
            llm_model="gpt-4o"
        )
        
        # Set API keys if provided
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
            
        # Load FAQ data if provided
        self.faq_data = self._load_faq_data(faq_file)
        
        print("Customer Support Agent initialized")
    
    def _load_faq_data(self, faq_file):
        """Load FAQ data from a file or use default data."""
        if faq_file and os.path.exists(faq_file):
            with open(faq_file, 'r') as f:
                return json.load(f)
        else:
            # Default FAQ data
            return [
                {
                    "question": "What are your business hours?",
                    "answer": "Our customer support is available 24/7. Our physical offices are open Monday to Friday, 9 AM to 5 PM local time."
                },
                {
                    "question": "How do I reset my password?",
                    "answer": "To reset your password, go to the login page and click on 'Forgot Password'. Follow the instructions sent to your email."
                },
                {
                    "question": "How do I cancel my subscription?",
                    "answer": "You can cancel your subscription by going to Account Settings > Subscription > Cancel Subscription. Please note that you'll still have access until the end of your billing period."
                },
                {
                    "question": "What payment methods do you accept?",
                    "answer": "We accept all major credit cards (Visa, MasterCard, American Express), PayPal, and bank transfers for annual subscriptions."
                },
                {
                    "question": "How do I contact customer support?",
                    "answer": "You can contact our customer support team via email at support@example.com, through the in-app chat, or by calling our toll-free number 1-800-123-4567."
                }
            ]
    
    def handle_inquiry(self, inquiry, session_id=None):
        """Handle a customer inquiry."""
        # First, check if the inquiry matches any FAQ
        faq_answer = self._check_faq(inquiry)
        if faq_answer:
            return faq_answer
        
        # If not an FAQ, process as a general inquiry
        response = self.agent.process_query(inquiry, session_id=session_id)
        
        return response
    
    def _check_faq(self, inquiry):
        """Check if the inquiry matches any FAQ."""
        # Simple keyword matching for demonstration purposes
        # In a real implementation, you would use a more sophisticated approach
        inquiry_lower = inquiry.lower()
        
        for faq in self.faq_data:
            question_lower = faq["question"].lower()
            
            # Check for keyword matches
            keywords = question_lower.split()
            if any(keyword in inquiry_lower for keyword in keywords if len(keyword) > 3):
                return f"## {faq['question']}\n\n{faq['answer']}\n\nIs there anything else you'd like to know?"
        
        return None
    
    def create_ticket(self, issue, priority=None, category=None, session_id=None):
        """Create a support ticket for the given issue."""
        # Format the ticket creation query
        if priority and category:
            query = f"Create a {priority} priority support ticket in the {category} category for this issue: {issue}"
        elif priority:
            query = f"Create a {priority} priority support ticket for this issue: {issue}"
        elif category:
            query = f"Create a support ticket in the {category} category for this issue: {issue}"
        else:
            query = f"Create a support ticket for this issue: {issue}"
        
        # Process the query using the ContentGenerationTool
        response = self.agent.process_query(
            query,
            session_id=session_id,
            tool_name="ContentGenerationTool"
        )
        
        return response
    
    def answer_faq(self, question, session_id=None):
        """Answer a frequently asked question."""
        # First, check if the question matches any FAQ
        faq_answer = self._check_faq(question)
        if faq_answer:
            return faq_answer
        
        # If not in FAQ, process as a general question
        query = f"Answer this customer support question: {question}"
        
        response = self.agent.process_query(
            query,
            session_id=session_id
        )
        
        return response
    
    def generate_response_template(self, scenario, tone="professional", session_id=None):
        """Generate a response template for a specific customer support scenario."""
        # Format the template generation query
        query = f"Create a {tone} customer support response template for this scenario: {scenario}"
        
        # Process the query using the ContentGenerationTool
        response = self.agent.process_query(
            query,
            session_id=session_id,
            tool_name="ContentGenerationTool"
        )
        
        return response


def main():
    """Run a demonstration of the customer support agent."""
    # Get API key from environment variable
    api_key = os.environ.get("OPENAI_API_KEY")
    
    # Create the customer support agent
    agent = CustomerSupportAgent(api_key=api_key)
    
    # Define a session ID
    session_id = "support_session"
    
    # Handle an FAQ question
    faq_question = "What are your business hours?"
    print(f"FAQ Question: {faq_question}")
    
    faq_response = agent.answer_faq(faq_question, session_id=session_id)
    print(f"FAQ Response:\n{faq_response}")
    
    # Create a support ticket
    issue = "I'm having trouble logging into my account. It says my password is incorrect, but I'm sure it's right."
    print(f"\nTicket Creation Request: {issue}")
    
    ticket_response = agent.create_ticket(issue, priority="high", category="account", session_id=session_id)
    print(f"Ticket Response:\n{ticket_response}")
    
    # Handle a general inquiry
    inquiry = "Can you tell me more about your premium subscription features?"
    print(f"\nGeneral Inquiry: {inquiry}")
    
    inquiry_response = agent.handle_inquiry(inquiry, session_id=session_id)
    print(f"Inquiry Response:\n{inquiry_response}")
    
    # Generate a response template
    scenario = "Customer requesting a refund for a service they were unhappy with"
    print(f"\nResponse Template Request: {scenario}")
    
    template_response = agent.generate_response_template(scenario, tone="empathetic", session_id=session_id)
    print(f"Response Template:\n{template_response}")

if __name__ == "__main__":
    main()
"""
Customer Support Template

This template provides a specialized agent for handling customer inquiries.
"""
import os
import json
import re
from metis_agent import SingleAgent, BaseTool, register_tool

class FAQTool(BaseTool):
    """Tool for handling frequently asked questions."""
    
    name = "faq_tool"
    description = "Answers frequently asked questions based on a knowledge base"
    
    def __init__(self, faq_file=None):
        """Initialize the FAQ tool."""
        self.faq_data = self._load_faq_data(faq_file)
        
    def can_handle(self, task):
        """Determine if this tool can handle the task."""
        # Check if the task matches any FAQ keywords
        task_lower = task.lower()
        
        # Look for question patterns
        question_indicators = [
            "how", "what", "when", "where", "why", "who", "which", "can", "do", "does", "is", "are"
        ]
        
        # Check if it starts with a question word
        if any(task_lower.startswith(indicator) for indicator in question_indicators):
            return True
            
        # Check if it ends with a question mark
        if task_lower.endswith("?"):
            return True
            
        # Check if it contains FAQ keywords
        faq_keywords = ["faq", "question", "answer", "help", "support", "issue", "problem"]
        if any(keyword in task_lower for keyword in faq_keywords):
            return True
            
        return False
        
    def execute(self, task):
        """Execute the FAQ task."""
        # Find the most relevant FAQ entry
        best_match, confidence = self._find_best_match(task)
        
        if confidence > 0.7:  # High confidence threshold
            return self._format_faq_response(best_match)
        else:
            # If no good match, provide a general response
            return self._format_general_response(task)
    
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
    
    def _find_best_match(self, query):
        """Find the best matching FAQ entry for the query."""
        query_lower = query.lower()
        best_match = None
        highest_score = 0
        
        for entry in self.faq_data:
            question = entry["question"].lower()
            
            # Calculate a simple similarity score
            # In a real implementation, you would use a more sophisticated approach
            words_query = set(re.findall(r'\b\w+\b', query_lower))
            words_question = set(re.findall(r'\b\w+\b', question))
            
            # Calculate Jaccard similarity
            if not words_query or not words_question:
                continue
                
            intersection = len(words_query.intersection(words_question))
            union = len(words_query.union(words_question))
            
            score = intersection / union if union > 0 else 0
            
            if score > highest_score:
                highest_score = score
                best_match = entry
        
        return best_match, highest_score
    
    def _format_faq_response(self, faq_entry):
        """Format the FAQ response."""
        if not faq_entry:
            return "I'm sorry, I couldn't find an answer to your question in our FAQ."
            
        response = f"## {faq_entry['question']}\n\n"
        response += f"{faq_entry['answer']}\n\n"
        response += "Is there anything else you'd like to know?"
        
        return response
    
    def _format_general_response(self, query):
        """Format a general response when no FAQ match is found."""
        response = "I don't have a specific answer to that question in my FAQ database. "
        response += "Here are some options that might help:\n\n"
        response += "1. Try rephrasing your question\n"
        response += "2. Contact our customer support team at support@example.com\n"
        response += "3. Check our documentation at https://example.com/docs\n\n"
        response += "How else can I assist you today?"
        
        return response


class TicketCreationTool(BaseTool):
    """Tool for creating support tickets."""
    
    name = "ticket_creation_tool"
    description = "Creates support tickets based on customer issues"
    
    def can_handle(self, task):
        """Determine if this tool can handle the task."""
        ticket_keywords = [
            "ticket", "issue", "problem", "bug", "error", "not working",
            "broken", "failed", "help me with", "support request"
        ]
        return any(keyword in task.lower() for keyword in ticket_keywords)
        
    def execute(self, task):
        """Execute the ticket creation task."""
        # Extract ticket information
        category = self._extract_category(task)
        priority = self._extract_priority(task)
        
        # Create a ticket
        ticket = self._create_ticket(task, category, priority)
        
        return ticket
    
    def _extract_category(self, task):
        """Extract the ticket category from the task."""
        task_lower = task.lower()
        
        categories = {
            "billing": ["billing", "payment", "charge", "invoice", "subscription"],
            "technical": ["technical", "bug", "error", "not working", "broken", "failed"],
            "account": ["account", "login", "password", "access", "profile"],
            "feature": ["feature", "enhancement", "improvement", "suggestion"],
            "other": ["other", "general", "question", "inquiry"]
        }
        
        for category, keywords in categories.items():
            if any(keyword in task_lower for keyword in keywords):
                return category
        
        # Default category
        return "general"
    
    def _extract_priority(self, task):
        """Extract the ticket priority from the task."""
        task_lower = task.lower()
        
        if "urgent" in task_lower or "emergency" in task_lower or "critical" in task_lower:
            return "high"
        elif "important" in task_lower or "significant" in task_lower:
            return "medium"
        else:
            return "normal"
    
    def _create_ticket(self, task, category, priority):
        """Create a support ticket."""
        # In a real implementation, this would create a ticket in a ticketing system
        
        # Generate a ticket ID
        import random
        ticket_id = f"TICKET-{random.randint(10000, 99999)}"
        
        response = f"# Support Ticket Created\n\n"
        response += f"## Ticket ID: {ticket_id}\n\n"
        response += f"**Category:** {category.capitalize()}\n"
        response += f"**Priority:** {priority.capitalize()}\n"
        response += f"**Description:** {task}\n\n"
        
        response += "## Next Steps\n\n"
        response += "Your ticket has been created and will be processed by our support team. "
        
        if priority == "high":
            response += "Due to the high priority, you can expect a response within 2 hours."
        elif priority == "medium":
            response += "You can expect a response within 24 hours."
        else:
            response += "You can expect a response within 48 hours."
        
        response += "\n\nYou will receive updates about your ticket via email. "
        response += "You can also check the status of your ticket by logging into your account and visiting the Support section."
        
        return response


class CustomerSupportAgent:
    """Specialized agent for handling customer inquiries."""
    
    def __init__(self, api_key=None, faq_file=None, use_titans_memory=True):
        """Initialize the customer support agent."""
        # Register the customer support tools
        register_tool("faq_tool", FAQTool(faq_file=faq_file))
        register_tool("ticket_creation_tool", TicketCreationTool())
        
        # Create the agent
        self.agent = SingleAgent(
            use_titans_memory=use_titans_memory,
            llm_provider="openai",
            llm_model="gpt-4o"
        )
        
        print("Customer Support Agent initialized")
    
    def handle_inquiry(self, inquiry, session_id=None):
        """Handle a customer inquiry."""
        # Process the inquiry
        response = self.agent.process_query(inquiry, session_id=session_id)
        
        return response
    
    def create_ticket(self, issue, session_id=None):
        """Create a support ticket for the given issue."""
        # Process the ticket creation request
        response = self.agent.process_query(
            issue,
            session_id=session_id,
            tool_name="ticket_creation_tool"
        )
        
        return response
    
    def answer_faq(self, question, session_id=None):
        """Answer a frequently asked question."""
        # Process the FAQ request
        response = self.agent.process_query(
            question,
            session_id=session_id,
            tool_name="faq_tool"
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
    
    ticket_response = agent.create_ticket(issue, session_id=session_id)
    print(f"Ticket Response:\n{ticket_response}")
    
    # Handle a general inquiry
    inquiry = "Can you tell me more about your premium subscription features?"
    print(f"\nGeneral Inquiry: {inquiry}")
    
    inquiry_response = agent.handle_inquiry(inquiry, session_id=session_id)
    print(f"Inquiry Response:\n{inquiry_response}")

if __name__ == "__main__":
    main()
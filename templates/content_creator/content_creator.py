"""
Content Creator Template

This template provides a specialized agent for creating various types of content.
It leverages the built-in tools from the Metis Agent framework.
"""
import os
from metis_agent import SingleAgent
from metis_agent.tools.content_generation import ContentGenerationTool

class ContentCreator:
    """Specialized agent for creating various types of content."""
    
    def __init__(self, api_key=None, use_titans_memory=True):
        """Initialize the content creator."""
        # Create the agent
        self.agent = SingleAgent(
            use_titans_memory=use_titans_memory,
            llm_provider="openai",
            llm_model="gpt-4o"
        )
        
        # Set API keys if provided
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
        
        print("Content Creator initialized")
    
    def create_blog_post(self, topic, tone="professional", length="medium", session_id=None):
        """Create a blog post on the given topic."""
        # Format the blog post request
        query = f"Write a {tone} {length} blog post about {topic}"
        
        # Process the query using the ContentGenerationTool
        response = self.agent.process_query(
            query,
            session_id=session_id,
            tool_name="ContentGenerationTool"
        )
        
        return response
    
    def create_social_media_post(self, platform, topic, session_id=None):
        """Create a social media post for the given platform and topic."""
        # Format the social media post request
        query = f"Create a {platform} post about {topic}"
        
        # Process the query using the ContentGenerationTool
        response = self.agent.process_query(
            query,
            session_id=session_id,
            tool_name="ContentGenerationTool"
        )
        
        return response
    
    def create_content_series(self, topic, platforms, session_id=None):
        """Create a series of content pieces for different platforms."""
        results = {}
        
        # Create a blog post as the main content
        blog_post = self.create_blog_post(topic, session_id=session_id)
        results["blog"] = blog_post
        
        # Create social media posts for each platform
        for platform in platforms:
            social_post = self.create_social_media_post(platform, topic, session_id=session_id)
            results[platform] = social_post
        
        return results
    
    def create_email_newsletter(self, topic, audience="general", session_id=None):
        """Create an email newsletter on the given topic."""
        # Format the email newsletter request
        query = f"Write an email newsletter about {topic} for a {audience} audience"
        
        # Process the query using the ContentGenerationTool
        response = self.agent.process_query(
            query,
            session_id=session_id,
            tool_name="ContentGenerationTool"
        )
        
        return response
    
    def create_product_description(self, product_name, features, benefits, session_id=None):
        """Create a product description."""
        # Format the product description request
        query = f"Write a compelling product description for {product_name} with these features: {features} and benefits: {benefits}"
        
        # Process the query using the ContentGenerationTool
        response = self.agent.process_query(
            query,
            session_id=session_id,
            tool_name="ContentGenerationTool"
        )
        
        return response
    
    def create_video_script(self, topic, duration="5 minutes", style="educational", session_id=None):
        """Create a video script on the given topic."""
        # Format the video script request
        query = f"Write a {style} video script about {topic} for a {duration} video"
        
        # Process the query using the ContentGenerationTool
        response = self.agent.process_query(
            query,
            session_id=session_id,
            tool_name="ContentGenerationTool"
        )
        
        return response


def main():
    """Run a demonstration of the content creator."""
    # Get API key from environment variable
    api_key = os.environ.get("OPENAI_API_KEY")
    
    # Create the content creator
    creator = ContentCreator(api_key=api_key)
    
    # Define a session ID
    session_id = "content_session"
    
    # Create a blog post
    topic = "Artificial Intelligence in Healthcare"
    print(f"Blog Post Request: {topic}")
    
    blog_post = creator.create_blog_post(topic, tone="professional", length="medium", session_id=session_id)
    print(f"Blog Post:\n{blog_post}")
    
    # Create social media posts
    print("\nSocial Media Post Requests:")
    
    platforms = ["twitter", "linkedin"]
    for platform in platforms:
        print(f"\nCreating {platform.capitalize()} post...")
        social_post = creator.create_social_media_post(platform, topic, session_id=session_id)
        print(f"{platform.capitalize()} Post:\n{social_post}")
    
    # Create an email newsletter
    print("\nEmail Newsletter Request:")
    newsletter = creator.create_email_newsletter(topic, audience="healthcare professionals", session_id=session_id)
    print(f"Email Newsletter:\n{newsletter}")

if __name__ == "__main__":
    main()
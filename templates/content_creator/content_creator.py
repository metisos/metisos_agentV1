"""
Content Creator Template

This template provides a specialized agent for creating various types of content.
"""
import os
from metis_agent import SingleAgent, BaseTool, register_tool

class BlogPostTool(BaseTool):
    """Tool for generating blog posts."""
    
    name = "blog_post_tool"
    description = "Generates blog posts on various topics"
    
    def can_handle(self, task):
        """Determine if this tool can handle the task."""
        blog_keywords = [
            "blog post", "article", "write a blog", "create a blog",
            "blog content", "blog article"
        ]
        return any(keyword in task.lower() for keyword in blog_keywords)
        
    def execute(self, task):
        """Execute the blog post generation task."""
        # Extract topic and parameters from the task
        topic = self._extract_topic(task)
        tone = self._extract_tone(task)
        length = self._extract_length(task)
        
        # Generate the blog post
        blog_post = self._generate_blog_post(topic, tone, length)
        
        return blog_post
    
    def _extract_topic(self, task):
        """Extract the blog post topic from the task."""
        # This is a simplified implementation
        task_lower = task.lower()
        
        # Look for common patterns
        patterns = [
            "blog post about ",
            "blog post on ",
            "article about ",
            "article on ",
            "write a blog about ",
            "write a blog on ",
            "create a blog about ",
            "create a blog on "
        ]
        
        for pattern in patterns:
            if pattern in task_lower:
                parts = task_lower.split(pattern, 1)
                if len(parts) > 1:
                    return parts[1].strip().split()[0].capitalize()
        
        # Default topic if we can't extract one
        return "Technology"
    
    def _extract_tone(self, task):
        """Extract the desired tone from the task."""
        task_lower = task.lower()
        
        tones = {
            "professional": ["professional", "formal", "business", "corporate"],
            "casual": ["casual", "informal", "conversational", "friendly"],
            "technical": ["technical", "detailed", "in-depth", "comprehensive"],
            "humorous": ["humorous", "funny", "light-hearted", "entertaining"]
        }
        
        for tone, keywords in tones.items():
            if any(keyword in task_lower for keyword in keywords):
                return tone
        
        # Default tone
        return "professional"
    
    def _extract_length(self, task):
        """Extract the desired length from the task."""
        task_lower = task.lower()
        
        if "short" in task_lower:
            return "short"
        elif "long" in task_lower or "detailed" in task_lower:
            return "long"
        else:
            return "medium"
    
    def _generate_blog_post(self, topic, tone, length):
        """Generate a blog post based on the topic, tone, and length."""
        # In a real implementation, this would use the LLM to generate content
        
        # Determine word count based on length
        word_counts = {
            "short": "500-700",
            "medium": "1000-1500",
            "long": "2000-2500"
        }
        
        word_count = word_counts.get(length, "1000-1500")
        
        blog_post = f"# {topic}: A {tone.capitalize()} Blog Post\n\n"
        
        blog_post += "## Introduction\n\n"
        blog_post += f"This is the introduction to the blog post about {topic}. "
        blog_post += "It sets the stage for the rest of the article and captures the reader's attention.\n\n"
        
        blog_post += "## Main Section 1\n\n"
        blog_post += f"This section covers the first main point about {topic}. "
        blog_post += "It provides valuable information and insights for the reader.\n\n"
        
        blog_post += "## Main Section 2\n\n"
        blog_post += "This section covers the second main point. "
        blog_post += "It builds upon the first section and adds more depth to the article.\n\n"
        
        blog_post += "## Main Section 3\n\n"
        blog_post += "This section covers the third main point. "
        blog_post += "It provides additional perspectives and information on the topic.\n\n"
        
        blog_post += "## Conclusion\n\n"
        blog_post += f"This conclusion summarizes the key points about {topic} and provides a call to action for the reader.\n\n"
        
        blog_post += f"*Word count: {word_count} words*\n"
        blog_post += f"*Tone: {tone}*\n"
        
        return blog_post


class SocialMediaTool(BaseTool):
    """Tool for generating social media content."""
    
    name = "social_media_tool"
    description = "Generates social media posts for various platforms"
    
    def can_handle(self, task):
        """Determine if this tool can handle the task."""
        social_keywords = [
            "social media", "tweet", "twitter", "facebook post", "instagram",
            "linkedin", "social post"
        ]
        return any(keyword in task.lower() for keyword in social_keywords)
        
    def execute(self, task):
        """Execute the social media content generation task."""
        # Extract platform and topic from the task
        platform = self._extract_platform(task)
        topic = self._extract_topic(task)
        
        # Generate the social media content
        content = self._generate_social_media_content(platform, topic)
        
        return content
    
    def _extract_platform(self, task):
        """Extract the social media platform from the task."""
        task_lower = task.lower()
        
        platforms = {
            "twitter": ["twitter", "tweet", "x"],
            "facebook": ["facebook", "fb"],
            "instagram": ["instagram", "ig"],
            "linkedin": ["linkedin", "li"],
            "tiktok": ["tiktok", "tt"]
        }
        
        for platform, keywords in platforms.items():
            if any(keyword in task_lower for keyword in keywords):
                return platform
        
        # Default platform
        return "twitter"
    
    def _extract_topic(self, task):
        """Extract the topic from the task."""
        # This is a simplified implementation
        task_lower = task.lower()
        
        # Look for common patterns
        patterns = [
            "post about ",
            "post on ",
            "content about ",
            "content on ",
            "write about ",
            "write on "
        ]
        
        for pattern in patterns:
            if pattern in task_lower:
                parts = task_lower.split(pattern, 1)
                if len(parts) > 1:
                    return parts[1].strip().split()[0].capitalize()
        
        # Default topic if we can't extract one
        return "Technology"
    
    def _generate_social_media_content(self, platform, topic):
        """Generate social media content based on the platform and topic."""
        # In a real implementation, this would use the LLM to generate content
        
        content = f"# Social Media Content for {platform.capitalize()}\n\n"
        content += f"## Topic: {topic}\n\n"
        
        if platform.lower() == "twitter":
            content += "### Twitter Post\n\n"
            content += f"Just learned some amazing facts about #{topic}! 🤯 Did you know that [interesting fact]? This changes everything about how we [related activity]. #Learning #{topic} #Mindblown\n\n"
            content += "Character count: 150 (within Twitter's 280 character limit)\n\n"
            
        elif platform.lower() == "facebook":
            content += "### Facebook Post\n\n"
            content += f"📣 **{topic} - What You Need to Know**\n\n"
            content += "I've been researching [topic] lately and wanted to share some fascinating insights:\n\n"
            content += "1. [First insight about the topic]\n"
            content += "2. [Second insight about the topic]\n"
            content += "3. [Third insight about the topic]\n\n"
            content += "What are your thoughts on this? Have you had any experiences with [topic]? Share in the comments below! 👇\n\n"
            
        elif platform.lower() == "instagram":
            content += "### Instagram Post\n\n"
            content += f"**Caption:**\n{topic} has been on my mind lately. Here's what I've discovered... 🧐\n\n"
            content += "[Main point about the topic]\n\n"
            content += "Double tap if you found this helpful! ❤️\n\n"
            content += f"##{topic} #Learning #Growth #Mindset #Knowledge\n\n"
            content += "**Image Suggestion:** [Description of an image that would work well with this post]\n\n"
            
        elif platform.lower() == "linkedin":
            content += "### LinkedIn Post\n\n"
            content += f"**{topic}: A Professional Perspective**\n\n"
            content += "I've recently been exploring [topic] and its implications for our industry. Here are three key takeaways:\n\n"
            content += "1. [Professional insight about the topic]\n"
            content += "2. [How this relates to industry trends]\n"
            content += "3. [Strategic recommendation]\n\n"
            content += "What has been your experience with [topic] in your professional journey? I'd love to hear your thoughts.\n\n"
            content += "#ProfessionalDevelopment #IndustryInsights #CareerGrowth\n\n"
            
        else:
            content += f"### {platform.capitalize()} Post\n\n"
            content += f"Content about {topic} tailored for {platform}.\n\n"
            content += "[Platform-specific content would be generated here]\n\n"
        
        return content


class ContentCreator:
    """Specialized agent for creating various types of content."""
    
    def __init__(self, api_key=None, use_titans_memory=True):
        """Initialize the content creator."""
        # Register the content creation tools
        register_tool("blog_post_tool", BlogPostTool)
        register_tool("social_media_tool", SocialMediaTool)
        
        # Create the agent
        self.agent = SingleAgent(
            use_titans_memory=use_titans_memory,
            llm_provider="openai",
            llm_model="gpt-4o"
        )
        
        print("Content Creator initialized")
    
    def create_blog_post(self, topic, tone="professional", length="medium", session_id=None):
        """Create a blog post on the given topic."""
        # Process the blog post request
        query = f"Write a {tone} {length} blog post about {topic}"
        
        response = self.agent.process_query(
            query,
            session_id=session_id,
            tool_name="blog_post_tool"
        )
        
        return response
    
    def create_social_media_post(self, platform, topic, session_id=None):
        """Create a social media post for the given platform and topic."""
        # Process the social media post request
        query = f"Create a {platform} post about {topic}"
        
        response = self.agent.process_query(
            query,
            session_id=session_id,
            tool_name="social_media_tool"
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

if __name__ == "__main__":
    main()
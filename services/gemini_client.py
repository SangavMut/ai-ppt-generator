import google.generativeai as genai
import json
import os

class GeminiClient:
    def __init__(self):
        """Initialize the Gemini Client"""
        self.api_key = os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("Gemini API key is required. Set GEMINI_API_KEY environment variable or pass it to the constructor.")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemma-3-27b-it')

    def generate_content_outline(self, topic, num_slides=5):
        """Generate content outline using Gemini"""
        prompt = f"""
        Create a detailed outline for a PowerPoint presentation on "{topic}" with {num_slides} slides.
        Return the response as a JSON array with the following structure:
        [
            {{
                "title": "Slide Title",
                "content": "Main content points as bullet points",
                "slide_type": "title|content|image|conclusion"
            }}
        ]"""

        try:
            response = self.model.generate_content(prompt)
            content = response.text.strip()

            if content.startswith('```json'):
                content = content.split('```json')[1].split('```')[0].strip()

            if not content.startswith('[') or not content.endswith(']'):
                print("Invalid JSON format received. Using fallback outline.")
                return self._get_fallback_outline(topic, num_slides)

            return json.loads(content)

        except Exception as e:
            print(f"Error generating content: {e}")
            return self._get_fallback_outline(topic, num_slides)

    def _get_fallback_outline(self, topic, num_slides):
        """Fallback outline if Gemini fails"""
        return [
            {"title": f"Introduction to {topic}", "content": "• Overview of the topic\n• Key objectives\n• What to expect", "slide_type": "title"},
            {"title": "Background Information", "content": "• Historical context\n• Current state\n• Important facts", "slide_type": "content"},
            {"title": "Key Concepts", "content": "• Main principles\n• Core ideas\n• Essential knowledge", "slide_type": "content"},
            {"title": "Applications and Examples", "content": "• Real-world applications\n• Case studies\n• Practical examples", "slide_type": "content"},
            {"title": "Conclusion", "content": "• Summary of key points\n• Final thoughts\n• Next steps", "slide_type": "conclusion"}
        ]

    def generate_image_description(self, slide_content):
        """Generate image description for slides using Gemini"""
        prompt = f"""
        Based on this slide content, suggest a relevant image description that would enhance the presentation:

        {slide_content}

        Return only a brief, descriptive phrase suitable for image search (max 10 words).
        """

        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except:
            return "professional presentation"

import os

from dotenv import load_dotenv
from google import genai


load_dotenv()


class AIService:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY is not configured")

        self.client = genai.Client(api_key=api_key)

    def generate_response(self, question: str) -> str:
        response = self.client.models.generate_content(
            model="gemini-3.8-flash",
            contents=question,
        )

        return response.text
import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError


load_dotenv()


class LLMService:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY is not configured")

        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt: str) -> str:
        max_retries = 3

        for attempt in range(max_retries):
            try:
                response = self.client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt,
                )

                return response.text

            except ServerError:
                if attempt == max_retries - 1:
                    raise

                time.sleep(2 ** attempt)
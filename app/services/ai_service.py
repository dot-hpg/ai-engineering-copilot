from app.services.llm_service import LLMService


class AIService:

    def __init__(self):
        self.llm = LLMService()

    def generate_response(self, question: str) -> str:
        return self.llm.generate(question)
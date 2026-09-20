from app.services.llm_service import LLMService
from app.services.retrieval_service import RetrievalService
from app.services.vector_service import VectorService


class AIService:

    def __init__(self):
        self.llm = LLMService()

        self.vector_service = VectorService()
        self.vector_service.create_collection()

        self.retrieval = RetrievalService(
            self.vector_service
        )

    def generate_response(self, question: str) -> str:
        results = self.retrieval.retrieve(question)

        context = "\n\n".join(
            result.payload["text"]
            for result in results
        )

        prompt = f"""
You are an AI Engineering Copilot.

Answer the user's question using the provided context.

Context:
{context}

Question:
{question}

If the context does not contain enough information,
say that clearly instead of inventing an answer.
"""

        return self.llm.generate(prompt)
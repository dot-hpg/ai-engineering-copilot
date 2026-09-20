from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService


class RetrievalService:

    def __init__(self, vector_service: VectorService):
        self.embedding_service = EmbeddingService()
        self.vector_service = vector_service

    def retrieve(self, query: str, limit: int = 3):
        query_vector = self.embedding_service.embed(query)

        return self.vector_service.search(
            vector=query_vector,
            limit=limit,
        )
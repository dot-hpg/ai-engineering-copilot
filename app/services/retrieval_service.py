from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService


class RetrievalService:

    RELEVANCE_THRESHOLD = 0.70

    def __init__(self, vector_service: VectorService):
        self.embedding_service = EmbeddingService()
        self.vector_service = vector_service

    def retrieve(
        self,
        query: str,
        limit: int = 3,
        route: str = "general",
    ):

        query_vector = self.embedding_service.embed(
            query
        )

        results = self.vector_service.search(
            vector=query_vector,
            limit=limit,
        )

        relevant_results = [
            result
            for result in results
            if result.score >= self.RELEVANCE_THRESHOLD
        ]

        return relevant_results
from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService


class IngestionService:

    def __init__(self, vector_service: VectorService):
        self.embedding_service = EmbeddingService()
        self.vector_service = vector_service

    def ingest(
        self,
        document_id: int,
        text: str,
    ):
        vector = self.embedding_service.embed(text)

        self.vector_service.add_document(
            document_id=document_id,
            text=text,
            vector=vector,
        )

        return {
            "document_id": document_id,
            "status": "ingested",
        }
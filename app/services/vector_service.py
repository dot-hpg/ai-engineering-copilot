import os

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams


class VectorService:
    COLLECTION_NAME = "engineering_docs"

    def __init__(self):
        qdrant_host = os.getenv("QDRANT_HOST", "localhost")

        self.client = QdrantClient(
            host=qdrant_host,
            port=6333,
        )

    def create_collection(self):
        if not self.client.collection_exists(self.COLLECTION_NAME):
            self.client.create_collection(
                collection_name=self.COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=3072,
                    distance=Distance.COSINE,
                ),
            )

    def add_document(
        self,
        document_id: int,
        text: str,
        vector: list[float],
    ):
        self.client.upsert(
            collection_name=self.COLLECTION_NAME,
            points=[
                PointStruct(
                    id=document_id,
                    vector=vector,
                    payload={
                        "text": text,
                    },
                )
            ],
        )

    def search(
        self,
        vector: list[float],
        limit: int = 3,
    ):
        return self.client.query_points(
            collection_name=self.COLLECTION_NAME,
            query=vector,
            limit=limit,
        ).points
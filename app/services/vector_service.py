from qdrant_client import QdrantClient


class VectorService:

    def __init__(self):
        self.client = QdrantClient(":memory:")
        
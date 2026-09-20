from pydantic import BaseModel, Field


class IngestionRequest(BaseModel):
    document_id: int = Field(
        ...,
        description="Unique identifier for the document",
    )

    text: str = Field(
        ...,
        min_length=1,
        description="Document text to ingest",
    )


class IngestionResponse(BaseModel):
    document_id: int
    status: str
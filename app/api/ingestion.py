from fastapi import APIRouter

from app.schemas.ingestion import IngestionRequest, IngestionResponse
from app.services.ingestion_service import IngestionService
from app.services.vector_service import VectorService


router = APIRouter(
    prefix="/api/v1",
    tags=["Ingestion"],
)


vector_service = VectorService()
vector_service.create_collection()

ingestion_service = IngestionService(
    vector_service
)


@router.post(
    "/ingest",
    response_model=IngestionResponse,
)
def ingest(request: IngestionRequest):

    result = ingestion_service.ingest(
        document_id=request.document_id,
        text=request.text,
    )

    return IngestionResponse(**result)
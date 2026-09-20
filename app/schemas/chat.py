from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.ai_service import AIService


router = APIRouter(
    prefix="/api/v1",
    tags=["Chat"],
)

ai_service = AIService()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = ai_service.generate_response(
        request.question
    )

    return ChatResponse(
        answer=result["answer"],
        sources=result["context"],
        route=result["route"],
        path=result["path"],
        execution_time_ms=result["execution_time_ms"],
    )
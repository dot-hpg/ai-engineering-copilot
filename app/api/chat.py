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
    answer, sources = ai_service.generate_response(
        request.question
    )

    return ChatResponse(
        answer=answer,
        sources=sources,
    )
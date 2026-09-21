import logging

from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.ai_service import AIService


logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/v1",
    tags=["Chat"],
)

ai_service = AIService()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        result = ai_service.generate_response(request.question)

        return ChatResponse(
            answer=result["answer"],
            sources=result["context"],
            route=result["route"],
            path=result["path"],
            evidence_sufficient=result["evidence_sufficient"],
            evidence_score=result["evidence_score"],
            evidence_reason=result["evidence_reason"],
            answer_supported=result["answer_supported"],
            answer_score=result["answer_score"],
            answer_evaluation_reason=result["answer_evaluation_reason"],
            answer_attempts=result["answer_attempts"],
            execution_time_ms=result["execution_time_ms"],
        )

    except Exception as exc:
        logger.exception(
            "AI agent execution failed for question: %s",
            request.question,
        )

        raise HTTPException(
            status_code=500,
            detail="AI agent execution failed",
        ) from exc
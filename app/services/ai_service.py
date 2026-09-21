from app.services.agent_service import AgentService


class AIService:

    def __init__(self):
        self.agent = AgentService()

    def generate_response(
        self,
        question: str,
    ):
        result = self.agent.run(question)

        return {
            "answer": result["answer"],
            "context": result["context"],
            "route": result["route"],
            "path": result["path"],
            "evidence_sufficient": result["evidence_sufficient"],
            "evidence_score": result["evidence_score"],
            "evidence_reason": result["evidence_reason"],
            "answer_supported": result["answer_supported"],
            "answer_score": result["answer_score"],
            "answer_evaluation_reason": result["answer_evaluation_reason"],
            "answer_attempts": result["answer_attempts"],
            "execution_time_ms": result["execution_time_ms"],
        }
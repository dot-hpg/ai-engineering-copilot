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
            "evidence_reason": result["evidence_reason"],
            "execution_time_ms": result["execution_time_ms"],
        }
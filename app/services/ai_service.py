from app.services.agent_service import AgentService


class AIService:

    def __init__(self):
        self.agent = AgentService()

    def generate_response(
        self,
        question: str,
    ):
        result = self.agent.run(question)

        return (
            result["answer"],
            result["context"],
        )
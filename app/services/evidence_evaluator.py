class EvidenceEvaluator:

    def evaluate(
        self,
        context: list[str],
    ) -> dict:

        if not context:
            return {
                "is_sufficient": False,
                "reason": "No relevant context found",
            }

        return {
            "is_sufficient": True,
            "reason": "Relevant context found",
        }
        
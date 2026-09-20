class EvidenceEvaluator:

    RELEVANCE_THRESHOLD = 0.70

    def evaluate(
        self,
        context: list[str],
    ) -> dict:

        if not context:
            return {
                "is_sufficient": False,
                "score": 0.0,
                "reason": "No relevant context found",
            }

        score = 1.0

        return {
            "is_sufficient": score >= self.RELEVANCE_THRESHOLD,
            "score": score,
            "reason": "Relevant context found",
        }
class EvidenceEvaluator:

    RELEVANCE_THRESHOLD = 0.70

    def evaluate(
        self,
        context: list[str],
        retrieval_scores: list[float],
    ) -> dict:

        if not context or not retrieval_scores:
            return {
                "is_sufficient": False,
                "score": 0.0,
                "reason": "No relevant context found",
            }

        score = max(retrieval_scores)

        return {
            "is_sufficient": score >= self.RELEVANCE_THRESHOLD,
            "score": round(score, 4),
            "reason": (
                "Relevant context found"
                if score >= self.RELEVANCE_THRESHOLD
                else "Evidence relevance below threshold"
            ),
        }
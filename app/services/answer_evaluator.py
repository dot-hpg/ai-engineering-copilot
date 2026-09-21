class AnswerEvaluator:

    def evaluate(
        self,
        answer: str,
        context: list[str],
    ) -> dict:

        if not answer:
            return {
                "is_supported": False,
                "score": 0.0,
                "reason": "Answer is empty",
            }

        if not context:
            return {
                "is_supported": False,
                "score": 0.0,
                "reason": "No supporting context available",
            }

        answer_words = set(
            answer.lower().split()
        )

        context_words = set(
            " ".join(context).lower().split()
        )

        overlap = (
            len(answer_words & context_words)
            / len(answer_words)
        )

        score = round(overlap, 4)

        return {
            "is_supported": score >= 0.50,
            "score": score,
            "reason": (
                "Answer is supported by context"
                if score >= 0.50
                else "Answer has insufficient support from context"
            ),
        }
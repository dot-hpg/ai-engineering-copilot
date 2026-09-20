class QueryClassifier:

    TECHNICAL_KEYWORDS = [
        "code",
        "python",
        "bug",
        "error",
        "exception",
        "api",
        "fastapi",
        "docker",
        "kubernetes",
        "database",
        "sql",
        "deployment",
        "server",
        "backend",
        "frontend",
        "architecture",
        "debug",
        "debugging",
    ]

    def classify(self, question: str) -> dict:

        question = question.lower()

        matched_keywords = [
            keyword
            for keyword in self.TECHNICAL_KEYWORDS
            if keyword in question
        ]

        if matched_keywords:
            return {
                "route": "technical",
                "reason": "engineering_keyword",
                "confidence": 0.95,
                "matched_keywords": matched_keywords,
            }

        return {
            "route": "general",
            "reason": "no_engineering_keyword",
            "confidence": 0.70,
            "matched_keywords": [],
        }
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

    def classify(self, question: str) -> str:

        question = question.lower()

        if any(
            keyword in question
            for keyword in self.TECHNICAL_KEYWORDS
        ):
            return "technical"

        return "general"
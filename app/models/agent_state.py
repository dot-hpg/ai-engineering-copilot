from typing import TypedDict


class AgentState(TypedDict):
    question: str
    route: str
    path: str
    context: list[str]
    answer: str
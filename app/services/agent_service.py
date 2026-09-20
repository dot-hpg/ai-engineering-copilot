from langgraph.graph import END, StateGraph

from app.models.agent_state import AgentState
from app.services.retrieval_service import RetrievalService
from app.services.vector_service import VectorService


vector_service = VectorService()
vector_service.create_collection()

retrieval_service = RetrievalService(
    vector_service
)


def route_question(state: AgentState):

    question = state["question"].lower()

    if any(
        keyword in question
        for keyword in [
            "code",
            "python",
            "bug",
            "error",
            "exception",
        ]
    ):
        route = "technical"
    else:
        route = "general"

    return {
        "route": route
    }


def technical_path(state: AgentState):

    results = retrieval_service.retrieve(
        state["question"]
    )

    context = [
        result.payload["text"]
        for result in results
    ]

    return {
        "context": context,
        "path": "technical",
    }


def general_path(state: AgentState):

    results = retrieval_service.retrieve(
        state["question"]
    )

    context = [
        result.payload["text"]
        for result in results
    ]

    return {
        "context": context,
        "path": "general",
    }


def generate_answer(state: AgentState):

    if state["context"]:
        answer = (
            "Test generation successful. "
            f"Retrieved {len(state['context'])} relevant "
            "document(s) through the "
            f"{state['path']} path."
        )
    else:
        answer = (
            "Test generation successful, "
            "but no relevant context was retrieved."
        )

    return {
        "answer": answer
    }


def select_path(state: AgentState):

    if state["route"] == "technical":
        return "technical"

    return "general"


class AgentService:

    def __init__(self):

        graph = StateGraph(AgentState)

        graph.add_node(
            "route_question",
            route_question,
        )

        graph.add_node(
            "technical_path",
            technical_path,
        )

        graph.add_node(
            "general_path",
            general_path,
        )

        graph.add_node(
            "generate_answer",
            generate_answer,
        )

        graph.set_entry_point(
            "route_question"
        )

        graph.add_conditional_edges(
            "route_question",
            select_path,
            {
                "technical": "technical_path",
                "general": "general_path",
            },
        )

        graph.add_edge(
            "technical_path",
            "generate_answer",
        )

        graph.add_edge(
            "general_path",
            "generate_answer",
        )

        graph.add_edge(
            "generate_answer",
            END,
        )

        self.graph = graph.compile()

    def run(self, question: str):

        initial_state: AgentState = {
            "question": question,
            "route": "",
            "path": "",
            "context": [],
            "answer": "",
        }

        return self.graph.invoke(
            initial_state
        )
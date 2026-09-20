import time

from langgraph.graph import END, StateGraph

from app.models.agent_state import AgentState
from app.services.evidence_evaluator import EvidenceEvaluator
from app.services.llm_service import LLMService
from app.services.query_classifier import QueryClassifier
from app.services.retrieval_service import RetrievalService
from app.services.vector_service import VectorService


vector_service = VectorService()
vector_service.create_collection()

retrieval_service = RetrievalService(
    vector_service
)

evidence_evaluator = EvidenceEvaluator()


def route_question(state: AgentState):

    classifier = QueryClassifier()

    classification = classifier.classify(
        state["question"]
    )

    return {
        "route": classification["route"],
        "classification_reason": classification["reason"],
        "classification_confidence": classification["confidence"],
        "matched_keywords": classification["matched_keywords"],
    }


def technical_path(state: AgentState):

    results = retrieval_service.retrieve(
        state["question"],
        route="technical",
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
        state["question"],
        route="general",
    )

    context = [
        result.payload["text"]
        for result in results
    ]

    return {
        "context": context,
        "path": "general",
    }


def evaluate_evidence(state: AgentState):

    evaluation = evidence_evaluator.evaluate(
        state["context"]
    )

    return {
        "evidence_sufficient": evaluation["is_sufficient"],
        "evidence_reason": evaluation["reason"],
        "answer": (
            ""
            if evaluation["is_sufficient"]
            else evaluation["reason"]
        ),
    }


def select_evidence_path(state: AgentState):

    if state["evidence_sufficient"]:
        return "generate"

    return "stop"


def generate_answer(state: AgentState):

    llm_service = LLMService()

    context = "\n\n".join(
        state["context"]
    )

    prompt = f"""
You are an AI Engineering Copilot.

Answer the user's question using only the provided context.

Route:
{state["route"]}

Classification Reason:
{state["classification_reason"]}

Classification Confidence:
{state["classification_confidence"]}

Execution Path:
{state["path"]}

Evidence Status:
{state["evidence_sufficient"]}

Evidence Reason:
{state["evidence_reason"]}

Context:
{context}

Question:
{state["question"]}

If the context does not contain enough information,
say that the available context is insufficient.

Answer clearly and concisely.
"""

    answer = llm_service.generate(prompt)

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
            "evaluate_evidence",
            evaluate_evidence,
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
            "evaluate_evidence",
        )

        graph.add_edge(
            "general_path",
            "evaluate_evidence",
        )

        graph.add_conditional_edges(
            "evaluate_evidence",
            select_evidence_path,
            {
                "generate": "generate_answer",
                "stop": END,
            },
        )

        graph.add_edge(
            "generate_answer",
            END,
        )

        self.graph = graph.compile()

    def run(self, question: str):

        start_time = time.perf_counter()

        initial_state: AgentState = {
            "question": question,
            "route": "",
            "classification_reason": "",
            "classification_confidence": 0.0,
            "matched_keywords": [],
            "path": "",
            "context": [],
            "evidence_sufficient": False,
            "evidence_reason": "",
            "answer": "",
            "execution_time_ms": 0.0,
        }

        result = self.graph.invoke(
            initial_state
        )

        execution_time_ms = (
            time.perf_counter() - start_time
        ) * 1000

        result["execution_time_ms"] = round(
            execution_time_ms,
            2,
        )

        return result
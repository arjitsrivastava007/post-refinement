from typing import TypedDict, List


# Define the state
class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        post: Current post content
        critique: Critique feedback
        iteration: Current iteration count
        history: list of History of critiques and improvements
    """
    post: str
    critique: str
    iteration: int
    history: List[dict]

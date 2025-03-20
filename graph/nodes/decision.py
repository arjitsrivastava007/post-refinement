from config.constants import ITERATIONS, ITERATION, END, CONTINUE
from config.state import GraphState


# Define the decision node
def decision_node(state: GraphState) -> str:
    if state[ITERATION] >= ITERATIONS:
        return END
    else:
        return CONTINUE

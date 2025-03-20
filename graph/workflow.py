from langgraph.graph import StateGraph
from config.state import GraphState
from graph.nodes import critique_node, improvement_node, decision_node, end_node
from config.constants import CRITIQUE, IMPROVE, CONTINUE, END, GENERATE


# Build the graph
workflow = StateGraph(GraphState)
workflow.add_node(GENERATE, critique_node)
workflow.add_node(IMPROVE, improvement_node)
workflow.add_node(END, end_node)  # Add the end node
workflow.add_conditional_edges(
    GENERATE,
    decision_node,
    {CONTINUE: IMPROVE, END: END}
)
workflow.add_edge(IMPROVE, GENERATE)
workflow.set_entry_point(GENERATE)

# Compile the graph
app = workflow.compile()

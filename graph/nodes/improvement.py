from langchain_core.messages import HumanMessage, SystemMessage
from config.chat_llm import llm
from config.state import GraphState
from config.constants import ITERATION, HISTORY, CRITIQUE, POST


# Define the improvement node
def improvement_node(state: GraphState) -> GraphState:
    improve_prompt = SystemMessage(content="Based on the feedback, rewrite the post to address the suggestions:")
    feedback = HumanMessage(content=state[CRITIQUE])
    post_content = HumanMessage(content=state[POST])
    response = llm.invoke([improve_prompt, feedback, post_content])
    state[POST] = response.content
    state[ITERATION] += 1
    state[HISTORY].append({
        ITERATION: state[ITERATION],
        POST: state[POST],
        CRITIQUE: state[CRITIQUE]
    })
    return state

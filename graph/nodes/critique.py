from langchain_core.messages import HumanMessage, SystemMessage
from config.chat_llm import llm
from config.state import GraphState


# Define the critique node
def critique_node(state: GraphState) -> GraphState:
    critique_prompt = SystemMessage(content="You are a helpful writing assistant. Provide constructive feedback on the following post:")
    post_content = HumanMessage(content=state["post"])
    response = llm.invoke([critique_prompt, post_content])
    state["critique"] = response.content
    return state

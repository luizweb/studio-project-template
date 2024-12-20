from langgraph.graph import StateGraph
from langgraph.prebuilt import tools_condition

from utils.state import State
from utils.nodes import chatbot, tool_node

# Build graph
workflow = StateGraph(State)
workflow.set_entry_point("chatbot")
workflow.add_node("chatbot", chatbot)

workflow.add_node("tools", tool_node)
workflow.add_conditional_edges(
    "chatbot",
    tools_condition, # tool calling OR route to the end.
)
workflow.add_edge("tools", "chatbot")
graph = workflow.compile()
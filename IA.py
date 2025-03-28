##########################################################
#                                                        #
#                   CODE BY UNIFORM SEGUE                #
#                                                        #
##########################################################

from typing import Annotated
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai import ChatMistralAI
from langgraph.prebuilt import ToolNode
from typing_extensions import TypedDict
from typing import Literal
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
import toolsFunc


class IA:

    config = {'configurable': {'thread_id': 'id'}}

    def __init__(self):

        class State(TypedDict):
            messages: Annotated[list, add_messages]

        graph_builder = StateGraph(State)

        api_key = "" #Your Api Keys

        tools = toolsFunc.tools
        tool_node = ToolNode(tools)

        llm = ChatMistralAI(model="mistral-large-latest",temperature=0.5,mistral_api_key=api_key) #ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.1, max_tokens=None, timeout=None,max_retries=2, api_key=api_key) --> for using Gemini Model


        llm_with_tools = llm.bind_tools(tools)

        graph_builder.add_node("tool_node", tool_node)

        def prompt_node(state: State):
            return {"messages": [llm_with_tools.invoke(state["messages"])]}

        graph_builder.add_node("prompt_node", prompt_node)

        def conditional_edge(state: State) -> Literal['tool_node', '__end__']:
            last_message = state["messages"][-1]
            if last_message.tool_calls:
                return "tool_node"
            else:
                return "__end__"

        graph_builder.add_conditional_edges('prompt_node', conditional_edge)

        graph_builder.add_edge("tool_node", "prompt_node")

        graph_builder.set_entry_point("prompt_node")

        from langgraph.checkpoint.sqlite import SqliteSaver
        from langgraph.checkpoint.memory import MemorySaver

        self.memory = SqliteSaver.from_conn_string(":memory:")

        self.graph = graph_builder.compile(checkpointer=MemorySaver())

    def send_message(self,user_input):
        response = self.graph.invoke({"messages": [{"role": "user", "content": user_input}]}, config=self.config)

        return response["messages"][-1].content


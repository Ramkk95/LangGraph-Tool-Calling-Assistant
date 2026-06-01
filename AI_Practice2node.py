from altair import condition
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph,START ,END
from langgraph.graph.message import add_messages
from typing import Annotated
import streamlit as st
from langgraph.prebuilt import ToolNode, tools_condition
from typing_extensions import TypedDict
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")



class State(TypedDict):
   messages:Annotated[list,add_messages]


llm=init_chat_model(model='gpt-4o-mini')


def fav1()->dict:
    """ my favourite game information"""
    return {'message': ['Cricket','hockey']}

def fav2()->dict:
    """ My favourite dish information"""
    return {"message": ["veg-briyani","dal"]}

tools=[fav1,fav2]

llm_plus_tools=llm.bind_tools(tools)

def tool_calling_llm(state:State):
    resp= llm_plus_tools.invoke(state['messages'])
    return {'messages':resp}

builder=StateGraph(State)
builder.add_node('tool_calling_llm',tool_calling_llm)
builder.add_node('tools',ToolNode(tools))

builder.add_edge(START,'tool_calling_llm')
#builder.add_edge('tool_calling_llm','tools')
builder.add_conditional_edges(
    'tool_calling_llm',
    tools_condition
)
builder.add_edge('tools','tool_calling_llm')

graph=builder.compile()
ac=st.text_input('Enter question')
res=graph.invoke({'messages':ac})
st.write(res)



# LangGraph-Tool-Calling-Assistant
This project demonstrates how to build a Tool-Calling AI Assistant using LangGraph, LangChain, OpenAI GPT-4o-mini, and Streamlit.
# LangGraph Tool Calling Assistant

This project demonstrates how to build a Tool-Calling AI Assistant using **LangGraph**, **LangChain**, **OpenAI GPT-4o-mini**, and **Streamlit**.

The application allows an LLM to intelligently decide when to invoke external tools based on user queries. Using LangGraph's conditional routing, the assistant can call predefined tools and integrate their outputs into the conversation flow.

## Features

* Built with **LangGraph StateGraph**
* Tool calling using **LangChain Tool Binding**
* Conditional tool execution with `tools_condition`
* Interactive web interface using **Streamlit**
* OpenAI GPT-4o-mini integration
* Multi-step reasoning between LLM and tools
* Extensible architecture for adding custom tools

## Implemented Tools

### Favourite Games Tool

Returns information about favourite games:

* Cricket
* Hockey

### Favourite Dishes Tool

Returns information about favourite dishes:

* Veg Biryani
* Dal

## Tech Stack

* Python
* LangChain
* LangGraph
* OpenAI API
* Streamlit
* dotenv

## Workflow

1. User enters a question in the Streamlit interface.
2. GPT-4o-mini analyzes the query.
3. If tool information is required, LangGraph routes the request to the appropriate tool.
4. Tool results are returned to the LLM.
5. The final response is displayed to the user.

## Learning Objectives

This project demonstrates:

* Agentic AI workflows
* Tool Calling with LLMs
* Graph-based AI orchestration
* State management in LangGraph
* Streamlit application development

A great beginner-friendly project for understanding how modern AI agents use tools and decision-making workflows.

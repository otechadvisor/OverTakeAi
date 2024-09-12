from langchain.agents import AgentType, initialize_agent
from llm import initialize_llm
from shell_tool import initialize_shell_tool

def initialize_agent_with_tools():
   
   
    llm = initialize_llm()
    shell_tool = initialize_shell_tool()


    agent = initialize_agent(
        tools=[shell_tool],
        llm=llm,
        agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent

import os
from langchain.prompts import PromptTemplate
from langchain.agents import create_react_agent, AgentExecutor, Tool
from llm import initialize_llm
from shell_tool import initialize_shell_tool
from storage import save_interaction, load_interactions
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

WORKING_DIRECTORY = os.getenv('WORKING_DIRECTORY')

# Define the prompt template for safe command execution
prompt_template = PromptTemplate(
    input_variables=["command", "tools", "agent_scratchpad", "tool_names"],
    template="""You are an advanced AI assistant tasked with executing shell commands on a Linux machine.
    Follow these guidelines:
    1. Always ensure safety for 'rm' and other potentially harmful commands by requesting user confirmation.
    2. Restrict actions to whitelisted commands: `ls`, `pwd`, `mkdir`, `touch`, `cat`, `echo`, and `rm` with user permission.
    3. Never perform irreversible operations without explicit user approval.

    Command to execute: {command}

    Tools available: {tools}
    Agent Scratchpad: {agent_scratchpad}
    Tool Names: {tool_names}

    Respond in the following format:
    Thought: What is the command supposed to do.
    Action: The command you will execute in this format: <tool_name>(tool_input='your command').
    Execution: After the action is performed, display the result.
    Final Answer: The result of the command execution.
    """
)

def enhance_prompt_with_history(command):
    """Enhance the current prompt with historical interactions."""
    past_interactions = load_interactions()
    history_str = "\n".join([f"Prompt: {i['prompt']}\nResponse: {i['response']}" for i in past_interactions])
    return f"{history_str}\n\nCurrent command: {command}"

def initialize_agent_with_tools():
    llm = initialize_llm()
    shell_tool = initialize_shell_tool()

    # Define the tools
    tools = [
        Tool(
            name="shell_tool",
            func=shell_tool.run,
            description="Executes shell commands on a Linux system."
        )
    ]

    # Create the react agent
    agent = create_react_agent(
        tools=tools,
        llm=llm,
        prompt=prompt_template,
    )

    # Create the AgentExecutor to handle the execution
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

    return agent_executor

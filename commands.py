from agent import enhance_prompt_with_history
from storage import save_interaction

def run_command(agent_executor, command):
    """Execute a command through the agent after enhancing it with history."""
    # Enhance the command with interaction history
    enhanced_command = enhance_prompt_with_history(command)
    
    # Prepare input for the AgentExecutor
    inputs = {"command": enhanced_command}
    
    # Run the enhanced command through the agent using the invoke method
    response = agent_executor.invoke(inputs)
    
    # Save the interaction for future reference
    save_interaction(command, response)
    
    return response

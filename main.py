from agent import initialize_agent_with_tools
from command_input import get_user_command
from commands import run_command

if __name__ == "__main__":
    # Initialize the agent
    agent = initialize_agent_with_tools()

    # Start the interactive shell
    while True:
        command = get_user_command()

        # Exit if the user types 'exit'
        if command.lower() == "exit":
            print("Exiting the interactive shell...")
            break

        # Run the command through the agent with validation and permission
        run_command(agent, command)

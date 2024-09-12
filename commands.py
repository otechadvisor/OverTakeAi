def is_dangerous_command(command):
    """
    Checks if the command is considered dangerous (e.g., involves removing files).
    Args:
        command: The command to check.
    Returns:
        True if the command is dangerous, False otherwise.
    """
    dangerous_commands = ['rm', 'rmdir', 'rm -rf', 'rm -r', 'rm -f', 'sudo rm']
    
    for dangerous in dangerous_commands:
        if dangerous in command:
            return True
    return False

def ask_for_permission(command):
    """
    Asks the user for permission to execute a dangerous command.
    Args:
        command: The command to ask permission for.
    Returns:
        True if the user grants permission, False otherwise.
    """
    confirmation = input(f"The command '{command}' is potentially dangerous. Do you want to proceed? (yes/no): ").strip().lower()
    return confirmation == "yes"

def run_command(agent, command):
    """
    Runs a single command using the agent, requesting permission for dangerous commands.
    Args:
        agent: The initialized agent.
        command: The command to be run.
    """
    # Check if the command is dangerous
    if is_dangerous_command(command):
        if not ask_for_permission(command):
            print(f"Permission denied for running '{command}'.\n")
            return
    
    print(f"Running command: {command}")
    try:
        result = agent.run(command)
        print(f"Result: {result}\n")
    except Exception as e:
        print(f"Error running command '{command}': {e}")

import os
from langchain_community.tools import ShellTool

def initialize_shell_tool():
    # Ensure the tool runs commands in the working directory
    working_directory = os.getenv('WORKING_DIRECTORY')

    class CustomShellTool(ShellTool):
        def run(self, command):
            if working_directory:
                # Change to the specified working directory before running the command
                os.chdir(working_directory)
            return super().run(command)

    return CustomShellTool()

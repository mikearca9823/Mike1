# Objectives

# The Python library “os” must be utilized
# At least three variables must be declared in Python that contain bash operations
# Use the python os function to print the following commands below.  These are bash commands and we are going to run them through a python script.
# Add description printed to the terminal of what is about to run
import os
#variables with bash commands
commands = [
    {"command": "whoami", "description": "Display current user"},
    {"command": "ip a", "description": "Display IP address information"}
    {"command": "lshw -short", "description": "display hardware information"}
]
#Function to execute command using os.system() with a descriptive message
def execute_command(command, description):
    print(f"Executing: {description}")
    os.system(command)
# whoami
# ip a
# lshw -short
# Stretch Goals (Optional Objectives)
# Pursue stretch goals if you are a more advanced user or have remaining lab time.
# Instead of os.system() function, utilize the subprocess module instead. Refer to python.org for how this can be achieved.



# This will not run on windows needs to be mac or linux due to os being bash

import subprocess
import os
import subprocess
import yaml, os


# Load the yaml file 
with open("build_exe.yml", 'r') as commands_file:
    data = yaml.safe_load(commands_file)

# Execute the commands in the yaml file
if "commands" in data:
    command_list = data["commands"]
    for command in command_list:
        subprocess.run(command, shell=True)

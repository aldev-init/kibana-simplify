import module.select_directory as sd
import module.select_file as sf
import module.generate_bat as gb
import module.get_user_input as io

print("Select Kubectl File")
sf.browseFileForEnv("KUBECTL_PATH","Select Kubectl tools")
print("Select Kubeconfig Directory")
sd.browseDirectoryForEnv("KUBECONFIG_PATH", "Select list of Kubeconfig directory")

tools_command_name = io.get_user_input("Enter name command python in your CLI (default 'py'): ")
cli_naming = io.get_user_input("What do you call this tool(default 'jarvis')? ")

# generate file bat 
gb.generate(
    "py" if tools_command_name == "" else tools_command_name  ,
    "jarvis" if cli_naming == "" else cli_naming)

print("Setup Complete....")
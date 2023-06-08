import os 
from dotenv import load_dotenv

#load .env file
load_dotenv()

default_port = os.environ.get("database_port")
kubeconfig = os.environ.get("kubeconfig_database_dev")
kube_command = os.environ.get("kube_database_dev_command").replace("<>",kubeconfig)

use_default_port = input("Use Default Port ["+default_port+"] (y/n)? ")
os.system("cls")
if(use_default_port == "y"):
    use_default = kube_command.replace(":port",default_port)
    os.system(use_default)
else:
    new_port = input("insert port (4 digit): ")
    os.system("cls")
    use_new_port = kube_command.replace(":port",new_port)
    os.system(use_new_port)




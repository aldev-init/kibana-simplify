import os
from dotenv import load_dotenv

# load .env file
load_dotenv()

# # load user directory
user_path = os.environ.get("kibana_path")
file_list_config = os.environ.get("list_kube_config")

print(file_list_config)

# setting kube config
index_config = 0
print("Silahkan pilih kubectl config: ")
path = os.environ.get("USERPROFILE") + "\Project\Kube-Database-dev"
list_dir = os.listdir(path)
lines = [line.strip() for line in list_dir if os.path.isfile(os.path.join(path,line))]
for list_config in lines:
    print([index_config],list_config)
    index_config+=1

default_config = lines[5]
print("Config default saat ini: "+default_config)

config = input("pilih config (tekan enter untuk default): ")

if(config == ""):
    kubeconfig = "%USERPROFILE%\Project\Kube-Database-dev\\"+default_config
else:
    kubeconfig = "%USERPROFILE%\Project\Kube-Database-dev\\"+lines[int(config)]

# command 
get_pods = os.environ.get("get_pods_command").replace("<>",kubeconfig)
describe_pod = os.environ.get("describe_pods_command").replace("<>",kubeconfig)
logs_pods = os.environ.get("logs_pods_command").replace("<>",kubeconfig)
delete_pods = os.environ.get("delete_pods_command").replace("<>",kubeconfig)
port_forward = os.environ.get("port_forward_command").replace("<>",kubeconfig)

#code configuration
prompt="input service name: "
parameter=":param"
port=":port"


class Behaviour:
    # create menu
    def __init__(self,*menu):
        if __name__=='__main__':
            print('[Author: AlDev]')
        index=1
        for i in menu:
            print([index],i)
            index+=1
        
    
# clear cli
os.system("cls")
print("Welcome To Kibana Simplify Cli")
print("Anda tidak perlu mengetikan command yang panjang lagi :)")
bh = Behaviour('Get Pods','Describe Pod','Logs pod','Delete Pod','Port Forward')
key = input("Choose Menu (enter for exit): ")
if(key == "1"):
    os.system("cls")
    os.system(get_pods)
if(key == "2"):
    os.system("cls")
    os.system(get_pods)
    service_name = input(prompt)
    describe_pods_with_param = describe_pod.replace(parameter,service_name)
    os.system(describe_pods_with_param)
if(key == "3"):
    os.system("cls")
    os.system(get_pods)
    service_name = input(prompt)
    logs_pods_with_param = logs_pods.replace(parameter,service_name)
    arg = input("Live Logs?(y/n)")
    if(arg == "y"):
        live_logs = logs_pods_with_param.replace(":arg","-f")
        os.system(live_logs)
    else:
        no_live_logs = logs_pods_with_param.replace(":arg","")
        os.system(no_live_logs)
if(key == "4"):
    os.system("cls")
    os.system(get_pods)
    service_name = input(prompt)
    delete_pods_with_param = delete_pods.replace(parameter,service_name)
    os.system(delete_pods_with_param)
if(key == "5"):
    os.system("cls")
    os.system(get_pods)
    service_name = input(prompt)
    input_port = input("Masukan Port, Dipisahkan dengan spasi jika lebih dari 1: ")
    port_forward_with_param_and_port = port_forward.replace(parameter,service_name).replace(port,input_port)
    os.system(port_forward_with_param_and_port)

#cooming soon improvement
# import keyboard
# still bug 
# keyword_python = os.environ.get("keyword_python")
    # def keyBehaviour(self,event):
    #     key = event.name
    #     if(key == "1"):
    #         os.system("cls")
    #         os.system(get_pods)
    #         print("press backspace to back on menu..")
    #     if(key == "2"):
    #         os.system("cls")
    #         os.system(get_pods)
    #         keyboard.clear_all_hotkeys
    #         service_name = input(prompt).replace("2","")
    #         describe_pods_with_param = describe_pods.replace(parameter,service_name)
    #         os.system(describe_pods_with_param)
    #     if(key == "backspace"):
    #         keyboard.press('esc')
    #         os.system(keyword_python+" kibana-logging.py")
# keyboard.on_press(bh.keyBehaviour)
# keyboard.wait('esc')
    
     
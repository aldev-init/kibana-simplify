import os
from dotenv import load_dotenv
import time
import random

# load .env file
load_dotenv()
kubectl_path = os.environ.get("KUBECTL_PATH")

# setting kube config
index_config = 0
print("Silahkan pilih kubectl config: ")
path = os.environ.get("KUBECONFIG_PATH")
list_dir = os.listdir(path)
lines = [line.strip() for line in list_dir if os.path.isfile(os.path.join(path,line))]
for list_config in lines:
    print([index_config],list_config)
    index_config+=1

default_config = random.choice(lines)
print("Config default saat ini: "+default_config)

config = input("pilih config (tekan enter untuk default): ")

if(config == ""):
    kubeconfig = path+"/"+default_config
    print(kubeconfig)
else:
    kubeconfig = path+"/"+lines[int(config)]
    print(kubeconfig)

# command 
get_pods = os.environ.get("get_pods_command").replace("<>",kubeconfig).replace("kubectl",kubectl_path)
describe_pod = os.environ.get("describe_pods_command").replace("<>",kubeconfig)
logs_pods = os.environ.get("logs_pods_command").replace("<>",kubeconfig)
delete_pods = os.environ.get("delete_pods_command").replace("<>",kubeconfig)
port_forward = os.environ.get("port_forward_command").replace("<>",kubeconfig)
ram_usage_pods = os.environ.get("ram_usage_pods_command").replace("<>",kubeconfig)

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
bh = Behaviour('Get Pods','Describe Pod','Logs pod','Delete Pod','Port Forward','Ram Usage Pod')
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
if(key == "6"):
    os.system("cls")
    os.system(get_pods)
    service_name = input(prompt)
    refresh_time = input("Masukan waktu refresh (enter for default 5s): ")
    ram_usage_pods_with_param = ram_usage_pods.replace(parameter,service_name)
    while True:
        os.system("cls")
        os.system(ram_usage_pods_with_param)
        time.sleep(int( 5 if refresh_time == "" else refresh_time))

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
    
     
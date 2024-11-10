from dotenv import load_dotenv
import os

def generate(pyName,name):
    
    load_dotenv()
    
    bat_content = pyName +" "+ str(os.environ.get("KUBECTL_PY_PATH")) + "\kubectl.py"

    with open(name+".bat",'w') as f:
        f.write(bat_content)
        
    print("Generate bat complete...")
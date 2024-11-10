def generate(pyName,name):
    bat_content = pyName + " %CD%/kubectl.py"

    with open(name+".bat",'w') as f:
        f.write(bat_content)
        
    print("Generate bat complete...")
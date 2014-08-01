import yaml
"""
cmdlist=[]
cmd=raw_input("Input COMMAND: ")

cmdlist.append(cmd)
##print cmdlist
stream=open('exec.yaml','a')
yaml.dump(cmdlist,stream,default_flow_style=False)
"""



def save2yaml(cmd):
    cmdlist=[]
    stream=open('exec.yaml','a')
    cmdlist.append(cmd)
    yaml.dump(cmdlist,stream,default_flow_style=False)

try:
    cmd=raw_input("Input COMMAND: ")
except:
    cmd=input("Input COMMAND: ")
    
save2yaml(cmd)

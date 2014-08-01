import os
import yaml

def runyaml():
    stream=open('exec.yaml','r')
    cmdlist=yaml.load(stream)
    return cmdlist

cmdlist=runyaml()
for i in range(len(cmdlist)):
    print(os.popen(cmdlist[i]).read())
    




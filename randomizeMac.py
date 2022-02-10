import subprocess
import random
from xxlimited import new

from defer import return_value

def getRandomValue():
    type = random.randint(0,1)
    if (type == 0):
        return random.randint(0,9)
    else:
        return chr(random.randint(97,102))


def newMacAddress():
    mac = ""
    for i in range(6):
        mac = mac + str(getRandomValue())
        mac = mac + str(getRandomValue())
        mac = mac + ":"
    return mac[:-1]

def changeMacAddress(macAddress):
    subprocess.call(["sudo", "ifconfig", "enp0s3" ,"down"])
    subprocess.call(["sudo", "ifconfig", "enp0s3" ,"hw", "ether", macAddress])
    subprocess.call(["sudo", "ifconfig", "enp0s3" ,"up"])


newMac = newMacAddress() 

print("New Mac: " + newMac)
changeMacAddress(newMac)




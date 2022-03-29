import requests
import time

urlTarget = input("Url: ")
delay = int(input("Delay: "))
requestType = int(input("1-Get 2-Post 3-Put 4-Delete: "))

myRange = input("Range (a-b): ")
rangeValues = myRange.split("-")



def getRequest(url, intPath):
    req = requests.get(url+intPath)
    return req





if requestType == 1 :
    for i in range(int(rangeValues[0]),int(rangeValues[1])+1):
        req = getRequest(urlTarget, str(i))
        print(urlTarget + str(i), "status: ", req.status_code)
        time.sleep(delay)

#elif requestType == 2:
#
#elif requestType == 3:
#
#elif requestType == 4:






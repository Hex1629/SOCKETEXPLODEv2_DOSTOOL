import json,time,threading,sys
from gui import controler
from attrs import access_file,menu_lang,hash_checked,read,write,color_gardient,green_gr,yellow_gr,red_gr,blue_gr,update_pypi
languages = menu_lang()

def is_update(file='update.json'):
    c = access_file(f'https://raw.githubusercontent.com/Tool-Free/socketexplodev2_assets/main/{file}')
    if c != False:
        c = c.replace(b',\n  }\n}', b'\n  }\n}')
        json_down = json.loads(c)
        r3 = json_down['PIP']
        c2 = 0
        load = ['','.','. .','. . .','. . . .']
        for b in r3.keys():
           c2 += 1; sys.stdout.write(f"\r\x1b[38;5;255m[\x1b[38;5;75mINFO\x1b[38;5;255m] \x1b[38;5;198m{b} \x1b[38;5;255mof \x1b[38;5;197m{c2}\x1b[38;5;255m/\x1b[38;5;196m{len(r3.keys())}\x1b[0m\x1b[K"); sys.stdout.flush()
           time.sleep(0.1)
           craft_payload = f"""import os\nload = {load}\ntry:\n    {r3[b]['import']}\n    print("\\r\\x1b[K\\x1b[38;5;196mDONE \\x1b[38;5;197mINSTALL \\x1b[38;5;198m{b} \\x1b[38;5;199mPIP!\\x1b[0m")\nexcept:\n    os.system("{r3[b]['command']}")\n    for b2 in load:\n        sys.stdout.write(f"\\r\\x1b[38;5;255m[\\x1b[38;5;76mWARN\\x1b[38;5;255m] \\x1b[38;5;198m{b} \\x1b[38;5;197m"""+"""{b2}"""+"""\\x1b[0m\\x1b[K")\n        sys.stdout.flush() \n        time.sleep(0.1)\n    print(f'\\r\\x1b[K\\x1b[38;5;255m[\\x1b[38;5;196mDONE\\x1b[38;5;255m] \\x1b[38;5;226m{b} \\x1b[38;5;227m. . . . \\x1b[38;5;228mdone\\x1b[0m')\n"""
           exec(craft_payload)
           time.sleep(0.2)
        c2 = 0
        print(f'\r\x1b[38;5;255m[\x1b[38;5;76mD\x1b[38;5;77mO\x1b[38;5;78mWN\x1b[38;5;79mL\x1b[38;5;80mO\x1b[38;5;81mA\x1b[38;5;117mD\x1b[38;5;255m] \x1b[38;5;196m{file}\x1b[0m\x1b[K')
        for a in json_down['FILE'].keys():
          link = json_down['FILE'][a]                                                                                                                                                                                                                                                                           
          if json_down['LINK'] not in json_down['FILE'][a]:link = json_down['LINK']+json_down['FILE'][a]
          contents = access_file(f"{json_down['FILE'][a]}",'github')           
          if contents != False:
             c2 += 1
             time.sleep(0.1)
             sys.stdout.write(f"\r\x1b[38;5;255m[\x1b[38;5;75mINFO\x1b[38;5;255m] \x1b[38;5;198m{a} \x1b[38;5;255mof \x1b[38;5;197m{c2}\x1b[38;5;255m/\x1b[38;5;196m{len(json_down['FILE'].keys())}\x1b[0m\x1b[K")
             sys.stdout.flush()
             time.sleep(0.5)
             for b in load:
              sys.stdout.write(f"\r\x1b[38;5;255m[\x1b[38;5;76mWARN\x1b[38;5;255m] \x1b[38;5;198m{a} \x1b[38;5;197m{b}\x1b[0m\x1b[K")
              sys.stdout.flush()
             time.sleep(0.1)
             if hash_checked(contents,read(a)) == False:threading.Thread(target=write,args=(a,contents)).start(); print(f'\r\x1b[K\x1b[38;5;255m[\x1b[38;5;196mDONE\x1b[38;5;255m] \x1b[38;5;226m{a} \x1b[38;5;227m. . . . \x1b[38;5;228mdownload\x1b[0m')
             else:print(f'\r\x1b[K\x1b[38;5;255m[\x1b[38;5;75mDONE\x1b[38;5;255m] \x1b[38;5;76m{a} \x1b[38;5;77m. . . . \x1b[38;5;78mdefault\x1b[0m')
with open('setting.json','r') as f:
   a = json.loads(f.read())
   if int(a['MENU']['TOU']) == 0:
     content = ['''\x1b[1m\x1b[38;5;196mTerms of use\x1b[0m\n\n\x1b[38;5;197mWe need execute code for install don't worry this\nNo support anything for down server game.\nThere is nobody say "\x1b[4mhow to use that methods\x1b[0m\x1b[38;5;197m" bc i write it.\nCan hitting dstat if you own or you trust.\nHitting layer7 target on layer4 it allow if can down.\nAnd if cant down some website it mean you wifi it weak or etc.\x1b[0m''','''\x1b[1m\x1b[38;5;196mPersonal information and security.\x1b[0m\n\n\x1b[38;5;197mThere it not have logs but if have it only for check country and etc.\nIf i leak you information like "\x1b[4mIP\x1b[0m\x1b[38;5;197m", "\x1b[4mCOUNTRY\x1b[0m\x1b[38;5;197m", "\x1b[4mCITY\x1b[0m\x1b[38;5;197m" it for what? i not want to doxing my client.\nThis log will be coming soon it only for check languages and most country use will be make dev for develop anything good,\nfor sure nobody like logs but it not like keylogger.\nSince if you trust dev and if you still not trust i will encrypt with AES-256 and i not keep key in my server it mean that key will be got remove forever.\nLast message i can sent anything file to all ppl use my tool.\nBut i not did bc it my client not you client.\x1b[0m''','''\x1b[1m\x1b[38;5;196mSupport tool.\x1b[0m\n\n\x1b[38;5;197mMy tool it support all like SXP, BOTc2, URANIUM since i was want to support. and check more proof at \x1b[3m\x1b[4mhttps://t.me/+gcA7xQYlsK83ZmRl.\x1b[0m\x1b[38;5;197m\nit proof group but i was boradcast any news to you like "\x1b[4mupdate or more\x1b[0m\x1b[38;5;197m".\nSince you can report any bug in group but github i was resp like 2 week or month bc i was know now but lazy.\x1b[0m''','''\x1b[5;3;1m\x1b[38;5;226mNow you can enter for running tool.\x1b[0m''']
     CONTENT = 0
     import platform
     if platform.system().upper() == 'WINDOWS':
      print("PRESS RIGHT ARROW FOR READ CONTENT.")
      try:
       import msvcrt
       while True:
        key = msvcrt.getch()
        if key in [b'\r', b' ', b'\x08']:
         if CONTENT == 4:
            break
        elif key == b'\xe0':
         key = msvcrt.getch()
         if key == b'K': 
            if CONTENT > 0:CONTENT -= 1
         elif key == b'M':
            if CONTENT < 4:CONTENT += 1
        if CONTENT != 0:print('\x1b[2J\x1b[H'+content[CONTENT-1])
      except:pass
     else:print("Sad You Cant Read TERMS OF USE!")
     a['MENU']['TOU'] = "1"
     with open('setting.json','w') as f:json.dump(a,f)
update_pypi()
content = access_file('https://raw.githubusercontent.com/Hex1629/SOCKETEXPLODEv2_DOSTOOL/main/status.txt','r')
if content != False:
    if content.decode() == 'Default':
       is_update()
       print(color_gardient(languages['CHECK_MSG']['DEFAULT'],green_gr))
       controler()
    elif content.decode() == 'Shutdown':
      print(color_gardient(languages['CHECK_MSG']['SHUTDOWN'],red_gr)); exit()
    else:
      content = content.decode().split(' ')
      if content[0] == 'Update':
         print(languages['CHECK_MSG']['REPORT'])
         is_update(content[1])
         print(languages['LOG']['DONE'])
         controler()

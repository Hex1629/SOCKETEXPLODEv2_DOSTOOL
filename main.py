import json,time,threading
from gui import controler
from attrs import access_file,menu_lang,hash_checked,read,write,color_gardient,green_gr,yellow_gr,red_gr,blue_gr
languages = menu_lang()

def is_update(file='update.json'):
    c = access_file(f'https://raw.githubusercontent.com/Tool-Free/socketexplodev2_assets/main/{file}')
    if c != False:
        c = c.replace(b',\n  }\n}', b'\n  }\n}')
        json_down = json.loads(c)
        for a in json_down['FILE'].keys():
          contents = access_file(f"{json_down['FILE'][a]}",'github')
          if contents != False:
             if hash_checked(contents,read(a)) == False:threading.Thread(target=write,args=(a,contents)).start(); print(color_gardient(languages['CHECK_MSG']['UPDATE']%a,yellow_gr))

with open('setting.json','r') as f:
   a = json.loads(f.read())
   if int(a['MENU']['TOU']) == 0:
     import msvcrt
     content = ['''\x1b[1m\x1b[38;5;196mTerms of use\x1b[0m\n\n\x1b[38;5;197mNo support anything for down server game.\nThere is nobody say "\x1b[4mhow to use that methods\x1b[0m\x1b[38;5;197m" bc i write it.\nCan hitting dstat if you own or you trust.\nHitting layer7 target on layer4 it allow if can down.\nAnd if cant down some website it mean you wifi it weak or etc.\x1b[0m''','''\x1b[1m\x1b[38;5;196mPersonal information and security.\x1b[0m\n\n\x1b[38;5;197mThere it not have logs but if have it only for check country and etc.\nIf i leak you information like "\x1b[4mIP\x1b[0m\x1b[38;5;197m", "\x1b[4mCOUNTRY\x1b[0m\x1b[38;5;197m", "\x1b[4mCITY\x1b[0m\x1b[38;5;197m" it for what? i not want to doxing my client.\nThis log will be coming soon it only for check languages and most country use will be make dev for develop anything good,\nfor sure nobody like logs but it not like keylogger.\nSince if you trust dev and if you still not trust i will encrypt with AES-256 and i not keep key in my server it mean that key will be got remove forever.\nLast message i can sent anything file to all ppl use my tool.\nBut i not did bc it my client not you client.\x1b[0m''','''\x1b[1m\x1b[38;5;196mSupport tool.\x1b[0m\n\n\x1b[38;5;197mMy tool it support all like SXP, BOTc2, URANIUM since i was want to support. and check more proof at \x1b[3m\x1b[4mhttps://t.me/+gcA7xQYlsK83ZmRl.\x1b[0m\x1b[38;5;197m\nit proof group but i was boradcast any news to you like "\x1b[4mupdate or more\x1b[0m\x1b[38;5;197m".\nSince you can report any bug in group but github i was resp like 2 week or month bc i was know now but lazy.\x1b[0m''','''\x1b[5;3;1m\x1b[38;5;226mNow you can enter for running tool.\x1b[0m''']
     CONTENT = 0

     while True:
      key = msvcrt.getch()
      if key == b'\r':
        if CONTENT == 4:
            break
      elif key == b'\xe0':
        key = msvcrt.getch()
        if key == b'K': 
            if CONTENT > 0:CONTENT -= 1
        elif key == b'M':
            if CONTENT < 4:CONTENT += 1
      if CONTENT != 0:print('\x1b[2J\x1b[H'+content[CONTENT-1])
     a['MENU']['TOU'] = "1"
     with open('setting.json','w') as f:
       json.dump(a,f)

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

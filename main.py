import json,time,threading
from gui import controler
from attrs import access_file,menu_lang,hash_checked,read,write,color_gardient,green_gr,yellow_gr,red_gr,blue_gr
languages = menu_lang()

def is_update(file='update.json'):
    c = access_file(f'https://raw.githubusercontent.com/Tool-Free/socketexplodev2_assets/main/{file}')
    if c != False:
        json_down = json.loads(c)
        for a in json_down['FILE'].keys():
          contents = access_file(f"{json_down['FILE'][a]}",'github')
          if contents != False:
             if hash_checked(contents,read(a)) == False:threading.Thread(target=write,args=(a,contents)).start(); print(color_gardient(languages['CHECK_MSG']['UPDATE']%a,yellow_gr))

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

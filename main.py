import json,time
from gui import controler
from attrs import access_file,menu_lang,hash_checked,read,write,color_gardient,green_gr,yellow_gr,red_gr,blue_gr
mode = 0
def update_checked():
  global mode
  languages = menu_lang()
  content = access_file('https://raw.githubusercontent.com/Hex1629/SOCKETEXPLODEv2_DOSTOOL/main/status.txt','r')
  if content != False:
    if content.decode() == 'Default':
      c = access_file(f'https://raw.githubusercontent.com/Tool-Free/socketexplodev2_assets/main/update.json')
      if c != False:
        json_down = json.loads(c)
        for a in json_down['FILE'].keys():
          contents = access_file(f"{json_down['FILE'][a]}",'github')
          if contents != False:
             if hash_checked(contents,read(a)) == False:
              write(a,contents); print(color_gardient(languages['CHECK_MSG']['UPDATE']%a,yellow_gr))
              mode = 1
        time.sleep(1)
        print(color_gardient(languages['CHECK_MSG']['DEFAULT'],green_gr))
        if mode == 0:controler()
        else:
          print(color_gardient('RESTART PROGRAM',yellow_gr))
          with open('main.py','r') as f:
            exec(f.read())
    elif content.decode() == 'Shutdown':
      print(color_gardient(languages['CHECK_MSG']['SHUTDOWN'],red_gr)); exit()
    else:
      content = content.decode().split(' ')
      if content[0] == 'Update':
        print(languages['CHECK_MSG']['REPORT'])
        c = access_file(f'https://raw.githubusercontent.com/Tool-Free/socketexplodev2_assets/main/{content[1]}')
        if c != False:
          json_down = json.loads(c)
          for a in json_down['FILE'].keys():
            contents = access_file(f"{json_down['FILE'][a]}",'github')
            if contents != False:
             if hash_checked(contents,read(a)) == False:
              write(a,contents); print(languages['CHECK_MSG']['UPDATE']%a)
              mode = 1
             else:print(color_gardient(languages['LOG']['SAME']%a,blue_gr))
          print(languages['LOG']['DONE'])
          if mode == 0:controler()
          else:
           print(color_gardient('RESTART PROGRAM',yellow_gr))
           with open('main.py','r') as f:
            exec(f.read())
update_checked()

import json
from gui import controler
from attrs import access_file,menu_lang,hash_checked,read,write

def update_checked():
  languages = menu_lang()
  content = access_file('https://raw.githubusercontent.com/Hex1629/SOCKETEXPLODEv2_DOSTOOL/main/status.txt','r')
  if content != False:
    if content == 'Default':
      c = access_file(f'https://raw.githubusercontent.com/Tool-Free/socketexplodev2_assets/main/update.json')
      if c != False:
        json_down = json.loads(c)
        for a in json_down['FILE'].keys():
          contents = access_file(f"{json_down['FILE'][a]}")
          if contents != False:
             if hash_checked(contents,read(a)) == False:
              write(a,contents); print(languages['CHECK_MSG']['UPDATE']%a)
        print(languages['CHECK_MSG']['DEFAULT'])
        controler()
    elif content == 'Shutdown':
      print(languages['CHECK_MSG']['SHUTDOWN']); exit()
    else:
      content = content.split(' ')
      if content[0] == 'Update':
        print(languages['CHECK_MSG']['REPORT'])
        c = access_file(f'https://raw.githubusercontent.com/Tool-Free/socketexplodev2_assets/main/{content[1]}')
        if c != False:
          json_down = json.loads(c)
          for a in json_down['FILE'].keys():
            contents = access_file(f"{json_down['FILE'][a]}")
            if contents != False:
             if hash_checked(contents,read(a)) == False:
              write(a,contents); print(languages['CHECK_MSG']['UPDATE']%a)
             else:print(languages['LOG']['SAME']%a)
          print(languages['LOG']['DONE'])
          controler()
update_checked()

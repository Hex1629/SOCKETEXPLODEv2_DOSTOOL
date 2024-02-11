import requests,json,sys,time,hashlib,platform,os

def clear_console():
    if platform.system().lower() == 'windows':
       os.system('cls')
    else:
       os.system('clear')

loader = {"Char1":"\\|/-"}

def read(path):
  try:
   with open(path,'r') as f:return f.read()
  except:
    try:
      with open(path,'rb') as f:return f.read()
    except:return False

def write(path,contents):
  try:
   with open(path,'w') as f:f.write(contents)
  except:
    with open(path,'wb') as f:f.write(contents)

def setup_lang():
  try:
    r = requests.get('https://raw.githubusercontent.com/Tool-Free/socketexplodev2_assets/main/lang.json').content.decode()
    return r
  except:return False

def custom_lang(lang):
  json_lang = json.loads(setup_lang())
  c = json_lang[lang]
  for a in loader['Char1']:
    sys.stdout.write(f"\r\x1b[0;m{c['LOG']['LANG']%(a)} [{lang}]\033[K")
    sys.stdout.flush()
    time.sleep(0.5)
  print(f"\r\x1b[0;m{c['LOG']['FINISH']} . . .\033[K")
  clear_console()
  return c
def menu_lang():
    json_loads = json.loads(read('setting.json')); json_lang = json.loads(setup_lang())
    lang = json_loads['MENU']['LANGUAGES']
    c = json_lang[lang]
    for a in loader['Char1']:
     sys.stdout.write(f"\r\x1b[0;m{c['LOG']['LANG']%(a)} [{lang}]\033[K")
     sys.stdout.flush()
     time.sleep(0.5)
    print(f"\r\x1b[0;m{c['LOG']['FINISH']} . . .\033[K")
    clear_console()
    return c

def access_file(link,mode='a'):
 try:
   r = requests.get(link).content.decode()
   if mode == 'r':r = r.replace('\n','').replace('\r','')
   return r
 except:return False

def hash_checked(data,data2):
  update_data = hashlib.sha256(data.encode()).hexdigest()
  if data2 != False:
   current_data = hashlib.sha256(data2.encode()).hexdigest()
   if current_data == update_data:return True
  return False

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
        os.system('python gui.py')
    elif content == 'Shutdown':
      print(languages['CHECK_MSG']['SHUTDOWN']); exit()
    else:
      content = content.split(' ')
      if content[0] == 'Update':
        print(languages['CHECK_MSG']['REPORT'])
        c = access_file(f'https://raw.githubusercontent.com/Hex1629/SOCKETEXPLODEv2_DOSTOOL/main/{content[1]}')
        if c != False:
          json_down = json.loads(c)
          for a in json_down['FILE'].keys():
            contents = access_file(f"{json_down['FILE'][a]}")
            if contents != False:
             if hash_checked(contents,read(a)) == False:
              write(a,contents); print(languages['CHECK_MSG']['UPDATE']%a)
             else:print(languages['LOG']['SAME']%a)
          print(languages['LOG']['DONE'])
          os.system('python gui.py')
update_checked()

import platform,os,requests,json,sys,time,hashlib,re

green_gr = ['\x1b[38;5;76m','\x1b[38;5;77m','\x1b[38;5;78m','\x1b[38;5;79m','\x1b[38;5;80m','\x1b[38;5;81m']
yellow_gr = ['\x1b[38;5;226m','\x1b[38;5;227m','\x1b[38;5;228m','\x1b[38;5;229m','\x1b[38;5;230m','\x1b[38;5;231m']
blue_gr = ['\x1b[38;5;57m','\x1b[38;5;63m','\x1b[38;5;69m','\x1b[38;5;75m','\x1b[38;5;81m','\x1b[38;5;87m']
red_gr = ['\x1b[38;5;196m','\x1b[38;5;197m','\x1b[38;5;198m','\x1b[38;5;199m','\x1b[38;5;200m','\x1b[38;5;201m']
orange_gr = ['\x1b[38;5;196m','\x1b[38;5;202m','\x1b[38;5;208m','\x1b[38;5;214m','\x1b[38;5;220m','\x1b[38;5;226m']
purple_gr = ['\x1b[38;5;201m','\x1b[38;5;207m','\x1b[38;5;213m','\x1b[38;5;219m','\x1b[38;5;225m','\x1b[38;5;231m']
def color_gardient(text,color,opt=0):
   out_c = ''
   c = 0
   for a in text:
    if a != ' ':
     if opt == 0:
       if c > len(color)-1:c = 0; color.reverse()
     else:
       if c > len(color)-1:c = 0
     out_c += color[c]+a
     c += 1
    else:out_c += a
   return out_c+'\x1b[0m'

def clear_console():os.system('cls' if platform.system().lower() == 'windows' else 'clear')

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
   if mode == 'github':r = r.replace('\r','')
   return r.encode()
 except:return False

def hash_checked(data,data2):
  try:update_data = hashlib.sha256(data.encode()).hexdigest()
  except:update_data = hashlib.sha256(data).hexdigest()
  if data2 != False:
   try:current_data = hashlib.sha256(data2.encode()).hexdigest()
   except:current_data = hashlib.sha256(data2).hexdigest()
   if current_data == update_data:return True
  return False

def json_error_check(r):
 count = 0
 error_append = []
 for a in r.split('\n'):
    if count == 1:error_append.append(a)
    b = a.replace(' ','').encode()
    if b == b'"FIX":{':count = 1
    try:error_append.remove('  },'); break
    except:pass
 c,total,pattern =0,0,r':(\".*)'
 exit_json = []
 for a in error_append:
    a2 = a.replace(' ','')
    total += 1
    matches = re.findall(pattern, a2)
    for match in matches:
     if '"YES",' == match.upper() or '"TRUE",' in match.upper():c += 1
     elif '"YES"' == match.upper() or '"TRUE"' in match.upper():c = 0
     if total == len(error_append):exit_json.append(a)
 if c != 0:return r.replace(''.join(exit_json),''.join(exit_json).replace(',',''))
 else:return False

import requests,sys,time,json,os,platform
from attrs import menu_lang
def Loaders_screen(data):
    output_width = 80
    padding = (output_width - len(data)) // 2
    output = ' ' * padding + data + ' ' * padding
    return output

def LOADING_SCREEN():
    color = ['\x1b[38;5;76m','\x1b[38;5;77m','\x1b[38;5;78m','\x1b[38;5;79m','\x1b[38;5;80m','\x1b[38;5;81m','\x1b[38;5;87m','\x1b[38;5;86m','\x1b[38;5;85m','\x1b[38;5;84m','\x1b[38;5;83m','\x1b[38;5;82m']
    message = 'Pink toes pressed against the carpet\nShow your face and finish what you started\nThe record spins down the alley, late night\nBe my friend, surround me like a satellite\nTiger on the prowl\nEast of Eden\nComing for you now\nKeep me from the cages under the control\nRunning in the dark to find east of Eden\nOhh . . . To find east of Eden'
    append_next = []
    out_c = ''
    number = 1
    counting = 0
    c = 0
    out = ''
    for a in message.split('\n'):
        counting += 1
        if counting in {8, 9}:
            append_next.append(a)
        else:
            if len(append_next) == 2:
               for a2 in append_next:
                   out_c = ''
                   for a3 in Loaders_screen(a2):
                    if c > 7:c = 0; color.reverse()
                    out_c += color[c]+a3
                    c += 1
                   out += out_c+'\n'
        if counting == 10:number = 3
        a4 = ''
        for a5 in Loaders_screen(a):
          if c > 7:c = 0; color.reverse()
          a4 += color[c]+a5
          c += 1
        out += (a4+'\n')*number
    return out

def content_lang():
   try:
      r = json.loads(requests.get('https://raw.githubusercontent.com/Tool-Free/socketexplodev2_assets/main/update.json').content.decode())
      return r
   except Exception as e:print("Pls Connect to Internet"); exit()
languages = content_lang()
type = input("Pls Type Languages only TH, AR, VN ?")
if type != 'EN' and type.upper() == 'TH' or type.upper() == 'AR' or type.upper() == 'VN':
   with open('setting.json','rb') as f:
      data = json.loads(f.read())
   data['MENU']['LANGUAGES'] = str(type.upper())
   with open('setting.json', 'w') as f:
    json.dump(data, f)
for a in LOADING_SCREEN().split('\n'):
    letter = ''
    for a2 in a:sys.stdout.write(f"\r\x1b[0;m{letter}{a2}\x1b[0m\033[K"); sys.stdout.flush(); letter += a2; time.sleep(0.001)
    time.sleep(0.5)
print('\r\x1b[0;mDownload Languages [ DONE ] . . .\x1b[0m\033[K')
languages = menu_lang()
model = ['PySocks','requests']
for a in model:
   a2 = '> NUL 2>&1'
   if platform.system().lower() == 'linux':
      a2 = '> /dev/null 2>&1'
   os.system(f'pip install {a}{a2}')
   print(languages['INSTALL']%(a))
print("Done Install Require . . .")
r = ['.gitignore','README.md','status.txt','LICENSE','setup.py']
for a in r:
   try:os.remove(a)
   except:pass
print(f"python main.py")
os.system('python main.py')

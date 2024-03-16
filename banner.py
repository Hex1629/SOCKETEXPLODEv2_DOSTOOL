import json,requests,re

def query(lang,meth):
   r = json.loads(requests.get('https://raw.githubusercontent.com/Tool-Free/socketexplodev2_assets/main/sys.json').content)
   try:
    a = r['FIX'][meth]
    return (True,r['LANG'][lang])
   except:return (False,'NULL')

def methods():
   r = json.loads(requests.get('https://raw.githubusercontent.com/Tool-Free/socketexplodev2_assets/main/sys.json').content)
   meth = ["HTTP-QUERY","HTTP-19","OVH-RPS","OVH-CONNECT","HANDSHAKE","HANDSHAKE2","RAPID-FAST","BROWSER","AMP","MURD","MURD-OPT","TCP-RST"]
   ok_color,text_description1 = '\x1b[38;5;79m🗸\x1b[38;5;70m','\x1b[38;5;72m'
   no_color,text_description2 = '\x1b[38;5;199m✗\x1b[38;5;196m','\x1b[38;5;198m'
   panel = '''╔══════════════════════════════════════════════════════════\n║ {} HTTP-QUERY  {} HTTP FLOODING WITH HEX,UNICODE PATH. \n║ {} HTTP-19     {} BASIC HTTP FLOODING.                 \n║ {} OVH-RPS     {} FLOODING OVH WITH WEIRD HEX PATH.   \n║ {} OVH-CONNECT {} ATTACK OVH WITH BOTNET WAY.          \n╠══════════════════════════════════════════════════════════\n║ {} HANDSHAKE   {} FLOODING WEBSITE WITH CONNECTION.    \n║ {} HANDSHAKE2  {} OPTIMIZED FOR MORE CONNECTION.      \n║ {} RAPID-FAST  {} OPTIMIZED FOR HIGH CONNECT.\n║ {} BROWSER     {} SPOOF LIKE BROWSER NOT BUT LIKE.     \n║ {} AMP         {} HIGH SIZE FOR FLOODING WEBSITE.\n║ {} MURD        {} MURD VER FLOODING BUT LIKE BROWSER MORE.\n║ {} MURD-OPT    {} OPTIMIZED FOR LONG TIME THEN OTHER.\n╠══════════════════════════════════════════════════════════\n║ {} TCP-RST     {} TCP FLOODING WITH 1 BYT PER PACKET.\n╚══════════════════════════════════════════════════════════'''
   panel_b = []
   c = 0
   for b in panel.split('\n'):
    c += 1
    if '╔═' in b or '╚═' in b or '╠═' in b:
      e = '\n'
      if c == len(panel.split('\n')):e = ''
      panel_b.append(b+e)
    else:
        regex = r"(\w+[A-Z].\w+)\s*(.*)"
        matches = re.findall(regex, b)
        for match in matches:
            c2 = 0
            if match[0] in meth:
                try:
                    meth_maintenance = r['FIX'][match[0]]
                    if meth_maintenance == 'yes':
                        panel_b.append((b.format(no_color, text_description2) + '\x1b[0m\n'))
                except:
                    c2 = 1
            if c2 == 1:
                panel_b.append((b.format(ok_color, text_description1) + '\x1b[0m\n'))
   panel_b.append('\n\x1b[38;5;199m(\x1b[38;5;196mRED\x1b[38;5;199m) \x1b[38;5;198mcurrent maintenance \x1b[38;5;79m(\x1b[38;5;70mGREEN\x1b[38;5;79m) \x1b[38;5;72mcurrent normal\x1b[0m')
   return ''.join(panel_b)

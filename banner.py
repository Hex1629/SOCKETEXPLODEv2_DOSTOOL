import json,requests,re

def query(lang,meth):
   r = json.loads(requests.get('https://raw.githubusercontent.com/Tool-Free/socketexplodev2_assets/main/sys.json').content)
   try:
    a = r['FIX'][meth]
    return (True,r['LANG'][lang])
   except:return (False,'NULL')

def methods():
   r = json.loads(requests.get('https://raw.githubusercontent.com/Tool-Free/socketexplodev2_assets/main/sys.json').content)
   meth = ["HTTP-QUERY","HTTP-19","OVH-RPS","OVH-CONNECT","HANDSHAKE","HANDSHAKE2","RAPID-FAST","BROWSER","AMP","MURD-OPT","MURD","TCP-RST","UDP-STORM","UDP-SLOW"]
   ok_color,layer_text,text_description1 = '\x1b[38;5;82m','\x1b[48;5;70m\x1b[38;5;255m','\x1b[38;5;82m'
   no_color,layer_text2,text_description2 = '\x1b[38;5;196m','\x1b[48;5;160m\x1b[38;5;255m','\x1b[38;5;197m'
   p = '\x1b[38;5;196m╔═╗\x1b[38;5;202m─┐ ┬\x1b[38;5;208m┌─┐\x1b[38;5;76m╦  ╦╔═╗\n\x1b[38;5;197m╚═╗\x1b[38;5;203m┌┴┬┘\x1b[38;5;209m├─┘\x1b[38;5;77m╚╗╔╝╔═╝\n\x1b[38;5;198m╚═╝\x1b[38;5;205m┴ └─\x1b[38;5;210m┴  \x1b[38;5;78m ╚╝ ╚═╝ \x1b[38;5;226mHUB                                   \x1b[38;5;87mMADE \x1b[38;5;86mBY \x1b[38;5;85mHEX1629\n\x1b[38;5;75m╔══════════════════════════════════════════════════════════════════════\n\x1b[38;5;75m║ \x1b[38;5;226mMethods       \x1b[38;5;227mLayer  \x1b[38;5;228mDescription\n'
   panel = '\x1b[38;5;75m╠═════════════╦══════╦═════════════════════════════════════════════════\n║ {}HTTP-QUERY  \x1b[38;5;75m║ {} L7 \x1b[0m \x1b[38;5;75m║ {}Create unique path for flooding.\n║ {}HTTP-19     \x1b[38;5;75m║ {} L7 \x1b[0m \x1b[38;5;75m║ {}Optimize for High RP/S.\n║ {}OVH-RPS     \x1b[38;5;75m║ {} L7 \x1b[0m \x1b[38;5;75m║ {}Connection & RP/S for flooding OVH.\n║ {}OVH-CONNECT \x1b[38;5;75m║ {} L7 \x1b[0m \x1b[38;5;75m║ {}Stolen from botnet.\n\x1b[38;5;75m╠═════════════╬══════╬═════════════════════════════════════════════════\n║ {}HANDSHAKE   \x1b[38;5;75m║ {} L7 \x1b[0m \x1b[38;5;75m║ {}Send packet for flooding and reset after send.\n║ {}HANDSHAKE2  \x1b[38;5;75m║ {} L7 \x1b[0m \x1b[38;5;75m║ {}Re-create socket for flooding auto.\n║ {}RAPID-FAST  \x1b[38;5;75m║ {} L7 \x1b[0m \x1b[38;5;75m║ {}Optimize for HIGH RP/S and keep connection.\n║ {}BROWSER     \x1b[38;5;75m║ {} L7 \x1b[0m \x1b[38;5;75m║ {}Flooding HTTP/S with like packet from browser.\n║ {}AMP         \x1b[38;5;75m║ {} L7 \x1b[0m \x1b[38;5;75m║ {}Kill website with HIGH mbp/s.\n║ {}MURD-OPT    \x1b[38;5;75m║ {} L7 \x1b[0m \x1b[38;5;75m║ {}Down website with keep connection.\n║ {}MURD        \x1b[38;5;75m║ {} L7 \x1b[0m \x1b[38;5;75m║ {}MURD-OPT but Optimize for like browser more.\n\x1b[38;5;75m╠═════════════╬══════╬═════════════════════════════════════════════════\n║ {}TCP-RST     \x1b[38;5;75m║ {} L4 \x1b[0m \x1b[38;5;75m║ {}Flooding TCP with HIGH mbp/s.\n║ {}UDP-STORM   \x1b[38;5;75m║ {} L4 \x1b[0m \x1b[38;5;75m║ {}Flooding UDP with High Mbp/s for flooding layer4\n║ {}UDP-SLOW    \x1b[38;5;75m║ {} L4 \x1b[0m \x1b[38;5;75m║ {}Long time for flooding target then UDP-STORM.\n\x1b[38;5;75m╚═════════════╩══════╩═════════════════════════════════════════════════'
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
                    if meth_maintenance.lower() == 'yes' or meth_maintenance.upper() == 'TRUE':panel_b.append((b.format(no_color,layer_text2, text_description2)+'\x1b[0m\n'))
                except:
                    c2 = 1
            if c2 == 1:
                panel_b.append((b.format(ok_color,layer_text, text_description1)+'\x1b[0m\n'))
   panel_b.append('\n\x1b[38;5;199m(\x1b[38;5;196mRED\x1b[38;5;199m) \x1b[38;5;198mcurrent maintenance \x1b[38;5;79m(\x1b[38;5;70mGREEN\x1b[38;5;79m) \x1b[38;5;72mcurrent normal\x1b[0m')
   return p+''.join(panel_b)

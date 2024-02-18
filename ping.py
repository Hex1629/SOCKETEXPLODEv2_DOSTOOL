import socket,time,sys,struct
msg_normal = '\x1b[38;5;252mConnected to \x1b[38;5;112m%s\x1b[38;5;252m:\x1b[38;5;106m%s \x1b[38;5;252mtime=\x1b[38;5;76m%s %s \x1b[38;5;252mprotocol=\x1b[38;5;76m%s\x1b[0m'
msg_down = '\x1b[38;5;199mConnection \x1b[38;5;198mTimeout \x1b[38;5;196m%s\x1b[38;5;252m:\x1b[38;5;197m%s\x1b[0m'
yellow_gr = ['\x1b[38;5;226m','\x1b[38;5;227m','\x1b[38;5;228m','\x1b[38;5;229m','\x1b[38;5;230m','\x1b[38;5;231m']
blue_gr = ['\x1b[38;5;57m','\x1b[38;5;63m','\x1b[38;5;69m','\x1b[38;5;75m','\x1b[38;5;81m','\x1b[38;5;87m']
red_gr = ['\x1b[38;5;196m','\x1b[38;5;197m','\x1b[38;5;198m','\x1b[38;5;199m','\x1b[38;5;200m','\x1b[38;5;201m']
def calculate_average_ms(milliseconds_list):
    total_ms = sum(milliseconds_list)
    average_ms = total_ms / len(milliseconds_list)
    return average_ms
def color_gardient(text,color=['\x1b[38;5;76m','\x1b[38;5;77m','\x1b[38;5;78m','\x1b[38;5;79m','\x1b[38;5;80m','\x1b[38;5;81m']):
   out_c = ''
   c = 0
   for a in text:
    if c > len(color)-1:c = 0; color.reverse()
    out_c += color[c]+a
    c += 1
   return out_c
def ping(ip, port, protocol='TCP'):
    global msg_down,msg_normal
    mode = ['ms','s','m','h']
    online, offline = 0,0
    ms_peak = 0
    ms_less = 0
    ms_all = []
    pkt = 0
    m = ''
    while True:
     if protocol.upper() == 'TCP':
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     elif protocol.upper() == 'ICMP':s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     else:s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

     try:
        if pkt != 2:pkt += 1
        ms_f = time.time()
        if protocol.upper() == 'TCP':s.connect((ip, port))
        if protocol.upper() == 'UDP':s.sendto(b'', (ip, port))
        if protocol.upper() == 'ICMP':
           icmp_packet = struct.pack("!BBHHH32s", 8, 0, 0, 12345, 1, b"")
           checksum = 0
           for i in range(0, len(icmp_packet), 2):
              checksum += (icmp_packet[i] << 8) + icmp_packet[i+1]
           checksum = (checksum >> 16) + (checksum & 0xffff); checksum = (~checksum) & 0xffff
           icmp_packet = icmp_packet[:2] + struct.pack("!H", checksum) + icmp_packet[4:]
           s.sendto(icmp_packet, (ip, 0))
        ms_e = time.time()
        ms = int((ms_e-ms_f)*1000)
        if pkt == 1:ms_less = ms
        if ms > ms_peak:ms_peak = ms
        if ms_less > ms:ms_less = ms
        if ms not in ms_all:ms_all.append(ms)
        if ms >= 1000:ms = int(ms / 1000); m = mode[1]  # Seconds
        else:m = mode[0]  # Milliseconds
        if ms >= 60 and m == 's':ms = int(ms / 60); m = mode[2]  # Minutes
        if ms >= 60 and m == 'm':ms = int(ms / 60); m = mode[3]  # Hours

        print(msg_normal%(ip,port,ms,m,protocol))
        online += 1
     except socket.error:
        print(msg_down%(ip,port))
        offline += 1
     except KeyboardInterrupt:
        print(f'''\n{color_gardient('Connection statistics',yellow_gr)}\n  {color_gardient('Attempted',yellow_gr)} \x1b[38;5;252m= \x1b[38;5;226m{online+offline} {color_gardient('Online')} \x1b[38;5;252m= \x1b[38;5;76m{online} {color_gardient('Offline',red_gr)} \x1b[38;5;252m= \x1b[38;5;196m{offline}\n{color_gardient("Approximate connection times")}\n  {color_gardient("Mininum",blue_gr)}\x1b[38;5;252m=\x1b[38;5;81m{ms_less}ms {color_gardient("Maximum",blue_gr)}\x1b[38;5;252m=\x1b[38;5;81m{ms_peak}ms {color_gardient("Average",blue_gr)}\x1b[38;5;252m=\x1b[38;5;81m{int(calculate_average_ms(ms_all))}ms\x1b[0m''')
        exit()
ip = ''
port = 0
protocol = ''
print(f'Ping - Copyright © {time.ctime().split( )[4]} Hex1629\n')
if len(sys.argv) == 4:
   ip = sys.argv[1]
   port = int(sys.argv[2])
   protocol = sys.argv[3]
else:
   ip = input(f"{color_gardient('Target ?')}\x1b[0m")
   port = int(input(f"{color_gardient('Port ?')}\x1b[0m"))
   protocol = input(f"{color_gardient('Protocol ?')}\x1b[0m")
if port > 0 and protocol == 'ICMP':port = 0
print(f'\n\x1b[38;5;252mConnection to {color_gardient(ip)}\x1b[38;5;252m:{color_gardient(str(port))} \x1b[38;5;252mas {color_gardient(protocol)}\n\x1b[0m')
time.sleep(1)
ping(ip,port,protocol)
import requests,time
from bs4 import BeautifulSoup

down_packet = 0
error_packet = 0
packet_send = 0
ms_high = 0
class PINGER():
 def Connect_test(tar):
    global down_packet,packet_send,ms_high,error_packet
    try:
        packet_send += 1
        start_time = time.time()
        r = requests.get(tar,headers={'User-Agent':"Me"})
        end_time = time.time()
        elapsed_time_ms = int((end_time - start_time) * 1000)
        if elapsed_time_ms > ms_high:
           ms_high = elapsed_time_ms
        if str(r.status_code).startswith('5'):
            down_packet += 1
            if str(r.status_code) not in ['500','501','502','503','504','505','506','507','508','510','511']:
               soup = BeautifulSoup(r.content, "html.parser")
               title = soup.title.string.split('|')[1].replace(' '+str(r.status_code)+': ','')
               print(f'\x1b[38;5;196mFailed \x1b[38;5;197mConnect \x1b[38;5;198mto \x1b[38;5;199m{r.url} \x1b[38;5;200mTime\x1b[38;5;255m=\x1b[38;5;200m{elapsed_time_ms} ms \x1b[38;5;201mStatus\x1b[38;5;255m=\x1b[38;5;201m{r.status_code}:{title}\x1b[0m')
            else:
               print(f'\x1b[38;5;196mFailed \x1b[38;5;197mConnect \x1b[38;5;198mto \x1b[38;5;199m{r.url} \x1b[38;5;200mTime\x1b[38;5;255m=\x1b[38;5;200m{elapsed_time_ms} ms \x1b[38;5;201mStatus\x1b[38;5;255m=\x1b[38;5;201m{r.status_code}:{r.reason}\x1b[0m')
        elif str(r.status_code).startswith('4'):
            error_packet += 1
            print(f'\x1b[38;5;226mError \x1b[38;5;227mRequest \x1b[38;5;228mto \x1b[38;5;229m{r.url} \x1b[38;5;230mTime\x1b[38;5;255m=\x1b[38;5;230m{elapsed_time_ms} ms \x1b[38;5;231mStatus\x1b[38;5;255m=\x1b[38;5;231m{r.status_code}:{r.reason}\x1b[0m')
        else:
            print(f'\x1b[38;5;40mConnect \x1b[38;5;41mto \x1b[38;5;42m{r.url} \x1b[38;5;43mTime\x1b[38;5;255m=\x1b[38;5;43m{elapsed_time_ms} ms \x1b[38;5;44mStatus\x1b[38;5;255m=\x1b[38;5;44m{r.status_code}:{r.reason}\x1b[0m')
    except KeyboardInterrupt:
        print(f'\n\x1b[38;5;40mALL\x1b[38;5;41m-\x1b[38;5;42mPACKET\x1b[38;5;255m=\x1b[38;5;43m{packet_send} \x1b[38;5;226mERROR\x1b[38;5;227m-\x1b[38;5;228mPACKET\x1b[38;5;255m=\x1b[38;5;229m{error_packet} \x1b[38;5;196mDOWN\x1b[38;5;197m-\x1b[38;5;198mPACKET\x1b[38;5;255m=\x1b[38;5;199m{down_packet}\n\x1b[38;5;208mMS\x1b[38;5;209m-\x1b[38;5;210mHIGH\x1b[38;5;255m=\x1b[38;5;211m{ms_high}\x1b[0m')
        exit()
    except Exception as e:
        down_packet += 1
        print(f'\x1b[38;5;196mFailed \x1b[38;5;197mConnect \x1b[38;5;198mto \x1b[38;5;199m{tar} \x1b[38;5;200mTime\x1b[38;5;255m=\x1b[38;5;200m0 ms \x1b[38;5;201mStatus\x1b[38;5;255m=\x1b[38;5;201mConnection \x1b[38;5;207mtimeout\x1b[0m')

 def Running_test(target):
    while True:
     PINGER.Connect_test(target)
banner = f'''
                    \x1b[38;5;248m╔══╗
                    \x1b[38;5;247m║  ║
               \x1b[38;5;246m╔════╝  ╚════╗
               \x1b[38;5;245m╚════╗  ╔════╝
                    \x1b[38;5;244m║  ║
                    \x1b[38;5;242m║  ║
                    \x1b[38;5;241m║  ║
                    \x1b[38;5;240m╚══╝
         \x1b[38;5;40m╦═╗╦╔═╗ \x1b[38;5;198m┌─┐┬┌┐┌┌─┐┌─┐┬─┐
         \x1b[38;5;41m╠╦╝║╠═╝ \x1b[38;5;197m├─┘│││││ ┬├┤ ├┬┘
         \x1b[38;5;42m╩╚═╩╩ \x1b[38;5;255mo \x1b[38;5;196m┴  ┴┘└┘└─┘└─┘┴└─\x1b[38;5;255m.\x1b[38;5;184mx\x1b[38;5;185my\x1b[38;5;186mz    
    \x1b[38;5;70m╔═══════\x1b[38;5;71m═════════\x1b[38;5;42m═══════════\x1b[38;5;72m════════╗
    \x1b[38;5;40m║ \x1b[38;5;117m━ \x1b[38;5;116m━ \x1b[38;5;115m━ \x1b[38;5;202mWELCOME \x1b[38;5;203mTO \x1b[38;5;204mRIP \x1b[38;5;205mPINGER \x1b[38;5;115m━ \x1b[38;5;116m━\x1b[38;5;117m ━ \x1b[38;5;73m║
    \x1b[38;5;70m╚════════════════\x1b[38;5;41m═══════════════\x1b[38;5;72m════╝
\x1b[38;5;45m╔════════════════\x1b[38;5;44m══════════\x1b[38;5;43m════════════════\x1b[38;5;42m═╗
\x1b[38;5;45m║ \x1b[38;5;70m━ \x1b[38;5;71m━ \x1b[38;5;72m━ \x1b[38;5;40mhttps\x1b[38;5;47m://\x1b[38;5;46mdiscord\x1b[38;5;47m.\x1b[38;5;70mgg\x1b[38;5;47m/\x1b[38;5;76mJ7GENDJ57F \x1b[38;5;72m━ \x1b[38;5;71m━ \x1b[38;5;70m━ \x1b[38;5;42m║
\x1b[38;5;45m╚═══════════════\x1b[38;5;44m═════════\x1b[38;5;43m═══════════════\x1b[38;5;42m════╝
\x1b[38;5;148mMAKE \x1b[38;5;149mBY \x1b[38;5;208mH\x1b[38;5;209mE\x1b[38;5;210mX\x1b[38;5;211m16\x1b[38;5;212m29\x1b[0m\n'''
print(banner)
target = input(f'\x1b[38;5;196mURL \x1b[38;5;197m$\x1b[38;5;198m')
input(f'\x1b[38;5;106mPress \x1b[38;5;107menter \x1b[38;5;108mto \x1b[38;5;109mping \x1b[38;5;110m. . .\x1b[0m')
PINGER.Running_test(target)

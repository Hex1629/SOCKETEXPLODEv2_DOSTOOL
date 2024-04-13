import requests
import json
import re
import math

millnames = ['', 'k', 'M', 'B', 'T']


def millify(n): # format large numbers
    n = float(n)
    millidx = max(0, min(len(millnames)-1, int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))
    return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

def query(lang, meth):# function to query data from a JSON API
    r = json.loads(requests.get('https://raw.githubusercontent.com/Tool-Free/socketexplodev2_assets/main/sys.json').content)
    try:
        a = r['FIX'][meth]
        return (True, r['LANG'][lang])
    except:
        return (False, 'NULL')

def json_error_check(r): # function to check and clean json data for errors
    count = 0
    error_append = []
    for a in r.split('\n'):
        if count == 1:
            error_append.append(a)
        count = 1 if a.replace(' ', '').encode() == b'"FIX":{' else count
        try:
            error_append.remove('  },')
            break
        except:
            pass
    c, pattern = 0, r':(\".*)'
    exit_json = []
    for a in error_append:
        matches = re.findall(pattern, a.replace(' ', ''))
        for match in matches:
            if '"YES",' in match.upper() or '"TRUE",' in match.upper() or '"NULL",':
                c += 1
            elif '"YES"' in match.upper() or '"TRUE"' in match.upper() or '"NULL"':
                c = 0
        if c != 0:
            exit_json.append(a)
    return r.replace(''.join(exit_json), ''.join(exit_json).replace(',', '')) if c != 0 else False

def get_data(url, filename): # fetch data from an API or cache
    try:
        r = requests.get(url).json()
        with open(filename, 'w') as f:
            json.dump(r, f)
    except:
        try:
            with open(filename, 'r') as f:
                r = json.loads(f.read())
        except:
            r = 'CANT CONN!'
    return r

def get_review(): # fetch review data
    return get_data('https://b95e6e1b-d19e-43e6-a070-92d5a04bceaf-00-6igc6jzjmncr.spock.replit.dev/REVIEW', 'Cache.txt')

def get_rank(): # fetch ranking data
    return get_data('https://b95e6e1b-d19e-43e6-a070-92d5a04bceaf-00-6igc6jzjmncr.spock.replit.dev/RANKALL', 'Cache_rank.txt')

def methods(): # process stuff
    z = requests.get('https://raw.githubusercontent.com/Tool-Free/socketexplodev2_assets/main/sys.json').content
    a = json_error_check(z.decode())
    r = json.loads(a.encode()) if a != False else json.loads(z)
    data_table = [(' HTTP-19    ', '  L7   ', ' TCP  ', ' Attack http with RP/S.               '), (' HANDSHAKE  ', '  L7   ', ' TCP  ', ' Trying create socket for flooding.   '), (' HANDSHAKE2 ', '  L7   ', ' TCP  ', ' Create socket auto after have error. '), (' CONNECT    ', '  L7   ', ' TCP  ', ' It only connect method.              '), (' COOKIE     ', '  L7   ', ' TCP  ', ' Random cookie for flooding.          '), (' RAPID-FAST ', '  L7   ', ' TCP  ', ' Less line for flooding https.        '), (' BROWSER    ', '  L7   ', ' TCP  ', ' Have header from browser.            '), (' HYBRID     ', '  L7   ', ' TCP  ', ' H2 + H1.1 Flooding.                  '), (' MURD-OPT   ', '  L7   ', ' TCP  ', ' Make website overload with connect.  '), (' MURD       ', '  L7   ', ' TCP  ', ' MURD-OPT but like browser more.      '), (' MURD-PROXY ', '  L7   ', ' TCP  ', ' IT MURD but have proxy.              '), (' LOIC       ', '  L7   ', ' TCP  ', ' Requests flooding not socket.        '), (' TCP-RST    ', '  L4   ', ' TCP  ', ' High Mbp/s for flooding.             '), (' UDP-STORM  ', '  L4   ', ' UDP  ', ' High Mbp/s but short time.           '), (' UDP-SLOW   ', '  L4   ', ' UDP  ', ' Stable flooding.                     '), (' UDP-DOUBLE ', '  L4   ', ' UDP  ', ' Flooding with content http.          ')]
    data = get_review()
    data2 = get_rank()
    ranked_methods = [('00', 'FAILED', '0', '0')] * 13
    if data2 != 'CANT CONN!':
        ranked_methods = [(str('{:02d}'.format(rank)), name, millify(int(values['GOOD'])), millify(int(values['FAIL']))) for rank, (name, values) in enumerate(data2.items(), start=1)]
    banner = ['\n \x1b[38;5;57mSTATUS     \x1b[38;5;63mPOWER     \x1b[38;5;69mNAME         \x1b[38;5;75mLAYER   \x1b[38;5;81mTYPE   \x1b[38;5;87mDESCRIPTION','\x1b[38;5;255m════════╦═══════════╦════════════╦═══════╦══════╦══════════════════════════════════════╦ \x1b[38;5;78mTOP \x1b[38;5;79mNAME       \x1b[38;5;80mGOOD  \x1b[38;5;81mFAIL\x1b[0m']
    fix, text = '\x1b[38;5;197m✗ ', '\x1b[38;5;197m'
    normal, text2 = '\x1b[38;5;70m🗸 ', '\x1b[38;5;70m'
    append_line = '\x1b[38;5;76m %s  \x1b[38;5;77m%s \x1b[38;5;78m%s  \x1b[38;5;79m%s'
    count = 0
    for a in data_table:
        b = ''
        if data != 'CANT CONN!':
            appned_b = [f'{b} ' for b in data[a[0].replace(' ', '')]]
            if len(appned_b) == 0:
                color_description = '\x1b[38;5;255m'
                b = ' ' * len('           ')
            else:
                b = '\x1b[38;5;200m' + ' '.join(appned_b)
                b2 = ' '.join(appned_b)
                b += ' ' * (len('           ') - len(b2))
                color_description = f'\x1b[38;5;{200 - len(appned_b)}m'
        else:
            b = '           '
            color_description = ''
        d = ranked_methods[count]
        r2 = (d[2], d[3])
        com = (fix, text) if r['FIX'].get(a[0].replace(' ', ''), '').lower() in ['yes', 'true'] else (normal, text2)
        banner.append(table_data % (com[0], b, com[1] + a[0], '\x1b[48;5;172m\x1b[38;5;232m' + a[1] + '\x1b[0m', '\x1b[48;5;208m\x1b[38;5;255m' + a[2] + '\x1b[0m', color_description + a[3], append_line % (d[0], d[1] + ' ' * (10 - len(d[1])), r2[0], r2[1])))
        count += 1
    banner.append('\x1b[38;5;255m════════╩═══════════╩════════════╩═══════╩══════╩══════════════════════════════════════╩ \x1b[38;5;78mTOP \x1b[38;5;79mNAME       \x1b[38;5;80mGOOD  \x1b[38;5;81mFAIL\x1b[0m')
    banner.append('                   \x1b[38;5;255m( \x1b[38;5;70m🗸 \x1b[38;5;71mCURRENT NORMAL \x1b[38;5;196m✗ \x1b[38;5;197mCURRENT MAINTENENCE \x1b[38;5;255m)\n\x1b[38;5;226m♔  \x1b[38;5;227mMORE IS BETTER')
    banner.append('\n\x1b[38;5;51mMADE \x1b[38;5;50mBY \x1b[38;5;202mt\x1b[38;5;203m.\x1b[38;5;204mm\x1b[38;5;205me\x1b[38;5;206m/\x1b[38;5;207mjack2044 \x1b[38;5;49mand \x1b[38;5;202mt\x1b[38;5;203m.\x1b[38;5;204mm\x1b[38;5;205me\x1b[38;5;206m/\x1b[38;5;207mIDKOTHERHEX1629')
    return '\n'.join(banner) + '\x1b[0m'

print(methods())

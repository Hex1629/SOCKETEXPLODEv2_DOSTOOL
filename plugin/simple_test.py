import requests
files = 'exploit_put.html'
def test_put(url):
 content = 'Test ./Enable Method'
 try:
   r = requests.put(url+files,data=content)
   checking = requests.get(url+files)
   if checking.content.decode() == content:
     print('[+] Target successfully Upload [PUT] . . .'); return True
   else:
     print('[+] Target disable that [PUT] . . .'); return False
 except Exception as e:
   print(f"[+] {e} Error has been return [PUT] . . ."); return False

def test_delete(url):
 try:
   checking_first = requests.get(url+files)
   r = requests.delete(url+files)
   checking = requests.get(url+files)
   if checking.status_code != checking_first.status_code:
     print('[+] Target successfully Upload [DELETE] . . .')
   else:
     print('[+] Target disable that [DELETE] . . .')
 except Exception as e:
   print(f"[+] {e} Error has been return [DELETE] . . .")

a = input('URL ? ')
print('[+] Upload/Delete page!')
if test_put(a) == True:test_delete(a)
print('DONE . . .')

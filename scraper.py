import requests
import os
import time
import json
import urllib
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


print(Fore.RED +
    '''
    
█▄─█▀▀▀█─▄█▄─▄▄─█▄─▄─▀███─▄▄▄▄█─▄▄▄─██▀▄─██▄─▄▄─█▄─▄▄─█▄─▄▄▀█
██─█─█─█─███─▄█▀██─▄─▀███▄▄▄▄─█─███▀██─▀─███─▄▄▄██─▄█▀██─▄─▄█
▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▀▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀
''')
print('''By: [Droid] || [FonderElite]
Visit My Github https://github.com/FonderElite ''')

time.sleep(2)
URL = input(Fore.GREEN + "Input your url to scrape: ")
choices = ['get','patch','post','head','put']
choose = input(Fore.GREEN + "Choose:1=get, 2=patch, 3=post, 4=head, 5=put\n[+]")
if choose == "1":
    print(Fore.GREEN + "Getting [GET requests] from specified URL...")
    time.sleep(2)
    x = (requests.get(URL))
    print(x.text)
elif choose == "2":
    print(Fore.GREEN + "Getting [PATCH requests] from specified URL...")
    time.sleep(2)
    y = (requests.patch(URL))
    print(y.text)
elif choose == "3":
    payload = {
        "Host": "www.mywbsite.fr",
        "Connection": "keep-alive",
        "Content-Length": 129,
        "Origin": "https://www.mywbsite.fr",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Referer": "https://www.mywbsite.fr/data/mult.aspx",
        "Accept-Encoding": "gzip,deflate,sdch",
        "Accept-Language": "fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4",
        "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "Cookie": "ASP.NET_SessionId=j1r1b2a2v2w245; GSFV=FirstVisit=; GSRef=https://www.google.fr/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0CHgQFjAA&url=https://www.mywbsite.fr/&ei=FZq_T4abNcak0QWZ0vnWCg&usg=AFQjCNHq90dwj5RiEfr1Pw; HelpRotatorCookie=HelpLayerWasSeen=0; NSC_GSPOUGS!TTM=ffffffff09f4f58455e445a4a423660; GS=Site=frfr; __utma=1.219229010.1337956889.1337956889.1337958824.2; __utmb=1.1.10.1337958824; __utmc=1; __utmz=1.1337956889.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)"
    }
    # Adding empty header as parameters are being sent in payload
    headers = {}
    r = requests.post(URL, data=json.dumps(payload), headers=headers)
    print(Fore.GREEN + "Getting [POST request] from specified URL...")
    time.sleep(2)
    print(r.content)
elif choose == "4":
    print(Fore.GREEN + "Getting [HEAD request] from specified URL...")
    time.sleep(2)
    a = (requests.head(URL))
    print(a.headers)
elif choose == "5":
    print(Fore.GREEN + "Getting [PUT request] from specified URL...")
    time.sleep(2)
    c = (requests.put(URL))
    print(c.text)

else:
   
    print(Fore.RED + '''
   
▒█▀▀▀ █▀▀█ █▀▀█ █▀▀█ █▀▀█ █ 
▒█▀▀▀ █▄▄▀ █▄▄▀ █░░█ █▄▄▀ ▀ 
▒█▄▄▄ ▀░▀▀ ▀░▀▀ ▀▀▀▀ ▀░▀▀ ▄
    ''')

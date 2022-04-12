import os
import requests
import socket
import time
import json
from bs4 import BeautifulSoup as sp

# VARS

msg1 = '        [-] List: '.upper()
WINDOWS_NEWLINE = '\r\n'
http = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
socks4 = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all"
socks5 = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all"
allofthem = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=10000&country=all&ssl=all&anonymity=all"
proxysite = "https://api.proxyscrape.com/v2/online_check.php"

httpget = requests.get(http)
socks4get = requests.get(socks4)
socks5get = requests.get(socks5)
allofthemget = requests.get(allofthem)

# GREETING


os.system('mode con: cols=200 lines=50')
os.system("color")
COLOR = {
    "cl": "\033[55m",
    "bgpurple": "\033[41m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
    "CYAN": "\033[0;34m",
    "YELLOW": "\033[33m"
}


print("                                                                                                                 ")
print("                                                                                                                 ")
print(COLOR["CYAN"],     "       ▄████████  ▄████████    ▄████████    ▄████████    ▄███████▄    ▄███████▄    ▄███████▄ ")
print(COLOR["CYAN"],     "      ███    ███ ███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ ")
print(COLOR["CYAN"],     "      ███    █▀  ███    █▀    ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ ")
print(COLOR["bgpurple"],     "      ███        ███         ▄███▄▄▄▄██▀   ███    ███   ███    ███   ███    ███   ███    ███ ")
print(COLOR["bgpurple"],   "    ▀███████████ ███        ▀▀███▀▀▀▀▀   ▀███████████ ▀█████████▀  ▀█████████▀  ▀█████████▀  ")
print(COLOR["bgpurple"],   "             ███ ███    █▄  ▀███████████   ███    ███   ███          ███          ███        ")
print(COLOR["CYAN"],   "       ▄█    ███ ███    ███   ███    ███   ███    ███   ███          ███          ███        ")
print(COLOR["CYAN"],   "     ▄████████▀  ████████▀    ███    ███   ███    █▀   ▄████▀       ▄████▀       ▄████▀      ")
print(COLOR["CYAN"],   "                              ███    ███                                                     ")

print("""     

    [Coder] : Joji
    [Version] : 2

""")


print(COLOR["YELLOW"], """
    [1] HTTPS PROXY | [5] CHECKER HTTPS       | [9]  PING LOOKUP             | [13] JOIN TELEGRAM          
    [2] SOCKS 4     | [6] OPEN PORT CHECKER   | [10] CHECK IF SITE IS DEAD   | [14] LEAVE 
    [3] SOCKS 5     | [7] WHOIS HOSTING       | [11] TEXT TO HASH               
    [4] ALL         | [8] REVERS DNS LOOKUP   | [12] SMTP CHECKER                         
    
    """)

print(COLOR["ENDC"])


# FUNCTIONS

vl = input("    Scrappp ..::[ ")

def HTTPPRX():
  print(COLOR["CYAN"], "        [-] STARTED WORKING WITH API 1")
  passwordhttp = 'http'
  print(COLOR["RED"], "        [-] [WORKING...]")
  print(COLOR["GREEN"],"        [-] SAVED IN http.txt")
  httpfile = open(f"{passwordhttp}.txt", "a")
  httpfile.write(f"{httpget.text}")
  httpfile.close()
  print(" ")
  print(COLOR["CYAN"], "        [-] STARTED WORKING WITH API 2")
  print(COLOR["RED"], "        [-] [WORKING...]")
  site = requests.get("https://proxy-daily.com/").content
  soupsite = sp(site, "html.parser")
  soupsitediv = soupsite.find_all("div", {"class": "centeredProxyList freeProxyStyle"})
  httpfile = open(f"{passwordhttp}.txt", "a")
  httpfile.write(f"{soupsitediv[0]}")
  httpfile.close()
  print(COLOR["GREEN"], "        [-] SAVED IN http.txt")
  print(" ")
  print(COLOR["GREEN"], "        [-] DONE")


def SOKS4PRX():
  print(COLOR["CYAN"], "        [-] STARTED WORKING WITH API 1")
  passwordsocks4 = 'socks4'
  print(COLOR["RED"], "        [-] [WORKING...]")
  print(COLOR["GREEN"], "        [-] SAVED IN socks4.txt")
  socks4file = open(f"{passwordsocks4}.txt", "a")
  socks4file.write(f"{socks4get.text}")
  socks4file.close()
  print(" ")
  print(COLOR["CYAN"], "        [-] STARTED WORKING WITH API 2")
  print(COLOR["RED"], "        [-] [WORKING...]")
  site = requests.get("https://proxy-daily.com/").content
  soupsite = sp(site, "html.parser")
  soupsitediv = soupsite.find_all("div", {"class": "centeredProxyList freeProxyStyle"})
  socks4file = open(f"{passwordsocks4}.txt", "a")
  socks4file.write(f"{soupsitediv[1]}")
  socks4file.close()
  print(COLOR["GREEN"], "        [-] SAVED IN socks4.txt")
  print(" ")
  print(COLOR["GREEN"], "        [-] DONE")

def SOKS5PRX():
  print(COLOR["CYAN"], "        [-] STARTED WORKING WITH API 1")
  passwordsocks5 = 'socks5'
  print(COLOR["RED"], "        [-] [WORKING...]")
  print(COLOR["GREEN"], "        [-] SAVED IN socks5.txt")
  socks5file = open(f"{passwordsocks5}.txt", "a")
  socks5file.write(f"{socks5get.text}")
  socks5file.close()
  print(" ")
  print(COLOR["CYAN"], "        [-] STARTED WORKING WITH API 2")
  print(COLOR["RED"], "        [-] [WORKING...]")
  site = requests.get("https://proxy-daily.com/").content
  soupsite = sp(site, "html.parser")
  soupsitediv = soupsite.find_all("div", {"class": "centeredProxyList freeProxyStyle"})
  socks4file = open(f"{passwordsocks5}.txt", "a")
  socks4file.write(f"{soupsitediv[2]}")
  socks4file.close()
  print(COLOR["GREEN"], "        [-] SAVED IN socks5.txt")
  print(" ")
  print(COLOR["GREEN"], "        [-] DONE")

def ALLPRX():
  print(COLOR["CYAN"], "        [-] STARTED WORKING WITH API 1")
  passwordall = 'all'
  print(COLOR["RED"], "        [-] [WORKING...]")
  print(COLOR["GREEN"],"        [-] SAVED IN all.txt")
  allofthemfile = open(f"{passwordall}.txt", "a")
  allofthemfile.write(f"{allofthemget.text}")
  allofthemfile.close()
  print(" ")
  print(COLOR["CYAN"], "        [-] STARTED WORKING WITH API 2")
  print(COLOR["RED"], "        [-] [WORKING...]")
  site = requests.get("https://www.us-proxy.org/").content
  soupsite = sp(site, "html.parser")
  souptextarea = soupsite.find('textarea')
  allofthemfile = open(f"{passwordall}.txt", "a")
  allofthemfile.write(f"{souptextarea.text}")
  allofthemfile.close()
  print(COLOR["GREEN"], "        [-] SAVED IN all.txt")
  print(" ")
  print(COLOR["CYAN"], "        [-] STARTED WORKING WITH API 3")
  print(COLOR["RED"], "        [-] [WORKING...]")
  site = requests.get("https://proxy-daily.com/").content
  soupsite = sp(site, "html.parser")
  soupsitediv = soupsite.find_all("div", {"class": "centeredProxyList freeProxyStyle"})
  allofthemfile = open(f"{passwordall}.txt", "a")
  allofthemfile.write(f"{soupsitediv}")
  allofthemfile.close()

  print(COLOR["GREEN"], "        [-] SAVED IN all.txt")
  print(" ")
  print(COLOR["GREEN"], "        [-] DONE")


def CHKHTTP():
  count = 0
  filename = input(msg1)
  if filename == f"{filename}":
    with open(f'{filename}') as text:
      while True:
        for line in text:
          if line == ' ':
            print(COLOR["RED"], "[-] SOMETHING IS WRONG, CHECK YOUR LIST AND TRY AGAIN")
            input('')
          else:
            proxyip = line.split(":")[0]
            try:
              proxyport = line.split(":")[1].removeprefix('b')
            except IndexError:
              pass

          proxyserver = f'{proxyip}:{proxyport}'.replace('\n', '')

          r = requests.get(f'https://proxylist.geonode.com/api/check-proxy?ip={proxyip}&port={proxyport}&publish_proxy=no&filter_protocol=http%2Chttps').json()

          isworking = r["data"]["is_google"]
          #statusforproxychecking = r["data"]["ip_info"]["status"]
          #countryproxy = r["data"]["ip_info"]["country"]
          #protocols = r["data"]["protocols"]

          if isworking == True:
            print(COLOR["GREEN"], f"       [+] WORKING : {proxyserver}")
            workinghttpsproxy = open("workinghttpsproxy.txt", "a")
            workinghttpsproxy.write(f"{proxyserver}\n")
            workinghttpsproxy.close()
          else:
            print(COLOR["RED"], f"       [-] NOT WORKING : {proxyserver}")

          count = count + 1

          if count == 8:
            count = 0
            time.sleep(3)
          else:
            pass


def OPC():
  ipnum = input("        [-] IP ADRESS TO CHECK : ")
  ipport = input("        [-] PORT NUMBER: ")

  site = f"https://ipasn.com/open-port-check/?host={ipnum}&port={ipport}"

  prtchkrzlt = requests.get(site).text

  # color:#F00000

  if "color:#F00000" in prtchkrzlt:
    print(COLOR["RED"],f"       [-] DEAD : {ipnum}")
  else:
    pass

  if "We can see service on port" in prtchkrzlt:
    print(COLOR["GREEN"], f"       [+] LIVE : {ipnum}:{ipport}")

  print(COLOR["CYAN"], "        [!] DONE")

def WHOISHOSTING():
    sitetochk = input("        [-] WEBSITE URL: ")
    payload = {
        'url': f'{sitetochk}'
    }
    whoishostingchk = requests.get(f'https://hooshosting.com/api/hosting?url={sitetochk}', params=payload)
    whoishostingchktxt = whoishostingchk.text
    if '"result":null' in whoishostingchktxt:
      print(COLOR["RED"], "       [x] ERROR, RE CHECK YOUR INFORMATION")
    else:
      whoishostingchk = whoishostingchk.json()
      whoishostingchklist = []
      for item in whoishostingchk["results"]:
        whoishostingchklist.append(item["ip"])
        whoishostingchklist.append(item["isp_name"])
      print(COLOR["GREEN"], "       [+] IP : "+ whoishostingchklist[0])
      print(COLOR["GREEN"], "       [+] HOSTING PROVIDER : "+ whoishostingchklist[1])

    print(COLOR["CYAN"], "        [!] DONE")

def REVERSDNS():
  api = input("        [-] PLEASE CHOOSE API ( 1 OR 2... READ GITHUB REPO TO KNOW MORE ): ")
  if api == "1":
    fromtext = input("        [+] DO YOU WANT TO GET WEBSITES FROM TEXT FILE ( Y / N) : ")
    if fromtext == "Y":
      filename = input("        [+] ENTER FILE NAME : ")
      print(" ")
      print(COLOR["RED"], "        [-] WORKING...")
      with open(f'{filename}') as text:
        for line in text:
          if line == ' ':
            print(COLOR["RED"], "        [-] SOMETHING IS WRONG, CHECK YOUR LIST AND TRY AGAIN")
            input('')
          else:
            try:
              domain_name = socket.gethostbyaddr(line)[0]
              print(COLOR["GREEN"], f"        [+] FOUND FOR {line} : {domain_name}")
              with open('reversdns.txt', 'a') as file:
                file.writelines(domain_name)
                file.write('\n')
                file.close()
              print(COLOR["GREEN"], f"        [+] SAVED IN reversdns.txt")
            except(socket.gaierror):
              pass
    elif fromtext == "N":
      iptochk = input("        [+] IP ADDRESS: ")
      try:
        domain_name = socket.gethostbyaddr(iptochk)[0]
        print(COLOR["GREEN"], f"        [+] FOUND : {domain_name}")
      except(socket.gaierror):
        pass
  elif api == "2":
    with open(f'{filename}') as text:
      for line in text:
        getdomains = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={line}").text
        print(COLOR["GREEN"], "        [+] DONE I FOUND A LIST")
        time.sleep(3)
        print(COLOR["GREEN"], getdomains)
        with open('reversdns.txt', 'a') as file:
          file.writelines(getdomains)
          file.close()

  
  
    print(COLOR["CYAN"], "        [!] DONE")
  else:
    print(" ")
    print(COLOR["RED"], "        [-] WORKING...")
    try:
      addressip = input("        [+] PLEASE ENTER A VALID IP ADDRESS : ")
      domain_name = socket.gethostbyaddr(addressip)[0]
      print(COLOR["GREEN"], f"        [+] FOUND FOR {line} : {domain_name}")
      print(COLOR["GREEN"], f"        [+] SAVED IN reversdns.txt")
    except(socket.gaierror):
      pass
    print(COLOR["CYAN"], "        [!] DONE")

def TEXTTOMD5():
  wordtomd5 = input("        [+] PLEASE ENTER THE TEXT YOU WANT TO HASH : ")
  hashtype = input("        [+] HASH METHODS ( MD5 , SHA1 , SHA256  ) : ")
  if hashtype == "MD5":
    sitetomd5 = requests.get(f"https://api.hashify.net/hash/md5/hex?value={wordtomd5}")
    sitetomd5content = sitetomd5.json()
    print(COLOR["GREEN"], "       [+] MD5 : "+ sitetomd5content["Digest"])
  elif hashtype == "SHA1":
    sitetomd5 = requests.get(f"https://api.hashify.net/hash/sha1/hex?value={wordtomd5}")
    sitetomd5content = sitetomd5.json()
    print(COLOR["GREEN"], "       [+] SHA1 : "+ sitetomd5content["Digest"])
  elif hashtype == "SHA256":
    sitetomd5 = requests.get(f"https://api.hashify.net/hash/sha256/hex?value={wordtomd5}")
    sitetomd5content = sitetomd5.json()
    print(COLOR["GREEN"], "       [+] SHA256 : "+ sitetomd5content["Digest"])
  else:
    print(COLOR["RED"], "       [x] ENTER VALID HASH TYPE :(")
  
  print(COLOR["CYAN"], "        [!] DONE")

def ISSITEDOWN():
  site = input("       [+] PLEASE ENTER A WEBSITE DOMAIN : ")
  issitedown = requests.get(f"https://www.isitdownrightnow.com/check.php?domain={site}").text
  if "UP" in issitedown:
    soupsite = sp(issitedown, "html.parser")
    soupsitedivsitedomainname = soupsite.find('div', {"class": "tabletrsimple"})
    domainname = soupsitedivsitedomainname.find("span", {"class": "tab"}).text
    print(COLOR["GREEN"], f"       [+] WEBSITE CHECKED : {domainname}")
    print(COLOR["GREEN"], f"       [+] IS IT DOWN : WEBSITE IS UP FOR EVERYONE")
  else:
    print(COLOR["RED"], "       [-] WEBSITE IS DOWN FOR EVERYONE !")
  
  print(COLOR["CYAN"], "        [!] DONE")

def SMTPCHK():
  isfromlist = input("        [!] DO YOU WANT TO CHECK SMTP FROM LIST ? ( Y / N ): ")
  if isfromlist == "N":
    smtp = input("")
    smtplogin = input("")
    smtploginpswd = input("")

    payload = {
      "hostname": smtp,
      "from_email": smtplogin,
      "user": smtplogin,
      "password": smtploginpswd,
      "chk:is_try_tls": "N"
    }


    chk = requests.post("https://pingability.com/smtptest.jsp", params=payload).text
    if "message successfully delivered" in chk:
      print(COLOR["GREEN"], f"       [+] SMTP IS WORKING : {smtp}")
    else:
      print(COLOR["RED"], "       [-] SMTP IS NOT WORKING, SOMETHING WENT WRONG...")

  elif isfromlist == "Y":
    print(COLOR["YELLOW"], "       [-] SOON... ")


def JOINTELEGRAM():
  print(COLOR["YELLOW"],"        [!] MY TELEGRAM CHANNEL : https://t.me/jojipydev")

def LEAVE():
  exit()
# SERVICES



if vl == '1':
    HTTPPRX()
if vl == '2':
    SOKS4PRX()
if vl == '3':
    SOKS5PRX()
if vl == '4':
    ALLPRX()
if vl == '5':
    CHKHTTP()
if vl == '6':
    OPC()
if vl == '7':
    WHOISHOSTING()
if vl == '8':
    REVERSDNS()
if vl == '10':
  ISSITEDOWN()
if vl == '11':
    TEXTTOMD5()
if vl == '12':
  SMTPCHK()
if vl == '13':
  JOINTELEGRAM()
if vl == '14':
  LEAVE()






input(" ")
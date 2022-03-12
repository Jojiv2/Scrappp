import os
import requests
import random
import string
import json
import time


os.system('mode con: cols=200 lines=50')
os.system("color")
COLOR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
    "CYAN": "\033[0;36m"
}

msg1 = '        [-] If the proxys is http change the name of the file to http ( same for socks4, socks5 or all ): '.upper()



print('''

   ▄████████  ▄████████    ▄████████    ▄████████    ▄███████▄    ▄███████▄    ▄███████▄ 
  ███    ███ ███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ 
  ███    █▀  ███    █▀    ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ 
  ███        ███         ▄███▄▄▄▄██▀   ███    ███   ███    ███   ███    ███   ███    ███ 
▀███████████ ███        ▀▀███▀▀▀▀▀   ▀███████████ ▀█████████▀  ▀█████████▀  ▀█████████▀  
         ███ ███    █▄  ▀███████████   ███    ███   ███          ███          ███        
   ▄█    ███ ███    ███   ███    ███   ███    ███   ███          ███          ███        
 ▄████████▀  ████████▀    ███    ███   ███    █▀   ▄████▀       ▄████▀       ▄████▀      
                          ███    ███                                                     

        [+] Author : Joji - DZ -
        [+] Version : 1.2.0
        [+] Telegram : @Jojigodamn


        [-] Please choose any option by number  

        [+] HTTP/S ( 1 )    [+] SOCKS 4 ( 2 ) 

        [+] SOCKS 5 ( 3 )   [+] ALL ( 4 )       

        [+] KEEP SCRAPING HTTP/S ( 5 )  [+] KEEP SCRAPING SOCKS 4 ( 6 ) 

        [+] KEEP SCRAPING SOCK 5 ( 7 )  [+] KEEP SCRAPING ALL OF PROXIES ( 8 )   

        [--------------------------]

        [+] CHECKER ( 9 )   [+] OPEN PORT CHECKER ( 10 )                                                                            
                                                                                                                 
''')

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


option = input('         >>>>>>  ')

if option == "1":
  passwordhttp = 'http'
  print(COLOR["RED"], "        [-] [WORKING...]")
  print(COLOR["GREEN"], httpget.text)
  httpfile = open(f"{passwordhttp}.txt", "a")
  httpfile.write(f"{httpget.text}")
  httpfile.close()

#else:
if option == "2":
  passwordsocks4 = 'socks4'
  print(COLOR["RED"], "        [-] [WORKING...]")
  print(COLOR["GREEN"], socks4get.text)
  socks4file = open(f"{passwordsocks4}.txt", "a")
  socks4file.write(f"{socks4get.text}")
  socks4file.close()
  #else:
if option == "3":
  passwordsocks5 = 'socks5'
  print(COLOR["RED"], "        [-] [WORKING...]")
  print(COLOR["GREEN"], socks5get.text)
  socks5file = open(f"{passwordsocks5}.txt", "a")
  socks5file.write(f"{socks5get.text}")
  socks5file.close()
   # else:
if option == "4":
  passwordall = 'all'
  print(COLOR["RED"], "        [-] [WORKING...]")
  print(COLOR["GREEN"], allofthemget.text)
  allofthemfile = open(f"{passwordall}.txt", "a")
  allofthemfile.write(f"{allofthemget.text}")
  allofthemfile.close()

# Keep scraping


if option == "5":
  passwordhttpscraping = 'https-scraping'
  print(COLOR["RED"], "       [-] [WORKING... | SCRAPING EVERY 5 MIN]")
  print(COLOR["HEADER"], "       [-] [SOMETIMES THE API TAKE TOO LONG TO UPDATE API'S SOOO... USE THE DUPLCATE REMOVING TOOL]")
  while True:
    print(COLOR["GREEN"], f"       [0] [SAVED IN {passwordhttpscraping}.... COOLDOWN 5 MIN? IM STILL WORKING]")
    httpfile = open(f"{passwordhttpscraping}.txt", "a")
    httpfile.write(f"{httpget.text}")
    httpfile.close()
    time.sleep(360)

if option == "6":
  passwordsocks4scraping = 'socks4-scraping'
  print(COLOR["RED"], "       [-] [WORKING... | SCRAPING EVERY 5 MIN]")
  print(COLOR["HEADER"], "       [-] [SOMETIMES THE API TAKE TOO LONG TO UPDATE API'S SOOO... USE THE DUPLCATE REMOVING TOOL]")
  while True:
    print(COLOR["GREEN"], f"       [0] [SAVED IN {passwordsocks4scraping}.... COOLDOWN 5 MIN? IM STILL WORKING]")
    socks4file = open(f"{passwordsocks4scraping}.txt", "a")
    socks4file.write(f"{socks4get.text}")
    socks4file.close()
    time.sleep(360)

if option == "7":
  passwordsocks5scraping = 'https-scraping'
  print(COLOR["RED"], "       [-] [WORKING... | SCRAPING EVERY 5 MIN]")
  print(COLOR["HEADER"], "       [-] [SOMETIMES THE API TAKE TOO LONG TO UPDATE API'S SOOO... USE THE DUPLCATE REMOVING TOOL]")
  while True:
    print(COLOR["GREEN"], f"       [0] [SAVED IN {passwordsocks5scraping}.... COOLDOWN 5 MIN? IM STILL WORKING]")
    httpfile = open(f"{passwordsocks5scraping}.txt", "a")
    httpfile.write(f"{httpget.text}")
    httpfile.close()
    time.sleep(360)

if option == "8":
  passwordallscraping = 'all-scraping'
  print(COLOR["RED"], "       [-] [WORKING... | SCRAPING EVERY 5 MIN]")
  print(COLOR["HEADER"], "       [-] [SOMETIMES THE API TAKE TOO LONG TO UPDATE API'S SOOO... USE THE DUPLCATE REMOVING TOOL]")
  while True:
    print(COLOR["GREEN"], f"       [0] [SAVED IN {passwordallscraping}.... COOLDOWN 5 MIN? IM STILL WORKING]")
    httpfile = open(f"{passwordallscraping}.txt", "a")
    httpfile.write(f"{httpget.text}")
    httpfile.close()
    time.sleep(360)

if option == "9":
  count = 0
  filename = input(msg1)
  if filename == "http":
    with open(f'{filename}.txt') as text:
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
          else:
            print(COLOR["RED"], f"       [-] NOT WORKING : {proxyserver}")

          count = count + 1

          if count == 8:
            count = 0
            time.sleep(3)
          else:
            pass

  if filename == "socks4":
    print(COLOR["RED"], "       [-] SOON :(")
    input("")

if option == "10":
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
  


  #print(prtchkrzlt)

  input(" ")


print(COLOR["RED"], f"[DONE], Saved in a text file")
input("")

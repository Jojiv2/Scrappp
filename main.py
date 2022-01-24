import imp
from itertools import count
import os
import site
from turtle import position
from weakref import proxy
import requests
import random
import string
import time
import urllib

os.system('mode con: cols=200 lines=50')
os.system("color")
COLOR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
}



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

        [+] CHECKER ( 9 )                                                                            
                                                                                                                 
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


option = input('>>>>>>  ')

if option == "1":
  passwordhttp = 'http'
  print(COLOR["RED"], "[WORKING...]")
  print(COLOR["GREEN"], httpget.text)
  httpfile = open(f"{passwordhttp}.txt", "a")
  httpfile.write(f"{httpget.text}")
  httpfile.close()

#else:
if option == "2":
  passwordsocks4 = 'socks4'
  print(COLOR["RED"], "[WORKING...]")
  print(COLOR["GREEN"], socks4get.text)
  socks4file = open(f"{passwordsocks4}.txt", "a")
  socks4file.write(f"{socks4get.text}")
  socks4file.close()
  #else:
if option == "3":
  passwordsocks5 = 'socks5'
  print(COLOR["RED"], "[WORKING...]")
  print(COLOR["GREEN"], socks5get.text)
  socks5file = open(f"{passwordsocks5}.txt", "a")
  socks5file.write(f"{socks5get.text}")
  socks5file.close()
   # else:
if option == "4":
  passwordall = 'all'
  print(COLOR["RED"], "[WORKING...]")
  print(COLOR["GREEN"], allofthemget.text)
  allofthemfile = open(f"{passwordall}.txt", "a")
  allofthemfile.write(f"{allofthemget.text}")
  allofthemfile.close()

# Keep scraping


if option == "5":
  passwordhttpscraping = 'https-scraping'
  print(COLOR["RED"], "[WORKING... | SCRAPING EVERY 5 MIN]")
  print(COLOR["HEADER"], "[SOMETIMES THE API TAKE TOO LONG TO UPDATE API'S SOOO... USE THE DUPLCATE REMOVING TOOL]")
  while True:
    print(COLOR["GREEN"], f"[SAVED IN {passwordhttpscraping}]")
    httpfile = open(f"{passwordhttpscraping}.txt", "a")
    httpfile.write(f"{httpget.text}")
    httpfile.close()
    time.sleep(360)

if option == "6":
  passwordsocks4scraping = 'socks4-scraping'
  print(COLOR["RED"], "[WORKING... | SCRAPING EVERY 5 MIN]")
  print(COLOR["HEADER"], "[SOMETIMES THE API TAKE TOO LONG TO UPDATE API'S SOOO... USE THE DUPLCATE REMOVING TOOL]")
  while True:
    print(COLOR["GREEN"], f"[SAVED IN {passwordsocks4scraping}]")
    socks4file = open(f"{passwordsocks4scraping}.txt", "a")
    socks4file.write(f"{socks4get.text}")
    socks4file.close()
    time.sleep(360)

if option == "7":
  passwordsocks5scraping = 'https-scraping'
  print(COLOR["RED"], "[WORKING... | SCRAPING EVERY 5 MIN]")
  print(COLOR["HEADER"], "[SOMETIMES THE API TAKE TOO LONG TO UPDATE API'S SOOO... USE THE DUPLCATE REMOVING TOOL]")
  while True:
    print(COLOR["GREEN"], f"[SAVED IN {passwordsocks5scraping}]")
    httpfile = open(f"{passwordsocks5scraping}.txt", "a")
    httpfile.write(f"{httpget.text}")
    httpfile.close()
    time.sleep(360)

if option == "8":
  passwordallscraping = 'all-scraping'
  print(COLOR["RED"], "[WORKING... | SCRAPING EVERY 5 MIN]")
  print(COLOR["HEADER"], "[SOMETIMES THE API TAKE TOO LONG TO UPDATE API'S SOOO... USE THE DUPLCATE REMOVING TOOL]")
  while True:
    print(COLOR["GREEN"], f"[SAVED IN {passwordallscraping}]")
    httpfile = open(f"{passwordallscraping}.txt", "a")
    httpfile.write(f"{httpget.text}")
    httpfile.close()
    time.sleep(360)

if option == "9":
  print(COLOR["RED"], "[SOON...]")
  input("")




print(COLOR["RED"], f"[DONE], Saved in a text file")
input("")

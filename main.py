import os
import requests
import random
import string

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
        [+] Version : 1
        [+] Telegram : @Jojigodamn


        [-] Please choose any option by number  

        [+] HTTP/S ( 1 )    [+] SOCKS 4 ( 2 ) 

        [+] SOCKS 5 ( 3 )   [+] ALL ( 4 )                                                                                              
                                                                                                                 
''')

WINDOWS_NEWLINE = '\r\n'
http = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
socks4 = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all"
socks5 = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all"
allofthem = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=10000&country=all&ssl=all&anonymity=all"

httpget = requests.get(http)
socks4get = requests.get(socks4)
socks5get = requests.get(socks5)
allofthemget = requests.get(allofthem)

password = ''.join(random.choice(string.printable) for i in range(8))

option = input('>>>>>>  ')

if option == "1":
  passwordhttp = ''.join(random.choice(string.printable) for i in range(8))
  print(COLOR["RED"], "[WORKING...]")
  print(COLOR["GREEN"], httpget.text)
  httpfile = open(f"{passwordhttp}http.txt", "a")
  httpfile.write(f"{httpget.text}")
  httpfile.close()

#else:
if option == "2":
  passwordsocks4 = ''.join(random.choice(string.printable) for i in range(8))
  print(COLOR["RED"], "[WORKING...]")
  print(COLOR["GREEN"], socks4get.text)
  socks4file = open(f"{passwordsocks4}socks4.txt", "a")
  socks4file.write(f"{socks4get.text}")
  socks4file.close()
  #else:
if option == "3":
  passwordsocks5 = ''.join(random.choice(string.printable) for i in range(8))
  print(COLOR["RED"], "[WORKING...]")
  print(COLOR["GREEN"], socks5get.text)
  socks5file = open(f"{passwordsocks5}socks5.txt", "a")
  socks5file.write(f"{socks5get.text}")
  socks5file.close()
   # else:
if option == "4":
  passwordall = ''.join(random.choice(string.printable) for i in range(8))
  print(COLOR["RED"], "[WORKING...]")
  print(COLOR["GREEN"], allofthemget.text)
  allofthemfile = open(f"{passwordall}all.txt", "a")
  allofthemfile.write(f"{allofthemget.text}")
  allofthemfile.close()

print(COLOR["RED"], f"[DONE], Saved in a text file ( random pass + type of proxy )")
input("")

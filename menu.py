import requests,os,sys, time
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
from bs4 import BeautifulSoup
import json
import requests
import time
from time import strftime
import os
import requests
import urllib.parse
from time import strftime
import os
from datetime import datetime
from time import sleep, strftime
import datetime
#Color
trang = "\033[1;37m"
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
xanhnhat = "\033[1;36m"
#Đánh Dấu Bản Quyền
HĐ_tool = trang + " " + trang + "[" + do + "+_+" + trang + "] " + trang + "=> "
mquang = trang + " " + trang + "[" + do + "÷_+" + trang + "] " + trang + "=> "
thanh = trang + "-------------------------------------------------------------------------"

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Gọi hàm để xóa màn hình
clear_screen()

# Lmao
thanh_xau=trang+'~'+do+'['+vang+'⟨⟩'+do+'] '+trang+'➩  '+xanhnhat
thanh_dep=trang+'~'+do+'['+xanh_la+'✓'+do+'] '+trang+'➩  '+xanhnhat
def get_ip_from_url(url):
     response = requests.get(url)
     ip_address = socket.gethostbyname(response.text.strip())
     return ip_address
     return "127.0.0.1"
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url
import os
import requests
from time import strftime
now = datetime.datetime.now()
thu = now.strftime('%A')
ngay_hom_nay = now.strftime('%d')
thang_nay = now.strftime('%m')
nam_ = now.strftime('%Y')
now = datetime.datetime.now()
gio_hien_tai = now.strftime('%H:%M:%S')
System.Clear()
System.Title("Vũ Tài (Minato)")
System.Size(300, 200)
banner = r"""



 __ __  _             _        __  _   ___                                 
|  \  \<_>._ _  ___ _| |_ ___  \ \/   | . \ ___  _ _  ___ ._ _ _  ___ ._ _ 
|     || || ' |<_> | | | / . \  \ \   | | |/ . \| '_>/ ._>| ' ' |/ . \| ' |
|_|_|_||_||_|_|<___| |_| \___/ _/\_\  |___/\___/|_|  \___.|_|_|_|\___/|_|_|
                                            
                                                                                 
                            ENTER ĐỂ VÀO TOOL                                
"""
Anime.Fade(Center.Center(banner), Colors.blue_to_green, Colorate.Vertical, enter=True)
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def save_key_to_file(key, filename='REVIEWTOOL247NDK-key.txt'):
    with open(filename, 'w') as file:
        file.write(str(key))


def load_key_from_file(filename='REVIEWTOOL247NDK-key.txt'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read().strip()
    return None


def fetch_shortened_url(url, token):
    try:
        encoded_url = urllib.parse.quote(url)
        api_url = f'https://yeumoney.com/QL_api.php?token={token}&url={encoded_url}&format=json'
        try:
            response = requests.get(api_url)
        except:
            print('Vui Lòng Kết Nối Mạng !')
            exit("")
        response.raise_for_status()
        result = response.json()
        if result["status"] == "success":
            return result["shortenedUrl"]
        else:
            return result["status"]
    except requests.exceptions.RequestException as e:
        return f"Error fetching shortened URL: {e}"


def main():
    clear_screen()

if __name__ == "__main__":
    main()
banner = ''' 
  \x1b[38;5;207m╔══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╗
  \033[1;31m __ __  _             _        __  _   ___                                 
  \033[1;34m|  \  \<_>._ _  ___ _| |_ ___  \ \/   | . \ ___  _ _  ___ ._ _ _  ___ ._ _ 
  \033[1;33m|     || || ' |<_> | | | / . \  \ \   | | |/ . \| '_>/ ._>| ' ' |/ . \| ' |
  \033[1;32m|_|_|_||_||_|_|<___| |_| \___/ _/\_\  |___/\___/|_|  \___.|_|_|_|\___/|_|_|
        \x1b[38;5;207mFB Admin: \x1b[38;5;46mhttps://www.facebook.com/Staw01/
        \x1b[38;5;207m ADMIN : \x1b[38;5;46m Vũ Tài (Minato)
   \x1b[38;5;207m╚══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;226m══\x1b[38;5;99m══\x1b[38;5;46m══\x1b[38;5;51m══\x1b[38;5;208m══\x1b[38;5;51m══\x1b[38;5;46m══\x1b[38;5;99m══\x1b[38;5;207m══\x1b[38;5;51m══\x1b[38;5;46m═╝
'''

for i in banner:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.00130)
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
#thanh_xau= print(f"{red}┌─────┬────────────────────────────────────┬─────────┬─────────┐")
#thanh_dep= print(f"{red}│{vang}      {red}│    {vang}      {red}        │ {vang}STATUS {red} │{vang} VERSION {red}│")
#thanh_cuoi=print(f"{red}├─────┼────────────────────────────────────┼─────────┼─────────┤")


Write.Print('╔═════════════════════| \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('║TOOL FACEBOOK  \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚═════════════════════| \n',Colors.yellow,interval=0.0001,end='\r')
print(f'{hong}🔥➩ {lam}Nhập Số [1] TOOL SHARE ẢO FB [ỔN]\n')
print(f'{hong}🔥➩ {lam}Nhập Số [2] TOOL BUFF LIKE [NGON]\n')
print(f'{hong}🔥➩ {lam}Nhập Số [3] TOOL LIKE BÀI VIẾT DẠO [NGON]\n')
Write.Print('╔═════════════════════| \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('║ TOOL  SPAM SMS   \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚═════════════════════| \n',Colors.yellow,interval=0.0001,end='\r')
print(f'{hong}🔥➩ \033[1;35mNhập Số [4] TOOL SPAM SMS V1[NGON]\n')
Write.Print('╔═════════════════════| \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('║ TOOL  TĐS    \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚═════════════════════| \n',Colors.yellow,interval=0.0001,end='\r')
print(f'{hong}🔥➩ \033[1;31mNhập Số [5] TOOL TIKTOK V1[NGON]\n')
Write.Print('╔═════════════════════| \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('║ TOOL  SPAM MESSENGER    \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚═════════════════════| \n',Colors.yellow,interval=0.0001,end='\r')
print(f'{hong}🔥➩ \033[1;32mNhập Số [6] TOOL NHÂY CÓ DẤU [NGON]\n')
print(f'{hong}🔥➩ \033[1;32mNhập Số [7] TOOL NHÂY KHÔNG DẤU [NGON]\n')
print(f'{hong}🔥➩ \033[1;32mNhập Số [8] TOOL NHÂY RÉO TÊN TRONG BOX [NGON]\n')
print(f'{hong}🔥➩ \033[1;32mNhập Số [9] TOOL NHÂY CODE LAG [NGON]\n')
print(f'{hong}🔥➩ \033[1;32mNhập Số [10] TOOL TREO SỚ [NGON]\n')
Write.Print('╔═════════════════════| \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('║ TOOL  SPAM DISCORD     \n',Colors.yellow,interval=0.0001,end='\r')
Write.Print('╚═════════════════════| \n',Colors.yellow,interval=0.0001,end='\r')
print(f'{hong}🔥➩ \033[1;36mNhập Số [11] TOOL NHÂY DISCORD [NGON]\n')
import requests


chon = str(input('\033[1;31m\033[1;3🔥\033[1;31m\033[1;33m➩ \033[1;34mNhập Số \033[1;37m: \033[1;33m'))

if chon == '1':
    exec(requests.get('https://run.mocky.io/v3/72f1d0a1-79fe-464c-977d-f32786f85bbb').text)
elif chon == '2':
    exec(requests.get('https://run.mocky.io/v3/b5a97776-a50a-4a2f-9bf5-9386840e0488').text)
elif chon == '3':
    exec(requests.get('https://run.mocky.io/v3/e1dc2d21-e7ca-4b02-be39-95ece9178078').text)
elif chon == '4':
    exec(requests.get('https://run.mocky.io/v3/e177d053-f347-4814-9ca6-e0c157ecdd5f').text)
elif chon == '5':
	exec(requests.get('https://run.mocky.io/v3/8131c898-ec27-4858-b082-b935ee1c0e52').text)
elif chon == '6':
	exec(requests.get('https://run.mocky.io/v3/e75227fe-7ab6-4b34-b9c8-a5cc145aa5dd').text)
elif chon == '7':
	exec(requests.get('https://run.mocky.io/v3/c6c8c3e5-3c0d-4d75-aefd-710e90b7bd9e').text)
elif chon == '8':
	exec(requests.get('https://run.mocky.io/v3/d1cbd1df-b9f6-41f3-b898-02097b35fbf0').text)
elif chon == '9':
	exec(requests.get('https://run.mocky.io/v3/e4a8494b-aaef-4d51-ac35-2cd3dcca02df').text)
elif chon == '10':
	exec(requests.get('https://run.mocky.io/v3/9077dc9f-18c1-4987-b131-a2518fd65b25').text)
elif chon == '11':
	exec(requests.get('https://run.mocky.io/v3/0bc64f61-c241-4305-9657-889639e8cb06').text)
elif chon == '12':
	exec(requests.get('https://run.mocky.io/v3/03fe1b39-0b31-4259-90e0-ea1e437c0617').text)
elif chon == '13':
	exec(requests.get('https://run.mocky.io/v3/988e7083-5ebb-461b-a54e-26bce533fbc4').text)
elif chon == '14':
	exec(requests.get('accc').text)
else:
    print("Sai Lựa Chọn")
    exit()
    

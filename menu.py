# AUTO CÀI THƯ VIỆN
import os
try:
    import pystyle, requests
except:
    os.system("pip install pystyle requests")

# IMPORT
import os, sys, time, platform, socket, getpass
from datetime import datetime
from pystyle import Colors, Colorate, Write, Center, System
import requests

# THÔNG TIN TOOL
VERSION = "v3.0"
ADMIN = "Vũ Tài (Minato)"
GITHUB = "https://raw.githubusercontent.com/deeth781/code/refs/heads/main/"

# DANH SÁCH TOOL
tools = {
    "1": ("TOOL SHARE ẢO FB", "share.py"),
    "2": ("TOOL SPAM SMS", "spam.py"),
    "3": ("TOOL TIKTOK", None),
    "4": ("TOOL NHÂY CÓ DẤU", None),
    "5": ("TOOL NHÂY KHÔNG DẤU", None),
    "6": ("TOOL NHÂY RÉO TÊN", None),
    "7": ("TOOL CODE LAG", None),
    "8": ("TOOL TREO SỚ", None),
    "9": ("TOOL DISCORD NHÂY", "4.py"),
    "0": ("THOÁT MENU", None)
}

# THIẾT BỊ, IP
def get_ip():
    try:
        return requests.get("https://api.ipify.org").text
    except:
        return "Không rõ"

def get_device():
    return f"{platform.system()} {platform.machine()} | {socket.gethostname()} | {getpass.getuser()}"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# HIỆU ỨNG
def slow_type(text, color=Colors.cyan_to_blue, speed=0.01):
    for char in text:
        sys.stdout.write(Colorate.Horizontal(color, char))
        sys.stdout.flush()
        time.sleep(speed)
    print()

def loading_bar(duration=2, length=30):
    sys.stdout.write(Colors.yellow + "[" + " " * length + "]")
    sys.stdout.flush()
    sys.stdout.write("\b" * (length + 1))
    for i in range(length):
        sys.stdout.write(Colors.green + "█")
        sys.stdout.flush()
        time.sleep(duration / length)
    print(Colors.reset)

def intro():
    clear()
    System.Title("MINATO TOOL MENU")
    slow_type("\n🌀 Đang khởi động Minato X Doraemon Tool...", Colors.purple_to_blue, 0.02)
    loading_bar()
    time.sleep(0.3)
    slow_type("📡 Kết nối máy chủ thành công...", Colors.blue_to_green, 0.02)
    time.sleep(0.4)
    slow_type("✅ Hệ thống sẵn sàng!", Colors.green_to_blue, 0.02)
    time.sleep(1)
    clear()

# MENU
def show_menu():
    ip = get_ip()
    device = get_device()
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    banner = r'''
 __  __ _                  _           __  _   ___               
|  \/  (_) ___ _ __  _   _| |_ ___    \ \/ | | __ \___ _ __ ___  
| |\/| | |/ __| '_ \| | | | __/ _ \    \  /  | |__) / _ \ '__/ _ \ 
| |  | | | (__| | | | |_| | || (_) |   /  \  |  _ <  __/ | | (_) |
|_|  |_|_|\___|_| |_|\__,_|\__\___/   /_/\_\ |_| \_\___|_|  \___/ 
               ✘ MINATO X DORAEMON ✘
    '''
    Write.Print(Center.Center(banner), Colors.cyan_to_blue, 0.002)

    print("\n" + Colorate.Horizontal(Colors.blue_to_green, "🌐 MENU CHÍNH TOOL VIP") + "\n")
    print("╔════╦════════════════════════════════════════════╦══════════════╗")
    print("║ ST ║ TÊN TOOL                                    ║ TRẠNG THÁI   ║")
    print("╠════╬════════════════════════════════════════════╬══════════════╣")
    for key, (name, file) in tools.items():
        status = "ONLINE" if file else ("THOÁT" if name == "THOÁT MENU" else "ĐANG UPDATE")
        color = Colors.green_to_white if file else (Colors.red_to_white if name == "THOÁT MENU" else Colors.red_to_yellow)
        print(f"║ {key.center(2)} ║ {name.ljust(44)} ║ ", end="")
        Write.Print(status.center(12), color)
        print(" ║")
    print("╚════╩════════════════════════════════════════════╩══════════════╝")

    print(f"\n🧠 ADMIN     : {ADMIN}")
    print(f"🌐 IP        : {ip}")
    print(f"💻 THIẾT BỊ  : {device}")
    print(f"🕐 THỜI GIAN : {now}")
    print(f"🧱 PHIÊN BẢN : {VERSION}\n")

# CHẠY TOOL
def run_tool(filename):
    try:
        url = GITHUB + filename
        code = requests.get(url).text
        exec(code)
    except Exception as e:
        Write.Print(f"❌ Lỗi tải tool: {e}\n", Colors.red_to_white)

# MAIN
def main():
    while True:
        intro()
        show_menu()
        chon = input(Colorate.Horizontal(Colors.purple_to_blue, "🔰 Nhập số để chọn tool ➤ ")).strip()
        if chon == "0":
            Write.Print("👋 Tạm biệt, hẹn gặp lại!\n", Colors.cyan_to_white)
            break
        elif chon in tools:
            name, file = tools[chon]
            if file:
                Write.Print(f"🚀 Đang chạy {name}...\n", Colors.green_to_blue)
                run_tool(file)
            else:
                Write.Print(f"⏳ {name} hiện đang cập nhật...\n", Colors.yellow_to_red)
            input("👉 Bấm Enter để quay lại menu...")
        else:
            Write.Print("❌ Không hợp lệ! Nhập lại...\n", Colors.red_to_white)
            time.sleep(1)

if __name__ == "__main__":
    main()

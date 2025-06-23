import os
import sys
import time
import json

# 🔄 Auto install missing modules
try:
    import requests
    from pystyle import Write, Colors, Colorate
except ImportError:
    os.system("pip install pystyle requests")
    import requests
    from pystyle import Write, Colors, Colorate

class Share:
    def __init__(self):
        self.config = {
            'cookies': '',
            'id': '',
            'mode': 'normal'
        }
        self.a = 0
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1'
        }

    def banner(self):
        os.system("cls" if os.name == "nt" else "clear")
        banner = r"""
 __ __  _             _        __  _   ___                                 
|  \  \<_>._ _  ___ _| |_ ___  \ \/   | . \ ___  _ _  ___ ._ _ _  ___ ._ _ 
|     || || ' |<_> | | | / . \  \ \   | | |/ . \| '_>/ ._>| ' ' |/ . \| ' |
|_|_|_||_||_|_|<___| |_| \___/ _/\_\  |___/\___/|_|  \___.|_|_|_|\___/|_|_|
         ⚡ Tool Share VIP by Minato ⚡
        """
        print(Colorate.Vertical(Colors.rainbow, banner))
        print(Colorate.Horizontal(Colors.green_to_blue, "📣 Auto Share bài viết Facebook - Có delay hoặc No delay!", 1))
        print("")

    def loading_effect(self, text="🚀 Đang khởi động"):
        for i in range(3):
            sys.stdout.write(f"\r{text}{'.' * (i + 1)}{' ' * (3 - i)}")
            sys.stdout.flush()
            time.sleep(0.5)
        print("\r✅ Khởi động hoàn tất!       ")

    def input_config(self):
        Write.Print("\n👉 Nhập cookie Facebook: ", Colors.purple_to_red, end="")
        self.config['cookies'] = input()
        Write.Print("👉 Nhập ID bài viết cần share: ", Colors.purple_to_red, end="")
        self.config['id'] = input()
        Write.Print("⚡ Chọn chế độ (1 = thường, 2 = nhanh): ", Colors.blue_to_purple, end="")
        mode = input()
        self.config['mode'] = 'fast' if mode.strip() == '2' else 'normal'

        with open("config.json", "w") as f:
            json.dump(self.config, f)

    def load_config(self):
        with open("config.json", "r") as f:
            self.config = json.load(f)

    def get_token(self):
        self.headers['Cookie'] = self.config['cookies']
        response = requests.get("https://business.facebook.com/content_management", headers=self.headers)
        if "EAAG" in response.text:
            access_token = 'EAAG' + response.text.split('EAAG')[1].split('","')[0]
            return access_token
        else:
            raise Exception("❌ Không lấy được access token. Kiểm tra cookie!")

    def share(self, token):
        headers = {
            'User-Agent': self.headers['User-Agent'],
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'graph.facebook.com',
            'Cookie': self.config['cookies']
        }
        delay = 1 if self.config['mode'] == 'normal' else 0
        Write.Print(f"⏱️ Bắt đầu share với delay: {delay} giây\n", Colors.yellow_to_green)
        while True:
            try:
                url = f"https://graph.facebook.com/me/feed?link=https://m.facebook.com/{self.config['id']}&published=0&access_token={token}"
                response = requests.post(url, headers=headers)
                data = response.json()
                if 'id' in data:
                    Write.Print(f"[✅ {self.a}] - Đã share: {data['id']}\n", Colors.green_to_blue)
                    self.a += 1
                else:
                    Write.Print("[❌] - Bị block hoặc token lỗi!\n", Colors.red)
            except Exception as e:
                Write.Print(f"[❌ Lỗi]: {str(e)}\n", Colors.red)
            time.sleep(delay)


if __name__ == "__main__":
    share = Share()
    share.banner()
    share.loading_effect()
    share.input_config()
    share.load_config()
    try:
        token = share.get_token()
        Write.Print("🔑 Lấy token thành công!\n", Colors.green_to_white)
        share.share(token)
    except Exception as e:
        Write.Print(f"⚠️ Lỗi khi lấy token: {e}\n", Colors.red)

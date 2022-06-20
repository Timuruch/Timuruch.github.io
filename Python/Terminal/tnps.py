import requests
import sys
import os
import json
import time

ver = json.load(open("version.json"))

print("Timuruch Computer Systems")
print("2019-2022")
print("Version: 0.2 Beta")
print("Checking version...")

ver_url = "https://timuruch.github.io/TNPS/version.json"
try:
    r = requests.get(ver_url)
    version = float(r.content.decode())
except:
    print("An error occured!")
    version = 0

if ver == version:
    print("Version checked")
else:
    input("Update TNPS. Click enter to exit.")
    sys.exit()
while True:
    print("[1] New mode (TNPS)")
    print("[2] Old mode (BBS, News surfer)")
    print("[3] Download (Boot) mode (TNPS)")
    print("[4] Exit (To usuall Terminal)")
    output = input("[?]")
    if output == "1":
        channel = input("Enter code: ")
        url = "https://timuruch.github.io/TNPS/TEXT/%s.json" % channel
        r = requests.get(url)
        file = open("text.json", "wb")
        file.write(r.content)
        file.close()
        try:
            text = json.load(open("text.json"))
            for x in text:
                print(x)
        except:
            print("An error occured")
    elif output == "2":
        channel = input("Enter code:")
        url = "https://timuruch.github.io/bbs/%s.py" % channel
        r = requests.get(url)
        file = open("text.py", "wb")
        file.write(r.content)
        file.close()
        try:
            import text
            #file = open("text.py")
            #eval(file.read())
            os.remove("text.py")
        except:
            print("An error occured")
    elif output == "3":
        print("Download (boot) mode")
    elif output == "4":
        print("Closing tnps terminal")
        time.sleep(0.5)
        break
    else:
        print("Wrong tnps terminal command!(Try to use 'help to see all commands')")
        

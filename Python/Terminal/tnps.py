import requests
import sys
import os
import json

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
    output = input("[?]")
    if output == "news":
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
    elif output == "archive":
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
    elif output == "help":
        print("Help menu")
        print('''archive - opens servers on old protocol (like news surfer or BBS) for example
        old Timuruch (now Redish) anoucments server code 8801''')
        print('''news - open servers on new protocol (TNPS 0.2) all codes are in replacing
        to new protocol''')
        print('''exit - exits from tnps terminal (to usuall terminal)''')
    elif output == "exit":
        print("Closing tnps terminal")
        break
    else:
        print("Wrong tnps terminal command!(Try to use 'help to see all commands')")
        

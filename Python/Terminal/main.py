from settings import *
from time import *

print("The Terminal")
sleep(0.5)
print("Version ", VERSION)
sleep(0.5)
print("By Redish")
sleep(0.5)
print(NOTE)

while True:
    command = input("[?]")
    if "exit" in command:
        print("Closing undertasks.")
        sleep(0.5)
        print("Undertasks closed.")
        break
    elif "help" in command:
        print("Help:")
        print("tutorial - opens tutorial menu")
        print("redish - diagnostic of terminal")
        print("settings - open settings menu")
        print("tnps - TNPS terminal (Old name: News Surfer (Older name: BBS)))")
        print("store - store of Timuruch programs (Our Partner)")
        print("run - run installed games/apps")
        print("help - opens this menu")
    elif "tutorial" in command:
        print("Tutorial Menu")
        print('''Terminal - is teamwork of two groups Radish and Timuruch (Thanks to Timuruch for his inventations
        in news technology and Ukrainian translation of end titles and EaStEr EgG) it's very easy to use terminal \
        for manual work and easy acess to comunications it's optimizateed to T-Live games (but no SUID saved)''')
        print("If you want to learn commands type command 'help'")
        print("If you want to optimize terminal for you type 'setings'")
        print("You can download programs from store type 'store'")
        print("End of tutorial (: Try to translate Redish to Ukrainian(it will be funny)")
    elif "redish" in command:
        sound = input("Enter sound check code: ")
        if "90AS" in sound:
            print("Secret info about landing")
            sleep(0.5)
            print("Place: Vroclav, Budzic")
            sleep(0.5)
            print("Date: 31.07.2022")
            sleep(0.5)
            print("Goal: Find HER.")
            sleep(0.5)
            print("Other: #[]323]]1 (Too secret (:))")
            print("Redish - редис")
            print("Timuruch - T.Z.")
            input("Press enter to see ending: ")
            import egg
            print("End of Terminal")
            print("Thanks for playing!")
    elif "settings" in command:
        print("Settings")
        print("[1] Boot settings")
        print("[2] Exit")
        val = input("[0]")
        if "1" in val:
            print("No settings!")
        else:
            print("No settings!")
    elif "tnps" in command:
        print("Launching TNPS Terminal")
        sleep(0.5)
        import tnps
    elif "store" in command:
        print("Store of Timuruch and Redish programs")
        print("[1] Games")
        print("[2] Programs")
        print("[3] Exit")
        while True:
            val = input("[0]")
            if "1" in val:
                print("Games")
                break
            elif "2" in val:
                print("Programs")
                break
            elif "3" in val:
                print("Exiting")
                val = False
                break
        if val:
            if "1" in val:
                print("Games list")
                print("[1] Infinity run")
                print("[2] Tic tac toe")
                print("[3] Камінь-Ножиці-Папір")
                while True:
                    val = input("[0]")
                    if "1" in val:
                        print("Error 90AS, try to patch it by using 'redish' command")
                        break
                    elif "2" in val:
                        print("Error 90AS, try to patch it by using 'redish' command")
                        break
                    elif "3" in val:
                        print("Error 90AS, try to patch it by using 'redish' command")
                        break
            elif "2" in val:
                print("[1] Very cool program")
                while True:
                    val = input("[0]")
                    if "1" in val:
                        print("Error 90AS, try to patch it by using 'redish' command")
                        break
    else:
        print("Wrong command.")

input("Press enter to exit: ")
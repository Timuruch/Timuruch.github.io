from settings import *
import time

def tutor_menu():
    print("Tutorial menu: ")
    print("Terminal - it's an operation system for windows machines")
    print("(MS-DOS) with easier for use commands. To see all comma-")
    print("nds type 'help'. If you want to take a test settings for")
    print("more expirience in tnps select 'boot_download' mode and ")
    print("download file from file server of project Arabella (boot ")
    print("set is must be turned off) - 8092.")

def help_menu():
    print("Help menu: ")
    print("tnps - launches TNPS terminal")
    print("tutorial - opens tutorial menu")
    print("help - opens this menu")
    print("store - launches programs store")
    print("updmng - launches UpdateManager")
    print("settings - launches settings")
    print("exit - exits terminal")

def settings():
    while True:
        print("[1] Store settings")
        print("[2] ")
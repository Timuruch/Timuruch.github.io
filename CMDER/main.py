import time
import random
import os
import requests

m = open('active.txt')
tn = open('user/tname.txt')
tp = open('user/tpass.txt')
n = open('user/name.txt')
p = open('user/pass.txt')
mm = m.read()
name = n.read()
password = p.read()
tname = tn.read()
tpass = tp.read()

print("CMDER beta 1.0")
print("Made by Timuruch")
print("Welcome %s" % name)

if(mm == "no"):
    print("You don't logined in Tlive")
elif(mm == "yes"):
    print("Logined")
x = 0 

while x == 0:
    passw = input("Enter password:")

    if(password == passw):
        print("You sucessfuly entered")
        x = 1
    else:
        print("You wrote wrong password")

while True:
    output = input("[?]")
    if(output == "get_started"):
        print("Welcome newfag")
        print("This is CMDER")
        print("A os what use all Timuruch programs")
        print("Tips:")
        print("1.To see all comands type help")
        print("2.If you see a bug please conatct Administator with command bug")
        print("Updates:")
        print("1.This is first version of CMDER what can use all Timuruch programs")
        print("2.It can easiy update")
        print("It has a magazine")
    elif(output == "settings"):
        print("Settings:")
        print("[1] Change user name")
        print("[2] Change pass word")
        print("[3] Activate CMDER")
        z = 0
        while z == 0:
            set_out = input("[?]")
            if(set_out == "3"):
                x = input("Please enter activation code:")
                if (x == "41265"):
                    print("CMDER succesfuy activated")
                    acti = open("activation.txt", 'wb')
                    acti.write('activated')
                    acti.close()
                    z = 1
            elif(set_out == "2"):
                print("Now it's didn't work")
                z = 1
            elif(set_out == "1"):
                print("Now it's didn't work")
                z = 1
    elif(output == "magazine"):
        time.sleep(0.5)
        print("Welcome to magazine:")
        time.sleep(0.5)
        if(b == 1):
            print("[1] BBS for CMDER")
        elif(b == 2):
            print("You don't logined in Tlive")
            print("While you don't logined in Tlive you can't use magazine")
            print("You can login just use tlive command")
        #print("[1] BBS for CMDER")
    elif(output == "clear"):
        os.system('cls') 
    elif(output == "tlive"):
        if(mm == "yes"):
            print("Welcome %s" % tn)
        elif(mm == "no"):
            if(m == "yes"):
                print("Welcome back %s" % tn)
            elif(m == "no"):
                print("You don't logined Yet")
                print("[1] Login")
                print("[2] Register")
                print("Note: Tlive is local account and work only with computer where you signed")
                pp = 0
                while pp == 0:
                    dd = input("[?]")
                    if(dd == "[1]"):
                        nnam = input("Enter name:")
                        ppas = input("Enter pass:")
                        if(nnam == tn and ppas == tp):
                            pp = 2
                            lll = open("active.txt")
                            lll.write("yes")
                            lll.close()
                            print("You succesfuly entered")
                    elif(dd == "[2]"):
                        nnnam = input("Enter name:")
                        pppas = input("Enter pass:")
                        vvv = open("user/name.txt", 'w')
                        ppp = open("user/pass.txt", 'w')
                        lll = open("active.txt")
                        vvv.write(nnnam)
                        ppp.write(pppas)
                        lll.write("yes")
                        vvv.close()
                        ppp.close()
                        lll.close()
                        print("User succesfuly created")
                        print("To work more stable requit pleas")


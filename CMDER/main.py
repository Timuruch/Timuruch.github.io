import time
import random
import requests

n = open('user/name.txt')
p = open('user/pass.txt')
name = n.read()
password = p.read()

print("CMDER beta 1.0")
print("Made by Timuruch")
print("Welcome %s" % name)

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
        print("Welcome to magazine:")
        print("[1] BBS for CMDER")
        

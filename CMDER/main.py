import time
import random
import requests

n = open('user/name.txt')
p = open('user/pass.txt')
name = n.read()
password = p.read()

print("CMDER beta 1.0")
print("Made by Timuruch")

while x == 0:
    print("Welcome %s" % name)
    passw = input("Enter password:")

    if(password == passw):
        print("You sucessfuly entered")
        x = 1
    else:
        print("You wrote wrong password")
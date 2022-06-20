from settings import *
from command import *
from time import *

print("The Terminal")
sleep(0.5)
print("Version ", VERSION)
sleep(0.5)
print("By Redish and Timuruch")
sleep(0.5)
print(NOTE)

while True:
    command = input("[?]")
    if com(command):
        break
    
input("Press enter to exit: ")
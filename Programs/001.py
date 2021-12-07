import os

x = 1
y = 1

mwp = ''

def drawer():
    global poc ,loc, mwp
    poc = ""
    loc = ""
    if x == 1 and y == 1:
        poc = "x "
        loc = "  "
    elif x == 2 and y == 1:
        poc = " x"
        loc = "  "
    elif x == 1 and y == 2:
        poc = "  "
        loc = "x "
    elif x == 2 and y == 2:
        poc = "  "
        loc = " x"
    mwp = ('''
####
#%s#
#%s#
####
''' % (poc, loc))

def move(symbol):
    global x,y
    if 'w' in symbol:
        y -= 1
    elif 's' in symbol:
        y += 1
    elif 'a' in symbol:
        x -= 1
    elif 'd' in symbol:
        x += 1
    drawer()
    
os.system("cls")

drawer()

while True:
    print(mwp)
    output = input("")
    os.system("cls")
    if "exit" in output:
        break
    move(output)

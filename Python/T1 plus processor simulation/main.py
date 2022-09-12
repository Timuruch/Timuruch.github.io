
while True:
    value = input(": ")
    if value == "10011":
        a = input("S1: ")
        b = input("S2: ") 
        sum = bin(int(a, 2) + int(b, 2))
        print(sum[2:])
    if value == "1111":
        a = input("O1: ")
        b = input("O2: ")
        if a == "1" or b == "1":
            print("1")
    if value == "1110":
        a = input("N1: ")
        if a == "1":
            print('0')
        if a == "0":
            print("1")
    if value == "101":
        break
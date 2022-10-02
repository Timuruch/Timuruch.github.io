from json import *
import random

class Register:
    def __init__(self):
        pass
    
    def shuffle(self, text=""):
        shuffles = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "1", "2", "3", "4", "4", "5", "6", "7", "8", "9", "0",
        "g", "G", "h", "H", "!", ".", "<", ">", "/", "?", "^"]
        result = ""
        for x in range(len(text)):
            result += text[x]
            n1 = random.choice(shuffles)
            n2 = random.choice(shuffles)
            n3 = random.choice(shuffles)
            result += n1 + n2 + n3
        print(result)
        return result

    def decrypt(self, text=""):
        result = ""
        counter = 0
        while True:
            result += text[counter]
            counter += 4
            if counter == len(text):
                break
        print(result)


r = Register()
result = r.shuffle("admin")
r.decrypt(result)
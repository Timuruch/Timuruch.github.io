from json import *

class Logins:
    def __init__(self):
        pass
    
    def decrypt(self, text=""):
        result = ""
        counter = 0
        while True:
            result += text[counter]
            counter += 4
            if counter == len(text):
                break
        print(result)

    def login(self, info=False):
        if not info:
            return (False, "No login data endtered! Err. N:01")
        else:
            pass

        

l = Logins()
result = l.login()
print(result[1])


from coms import *
from settings import *
import json

def com(result):
    dictory = json.load(open("com.json"))
    keys = list(dictory.keys())
    if "exit" in result:
        return True
    else:
        for x in range(0, len(keys)):
            if keys[x] in result:
                exec(dictory.get(keys[x]))
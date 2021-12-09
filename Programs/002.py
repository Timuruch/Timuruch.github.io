import random
import sys

while True:
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    value = input(str(x) + " + " + str(y) + " = ")
    if 'exit' in value:
        sys.exit()
    elif x+y == int(value):
        print("You win. Next round!")


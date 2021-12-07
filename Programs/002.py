import random

while True:
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    value = input(str(x) + " + " + str(y) + " = ")
    if x+y == int(value):
        print("You win. Next round!")


def update():
    a = open("upgrade.txt")
    t = a.read()
    exec(t)
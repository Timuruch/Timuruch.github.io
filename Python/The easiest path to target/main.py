world = [
    "WWWWWWWW",
    "WP.....W",
    "W......W",
    "W......W",
    "Wwww...W",
    "W......W",
    "WT.w...W",
    "WWWWWWWW"
]

size_of_world = (800, 800)
old_target = False
d_player = ()

def replicate():
    coords = []
    player = ()
    target = ()
    walls = []

    for x in range(len(world)):
        for i in range(len(world[x])):
            if world[x][i] == "P":
                player = ((i*100, x*100))
            elif world[x][i] == "T":
                target = ((i*100, x*100))
            elif world[x][i] == "w":
                walls.append((i*100, x*100))
            else:
                coords.append((i*100, x*100))
    return coords, player, target, walls

def find_new_target(player, target, walls) :
    y_coord = d_player[1]
    x = 0
    y = 0
    wall = []
    x_axes = []
    y_axes = []

    for x in walls:
        if x[1] == y_coord:
            wall.append(x[1])

    for x in wall:
        if wall[0] == 100:
            continue
        x_axes.append(wall[0])
        y_axes.append(wall[1])

    x = max(x_axes) + 100
    y = y_coord + 100

    return x, y, "max"
def set_new_target(x, y, target, prefix):
    global old_target
    old_target = target
    target = (x, y)
    return target

def check_on_walls(player, target, x_moves, y_moves, walls):
    global d_player
    d_player = player
    test = False
    run = True
    while run:
        if x_moves == "-X":
            d_player = (d_player[0]-100, d_player[1])
        elif x_moves == "+X":
            d_player = (d_player[0]+100, d_player[1])
        elif y_moves == "-Y":
            d_player = (d_player[0], d_player[1]-100)
        elif y_moves == "+Y":
            d_player = (d_player[0], d_player[1]+100)


        if d_player[0] == target[0]:
            x_moves = ""
        if d_player[1] == target[1]:
            y_moves = ""
        if d_player[0] == target[0] and d_player[1] == target[1]:
            run = False
        for x in range(len(walls)):
            if d_player[0] == walls[x][0] and d_player[1] == walls[x][1]:
                test = True
                print("Collision Accepted")
                print(d_player)
                run = False
                break
    
    print("Status of test: ", test)
    return test

def recalibration(player, target, x_moves, y_moves, walls):
    global old_target
    print("Checking new way from new target to old one.")
    target = old_target
    old_target = False
    x_moves, y_moves = moves(player, target)
    print("New moves: ", x_moves, y_moves)
    print("Changing targets.")
    test = check_on_walls(player, target, x_moves, y_moves, walls)
    move(player, target, x_moves, y_moves, test)

def splice(list, pos, symbol):
    out = ""
    for x in range(len(list)):
        if x == pos:
            out += symbol
        else:
            out += list[x]
    return out

def print_map(player, target, walls):
    m_player = (int(player[0]/100), int(player[1]/100))
    m_target = (int(target[0]/100), int(target[1]/100))
    mini_map = [
        "WWWWWWWW",
        "W......W",
        "W......W",
        "W......W",
        "W......W",
        "W......W",
        "W......W",
        "WWWWWWWW"
    ]
    for x in walls:
        wall = (int(x[0]/100), int(x[1]/100))
        mini_map[wall[1]] = splice(mini_map[wall[1]], wall[0], "w")
    
    mini_map[m_player[1]] = splice(mini_map[m_player[1]], m_player[0], "P")

    mini_map[m_target[1]] = splice(mini_map[m_target[1]], m_target[0], "T")

    if old_target:
        o_target = (int(old_target[0]/100), int(old_target[1]/100))
        mini_map[o_target[1]] = splice(mini_map[o_target[1]], o_target[0], "O")

    for x in mini_map:
        print(x)

def moves(player, target):
    x_moves = ""
    y_moves = ""
    px, py = player
    tx, ty = target
    if px > tx:
        x_moves = "-X"
    if px < tx:
        x_moves = "+X"
    if py < ty:
        y_moves = "+Y"
    if py > ty:
        y_moves = "-Y"
    return x_moves, y_moves

def move(player, target, x_moves, y_moves, test):
    moves = x_moves + y_moves
    run = False
    if not test:
        run = True
    while run:
        if x_moves == "-X":
            player = (player[0]-100, player[1])
        elif x_moves == "+X":
            player = (player[0]+100, player[1])
        elif y_moves == "-Y":
            player = (player[0], player[1]-100)
        elif y_moves == "+Y":
            player = (player[0], player[1]+100)

        print("Moves to do: ", x_moves, y_moves)
        print("Player: ", player)
        print("Target: ", target)

        if player[0] == target[0]:
            x_moves = ""
        if player[1] == target[1]:
            y_moves = ""
        if player[0] == target[0] and player[1] == target[1]:
            run = False

        print_map(player, target, walls)

    if not test:
        print("Done!")
        print("Moves: ", moves)
    else:
        print("Aborted because of not succseded wall colision test!")
    
    if old_target:
        recalibration(player, target, x_moves, y_moves, walls)

coords, player, target, walls = replicate()
x_moves, y_moves = moves(player, target)
test = check_on_walls(player, target, x_moves, y_moves, walls)
print(target)
if test:
    x, y, prefix = find_new_target(player, target, walls)
    target = set_new_target(x, y, target, prefix)
    print("Old moves: ", x_moves, y_moves)
    x_moves, y_moves = moves(player, target)
    print("New moves: ", x_moves, y_moves)
    test = check_on_walls(player, target, x_moves, y_moves, walls)

for x in world:
    print(x)
move(player, target, x_moves, y_moves, test)

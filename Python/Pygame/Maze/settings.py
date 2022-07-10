import math

#window settings
WIDTH = 500
HEIGHT = 400
TITLE = "Pygame"

#map settings
MX = 0
#MY = HEIGHT - 100
MY = 0
TALE = 20
TUTOR_MAP = [
    "#########################",
    "# #                ##   #",
    "# #   #  ## #      ##   #",
    "# #####  # #            #",
    "#        # #            #",
    "#####  ### #      ##    #",
    "#        # #      ##    #",
    "#        # #      ##    #",
    "#        # #      ##    #",
    "#        # #      ##    #",
    "#        # #      ##    #",
    "#        # #      ##    #",
    "#        # #      ##    #",
    "#        # #      ##    #",
    "#########################"
]

#player settings
SX = TALE
SY = TALE
SIZE = 20
PSPEED = 3
FPS = 60

#ray casting
NUM_RAYS = 100
MAX_LENGHT = 50

#color settings
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#display setting
PERMISSION = True
HEIGHT = 600
WIDTH = 700
TITLE = "Sandbox"
FPS = 60

#Color settings
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SAND = (194, 178, 128)

#World settings 
WDTH = 4
BLCK = 10
BLOCK = 400 + WDTH*2
RES = int(400/10) #resolution of world

#Seasons settings
SEASONS = 2
WINTER_W_COEFF = 10
SUMMER_W_COEFF = 20
WATER_ISL_W_COEFF = 90
SEASONS_KEYS = {
    0 : WINTER_W_COEFF, #WINTER
    1 : SUMMER_W_COEFF, #SUMMER
    2 : WATER_ISL_W_COEFF #WATER_ISLAND
}
SEASONS_COLOR_KEYS = {
    0 : WHITE,
    1 : GREEN,
    2 : SAND
}
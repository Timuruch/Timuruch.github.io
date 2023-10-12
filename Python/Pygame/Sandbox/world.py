from settings import *
import random

class world:
    def __init__(self, w, pygame):
        self.w = w
        self.p = pygame
        self.generate_world()
        self.generate_water()
    
    def draw(self):
        self.p.draw.rect(self.w, RED, (0, 0, BLOCK, BLOCK), WDTH)

        x = WDTH
        y = WDTH

        for r in self.world:
            for c in r:
                self.p.draw.rect(self.w, c, (x, y, BLCK, BLCK))
                x += BLCK
            x = WDTH
            y += BLCK
    
    def generate_world(self):
        self.season = random.randint(0, SEASONS)
        self.world = []
        for x in range(RES):
            row = []
            for y in range(RES):
                row.append(SEASONS_COLOR_KEYS[self.season])
                pass
            self.world.append(row)
    
    def generate_water(self):
        coeff = SEASONS_KEYS[self.season]
        self.size = ()
        seasones = [[20, (10, 10), (20, 0), (15, 5)], [10, (10, 0), (5, 5), (8, 2)]]
        for x in seasones:
            if x[0] == coeff:
                self.size = random.choice([x[1], x[2], x[3]])
                break
            else:
                self.size = random.randint(5, 30)
        if self.season != 2:
            x = random.randint(1, 39)
            y = random.randint(1, 39)
            
            print(x*10, y*10)

        else:
            pass
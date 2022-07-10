from settings import *
import pygame

class player:
    def __init__(self, w, pygame, walls):
        self.w = w
        self.pygame = pygame
        self.PX = SX
        self.PY = SY
        self.walls = walls

    def draw(self):
        self.pygame.draw.rect(self.w, BLUE, (self.PX, self.PY, SIZE, SIZE))

    def move(self):
        keys = self.pygame.key.get_pressed()

        if keys [self.pygame.K_w] and self.PY > TALE:
            self.PY -= PSPEED
        if keys [self.pygame.K_s] and self.PY < (len(TUTOR_MAP)-2)*20:
            self.PY += PSPEED
        if keys[self.pygame.K_a] and self.PX > TALE:
            self.PX -= PSPEED
        if keys[self.pygame.K_d] and self.PX < WIDTH-TALE-TALE:
            self.PX += PSPEED 
        if keys[self.pygame.K_ESCAPE]:
            self.pygame.quit()

    def check_touch(self):
        xmax = self.PX + SIZE
        ymax = self.PY + SIZE
        for i in self.walls: #[(x, y)]
            x, y = i
            if self.PX > x and self.PX < x+TALE:
                if self.PY > y and self.PY < y+TALE:
                    self.PX -= x - self.PX
    
    def get_pos(self):
        return (self.PX, self.PY)

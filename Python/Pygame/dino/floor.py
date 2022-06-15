from settings import *
from borders import *
import random
import pygame

class floor:
    def __init__(self, w, pygame):
        self.w = w
        self.pygame = pygame
        self.floor = self.pygame.image.load("assets\dido.png")
        self.cof = 0
    
    def restart(self):
        self.cof = 0

    def draw(self, start, pos):
        for x in range(WIDTH//SIZE+1):
            #self.pygame.draw.line(self.w, BLACK, (SIZE*x, YF), (SIZE*(x+1), YF))
            self.w.blit(self.floor, ((SIZE*x)+self.cof, YF))
            if self.cof == -SIZE:
                self.cof = 0
            elif start:
                self.cof -= SPS
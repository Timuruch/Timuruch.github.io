from settings import *
import pygame

class Map:
    def __init__(self, w, pygame):
        self.w = w
        self.pygame = pygame
        self.map = set()
        x = MX
        y = MY
        for i in TUTOR_MAP:
            for c in i:
                if c == "#":
                    self.pygame.draw.rect(self.w, GREEN, (x, y, TALE, TALE))
                    self.map.add((x,y))
                    x += TALE
                else:
                    x += TALE
            x = MX
            y += TALE 

    def draw(self):
        for x in self.map:
           self.pygame.draw.rect(self.w, GREEN, (x[0], x[1], TALE, TALE)) 

    def get_walls(self):
        return self.map

            

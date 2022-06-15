from settings import *
from scores import *
import random
import pygame

class border:
    def __init__(self, w, pygame):
        self.w = w
        self.pygame = pygame
        self.s = score_system(self.w, self.pygame)
        self.assets = [self.pygame.image.load("assets/cactus.png")]
        self.simples = [" ", "c", " ", " ", " ", " "]
        self.borders = []
        self.stop = False
        self.y = 176
    
    def restart(self):
        self.s.restart()
        self.borders = []
        self.stop = False

    def create(self, start):
        if start:
            l = len(self.borders)
            if l != MAX_BORDERS:
                g = "c"
                if g == "c":
                    c = random.randint(500, 800)
                    self.borders.append(c)

    def draw(self, start, pos):
        x, y = pos
        if start:
            self.s.print_score(start)
            l = len(self.borders)
            for i in range(l):
                self.w.blit(self.assets[0], (self.borders[i],self.y))
                self.borders[i] = self.borders[i] - 10
                if self.borders[i] <= 0:
                    self.borders[i] = random.randint(500, 800)
                if 35 >= self.borders[i] and y >= 176-15:#33
                    self.s.save()
                    self.stop = True
                
        else:
            l = len(self.borders)
            self.s.print_score(start)
            for x in range(l):
                self.w.blit(self.assets[0], (self.borders[x],self.y))
        
        




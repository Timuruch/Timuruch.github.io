from settings import *
from random import *
import pygame

class food:
    def __init__(self, pygame, w):
        self.pygame = pygame
        self.w = w
        self.buffer = []
        self.counter = 0

    def create(self):
        cans = [True, False, False, False, False]
        choise = choice(cans)
        if len(self.buffer) == 0 and not choise:
            w = WIDTH / 50
            h = HEIGHT / 50
            rw = randint(1, w-1)
            rh = randint(1, h-1)
            self.buffer = [rw*50, rh*50, BLUE]
        elif choise:
            w = WIDTH / 50
            h = HEIGHT / 50
            rw = randint(1, w-1)
            rh = randint(1, h-1)
            self.buffer = [rw*50, rh*50, BLACK]
    
    def draw(self):
        self.pygame.draw.rect(self.w, self.buffer[2], (self.buffer[0], self.buffer[1], SIZE, SIZE))
        if self.buffer[2] == BLACK:
            self.counter += 0.005
        if int(self.counter) == 1:
            self.buffer = []
            self.create()
            self.counter = 0

    def refresh(self, pos):
        x, y = pos
        if x == self.buffer[0] and y == self.buffer[1] and self.buffer[2] == BLUE:
            self.buffer = []
            self.create()
            return True
        elif x == self.buffer[0] and y == self.buffer[1] and self.buffer[2] == BLACK:
            return False
        

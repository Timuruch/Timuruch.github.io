from re import S
from settings import *
import pygame

class snake:
    def __init__(self, pygame, w):
        self.pygame = pygame
        self.w = w
        self.buffer = [(SPAWN_X, SPAWN_Y)]
        self.counter = 0
        self.xd = True
        self.yd = None
        self.game = True
        self.score = 0
    
    def text(self, text, pos, sz):
        fnt = self.pygame.font.Font('Fixedsys.ttf', sz)
        text = fnt.render(str(text), False, (255, 255, 255))
        self.w.blit(text, pos)

    def draw(self):
        for i in self.buffer:
            self.pygame.draw.rect(self.w, SNAKE_COLOR, (i[0], i[1], SIZE, SIZE))
        if self.game == False:
            self.text("Game over", ((WIDTH//2)-170, (HEIGHT//2)-40), 80)
        self.text(self.score, (750, 25), 50)
        self.counter += 0.05
        if int(self.counter) == 1 and self.game:
            if self.xd:
                for i in range(len(self.buffer)):
                    x,y = self.buffer[i]
                    try:
                        d = self.buffer[2]
                    except:
                        d = True
                    self.buffer[i] = (x+SIZE, y)
                self.counter = 0
            elif self.xd == False:
                for i in range(len(self.buffer)):
                    x,y = self.buffer[i]
                    self.buffer[i] = (x-SIZE, y)
                self.counter = 0
            
            if self.yd:
                for i in range(len(self.buffer)):
                    x,y = self.buffer[i]
                    self.buffer[i] = (x, y+SIZE)
                self.counter = 0
            elif self.yd == False:
                for i in range(len(self.buffer)):
                    x,y = self.buffer[i]
                    self.buffer[i] = (x, y-SIZE)
                self.counter = 0

    def refresh(self, boole):
        if boole:
            self.score += 1
            v = self.buffer[len(self.buffer)-1]
            if self.xd:
                self.buffer.append((v[0]-SIZE, v[1], self.xd))
            elif self.yd == False:
                self.buffer.append((v[0]+SIZE, v[1], self.xd))
            
            if self.yd:
                self.buffer.append((v[0], v[1]-SIZE, self.yd))
            elif self.yd == False:
                self.buffer.append((v[0], v[1]+SIZE, self.yd))
        elif boole == False:
            self.game = False

    def move(self):
        keys = self.pygame.key.get_pressed()
        
        if self.game:
            if keys[self.pygame.K_w]:
                self.yd = False
                self.xd = None
            if keys[self.pygame.K_s]:
                self.yd = True
                self.xd = None
            if keys[self.pygame.K_a]:
                self.xd = False
                self.yd = None
            if keys[self.pygame.K_d]:
                self.xd = True
                self.yd = None

        if keys[self.pygame.K_ESCAPE]:
            self.pygame.quit()
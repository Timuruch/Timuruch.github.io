from time import *
from settings import *
import pygame

pygame.init()
pygame.mixer.init()

class dino:
    def __init__(self, w, pygame):
        self.w = w
        self.pygame = pygame
        self.x = 5
        self.y = 160
        self.down = False
        self.up = False
        self.start = False
        self.go = False
        self.restart = False
        self.animCount = 0
        self.dino = [self.pygame.image.load("assets\dino.png"), self.pygame.image.load("assets\dino_closed_eyes.png")]
        self.crouch = [self.pygame.image.load("assets\crouch_walk_1.png"), self.pygame.image.load("assets\walk_crouch_2.png")]
        self.walk = [self.pygame.image.load("assets\walk_1.png"), self.pygame.image.load("assets\walk_2.png")]
        self.w.blit(self.dino[0], (self.x, self.y))
    
    def text(self, text, x, y):
        fnt = self.pygame.font.SysFont('Verdana', 30)
        text = fnt.render(str(text), False, (0, 0, 0))
        self.w.blit(text,(x, y))

    def move(self):
        keys = self.pygame.key.get_pressed()
        if keys[self.pygame.K_UP] and self.start:
            self.down = False
            self.up = True
        if keys[self.pygame.K_DOWN] and self.start:
            self.up = False
            self.down = True
        if keys[self.pygame.K_SPACE] and self.go != True:
            self.start = True
            self.restart = False
            self.down = False
            self.up = False
        if keys[self.pygame.K_SPACE] and self.start:
            self.down = False
            self.up = True
        if keys[self.pygame.K_ESCAPE]:
            self.start = False

    def get_pos(self):
        return (self.x, self.y)

    def stop(self, ansver):
        if ansver and self.restart != True:
            self.start = False
            self.go = True

    def click(self, pos):
        x, y = pos
        x2 = 34 + 230
        y2 = 110 + 130
        if y <= y2:
            if y >= 50:
                if x <= x2:
                    if x >= 230:
                        self.restart = True
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def draw(self):
        if self.down:
            try:
                self.w.blit(self.crouch[self.animCount // 1], (self.x, self.y+15))
                self.down = False
                self.animCount += 1
                #pygame.time.delay(DELAY)
                #sleep(DELAY)
            except:
                self.animCount = 0
                self.w.blit(self.crouch[self.animCount // 1], (self.x, self.y+15))
                self.down = False
                self.animCount += 1
                #pygame.time.delay(DELAY)
                #sleep(DELAY)
        elif self.up:
            pygame.mixer.music.load("assets\music\jump.mp3")
            pygame.mixer.music.play(1) 
            pygame.mixer.music.set_volume(0.9)
            try:
                if self.y >= 160-JUMP:
                    self.y -= 10
                #self.y -= JUMP
                else:
                    self.up = False
                self.w.blit(self.walk[self.animCount // 1], (self.x, self.y))
                self.animCount += 1
                #pygame.time.delay(DELAY)
                #sleep(DELAY)
            except:
                if self.y >= 160-JUMP:
                    self.y -= 10
                #self.y -= JUMP
                else:
                    self.up = False
                self.animCount = 0
                self.w.blit(self.walk[self.animCount // 1], (self.x, self.y))
                self.animCount += 1
                #pygame.time.delay(DELAY)
                #sleep(DELAY)
        elif self.start:
            try:
                self.w.blit(self.walk[self.animCount // 1], (self.x, self.y))
                self.animCount += 1
                #pygame.time.delay(DELAY)
                #sleep(DELAY)
            except:
                self.animCount = 0
                self.w.blit(self.walk[self.animCount // 1], (self.x, self.y))
                self.animCount += 1
                #pygame.time.delay(DELAY)
                #sleep(DELAY)
        else:
            self.w.blit(self.dino[0], (self.x, self.y))
            if self.go and self.restart != True:
                self.w.blit(self.pygame.image.load("assets\\game_over.png"), (160, 110))
                self.w.blit(self.pygame.image.load("assets\\replay.png"), (230, 130))
            else:
                self.text("Press escape or space to start!", 0,450)
                self.go = False
        if self.y <= 160 and self.up != True:
            self.y += 10
from pickle import FALSE
from settings import *
from random import *
import pygame

class aliens:
    def __init__(self, pygame, w):
        self.pygame = pygame
        self.w = w
        self.costumes = [self.pygame.image.load("assets/aliens/alien_1.png"), self.pygame.image.load("assets/aliens/alien_2.png")]
        self.aliens = False
        self.bullets = []
        self.animCount = 0
    
    def create(self):
        self.aliens = []
        x = MINX
        y = MIXY
        for i in range(MAX_ALIENS):
            self.aliens.append((x, y))
            if x >= MAXX:
                x = MINX
                y += SIZE
            else:
                x += SIZE

    def test_bullet(self, bullets, score): #size 50x50
        try:
            for i in range(0, len(self.aliens)):
                x, y = self.aliens[i]
                xp = x + 50
                yp = y + 50
                for c in range(0, len(bullets)):
                    xb, yb = bullets[c] #[(x, y)]
                    if x <= xb and y <= yb:
                        if xp >= xb and yp >= yb:
                            print("Touch")
                            del self.aliens[i]
                            del bullets[c]
                            score += 1
                            break
            return bullets, score
        except:
            pass

    def draw(self, start):
        tries = [True, False, False, False]
        if self.aliens:
            for x in self.aliens:
                if int(self.animCount) >= 2:
                    self.animCount = 0
                shuffle(tries)
                if int(self.animCount) == 1 and len(self.bullets) <= MAX_ABULLETS and tries[0] and start:
                    self.bullets.append(x)
                self.w.blit(self.costumes[int(self.animCount) // 1], x)
            if start:
                self.animCount += 0.025
            for x in range(0, len(self.bullets)):
                try:
                    i = self.bullets[x]
                except:
                    break
                if i[1] >= HEIGHT:
                    del self.bullets[x]
                else:
                    spd = randint(1, MAX_ABULLET_SPEED)
                    self.w.blit(self.pygame.image.load("assets/bullet.png"), (i[0], i[1]))
                    self.bullets[x] = (i[0], i[1]+spd)
        else:
            self.create()
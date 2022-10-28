from settings import *
from random import *  
import json 
import sys
import pygame

class starship:
    def __init__(self, pygame, w, image, size, aliens):
        self.a = aliens
        self.pygame = pygame
        self.w = w
        self.img = self.pygame.image.load(image)
        self.x = SX
        self.y = SY
        self.size = size
        self.start = False
        self.shoot = False
        self.movement = False
        self.gameover = False
        self.score = 0
        self.index = 1
        self.state = 0
        self.hi_score = json.load(open("score.json"))
        self.bullets = []

    def play_demo(self):
        if self.start == False:
            shoot = [True, False, False, False, False, False, False]
            Left = [True, True, True, False, False, False, False]
            Right = [True, False, True, False, False, True, False]
            shuffle(shoot)
            shuffle(Left)
            shuffle(Right)
            self.shoot = shoot[0]
            if Left[0]:
               self.x -= SPEED
            if Right[0]:
                self.x += SPEED 

    def text(self, text, pos, sz):
        fnt = self.pygame.font.Font('assets/fonts/Fixedsys.ttf', sz)
        text = fnt.render(str(text), False, (255, 255, 255))
        self.w.blit(text, pos)


    def blow(self, x, y):
        if int(self.index) >= 5:
            self.index = 1
        else:
            direc = str("assets/blow/blow%s.png" % int(self.index))
            self.w.blit(self.pygame.image.load(str(direc)), (x, y))
            self.index += 1

    def draw(self):
        l = len(self.bullets)
        if self.shoot and l <= MAX_BULLETS:
            self.shoot = False
            self.bullets.append((self.x+23, self.y))
        for x in range(0, len(self.bullets)):
            try:
                i = self.bullets[x]
            except:
                break
            try:
                if i[1] <= 0:
                    del self.bullets[x]
                else:
                    self.w.blit(self.pygame.image.load("assets/bullet.png"), (i[0], i[1]))
                    self.bullets[x] = (i[0], i[1]-BULLET_SPEED)
            except:
                pass
        self.w.blit(self.img, (self.x, self.y))
        self.text("HI-SCORE", (590, 50), 50)
        self.hi_score = json.load(open("score.json"))
        self.text(max(self.hi_score), (720, 90), 50)
        self.text("SCORE", (660, 130), 50)
        self.text(self.score, (720, 170), 50)
        if not self.start and not self.gameover:
            if self.state == 4:
                self.state = 0
            if self.state == 0:
                self.text(">Start<", (324, (HEIGHT//2)-60), 50)
            else:
                self.text("Start", (330, (HEIGHT//2)-60), 50)
            if self.state == 1:
                self.text(">Multiplayer<", (254, (HEIGHT//2)), 50)
            else:
                self.text("Multiplayer", (260, (HEIGHT//2)), 50)
            if self.state == 2:
                self.text(">Settings<", (294, (HEIGHT//2)+60), 50)
            else:
                self.text("Settings", (300, (HEIGHT//2)+60), 50)
        elif self.gameover:
            self.text("Press enter to restart", (150, HEIGHT//2-10), 50)
        if self.gameover:
            self.play_demo()
            self.text("Game Over", (WIDTH//2-120, HEIGHT//2-100), 50)
            self.hi_score.append(self.score)
            json.dump(self.hi_score, open("score.json", 'w'))


    def stat(self, b):
        if b:
            self.start = True
        elif b and self.start:
            self.start = False

    def test_bullet(self, abullets=[]):
        xp = self.x + self.size[0]
        yp = self.y + self.size[1]

        for i in abullets:
            x, y = i
            if self.x <= x and self.y <= y:
                if x <= xp and y <= yp:
                    self.start = False
                    self.gameover = True
                    self.blow(x, y)
                    break

    def change_bullet(self, data=False):
        if data:
            bullets, score = data
            self.bullets = bullets
            self.score += 1

            
    def move(self):
        keys = self.pygame.key.get_pressed()
        if keys[self.pygame.K_UP] and not self.start:
            self.state += 1
        if keys[self.pygame.K_ESCAPE]:
            sys.exit()
        if keys[self.pygame.K_UP] and self.start and self.movement == False and self.shoot == False:
            self.shoot = True
        if keys[self.pygame.K_SPACE] and self.start and self.movement == False and self.shoot == False:
            self.shoot = True
        if keys[self.pygame.K_RETURN] and self.gameover:
            self.score = 0
            self.x = SX
            self.y = SY
            self.stat(True)
            self.a.create()
            self.bullets = []
            self.gameover = False
        elif keys[self.pygame.K_RETURN]:
            self.stat(True)
        if keys[self.pygame.K_LEFT] and self.x >= SPEED and self.start:
            self.x -= SPEED
            self.movement = True
        elif keys[self.pygame.K_RIGHT] and self.x <= 530 and self.start:
            self.x += SPEED
            self.movement = True
        else:
            self.movement = False

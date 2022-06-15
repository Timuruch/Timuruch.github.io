from settings import *
import json
import pygame

class score_system:
    def __init__(self, w, pygame):
        self.w = w
        self.pygame = pygame
        self.numbers = [self.pygame.image.load("assets/numbers/zero.png"), self.pygame.image.load("assets/numbers/one.png"), self.pygame.image.load("assets/numbers/two.png"), self.pygame.image.load("assets/numbers/three.png"), self.pygame.image.load("assets/numbers/four.png"), self.pygame.image.load("assets/numbers/five.png"), self.pygame.image.load("assets/numbers/six.png"), self.pygame.image.load("assets/numbers/seven.png"), self.pygame.image.load("assets/numbers/eight.png"), self.pygame.image.load("assets/numbers/nine.png")]
        self.start = False
        self.score = 0
        f = open("score.json")
        try:
            self.scores = json.load(f)
        except:
            self.scores = []
        

    def draw_score(self):
        pass

    def restart(self):
        self.score = 0

    def save(self):
        f = open("score.json", "w")
        self.scores.append(self.score)
        json.dump(self.scores, f)
        f.close()

    def adder(self):
        if self.start:
            self.draw_score()
            self.score += 1
            l = len(str(self.score))
            s = str(self.score)
            y = 20
            x1 = 470
            for x in range(l):
                #print(x)
                self.w.blit(self.numbers[int(s[x-1])], (x1, y))
                x1 -= 10
        else:
            self.draw_score()
            l = len(str(self.score))
            s = str(self.score)
            y = 20
            x1 = 470
            for x in range(l):
                self.w.blit(self.numbers[int(s[x-1])], (x1, y))
                x1 -= 10
    
    def print_score(self, start):
        self.start = start
        #fnt = self.pygame.font.SysFont('Verdana', 30)
        #text = fnt.render(str(self.score), False, (0, 0, 0))
        #self.w.blit(text,(450,0))
        self.adder()

from settings import *
import random

class walls:
    def __init__(self, pygame, w):
        self.w = w
        self.pygame = pygame
        self.walls = []
        self.id = 0
    
    def generate(self):
        to_generate = (MAX_WALLS - len(self.walls)) // 2
        dist_plus = 0
        for x in range(to_generate):
            point = random.randint(SPACE_IN_BEETWEN, SPACE_IN_BEETWEN*2)
            y2 = point + SPACE_IN_BEETWEN

            list1 = [y2, WALL_X+dist_plus, HEIGHT-y2, self.id]
            self.id += 1
            list2 = [0, WALL_X+dist_plus, point, self.id]
            self.id += 1

            self.walls.append(list1)
            self.walls.append(list2)
            dist_plus += DISTANCE



    def draw(self, game):
        if game:
            if len(self.walls) < MAX_WALLS:
                self.generate()
            else:
                intenger = 0
                for i in range(len(self.walls)):
                    x = self.walls[i-intenger]
                    if x[1] <= 0-LENGHT:
                        del self.walls[i-intenger]
                        intenger += 1
                        #continue
                    else:
                        self.pygame.draw.rect(self.w, GREEN, (x[1], x[0], LENGHT, x[2]))
                        if x[0] == 0:
                            self.w.blit(self.pygame.image.load("paddle_down.png"), (x[1]-10, x[2]))
                        else:
                            self.w.blit(self.pygame.image.load("paddle.png"), (x[1]-10, x[0]-20))
                        self.walls[i-intenger] = [self.walls[i-intenger][0], self.walls[i-intenger][1]-SPEED, self.walls[i-intenger][2], self.walls[i-intenger][3]]
        else:
            for i in range(len(self.walls)):
                x = self.walls[i]
                if x[0] == 0:
                    self.w.blit(self.pygame.image.load("paddle_down.png"), (x[1]-10, x[2]))
                else:
                    self.w.blit(self.pygame.image.load("paddle.png"), (x[1]-10, x[0]-20))
                self.pygame.draw.rect(self.w, GREEN, (x[1], x[0], LENGHT, x[2]))

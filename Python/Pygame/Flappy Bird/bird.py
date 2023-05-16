from settings import *

class bird:
    def __init__(self, pygame, w):
        self.pygame = pygame
        self.w = w
        self.x = SPAWN_X
        self.y = SPAWN_Y
        self.counter = 0
        self.score = 0
        self.agree = False
        self.game = True
        self.exception = [0]
    
    def draw(self):
        self.y += FALL_SPEED
        if self.y >= HEIGHT-SIZE:
            self.y = HEIGHT-SIZE
        self.w.blit(self.pygame.image.load("bird.png"), (self.x-15, self.y-15))
    
    def test(self, walls):
        intenger = 0
        for x in walls:
            if x[0] == 0:
                if x[1]-10 <= self.x and x[1]+LENGHT+10 >= self.x:
                    if x[0] <= self.y and x[0]+x[2]+20 >= self.y:
                        self.game = False
            else:
                if x[1]-10 <= self.x and x[1]+LENGHT+10 >= self.x:
                    if x[0]-20 <= self.y and x[0]+x[2] >= self.y:
                        self.game = False

            for i in range(len(self.exception)):
                y = self.exception[i-intenger]
                if self.x > x[1]+20 and self.game and y != x[3]:
                    print(y, x[3])
                    self.score += 1
                    self.exception.append(x[3])


    def jump(self):
        if self.counter < CURIOSITY and self.y > AIR_BLOCK:
            if self.agree:
                self.y -= JUMP_PER_FRAME
                self.counter += 1
        elif self.counter == CURIOSITY or self.y <= AIR_BLOCK:
            self.counter = 0
            self.agree = False
        
        if self.y == HEIGHT-SIZE and self.game:
            self.game = False    
    
    def move(self):
        keys = self.pygame.key.get_pressed()

        if keys [self.pygame.K_UP] and self.y > 0 and self.game and self.y >= 0:
            self.agree = True
        if keys[self.pygame.K_SPACE] and self.y > 0 and self.game and self.game and self.y >= 0:
            self.agree = True
        if keys[self.pygame.K_ESCAPE]:
            self.pygame.quit()
        
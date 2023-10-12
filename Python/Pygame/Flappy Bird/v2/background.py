from settings import *

class background:
    def __init__(self, pygame, w):
        self.w = w
        self.pygame = pygame
        self.x = BG_SPAWN_X
        self.y = BG_SPAWN_Y
        self.x_t = WIDTH

    def draw(self):
        self.w.blit(self.pygame.image.load("bg.png"), (self.x, self.y))
        self.w.blit(self.pygame.image.load("bg.png"), (self.x_t, self.y))
        if self.x <= -WIDTH:
            self.x = BG_NEW_SPAWN_X
        if self.x_t <= -WIDTH:
            self.x_t = BG_NEW_SPAWN_X
        self.x -= BG_SPEED
        self.x_t -= BG_SPEED
from settings import *

class bird:
    def __init__(self, p, w):
        self.w = w
        self.pygame = p
        self.x = 225
        self.y = 250
        self.tick = 100
        self.jump = 0
    
    def draw(self):
        self.tick += 1
        self.w.blit(self.pygame.image.load("bird.png").convert_alpha(), (self.x, self.y))
        if self.jump > 0:
            self.y -= JUMP // JUMP_COEFF
            self.jump -= 1
        if self.y < 500-36:
            self.y += FALL_SPEED
            return True
        else:
            return False
    
    def move(self):
        k = self.pygame.key.get_pressed()

        if k[self.pygame.K_UP] and self.y > 0 and self.tick >= TICK and self.jump <= 1:
            self.jump = JUMP_COEFF
            self.tick = 0

    
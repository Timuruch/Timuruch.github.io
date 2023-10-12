from settings import *

class debug:
    def __init__(self, w, pygame, clock):
        self.w = w
        self.pygame = pygame
        self.clock = clock
    
    def text(self, text, pos, size):
        fnt = self.pygame.font.Font('Fixedsys.ttf', size)
        text = fnt.render(str(text), False, (0, 0, 0))
        self.w.blit(text, pos)
    
    def draw(self):
        self.text(int(self.clock.get_fps()), (SIZE, SIZE), SIZE)
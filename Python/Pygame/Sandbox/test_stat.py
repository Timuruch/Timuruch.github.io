from settings import *
import sys

class stat:
    def __init__(self, p, w, c):
        self.w = w
        self.p = p
        self.c = c
    
    def text(self, text, pos, size):
        fnt = self.p.font.Font('Fixedsys.ttf', size)
        text = fnt.render(str(text), False, WHITE)
        self.w.blit(text, pos)
    
    def draw(self):
        if PERMISSION:
            self.text(str(int(self.c.get_fps())), (WIDTH-20, 0), 20)

    def keys(self):
        keys = self.p.key.get_pressed()
        if keys[self.p.K_ESCAPE]:
            sys.exit()
    

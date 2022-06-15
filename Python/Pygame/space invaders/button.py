from settings import *
import pygame

class button:
    def __init__(self, pygame, w, x, y, image, img_size):
        self.pygame = pygame
        self.w = w
        self.pos = (x ,y)
        self.image = self.pygame.image.load(image)
        self.img_size = img_size
        self.show = True
    def draw(self):
        if self.show:
            self.w.blit(self.image, self.pos)
    def change_state(self):
        if self.show:
            self.show = False
        else:
            self.show = True
    
    def change_state_by_bool(self, bool):
        if bool:
            if self.show:
                self.show = False
            else:
                self.show = True
        return bool

    def test_click(self, click_pos):
        x, y = self.pos
        xc, yc = click_pos
        x2 = x + self.img_size[0]
        y2 = y + self.img_size[1]
        if yc <= y2 and self.show:
            if yc >= y:
                if xc <= x2:
                    if xc >= self.img_size[0]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
        
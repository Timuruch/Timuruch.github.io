import pygame
from background import *
from debug import *
from settings import *

pygame.init()
w = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

d = debug(w, pygame, clock)
bg = background(pygame, w)
y = True

while y:
    for x in pygame.event.get():
        if x.type == pygame.QUIT:
            y = False
            break
    
    w.fill((255, 255, 255))
    
    bg.draw()

    d.draw()
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()    
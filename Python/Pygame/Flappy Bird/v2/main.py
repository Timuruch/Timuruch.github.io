import pygame
from background import *
from debug import *
from bird import *
from settings import *

pygame.init()
w = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

d = debug(w, pygame, clock)
bg = background(pygame, w)
b = bird(pygame, w)
y = True

while y:
    for x in pygame.event.get():
        if x.type == pygame.QUIT:
            y = False
            break
    
    w.fill((255, 255, 255))
    
    bg.draw()
    bg.run = b.draw()
    b.move()

    d.draw()
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()    
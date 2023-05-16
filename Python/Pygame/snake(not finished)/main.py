from settings import *
from food import *
from snake import *
import pygame

pygame.init()
w = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

s = snake(pygame, w)
f = food(pygame, w)
f.create()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    w.fill(BG_COLOR)

    f.draw()
    s.draw()
    s.move()
    s.refresh(f.refresh(s.buffer[0]))

    pygame.display.update()
    pygame.time.Clock().tick(FPS)

pygame.quit()
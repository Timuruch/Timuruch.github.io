from settings import *
from map import *
from player import *
import pygame

pygame.init()
w = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

m = Map(w, pygame)
p = player(w, pygame, m.get_walls())

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    w.fill(RED)

    m.draw()
    p.draw()
    p.check_touch()
    p.move()

    try:
        pygame.display.update()
        pygame.time.Clock().tick(FPS)
    except:
        pass

pygame.quit()
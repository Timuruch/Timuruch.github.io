from test_stat import *
from settings import *
from world import *
import pygame
import sys

pygame.init()
c = pygame.time.Clock()
w = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

wrld = world(w, pygame)
info = stat(pygame, w, c)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    w.fill(BLACK)

    info.keys()

    wrld.draw()
    info.draw()

    pygame.display.flip()
    c.tick(FPS)
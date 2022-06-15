from re import T
from settings import *
from floor import *
from Dino import *
from threading import *
import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()
w = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

d = dino(w, pygame)
f = floor(w, pygame)
b = border(w, pygame)

t1 = pygame.time.get_ticks()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if d.click(event.pos):
                b.restart()
                f.restart()
    t2 = pygame.time.get_ticks()
    
    t = t2 - t1
    if t >= 2000:
        b.create(d.start)
        t1 = t2

    w.fill(WHITE)
    d.move()
    f.draw(d.start, d.get_pos())
    b.draw(d.start, d.get_pos())
    d.stop(b.stop)
    #Thread(target=d.draw).start()
    d.draw()

    pygame.display.update()
    pygame.time.delay(DELAY)
    #pygame.time.Clock().tick(60)

pygame.quit()
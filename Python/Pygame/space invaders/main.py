from settings import *
from aliens import *
from starship import *
import pygame

pygame.init()
w = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

bg = pygame.image.load("assets/backgrounds/bg.png")
s = starship(pygame, w, "assets/starships/starship.png", (50, 54))
a = aliens(pygame, w)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    w.blit(bg, (0,0))

    #s.play_demo()
    a.draw(s.start)
    s.draw()
    s.test_bullet(a.bullets)
    s.move()
    s.change_bullet(a.test_bullet(s.bullets))

    pygame.display.update()
    pygame.time.Clock().tick(FPS)

pygame.quit()
from settings import *
from button import *
from aliens import *
from starship import *
import pygame

pygame.init()
w = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

#play_button = button(pygame, w, 325, 230, "assets/buttons/play.png", (150, 45))
#mp_button = button(pygame, w, 325, 280, "assets/buttons/play.png", (150, 45))#multiplayer button
#exit_button = button(pygame, w, 325, 330, "assets/buttons/exit.png", (150, 45))
bg = pygame.image.load("assets/backgrounds/bg.png")
s = starship(pygame, w, "assets/starships/starship.png", (50, 54))
a = aliens(pygame, w)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #s.stat(exit_button.change_state_by_bool(mp_button.change_state_by_bool(play_button.change_state_by_bool(play_button.test_click(event.pos)))))

    #w.fill(WHITE)
    w.blit(bg, (0,0))

    #s.play_demo()
    a.draw(s.start)
    s.draw()
    s.test_bullet(a.bullets)
    s.move()
    #play_button.draw()
    #mp_button.draw()
    #exit_button.draw()
    s.change_bullet(a.test_bullet(s.bullets, s.score))

    pygame.display.update()
    pygame.time.Clock().tick(FPS)

pygame.quit()
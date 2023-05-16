from threading import *
from settings import *
from bird import *
from menu import *
from walls import *
import pygame 

pygame.init()
w = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

b = bird(pygame, w)
ws = walls(pygame, w)
m = Menu(pygame, w)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    w.fill(WHITE)
    m.draw(b.game)
    Thread(target=b.test, args=(ws.walls, )).start()
    b.move()
    b.jump()
    ws.draw(b.game)
    m.draw_stats(b.game, b.score)
    b.draw()

    clock.tick(60)
    m.text(str(int(clock.get_fps())), (WIDTH-30, 10), 20)

    pygame.display.update()

pygame.quit()
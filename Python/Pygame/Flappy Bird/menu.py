from settings import *

class Menu:
    def __init__(self, pygame, w):
          self.pygame = pygame
          self.w = w
          self.bg_coords = (0, 0)

    def text(self, text, pos, size):
        fnt = self.pygame.font.Font('Fixedsys.ttf', size)
        text = fnt.render(str(text), False, (0, 0, 0))
        self.w.blit(text, pos)
    
    def calculate(self, game):
        x, y = self.bg_coords
        if x <= BG_ENDPOINT:
            self.w.blit(self.pygame.image.load("bg.png"), (self.bg_coords[0]+BG_WIDTH-2, 0))
        if x == -BG_WIDTH:
            x = 0
            y = 0
        if game:
            x -= BG_SPEED
        self.bg_coords = (x, y)
    
    def draw(self, game):
        self.calculate(game)
        self.w.blit(self.pygame.image.load("bg.png"), self.bg_coords)
    
    def draw_stats(self, game, score):
        if not game:
            self.text("GAME OVER", (WIDTH//2-100, HEIGHT//2-50), 50)
        self.text(str(score), (10, 10), 50)
            
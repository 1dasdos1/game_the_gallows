import pygame as pg
import random

WIDTH = 700
HEIGHT = 610
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (225, 225, 225)
GREEN = (225, 225, 225)
BLUE = (225, 225, 255)

T = 4

def line(color, x1, y1, x2, y2, thickness):
    pg.draw.line(screen, color, (x1, y1), (x2, y2), thickness)

# -------init pygame--------------
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")
clock = pg.time.Clock()

# -------/init pygame--------------

running = True
while running:
    screen.fill(WHITE)
    clock.tick(FPS)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    

   
    line(BLACK, 200, 10, 200, 400, T)
    line(BLACK, 200, 10, 400, 10, T)
    line(BLACK, 400, 10, 400, 100, T)
    
    pg.display.flip()
    
pg.quit()

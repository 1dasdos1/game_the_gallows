import pygame as pg
import random as rnd

WIDTH = 700
HEIGHT = 610
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (225, 225, 225)
GREEN = (225, 225, 225)
BLUE = (225, 225, 255)

NULL = 0
WRONG = 1
RIGHT = 2

LINE_WIDTH = 4
CIRCLE_WIDTH = 4

keyboard = {102: "А", 44: "Б", 100: "В", 117: "Г", 108: "Д", 116: "Е", 96: "Ё", 59: "Ж", 112: "З", 98: "И", 113: "Й",
114: "К", 107: "Л", 118: "М", 121: "Н", 106: "О", 103: "П", 104: "Р", 99: "С", 110: "Т", 101: "У", 97: "Ф", 1093: "Х", 
119: "Ц", 120: "Ч", 105: "Ш", 111: "Щ", 1098: "Ъ", 115: "Ы", 109: "Ь", 1101: "Э", 1102: "Ю", 122: "Я"}

words = ['кот', 'сок']
n = rnd.choice(words)
#


def line(color, x1, y1, x2, y2, thickness):
    pg.draw.line(screen, color, (x1, y1), (x2, y2), thickness)
#def circle(color,)

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
        if event.type == pg.KEYDOWN:
            print(event.key)
        l = keys[event.key]
        spots = []
        print (event.key, l)

        for i, s in enumerate(n)
        if l == s:
            spots.append(i)
            user_symbols.append(i)
            if len(spots) > 0: choice = RIGHT
            else: choice = WRONG
        
    line(BLACK, 200, 10, 200, 300, LINE_WIDTH)
    line(BLACK, 200, 10, 330, 10, LINE_WIDTH)
    line(BLACK, 330, 10, 330, 60, LINE_WIDTH)
    
    pg.display.flip()
    
pg.quit()

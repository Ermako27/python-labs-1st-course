import pygame
from pygame.locals import *
from math import pi, cos, sin

pygame.init()
(windows_width, windows_height, windows_title) = (1200, 600, 'Truck')

screen = pygame.display.set_mode((windows_width, windows_height), 0, 32)
pygame.display.set_caption(windows_title)
window_bgcolor = (72,155,228)
clock = pygame.time.Clock()

def earth():
    pygame.draw.rect(screen, (54,186,50), ((0, 500), (1200, 600)), 0)

def truck(x):
    pygame.draw.rect(screen, (85, 107, 47), ((100 + x, 300), (300, 150)), 0)
    pygame.draw.rect(screen, (155, 140, 0), ((100 + x, 420), (300, 30)), 0)
    pygame.draw.rect(screen, (139, 69, 19), ((400 + x, 340), (100, 100)), 0)
    pygame.draw.rect(screen, (0, 0, 139), ((450 + x, 340), (50, 50)), 0)
    pygame.draw.circle(screen, (0, 0, 0), (470 + x, 355), 10, 0)
    pygame.draw.line(screen, (0, 0, 0), (470 + x, 355), (470 + x, 388), 4)

    #pygame.draw.line(screen, (0,0,0),(),(425,295))
    pygame.draw.circle(screen, (0, 0, 0), (150 + x, 475), 40, 0)
    pygame.draw.circle(screen, (0, 0, 0), (290 + x, 475), 40, 0)
    pygame.draw.circle(screen, (0, 0, 0), (430 + x, 475), 40, 0)
    pygame.draw.circle(screen, (105, 105, 105), (150 + x, 475), 25, 0)
    pygame.draw.circle(screen, (105, 105, 105), (290 + x, 475), 25, 0)
    pygame.draw.circle(screen, (105, 105, 105), (430 + x, 475), 25, 0)
    pygame.draw.line(screen, (0, 0, 0),
                     (37 * cos(teta1 + pi / 2) + x + 150, 475 + 37 * sin(teta1 + pi / 2)),
                     (37 * cos(teta2 - pi / 2) + x + 150, 475 + 37 * sin(teta2 - pi / 2)), 4)
    pygame.draw.line(screen, (0, 0, 0),
                     (37 * cos(teta1 + pi) + x + 150, 475 + 37 * sin(teta1 + pi)),
                     (37 * cos(teta2) + x + 150, 475 + 37 * sin(teta2)), 4)
    pygame.draw.line(screen, (0, 0, 0),
                     (37 * cos(teta1 + pi / 2) + x + 290, 475 + 37 * sin(teta1 + pi / 2)),
                     (37 * cos(teta2 - pi / 2) + x + 290, 475 + 37 * sin(teta2 - pi / 2)), 4)
    pygame.draw.line(screen, (0, 0, 0),
                     (37 * cos(teta1 + pi) + x + 290, 475 + 37 * sin(teta1 + pi)),
                     (37 * cos(teta2) + x + 290, 475 + 37 * sin(teta2)), 4)
    pygame.draw.line(screen, (0, 0, 0),
                     (37 * cos(teta1 + pi / 2) + x + 430, 475 + 37 * sin(teta1 + pi / 2)),
                     (37 * cos(teta2 - pi / 2) + x + 430, 475 + 37 * sin(teta2 - pi / 2)), 4)
    pygame.draw.line(screen, (0, 0, 0),
                     (37 * cos(teta1 + pi) + x + 430, 475 + 37 * sin(teta1 + pi)),
                     (37 * cos(teta2) + x + 430, 475 + 37 * sin(teta2)), 4)



def sun(x):
    pygame.draw.line(screen, (255, 215, 0), (20+x, 20), (40+x, 40), 4)
    pygame.draw.line(screen, (255, 215, 0), (55+x, 10), (55+x, 30), 4)
    pygame.draw.line(screen, (255, 215, 0), (90+x, 20), (70+x, 40), 4)
    pygame.draw.line(screen, (255, 215, 0), (100+x, 52), (70+x, 52), 4)
    pygame.draw.line(screen, (255, 215, 0), (12+x, 52), (70+x, 52), 4)
    pygame.draw.line(screen, (255, 215, 0), (22+x, 84), (53+x, 53), 4)
    pygame.draw.line(screen, (255, 215, 0), (55+x, 93), (55+x, 30), 4)
    pygame.draw.line(screen, (255, 215, 0), (90+x, 84), (65+x, 59), 4)
    pygame.draw.circle(screen, (255, 215, 0), (57+x, 50), 22, 0)

def obl(x3,y1):
    pygame.draw.ellipse(screen,(240, 255, 255),((50+x3,15+y1),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((100+x3,40+y1),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((50+x3,65+y1),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((0+x3,40+y1),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((20+x3,55+y1),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((20+x3,30+y1),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((85+x3,30+y1),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((85+x3,55+y1),(100,40)),0)


x = -500
x_s = -300
x_c1 = 150
y_c1 = 475
x_c2 = 330
y_c2 = 475
teta = 0
teta1 = 0
teta2 = 0
y1 = 30
x3 = -200

mainLoop = True
while mainLoop:
    for event in pygame.event.get():
        if event.type == QUIT:
            mainLoop = False
    screen.fill(window_bgcolor)
    sun(x_s)
    earth()
    x += 5
    x_s += 2
    x3 += 5
    truck(x)
    obl(x3, y1)
    if x_s > 1300:
        x_s = -300
    if x > 1300:
        x = -500
    if x3 == 1400:
        x3 = -200

    milli = clock.tick(50)
    sec = milli / 500.0

    teta += sec * pi / 12
    teta1 += 3 * sec * pi / 4
    teta2 += 3 * sec * pi / 4


    pygame.display.update()
    clock.tick(50)
pygame.quit()

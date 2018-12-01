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

def obl1(x1,y1):
    pygame.draw.ellipse(screen,(240, 255, 255),((50+x1,15+y1),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((100+x1,40+y1),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((50+x1,65+y1),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((0+x1,40+y1),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((20+x1,55+y1),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((20+x1,30+y1),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((85+x1,30+y1),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((85+x1,55+y1),(100,40)),0)

def obl2(x2,y2):
    pygame.draw.ellipse(screen,(240, 255, 255),((50+x2,15+y2),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((100+x2,40+y2),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((50+x2,65+y2),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((0+x2,40+y2),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((20+x2,55+y2),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((20+x2,30+y2),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((85+x2,30+y2),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((85+x2,55+y2),(100,40)),0)

def obl3(x3,y3):
    pygame.draw.ellipse(screen,(240, 255, 255),((50+x3,15+y3),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((100+x3,40+y3),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((50+x3,65+y3),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((0+x3,40+y3),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((20+x3,55+y3),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((20+x3,30+y3),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((85+x3,30+y3),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((85+x3,55+y3),(100,40)),0)

def sun(x, y,):
    pygame.draw.line(screen, (255, 215, 0), (20+x, 20+y), (40+x, 40+y), 4)
    pygame.draw.line(screen, (255, 215, 0), (55+x, 10+y), (55+x, 30+y), 4)
    pygame.draw.line(screen, (255, 215, 0), (90+x, 20+y), (70+x, 40+y), 4)
    pygame.draw.line(screen, (255, 215, 0), (100+x, 52+y), (70+x, 52+y), 4)
    pygame.draw.line(screen, (255, 215, 0), (12+x, 52+y), (70+x, 52+y), 4)
    pygame.draw.line(screen, (255, 215, 0), (22+x, 84+y), (53+x, 53+y), 4)
    pygame.draw.line(screen, (255, 215, 0), (55+x, 93+y), (55+x, 30+y), 4)
    pygame.draw.line(screen, (255, 215, 0), (90+x, 84+y), (65+x, 59+y), 4)
    pygame.draw.circle(screen, (255, 215, 0), (57+x, 50+y), 22, 0)

def home(color):
    pygame.draw.rect(screen, (85, 107, 47), ((400, 450), (200, 200)), 0)
    pygame.draw.polygon(screen, (0,0,0), ((400, 450), (500, 350), (600, 450)), 0)
    pygame.draw.rect(screen, color, ((500, 500), (50, 50)), 0)




x1 = x2 = -200
y1 = 10
y2 = 200
x3 = 1400
y3 = 100
c = 0
fi = pi/2
x_s = -200
y_s = 110 + int(10*sin(fi))
mainLoop = True
while mainLoop:
    for event in pygame.event.get():
        if event.type == QUIT:
            mainLoop = False
    screen.fill(window_bgcolor)
    earth()
    #home(c)
    sun(x_s,y_s)
    x1 += 1
    x2 += 1
    x3 -= 1

    x_s += 1
    fi += pi/60
    y_s = 110 + int(100 * sin(fi))
    obl1(x1,y1)
    obl2(x2,y2)
    obl3(x3,y3)





    if 190 <= y_s <= 210:
            home((255,255,255))
    elif 10 <= y_s <= 30:

        home((255,255,255))
    #elif 100 <= y_s <= 120:
     #   home((255,255,255))
    else:
        home((0,0,0))



    if x3 < -200:
        x3 = 1400
    if x1 > 1400:
        x1 = -200
    if x2 > 1400:
        x2 = -200
    if x_s > 1400:
        x_s = -200



    pygame.display.update()
    clock.tick(50)
pygame.quit()
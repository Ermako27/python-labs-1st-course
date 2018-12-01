import pygame, sys
from pygame.locals import *
import math
 
pygame.init()
(windows_width, windows_height, windows_title) = (1200, 600, 'Tank')
 
screen = pygame.display.set_mode((windows_width, windows_height), 0, 32)
pygame.display.set_caption(windows_title)
window_bgcolor = (72,155,228)
clock = pygame.time.Clock()
 
def earth():
    pygame.draw.rect(screen, (54,186,49),((0,500),(1200,100)), 0)
def tank (x):
    pygame.draw.ellipse(screen, (19,41,4), ((450+x,300),(75,50)), 0)
    pygame.draw.rect(screen, (23,40,11),((225+x,350),(200,25)), 0)
    pygame.draw.polygon(screen, (46,82,21), ((375+x,400),(425+x,325),(550+x,325),(600+x,400)), 0)
    pygame.draw.ellipse(screen, (24,43,10), ((300+x,425),(402,275)), 0)
    pygame.draw.circle(screen, (21,23,20), (320+x,555), 45, 0)
    pygame.draw.circle(screen, (21,23,20), (500+x,555), 45, 0)
    pygame.draw.circle(screen, (21,23,20), (680+x,555), 45, 0)
    pygame.draw.polygon(screen, (37,64,18), ((250+x,530),(325+x,400),(650+x,400),(750+x,530)), 0)
def pula (x1):
    pygame.draw.rect(screen, (53,56,50),((100+x1,350),(50,25)), 0)
    pygame.draw.polygon(screen, (41,43,34), ((75+x1,362),(100+x1,350),(100+x1,374)), 0)
def olen(x7,r):
    pygame.draw.rect(screen, (85,58,21),((830+x7,365),(40,100)), 0)
    pygame.draw.line(screen, (205,144,59), (765+x7,250), (785+x7,345),5)
    pygame.draw.line(screen, (205,144,59), (900+x7,250), (850+x7,345),5)    
    pygame.draw.ellipse(screen, (85,58,21), ((750+x7,325),(125,70)), 0)
    pygame.draw.ellipse(screen, (85,58,21), ((830+x7,425),(250,85)), 0)
    pygame.draw.circle(screen, (85,58,21), (1075+x7,435), 22, 0)
 
    az = 0
    for i in range(4):
        if r%2==0:  
            pygame.draw.line(screen, (85,58,21), (880+az+x7,470), (890+az+x7,540),9)
        else:
            pygame.draw.line(screen, (85,58,21), (880+az+x7,470), (870+az+x7,540),9)
 
        az+=50
 
def tarelka(x2,y):
    pygame.draw.circle(screen, (28,122,238), (925+x2,135+y), 65, 0)
    az=0
    pygame.draw.ellipse(screen, (36,60,89), ((775+x2,135+y),(300,100)), 0)
    for i in range(3):  
        pygame.draw.circle(screen, (157,215,215), (830+x2+az,185+y), 20, 0)
        az+=100    
 
 
def sun ():
    # ������
    pygame.draw.line(screen, (255, 215, 0), (20,20),(40,40),4)
    pygame.draw.line(screen, (255, 215, 0), (55,10),(55,30),4)
    pygame.draw.line(screen, (255, 215, 0), (90,20),(70,40),4)
    pygame.draw.line(screen, (255, 215, 0), (100,52),(70,52),4)
    pygame.draw.line(screen, (255, 215, 0), (12,52),(70,52),4)
    pygame.draw.line(screen, (255, 215, 0), (22,84),(53,53),4)
    pygame.draw.line(screen, (255, 215, 0), (55,93),(55,30),4)
 
    pygame.draw.line(screen, (255, 215, 0), (90,84),(65,59),4)
    pygame.draw.circle(screen, (255, 215, 0), (57,50), 22, 0)
def obl(x3,y1):
    pygame.draw.ellipse(screen,(240, 255, 255),((50+x3,15+y1),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((100+x3,40+y1),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((50+x3,65+y1),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((0+x3,40+y1),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((20+x3,55+y1),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((20+x3,30+y1),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((85+x3,30+y1),(100,40)),0)
    pygame.draw.ellipse(screen,(240, 255, 255),((85+x3,55+y1),(100,40)),0)
 
 
 
 
 
 
r = 0
x = 975
y = 0
x1 = 800
y1 = 30
x2 = 1000
x3 = -200
x7 = 1200
mainLoop = True
while mainLoop:
    for event in pygame.event.get():
        if event.type == QUIT:
            mainLoop = False
    screen.fill(window_bgcolor) # ����
    sun ()
    earth() # �����
    x-=3
    if x < 600:
        pula (x1)
        x1-=10
    tank(x)
    if x > 50:
        x2-=5
    elif x>20:
        x2-=0
    else:
        x2+=12
        y-=7
    x3+=1
    obl(x3,y1)
    tarelka(x2,y)
    olen(x7,r)
    x7-=3
    r+=1
 
 
    if x < - 900:
        x = 975
        y = 0
        x1 = 775
        x2 = 1000
 
    if x3 == 1400:
        x3 = -200
    if x7 < - 1200:
        x7 = 700
 
 
 
 
    pygame.display.update()
   
   
    clock.tick(100)
pygame.quit()

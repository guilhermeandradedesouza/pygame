import pygame
from random import randint,sample
from pygame.locals import *
from pygame.draw import *
pygame.init()
cores=sample(('red','blue','yellow','orange','green',(5,100,10),(76,0,155),(10,57,30),(128,128,0),(127,255,0),(0,255,255),(139,69,19)),12)
tela=pygame.display.set_mode((700,550))
pygame.display.set_caption('tv parada.')
direcao=cor=x=y=0
mult,pos_x,pos_y=(1,-1),335,210
while True:
    pygame.time.Clock().tick(60)
    tela.fill('black')
    rect(tela,cores[cor%12],(pos_x,pos_y,30,30),0,20)
    for evento in pygame.event.get():
        if evento.type==QUIT:exit()
    if x==0 or y==0:x,y=randint(0,1)*mult[randint(0,1)],randint(0,1)*mult[randint(0,1)]
    elif pos_x==670 or pos_x==0:x=-1 if pos_x==670 else 1
    elif pos_y==0 or pos_y==520:y=-1 if pos_y==520 else 1
    pos_x+=x
    pos_y+=y
    pygame.display.update()
    if pos_x==0 or pos_x==670 or pos_y==0 or pos_y==520:cor+=1
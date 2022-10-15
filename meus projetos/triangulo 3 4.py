from time import time
from random import choice,randint
from keyboard import is_pressed as pressed
from pygame.draw import polygon,lines
from pygame.gfxdraw import pixel as px
from pygame import QUIT
import pygame
pygame.init()
tam=(800,600)
tela=pygame.display.set_mode(tam)
vertices=((tam[0]*7//10,tam[1]//2),(tam[0]*3//10,tam[1]//2),(tam[0]//2,tam[1]*7//8))
vertice,pixel=choice(vertices),[(randint(200,300), randint(200,300),(0,0,255))]
while True:
    tempo=time()
    tela.fill('white')
    for evento in pygame.event.get():
        if evento.type==QUIT:exit()
    vertice=choice(vertices)
    if pressed('w'):
        pygame.time.wait(10**2)
        cor=(255,0,0)
    else:cor=(0,0,255)
    ponto=((vertice[0]-pixel[-1][0]+tam[0])/2,(tam[1]-vertice[1]+pixel[-1][1])/2,cor)
    if not pressed('space'):lines(tela,'green',0,((pixel[-1][0],pixel[-1][1]),(pixel[-1][0], ponto[1]), (ponto[0],ponto[1])),2)
    pixel.append(ponto)
    polygon(tela,'black',((tam[0]*3//10,tam[1]//2),(tam[0]*7//10,tam[1]//2),(tam[0]//2,tam[1]//8)),1)
    for X_Y in pixel:px(tela,int(X_Y[0]),int(X_Y[1]),X_Y[2])
    pygame.display.flip()
    if pressed('p'):pygame.image.save(tela,'screenshot.jpg')
    print(f'demorou {time()-tempo:.6f} segundos,{"muito." if time()-tempo>=.075 else "normal"}')
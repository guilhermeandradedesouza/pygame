import pygame
from random import choice,randint
from pygame import QUIT
from pygame.gfxdraw import pixel,rectangle
tam=600
vertices=((tam//8,tam//8),(tam//8,tam*7//8-1),(tam*7//8-1,tam*7//8-1),(tam*7//8-1,tam//8))
pontos=[(randint(vertices[0][0],vertices[3][1]),randint(vertices[0][1],vertices[3][1]))]
tela=pygame.display.set_mode((tam,tam))
vertice=choice(vertices)
while True:
    repetido=vertice
    tela.fill('white')
    for evento in pygame.event.get():
        if evento.type==QUIT:exit()
    rectangle(tela,(tam//8,tam//8,tam*6//8,tam*6//8),(0,0,0))
    while vertice==repetido:vertice=choice(vertices)
    pontos.append(((vertice[0]-pontos[-1][0]+tam)//2,(vertice[1]-pontos[-1][1]+tam)//2))
    for x_y in pontos:pixel(tela,x_y[0],x_y[1],(255,0,125))
    pygame.display.flip()
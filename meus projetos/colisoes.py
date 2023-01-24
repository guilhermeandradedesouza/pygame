import pygame
from pygame import QUIT
from random import choice
from pygame.draw import rect
tela=pygame.display.set_mode((600,500))
x=y=250
c=[200,400]
add=1
v={'x':choice((2,-2)),'y':choice((2,-2))}
cor=choice(('red','green','blue','brown','yellow','black'))
while QUIT not in (evento.type for evento in pygame.event.get()):
    tela.fill('gray')
    pygame.time.Clock().tick(60)
    colidir=rect(tela,'orange',tuple(c)+(160,60))
    if x%550==y%450==0:
        for _ in v:v[_]=-v[_]
    elif x%550==0 or y%450==0:v['x' if x%550==0 else 'y'],cor=-v['x' if x%550==0 else 'y'],choice(('red','green','blue','brown','yellow','black'))
    x+=v['x']
    y+=v['y']
    add=-add if c[1]%440==0 else add
    c[1]+=add
    pygame.display.flip()
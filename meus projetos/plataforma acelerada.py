import pygame
from pygame import QUIT
from pygame.draw import rect
from pygame.mouse import get_pos
tela=pygame.display.set_mode((500,500))
x=250
aceleracao=0
while QUIT not in (evento.type for evento in pygame.event.get()):
    tela.fill('white')
    if int(x)!=get_pos()[0] and 460>=get_pos()[0]>=40:aceleracao+=.1 if get_pos()[0]>x else -.1
    x+=aceleracao
    aceleracao=0 if int(aceleracao) in (1,-1) or int(x) in (get_pos()[0],460,40) else aceleracao
    for num,_ in enumerate(((int(x)-40,400,80,26),(int(x)-25,405,50,16))):rect(tela,('red','gray')[num],_,0,10)
    pygame.display.flip()
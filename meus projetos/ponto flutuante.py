import pygame
from pygame import QUIT
from pygame.draw import circle
from pygame.mouse import get_pos as pos
tela=pygame.display.set_mode()
x,y=pos()
while QUIT not in (evento.type for evento in pygame.event.get()):
    tela.fill('white')
    circle(tela,'black',(x, y),7)
    x+=(pos()[0]-x)/250
    y+=(pos()[1]-y)/250
    pygame.display.flip()
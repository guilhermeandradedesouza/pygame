import pygame
from pygame import QUIT
from pygame.draw import circle
tela=pygame.display.set_mode((600,600))
while QUIT not in (evento.type for evento in pygame.event.get()):
    tela.fill('white')
    circle(tela,)
    pygame.display.flip()
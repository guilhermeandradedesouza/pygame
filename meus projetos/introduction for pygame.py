import pygame
from pygame import QUIT
tela=pygame.display.set_mode((500,500))
surface=pygame.Surface((100,200))
while QUIT not in (evento.type for evento in pygame.event.get()):
    surface.fill('red')
    tela.blit(surface,(200,100))
    pygame.display.flip()
from pygame.locals import *
import pygame
a=1
pygame.init()
tela=pygame.display.set_mode((920,700))
pygame.display.set_caption('teste')
while 1:
    pygame.time.Clock().tick(30)
    tela.fill('black')
    for evento in pygame.event.get():
        if evento.type==QUIT:exit()
        if pygame.key.get_pressed()[K_a]:tela.fill('blue')
        elif pygame.key.get_pressed()[K_d]:tela.fill('white')
        else:
            print(f'parada {a}')
            a+=1
    pygame.display.flip()
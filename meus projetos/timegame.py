import pygame
from pygame import QUIT,K_SPACE
from pygame.draw import rect,polygon
from pygame.surface import Surface
from pygame.key import get_pressed as pressed
from random import randint,uniform,choice
tela=pygame.display.set_mode()
width,height=tela.get_size()
obj=Surface((40,80))
obj.fill('yellow')
obj.set_alpha(150)
velocidade=.5
pos=[randint((width-285)//2+5,(width-285)//2+275-40),(height-80)/2]
ponteiro=[width/2,height*22.7/43]
direcao=choice((1,-1))*velocidade
precionado=True
while QUIT not in (evento.type for evento in pygame.event.get()):
    tela.fill('black')
    surf_rect=obj.get_rect(topleft=pos)
    tela.blit(obj,surf_rect)
    rect(tela,'white',((width-285)/2,(height-90)/2,285,90),5,12)
    if int(ponteiro[0]) in ((width-285)//2+5,(width-285)//2+275):direcao=-direcao
    polygon(tela,'green',(ponteiro,(ponteiro[0]-15,ponteiro[1]+50),(ponteiro[0]+15,ponteiro[1]+50)),3)
    if surf_rect.collidepoint(ponteiro) and pressed()[K_SPACE] and precionado:
        if direcao<0:lins=ponteiro[0],(width-285)//2+275-40
        else:lins=(width-285)//2+5,ponteiro[0]
        pos=[uniform(*lins),(height-80)/2]
    precionado=not pressed()[K_SPACE]
    ponteiro[0]+=direcao
    pygame.display.flip()
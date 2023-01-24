import pygame
from pygame import time,image,font,display,draw
from pygame import QUIT
pygame.init()
tela=display.set_mode((800,400))
#movimento,direcao=0,2
x=800
sky,ground=image.load('Sky.png').convert(),image.load('ground.png').convert()
while QUIT not in (evento.type for evento in pygame.event.get()):
    time.Clock().tick(100)
    for num,mostrar in enumerate((sky,ground)):tela.blit(mostrar,((0,0),(0,300))[num])
    tela.blit(font.Font('Pixeltype.ttf',50).render('Jogo',True,'black'),(360,60))
    draw.rect(tela,'red',(x%850-50,250,50,50))
    x-=2
    #direcao=-direcao if movimento in (50,-50) else direcao
    #movimento+=direcao
    display.flip()
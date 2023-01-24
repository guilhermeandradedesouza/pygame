import pygame
from pygame.draw import rect,circle
from pygame.mouse import get_pos,get_pressed,set_visible
from pygame import font,display,mixer,image
from random import choice
pygame.init()
cor=choice(('blue','orange'))
tela=display.set_mode()
set_visible(False)
x,y=get_pos()
v=True
fechar=image.load('fechar.png').convert_alpha()
fechar_rect=fechar.get_rect(topright=(tela.get_size()[0],0))
#mixer.music.load('y2meta.com - C418 - Subwoofer Lullaby - Minecraft Volume Alpha (192 kbps).mp3')
#mixer.music.play(10)
textos={'iniciar':(font.Font('C:\\Users\\Ricardo\\PycharmProjects\\pygame\\resources\\Pixeltype.ttf',45).render('Iniciar',1,'gray'),font.Font('C:\\Users\\Ricardo\\PycharmProjects\\pygame\\resources\\Pixeltype.ttf',45).render('Iniciar',1,'gray').get_rect(center=(tela.get_size()[0]/2,tela.get_size()[1]/2-50))),'opcoes':(font.Font('C:\\Users\\Ricardo\\PycharmProjects\\pygame\\resources\\Pixeltype.ttf',45).render('Options',1,'gray'),font.Font('C:\\Users\\Ricardo\\PycharmProjects\\pygame\\resources\\Pixeltype.ttf',45).render('Options',1,'gray').get_rect(center=(tela.get_size()[0]/2,tela.get_size()[1]/2+50)))}
while pygame.QUIT not in (evento.type for evento in pygame.event.get()) and not all((fechar_rect.collidepoint((x,y)),get_pressed()[0])):
    tela.fill('pink')
    x+=(get_pos()[0]-x)/40
    y+=(get_pos()[1]-y)/40
    release=True
    for mostrar in textos.values():
        if rect(tela,'red',[r-8 for r in mostrar[1].topleft]+[a+10 for a in mostrar[1].size],0,20).collidepoint((x,y)):release=False
        tela.blit(mostrar[0],mostrar[1])
    if v!=release and not release:mixer.Sound('click.wav').play()
    v=release
    tela.blit(fechar,fechar_rect)
    circle(tela,cor,(x,y),7)
    display.flip()
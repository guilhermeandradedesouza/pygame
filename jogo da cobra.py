from random import randint
from pygame.draw import *
from pygame.locals import *
import pygame
pygame.init()
lista_cobra=[]
lista_obstaculo=[]
pontos=movimento_y=movimento_x=0
tela=pygame.display.set_mode((800,600))
pygame.display.set_caption('jogo da cobrinha')
encontro,cobra_x,cobra_y,maca_x,maca_y=False,386,286,randint(40,750),randint(40,550)
while True:
    for evento in pygame.event.get():
        if evento.type==QUIT:exit()
        if evento.type==KEYDOWN:
            if evento.key == K_a or evento.key == K_d:
                movimento_y = 0
                if evento.key == K_d and movimento_x!=-2:movimento_x = 2
                elif movimento_x!=2:movimento_x = -2
            elif evento.key==K_w or evento.key==K_s:
                movimento_x = 0
                if evento.key == K_s and movimento_y!=-2:movimento_y = 2
                elif movimento_y!=2:movimento_y = -2
            elif evento.key==K_r:
                movimento_y,movimento_x,cobra_x,cobra_y,pontos,lista_cobra,encontro=0,0,386,286,0,[],False
    if cobra_x == 772 or cobra_y == 572 or cobra_x == 0 or cobra_y == 0 or encontro:
        movimento_y=movimento_x=0
        tela.fill('white')
        tela.blit(pygame.font.SysFont('arial', 50, True).render('Derrota aperte r para recomeçar.', True, 'red'), (85, 240))
    else:
        pygame.time.Clock().tick(65)
        tela.fill('white')
        cobra=rect(tela,'green',(cobra_x,cobra_y,28,28),0,5)
        maca=rect(tela,'red',(maca_x,maca_y,22,22),0,10)
        lista_cobra.append((cobra_x,cobra_y))
        if len(lista_cobra)>pontos*14:del lista_cobra[0]
        for XeY in lista_cobra:
            rect(tela, 'green', (XeY[0], XeY[1], 28, 28),0,5)#14 porque estou indo de dois em dois obs:queria que fosse 13 :(
            if lista_cobra.count(XeY) > 1: encontro = True
        if cobra.colliderect(maca):
            pygame.mixer.Sound('smw_coin.wav').play()
            lista_obstaculo.append((randint(40,750),randint(40,550),30,30))
            maca_x,maca_y=randint(40,750),randint(40,550)
            pontos+=1
        for obst in lista_obstaculo:
            if rect(tela,'yellow',obst,0,10).colliderect(cobra):encontro=True
        cobra_x+=movimento_x
        cobra_y+=movimento_y
        tela.blit(pygame.font.SysFont('arial',20).render(f'Pontos:{pontos}',True,(120,10,100)),(10,10))
    pygame.display.update()
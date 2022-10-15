from random import uniform,randint
from pygame.draw import rect
import pygame
from pygame.locals import *
pos=[]
for colocar in range(4):
    a=-1*round(uniform(95,400),1)
    while len(pos)>1 and abs(pos[-1]-a)<10:a=-1*round(uniform(95,400),1)
    pos.append(a)
aleatorio=[randint(0,3) for x in range(4)]
pressionando=False
pontos=num=0
descer=[0 for x in range(4)]
pygame.init()
tela=pygame.display.set_mode((550,700))
pygame.display.set_caption('setinhas')
blocos=[rect(tela,('green','red','purple','blue')[aleatorio[vez]],((20,147.5,275,402.5)[aleatorio[vez]],pos[vez],95,95),0,5) for vez in range(4)]
while True:
    pygame.time.Clock().tick(200)
    tela.fill('white')
    pressionando=True if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_f] else False
    for evento in pygame.event.get():
        if evento.type==QUIT:exit()
        elif evento.type==KEYDOWN:
            if evento.key==K_a:num=0
            elif evento.key==K_s:num=1
            elif evento.key==K_d:num=2
            elif evento.key==K_f:num=3
    if pressionando:selecionado=rect(tela, ('green', 'red', 'purple', 'blue')[num], ((20, 580, 100, 100), (147.5, 580, 100, 100), (275, 580, 100, 100), (402.5, 580, 100, 100))[num], 0, 5)
    for bloco in range(len(blocos)):
        descer[bloco]+=2
        blocos[bloco]=rect(tela,('green','red','purple','blue')[aleatorio[bloco]],((20,147.5,275,402.5)[aleatorio[bloco]],pos[bloco]+descer[bloco],95,95),0,5)
        try:
            if blocos[bloco].colliderect(selecionado) or blocos[bloco].collidepoint((20,147.5,275,402.5)[aleatorio[bloco]],640):
                pos[bloco]=-1*round(uniform(95,400),1)
                descer[bloco]=0
                aleatorio[bloco]=randint(0,3)
                pontos+=100
        except NameError:
            if blocos[bloco].collidepoint((20,147.5,275,402.5)[aleatorio[bloco]],640):
                pos[bloco]=-1*round(uniform(95,400),1)
                descer[bloco]=0
                aleatorio[bloco]=randint(0,3)
                pontos+=100
    pygame.display.flip()
    tela.blit(pygame.font.SysFont('arial',20).render(f'Pontos:{pontos}', 1, 'black'),(350,60))
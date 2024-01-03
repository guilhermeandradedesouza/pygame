import pygame
from pygame import QUIT
from pygame.mouse import get_pos,get_pressed,set_visible
from pygame.draw import circle
from pygame.surface import Surface
from random import randint,choice
v=.55
class Target:
    cores=[]
    for r in range(80,256):
        for g in range(80,256):
            for b in range(80,256):cores.append((r,g,b))
    def __init__(self,center):
        self.center=center
        self.cor=choice(self.cores)
        self.gradual=1
    def mostrar(self):
        self.circulo=circle(tela,self.cor,self.center,self.gradual)
        self.center=(self.center[0],self.center[1]+v)
        self.gradual+=.1 if int(self.gradual)<20 else 0
    def reset(self,center):
        self.cor=choice(self.cores)
        self.gradual=1
        self.center=center
tela=pygame.display.set_mode()
blur=Surface(tela.get_size())
blur.set_alpha(15)#tecido totalmente vermelho é 1 tecido pouco mais opaco é maior que 1 fazendo com que a luz passe parcialmente
set_visible(0)
precionado=True
mouse_pos=list(get_pos())
targets=[Target(tuple(randint(20,g_pos-20) for g_pos in tela.get_size())) for quant in range(4)]
while QUIT not in (evento.type for evento in pygame.event.get()):
    tela.blit(blur,(0,0))
    for alvo in targets:
        alvo.mostrar()
        if alvo.circulo.collidepoint(mouse_pos) and any(get_pressed()) and precionado or alvo.center[1]>tela.get_height()+40:
            alvo.reset((randint(50,tela.get_width()-50),randint(25,tela.get_height()-680)))
            precionado=False
    for mover in range(2):mouse_pos[mover]+=(get_pos()[mover]-mouse_pos[mover])/22
    circle(tela,'blue',mouse_pos,5,3)
    precionado=not any(get_pressed())
    pygame.display.flip()
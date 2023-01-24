import pygame as game
from pygame import QUIT,K_UP,K_w,K_s,K_DOWN
from pygame.key import get_pressed as pressed
from pygame.color import THECOLORS as colors
from pygame.draw import rect,circle
from random import choice
class Bola:
    def __init__(self,vel:int|float,raio=5):
        self.pos=center.copy()
        self.r=raio
        self.vel=vel
        self.direcao=[choice((vel[0],-vel[0])),choice((vel[1],-vel[1]))]# NOQA
        self.cor=choice(tuple(colors))
    def mostrar(self):
        for index,add in enumerate(self.direcao):self.pos[index]+=add
        if round(self.pos[1])>=height-5 or round(self.pos[1])<=5:self.direcao[1]=-self.direcao[1]
        elif round(self.pos[0])<=-self.r or round(self.pos[0])>=width+self.r:
            global pos1,pos2
            self.pos=center.copy()
            self.direcao=[choice((self.vel[0],-self.vel[0])),choice((self.vel[1],-self.vel[1]))]# NOQA
            pos1,pos2=[20,(height-tam[1])/2],[width-tam[0]-20,(height-tam[1])/2]
        return circle(tela,self.cor,self.pos,self.r)
tela=game.display.set_mode((650,450))
width,height=tela.get_size()
center=list(map(lambda x:x/2,tela.get_size()))
velocidade=.5
tam=[20,80]
pos1,pos2=[20,(height-tam[1])/2],[width-tam[0]-20,(height-tam[1])/2]
bola=Bola((.2,.2))
blur=game.Surface(tela.get_size())
blur.set_alpha(9)
while QUIT not in (evento.type for evento in game.event.get()):
    tela.blit(blur,(0,0))
    area=bola.mostrar()
    if area.colliderect(rect(tela,'green',pos1+tam)):bola.direcao[0]=-bola.direcao[0]
    elif area.colliderect(rect(tela,'blue',pos2+tam)):bola.direcao[0]=-bola.direcao[0]
    if pressed()[K_w] and round(pos1[1])>=0:pos1[1]-=velocidade
    elif pressed()[K_s] and round(pos1[1])<=height-tam[1]:pos1[1]+=velocidade
    if pressed()[K_UP] and round(pos2[1])>=0:pos2[1]-=velocidade
    elif pressed()[K_DOWN] and round(pos2[1])<=height-tam[1]:pos2[1]+=velocidade
    game.display.flip()
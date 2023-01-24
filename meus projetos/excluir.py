import pygame
from pygame.draw import polygon,circle
from pygame import QUIT as sair
from pygame.key import get_pressed
from os import path,listdir,remove
from shutil import rmtree
from random import randint,uniform
class Projetil:
    def __init__(self,center,raio,cor):
        self.center=list(center)
        self.r=raio
        self.cor=cor
    def mostrar(self,alvo):
        self.center[1]-=.2
        return circle(tela,self.cor,self.center,self.r).colliderect(alvo)
class Alvo:
    def __init__(self,arquivo,centro,raio,contante_de_queda,cor):
        self.arquivo=arquivo
        self.r=raio
        self.center=list(centro)
        self.color=cor
        self.mov=contante_de_queda
    def mostrar(self):
        self.center[1]+=self.mov
        return circle(tela,self.color,self.center,self.r)
    def __del__(self):
        if path.isdir(self.arquivo):rmtree(self.arquivo)
        else:remove(self.arquivo)
try:arquivos=tuple(listdir()[posicao] for posicao in map(lambda x:int(x)-1,input('arquivos para excluir:\n\t'+'\n\t'.join(f'{index}:{arq}' for index,arq in enumerate(listdir(),start=1))+'\nEscolhas os arquivos que deseja deletar com os números(separados por virgula):').strip().split(','))) #pega o nome dos arquivos selecionados
except IndexError:print('Número inválido.'),exit()
except PermissionError as error:print(f'Erro de permição ao arquivo/pasta {error.filename}'),exit()
except ValueError:print('Digite apênas números.'),exit()
disparar=True
projeteis=[]
tela=pygame.display.set_mode((450,650))
nave=[tela.get_width()/2,tela.get_height()*29/32]
width,height=tela.get_size()
alvos=[Alvo(arquivo,(randint(10,tela.get_width()-10),randint(-80,-15)),randint(12,15),uniform(.1,.24),'green') for arquivo in arquivos]
while sair not in (evento.type for evento in pygame.event.get()) and alvos:
    tela.fill('black')
    if get_pressed()[pygame.K_RIGHT] and nave[0]+30<width-5:nave[0]+=.55
    elif get_pressed()[pygame.K_LEFT] and nave[0]-30>5:nave[0]-=.55
    for index,objetivo in enumerate(alvos):
        cords=objetivo.mostrar()
        if objetivo.center[1]>tela.get_height()+50:objetivo.center=[randint(10,width-10),randint(-80,-15)]
        for projetil_index,projetil in enumerate(projeteis):
            if projetil.mostrar(cords):del alvos[index],projeteis[projetil_index]
    if get_pressed()[pygame.K_SPACE] and disparar:projeteis.append(Projetil(nave,6,'red'))
    disparar=not get_pressed()[pygame.K_SPACE]
    polygon(tela,'blue',((nave[0]-28,nave[1]+5),(nave[0]-16,nave[1]+17),(nave[0]+16,nave[1]+17),(nave[0]+28,nave[1]+5),(nave[0]+8,nave[1]-10+5),(nave[0]-8,nave[1]-10+5)))
    pygame.display.flip()
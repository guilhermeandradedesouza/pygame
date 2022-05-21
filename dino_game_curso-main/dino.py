import pygame
from pygame.locals import *
import os
diretorio=os.path.dirname(__file__)
imagens=os.path.join(diretorio,'imagem')
sons=os.path.join(diretorio,'sons')
pygame.init()
tela=pygame.display.set_mode((640,480))
pygame.display.set_caption('dino')
class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens=[]
        self.img=pygame.image.load('imagens/dinoSpritesheet.png').convert_alpha().subsurface((32*3,0),(32,32))
        self.img=pygame.transform.scale(self.img,(320,320))
        self.image=self.img
        self.rect=0,0
dino=Dino()
grupo=pygame.sprite.Group()
grupo.add(dino)
while 1:
    pygame.time.Clock().tick(30)
    tela.fill('white')
    for evento in pygame.event.get():
        if evento.type==QUIT:exit()
    grupo.draw(tela)
    grupo.update()
    pygame.display.flip()
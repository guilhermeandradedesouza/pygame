from pygame.locals import *
import pygame
pygame.init()
tela=pygame.display.set_mode((920,700))
pygame.display.set_caption('minecraft')
class Crepper(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.acontecendo_esquerda=self.acontecendo_direita=False
        self.frame=0
        self.imagens=[]
        self.y=250
        self.x=600
        self.image=pygame.transform.scale(pygame.image.load('creeper/crepper_frente.png').subsurface((0,0),(32,32)),(320,320))
        self.rect=self.image.get_rect()
        self.rect.topleft=self.x%841,self.y
    def parado(self):self.acontecendo_direita=self.acontecendo_esquerda=False
    def lado_esquerda(self):
        self.x-=1
        if self.acontecendo_direita:self.frame=0
        self.acontecendo_esquerda,self.acontecendo_direita=True,False
        self.imagens=[pygame.transform.scale(pygame.image.load('creeper/crepper_lado_esquerda.png').subsurface((0,32*x),(32,32)),(400,400)) for x in range(2)]
        self.image=self.imagens[self.frame%2]
    def lado_direito(self):
        self.x+=1
        print(self.x)
        if self.acontecendo_esquerda:self.frame=0
        self.acontecendo_direita,self.acontecendo_esquerda=True,False
        self.imagens = [pygame.transform.scale(pygame.image.load('creeper/crepper_lado_direita.png').subsurface((0,32*x),(32,32)),(400,400)) for x in range(2)]
        self.image = self.imagens[self.frame%2]
    def update(self):
        if not self.acontecendo_direita or not self.acontecendo_esquerda:
            self.imagens = [pygame.transform.scale(pygame.image.load('creeper/crepper_frente.png').subsurface((32*pos_x, 0), (32, 32)),(320,320)) for pos_x in range(3)]
            self.image=self.imagens[self.frame%3]
            self.frame+=1
        else:
            self.frame+=1
            self.image = self.imagens[self.frame % 2]
            if self.lado_direito:self.x+=1
            else:self.x-=1
        self.acontecendo_esquerda=self.acontecendo_direita=False
crepper=Crepper()
creppers=pygame.sprite.Group()
creppers.add(crepper)
while 1:
    pygame.time.Clock().tick(20)
    for evento in pygame.event.get():
        if evento.type==QUIT:exit()
        if evento.type==TEXTINPUT:
            if pygame.key.get_pressed()[K_a]:crepper.lado_esquerda()
            elif pygame.key.get_pressed()[K_d]:crepper.lado_direito()
    if not len(pygame.event.get()):crepper.parado()
    #for pos in range(920//16*6):tela.blit(pygame.transform.scale(pygame.image.load('creeper/terra.png'),(16*6,16*6)),(920-pos*16*6,700-16*6))
    tela.blit(pygame.transform.scale(pygame.image.load('creeper/cenario.png'), (32*28.75,32*21.875)),(920-32*28.75, 0))
    creppers.draw(tela)
    creppers.update()
    pygame.display.flip()
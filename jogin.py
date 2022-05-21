import pygame
from pygame.locals import *
from pygame.draw import *
pygame.init()
tela=pygame.display.set_mode((400,350))
class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites=[pygame.image.load(f'boneco/sprite_{num}.png') for num in range(4)]
        self.atual=0
        self.image=self.sprites[self.atual%4]
        self.rect=self.image.get_rect()
        self.image=pygame.transform.scale(self.image,(32*10,32*10))
        self.rect.topleft=70,-10
        self.animar=False
    def atacar(self):self.animar=True
    def update(self):
        if self.animar:
            self.atual+=0.5
            self.image=self.sprites[int(self.atual%4)]
            self.image = pygame.transform.scale(self.image, (32 * 10, 32 * 10))
        if int(self.atual%4)==0 and int(self.atual)!=0:self.animar=False
personagem=Personagem()
todas=pygame.sprite.Group()
todas.add(personagem)
fundo=pygame.transform.scale(pygame.image.load('fundo.jpg').convert(),(400,350))
while True:
    pygame.time.Clock().tick(20)
    tela.fill('blue')
    tela.blit(fundo,(0,0))
    for evento in pygame.event.get():
        if evento.type==QUIT:exit()
        elif evento.type == KEYDOWN:
            if evento.key == K_SPACE:personagem.atacar()
    for v in (('brown',(0,310,400,40)),('green',(0,300,400,10)),('yellow',(0,0,50,50))):rect(tela,v[0],v[1])
    todas.draw(tela)
    todas.update()
    pygame.display.flip()
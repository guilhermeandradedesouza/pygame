from pygame.locals import *
import pygame
pygame.init()
tela=pygame.display.set_mode((640,500))
pygame.display.set_caption('Sprites')
class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites=[pygame.image.load(f'boneco/sprite_{num}.png') for num in range(4)]
        self.atual=0
        self.image=self.sprites[self.atual%4]
        self.rect=self.image.get_rect()
        self.image=pygame.transform.scale(self.image,(32*10,32*10))
        self.rect.topleft=150,100
        self.animar=False
    def atacar(self):self.animar=True
    def update(self):
        if self.animar:
            self.atual+=0.5
            self.image=self.sprites[int(self.atual%4)]
            self.image = pygame.transform.scale(self.image, (32 * 10, 32 * 10))
        if int(self.atual%4)==0 and int(self.atual)!=0:self.animar=False
todas=pygame.sprite.Group()
sapo=Personagem()
todas.add(sapo)
while 1:
    pygame.time.Clock().tick(30)
    tela.fill('white')
    for evento in pygame.event.get():
        if evento.type==QUIT:exit()
        elif evento.type==KEYDOWN:
            if evento.key==K_SPACE:sapo.atacar()
    todas.draw(tela)
    todas.update()
    pygame.display.flip()
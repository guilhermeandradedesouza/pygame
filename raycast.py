import pygame
class Parede:
    def __init__(self,x,y,tam,color):self.x,self.y,self.tam,self.color=x,y,tam,color
    def draw(self):self.rect=pygame.draw.rect(display,self.color,(self.x,self.y,self.tam,self.tam))
    def get_rect(self):return self.rect
pygame.init()
display=pygame.display.set_mode((800,800))
cor='black'
tam=40
paredes=tuple(Parede(x,m*tam*8,tam,cor) for x in range(0,tam*8+1,tam) for m in (0,1))+tuple(Parede(mk*tam*8,y,tam,cor) for y in range(0,tam*8+1,tam) for mk in (0,1))
while True:
    display.fill('white')
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:exit()
    for k in paredes:
        k.draw()
    pygame.display.flip()
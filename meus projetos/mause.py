import pygame
from pygame.locals import QUIT
from pygame.draw import rect,circle
tela=pygame.display.set_mode((500,250))
pygame.mouse.set_visible(0)
x=y=0
while QUIT not in (evento.type for evento in pygame.event.get()):
    if not pygame.mouse.get_pressed()[0]:tela.fill('white')
    pos=pygame.mouse.get_pos()
    if pos[0]>475:x=-475+pos[0]
    elif pos[0]<25:x=-25+pos[0]
    else:x=0
    if pos[1]>225:y=-225+pos[1]
    elif pos[1]<25:y=-25+pos[1]
    else:y=0
    if not pygame.mouse.get_pressed()[0]:rect(tela,'red',(pos[0]-25+x,pos[1]-25+y,50,50))
    circle(tela,'red',(pos[0]-x,pos[1]-y),25,1)
    pygame.display.flip()
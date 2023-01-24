from pygame import QUIT
from pygame import draw,display,event
from pygame.mouse import get_pos
tela=display.set_mode((600,600))
while QUIT not in (evento.type for evento in event.get()):
    tela.fill('white')
    r=((get_pos()[0]-300)**2+(get_pos()[1]-300)**2)**.5
    draw.circle(tela,'black',(299,299),r,1)
    draw.polygon(tela,'black',((299+r,299),(299-r,299),get_pos()),1)
    display.flip()
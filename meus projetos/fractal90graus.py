from turtle import *
from math import cos,radians
Screen().setup(800,600,starty=60)
def mover(lapis,posicao,metodo='up'):
    if metodo=='up':lapis.pu()
    elif metodo=='down':lapis.pd()
    else:raise 'Metodo não existe.'
    lapis.setpos(posicao)
inicial=(-300,-260)
d=Pen()
d.speed(1.2)
lado=550
mover(d,inicial)
for posicoes in ((inicial[0]+lado,inicial[1]),(inicial[0],inicial[1]+lado),inicial):mover(d,posicoes,'down')
while 1:
    if lado==550:d.lt(45)
    else:d.rt(135)
    d.fd(cos(radians(45))*lado)
    lado=cos(radians(45))*lado
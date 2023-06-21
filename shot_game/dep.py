import pygame
from pygame import QUIT
from pygame.draw import circle
from math import dist
quit_verification=lambda:QUIT in (evento.type for evento in pygame.event.get())
pygame.init()

def regular_polygon(sides,center,r,rotation=0):
    """
    :return: cords to make a regular polygon
    """

    from math import pi,sin,cos,radians
    vertices=[]
    angle=2*pi/sides
    rotate=radians(rotation)
    for i in range(sides):vertices.append((center[0]+r*cos(rotate+i*angle),center[1]+r*sin(rotate+i*angle)))
    return vertices

class Timer:
    from time import time
    def start(self):
        self.start_time=self.time()
        return self
    def get(self):return self.time()-self.start_time
    def reset(self):
        self.start_time=self.time()
        return self

class Mouse:
    from pygame import mouse
    def __init__(self,smooth_coefficient:int|float,visibilidade:bool):
        self.mouse.set_visible(visibilidade)
        self.smooth=smooth_coefficient
        self.pos=list(self.mouse.get_pos())
    def get_pos(self):
        actual_pos=self.mouse.get_pos()
        self.pos[0]+=(actual_pos[0]-self.pos[0])/self.smooth
        self.pos[1]+=(actual_pos[1]-self.pos[1])/self.smooth
        return self.pos

class Click:
    def __init__(self,m_button):
        self.bt=m_button
        self.is_pressed=False
    def get(self):
        mouse=pygame.mouse.get_pressed()
        if not mouse[self.bt]:self.is_pressed=False
        elif not self.is_pressed and mouse[self.bt]:
            self.is_pressed=True
            return True
        return False

class Bullet:
    def __init__(self,display,raio,start:list,direction:tuple,speed):
        self.disp=display
        self.speed=speed
        self.pos=start
        self.comps=direction
        self.r=raio
    def update(self):
        circle(self.disp,'red',self.pos,self.r)
        for mov_part in range(2):self.pos[mov_part]+=self.comps[mov_part]*self.speed

class Enemy:
    def __init__(self,display,player,start:list,raio,speed=2,**ext):

        self.disp=display
        self.player=player

        self.pos=start
        self.r=raio
        self.speed=speed

        self.damage_color=ext.get('damage_color','green')
        self.color=ext.get('color','red')

        self.start_life=self.life=ext.get('life',1)
        self.q=ext.get('end_animation_q',.9)
        self.is_boss=ext.get('boss',False)

    def update(self):

        circle(self.disp,self.color,self.pos,self.r)
        circle(self.disp,self.damage_color,self.pos,self.r*(self.start_life-self.life)/self.start_life)

        distancia=dist(self.player.pos,self.pos)
        dx=self.player.pos[0]-self.pos[0]
        dy=self.player.pos[1]-self.pos[1]

        self.pos[0]+=self.speed*dx/distancia
        self.pos[1]+=self.speed*dy/distancia

    #animação para BOSS
    def BOSS(self):
        from pygame.draw import polygon
        for color in (self.damage_color,self.color)*10:
            circle(self.disp,color,self.pos,self.r)
            pygame.display.flip()
            pygame.time.wait(20)
        while self.r>1:
            self.disp.fill('black')
            for rotate in range(0,360,30):polygon(self.disp,self.damage_color,regular_polygon(3,self.pos,self.r,rotate))
            pygame.time.wait(20)
            self.r*=self.q
            pygame.display.flip()

        return Enemy(self.disp,self.player,self.pos,30,4,color=self.damage_color,life=1)

class Player:
    def __init__(self,display:pygame.Surface,raio:int,mouse:Mouse,**ext):
        self.click=Click(0)
        self.mouse=mouse

        self.disp=display
        self.disp_size=display.get_size()

        self.r=raio
        self.pos=list(ext.get('start',[display.get_width()/2,display.get_height()/2]))
        self.color=ext.get('color','blue')
        self.danger_color=ext.get('danger_color',(145,0,0))
        self.aim_color=ext.get('aim_color','yellow')
        self.defeat_message=ext.get('defeat','Game Over')
        self.const_width=self.width=ext.get('width',5)

        self.shoot_time=Timer().start()
        self.bullet_rate=ext.get('shoot_delay',.1)
        self.bullet_speed=ext.get('bullet_speed',1.5)
        self.bullet_range=ext.get('bullet_range',5)
        self.bullets=[]

        self.speed=ext.get('speed',1)
        self.regen_time=ext.get('regen_time',5)
        self.regen_rate=ext.get('regen_rate',.05)
        self.life=ext.get('life',5)
        self.danger_life=ext.get('danger_amount_of_life',2)
        self.damage=(raio-self.width)/self.life
        self.time=Timer().start()

    def update(self,enemies:list[Enemy]=None,integrar=False):
        from pygame.key import get_pressed as pressed
        pos=self.mouse.get_pos()
        distancia=dist(pos,self.pos)
        const_k=self.r/distancia
        borda=[const_k*(pos[0]-self.pos[0])+self.pos[0],const_k*(pos[1]-self.pos[1])+self.pos[1]]
        if self.click.get() and self.shoot_time.get()>self.bullet_rate:
            self.bullets.append(
            Bullet(self.disp,self.bullet_range,borda,((pos[0]-self.pos[0])/distancia,(pos[1]-self.pos[1])/distancia),self.bullet_speed)
            )
            self.shoot_time.reset()

        if pressed()[pygame.K_a] and self.pos[0]-self.r>0:self.pos[0]-=self.speed
        if pressed()[pygame.K_d] and self.pos[0]+self.r<self.disp_size[0]:self.pos[0]+=self.speed
        if pressed()[pygame.K_w] and self.pos[1]-self.r>0:self.pos[1]-=self.speed
        if pressed()[pygame.K_s] and self.pos[1]+self.r<self.disp_size[1]:self.pos[1]+=self.speed

        cor=self.danger_color if self.width>=self.const_width+self.damage*(self.life-self.danger_life) else self.color
        circle(self.disp,cor,self.pos,self.r,round(self.width)) #player range
        circle(self.disp,self.aim_color,borda,4) #borda

        for bullet_pos,bullet in enumerate(self.bullets):
            limits=bullet.pos[0]+bullet.r,bullet.pos[1]+bullet.r
            if any((limits[0]>self.disp_size[0],limits[0]<0)) or any((limits[1]>self.disp_size[1],limits[1]<0)):del self.bullets[bullet_pos]
            else:bullet.update()

        if enemies:
            for enemy_pos,enemy in enumerate(enemies):

                if dist(enemy.pos,self.pos)<self.r+enemy.r:
                    self.width+=self.damage*enemy.life
                    enemy.life=0
                    self.time.reset()

                else:
                    for bullet_pos,bullet in enumerate(self.bullets):
                        if dist(bullet.pos,enemy.pos)<bullet.r+enemy.r:
                            enemy.life-=1
                            del self.bullets[bullet_pos]

                if enemy.life==0:
                    if enemy.is_boss:enemies.append(enemy.BOSS())
                    del enemies[enemy_pos]
                elif integrar:enemy.update()

        if self.time.get()>=self.regen_time and self.width!=self.const_width:
            if self.width-self.regen_rate>self.const_width:self.width-=self.regen_rate
            else:self.width=self.const_width

    def animate_death(self,q):
        self.r*=q
        circle(self.disp,self.danger_color,self.pos,self.r)
        return self.r<1

    def state(self):
        if self.width>=self.r:return self.defeat_message
        return False

def show_text(display:pygame.Surface,text,size,pos,color='black',font='arial'):
    fonte=pygame.font.SysFont(font,size)
    display.blit(fonte.render(text,True,color),pos)
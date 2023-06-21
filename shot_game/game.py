from dep import *
from random import randint,choice
tela=pygame.display.set_mode()
size=tela.get_size()
mouse=Mouse(60,False)
player_config={'life':10,'regen_time':4,'bullet_range':5,'bullet_speed':2,'width':3,'speed':2,'defeat':'Derrota','shoot_delay':.15}
BOSS_config={'raio':56,'life':20,'speed':1,'damage_color':'yellow','boss':True}
enemy_config={'raio':18,'speed':1.4,'life':2}
player=Player(tela,40,mouse,**player_config)
enemies=[]
while not quit_verification():
    pygame.time.Clock().tick(480)
    tela.fill('black')
    if player.state()==player_config['defeat']:
        enemies.clear()
        if player.animate_death(.99):exit()
    else:player.update(enemies,True)
    if len(enemies)<5:
        config=enemy_config if randint(0,10) else BOSS_config
        possibilities=[randint(-80,-40),randint(0,size[1])],[randint(0,size[0]),randint(-80,-40)],[randint(0,size[0]),randint(size[1]+40,size[1]+80)],[randint(size[0]+40,size[0]+80),randint(0,size[1])]
        enemies.append(Enemy(tela,player,choice(possibilities),**config))
    pygame.draw.circle(tela,'lightblue',mouse.get_pos(),5)
    pygame.display.flip()
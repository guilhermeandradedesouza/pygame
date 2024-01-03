from dep import *
from random import randint,choice
from pygame import *
centralize=lambda img_size:((size[0]-img_size[0])/2,(size[1]-img_size[1])/2)

tela=pygame.display.set_mode()
size=tela.get_size()
mouse=Mouse(45,False)

player_config={'life':10,'regen_time':4,'bullet_range':5,'bullet_speed':2.5,'width':3,'speed':2,'defeat':'Derrota','shoot_delay':.15}
BOSS_config={'raio':56,'life':20,'speed':1,'damage_color':'yellow','boss':True}
enemy_config={'raio':21,'speed':1.4,'life':2}

player=Player(tela,40,mouse,**player_config)
tecla=Pressed(pygame.K_ESCAPE)

start_menu=Menu(tela,mouse,'white',True)

play_image=pygame.transform.scale(image.load('play.png').convert_alpha(),(256,256))
start_center=centralize(play_image.get_size())

close_image=pygame.transform.scale(image.load('fechar.png').convert_alpha(),(192,192))
song=pygame.transform.scale(image.load('audio_on.png').convert_alpha(),(256,256)),pygame.transform.scale(image.load('audio_mute.png'),(256,256))

mode=0
def song_mode():
    global mode
    start_menu['audio_mode'][0]=song[not mode]
    mode=not mode

start_menu.add_surface(close_image,(-10,-10),'fechar',lambda :exit())
start_menu.add_surface(play_image,start_center,'play',lambda :start_menu.set_state(False))
start_menu.add_surface(song[mode],(size[0]-300,0),'audio_mode',song_mode)

enemies=[]
spawn_enemies=5
enemies_count=-spawn_enemies

f_name='arial'
f_size=35
fonte=pygame.font.SysFont(f_name,f_size)

def start():
    global enemies,player,tecla,enemies_count
    enemies=[]
    player=Player(tela,40,mouse,**player_config)
    enemies_count=-spawn_enemies

while not quit_verification():
    pygame.time.Clock().tick(460)
    if start_menu.get_state():start_menu.update()

    else:
        tela.fill('black')
        if player.state()==player_config['defeat']:
            enemies.clear()
            if player.animate_death(.95):
                start_menu.set_state(True)
                start()
            pygame.time.wait(20)
        else:
            player.update(enemies,True)
            if len(enemies)<spawn_enemies:
                config=enemy_config if randint(0,10) else BOSS_config
                possibilities=[randint(-80,-40),randint(0,size[1])],[randint(0,size[0]),randint(-80,-40)],[randint(0,size[0]),randint(size[1]+40,size[1]+80)],[randint(size[0]+40,size[0]+80),randint(0,size[1])]
                enemies.append(Enemy(tela,player,choice(possibilities),**config))
                enemies_count+=1
        tela.blit(fonte.render('SCORE:'+str(enemies_count),True,'white'),(10,10))

    if tecla.get():start_menu.set_state(not start_menu.get_state())
    pygame.draw.circle(tela,'lightblue',mouse.get_pos(),5)
    pygame.display.flip()
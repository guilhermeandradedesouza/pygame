from pyautogui import write,press
from random import sample
from time import sleep
letras='qwertyuiopasdfghjklçzxcvbnm'
sleep(1)
while 1:
    write(''.join(sample([letra for letra in letras],26)),interval=0)
    press('enter')
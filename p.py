from pyautogui import write,press
from random import sample
from time import sleep
from string import ascii_letters
letras=ascii_letters
sleep(1)
while 1:
    write(''.join(sample([letra for letra in letras],len(ascii_letters))),interval=0)
    press('enter')
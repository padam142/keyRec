import keyboard  # using module keyboard
import random
import time
from pynput.keyboard import Controller
from pynput.keyboard import Key, Listener

keyboard1 = Controller()

var=["a","b","c","1","2","3","@","%","*"]

def keyChange():
    for i in var:
        r=random.choices(var)
        delay = random.uniform(0, 1)  # Generate a random number between 0 and 10
        time.sleep(delay)
        return r

def lists():
    for i in list:
        return i

while True:  # making a loop
    try:
        if keyboard.is_pressed('a'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('b'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('c'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('d'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('e'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('f'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('g'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('h'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('i'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('j'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('k'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('l'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('m'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('n'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('o'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('p'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('q'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('r'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('s'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('t'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('u'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('v'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('w'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('x'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('y'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('z'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('1'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('2'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('3'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('4'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('5'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('6'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('7'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('8'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('9'): # if key 'q' is pressed
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('0'): # if key 'q' is pressed
            keyboard1.type(keyChange())
    except:

        break  # if user pressed a key other than the given key the loop will break
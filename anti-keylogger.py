import keyboard  # using module keyboard
import random
import time
from pynput.keyboard import Controller
from pynput.keyboard import Key, Listener

keyboard1 = Controller()

var=["a","b","c","i","o","u","1","2","3","@","%","*","A","B","C","E","I","O","U"]

def keyChange():
    for i in var:
        r=random.choices(var)
        delay = random.uniform(0, 1)
        time.sleep(delay)
        return r

def lists():
    for i in list:
        return i

while True:  # making a loop
    try:
        if keyboard.is_pressed('a'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('b'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('c'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('d'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('e'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('f'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('g'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('h'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('i'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('j'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('k'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('l'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('m'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('n'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('o'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('p'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('q'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('r'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('s'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('t'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('u'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('v'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('w'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('x'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('y'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('z'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('1'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('2'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('3'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('4'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('5'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('6'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('7'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('8'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('9'):
            keyboard1.type(keyChange())
        elif keyboard.is_pressed('0'):
            keyboard1.type(keyChange())
    except:

        break  # if user pressed a key other than the given key the loop will break
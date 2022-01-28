import time
import random
from pynput.keyboard import Controller
import keyboard

keyboard = Controller()  # Create the controller

def type_string_with_delay(string):
    for character in string:  # Loop over each character in the string
        keyboard.type(character)  # Type the character
        delay = random.uniform(0, 2)  # Generate a random number between 0 and 10
        time.sleep(delay)  # Sleep for the amount of seconds generated

var=['1','2','3','4','5','6','7','8','9','0',"!","@","#","$","%","&","a","*","e","i",")","o","u","B","Z"]
# while True:
#     for i in var:
#         type_string_with_delay(var)

while True:
    if keyboard.is_pressed():
        for i in var:
            type_string_with_delay(var)

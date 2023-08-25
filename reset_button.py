from subprocess import call
from gpiozero import Button

button = Button(26)

def print_thing():
    print('System reset successful!')
    
button.when_pressed =print_thing
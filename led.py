from gpiozero import LED
from time import sleep

green = LED(26)

print(green.on)
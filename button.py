from gpiozero import LED, Button
from signal import pause

led = LED(21)
button = Button(26)

button.when_pressed = led.on
button.when_released = led.off

pause()
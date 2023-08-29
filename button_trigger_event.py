from gpiozero import Button
from signal import pause
import requests


ifttt_webhook: str = "https://maker.ifttt.com/trigger/{}/json/with/key/hCEZUGJjT1LfuQhr-4tXs7rDpg6XY4Mq98-gkcio68g"

def trigger_event(event: str):
    return requests.get(ifttt_webhook.format(event))


button = Button(21)

while True:
    if button.is_pressed:
        trigger_event(event="button_pressed")
        





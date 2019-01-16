from gpiozero import LED, Button
from time import sleep
led = LED(14)
button = Button(2)

while True:
    button.wait_for_press()
    led.toggle()
    sleep(1)
    

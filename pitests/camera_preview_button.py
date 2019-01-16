from gpiozero import LED, Button
from time import sleep
from picamera import PiCamera
from datetime import datetime

button = Button(2)
camera = PiCamera()
#ledCapture = LED(2)

while True:
    button.wait_for_press()
    dt = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    camera.start_preview()
    sleep(2)
    #ledCapture.on()
    camera.capture('/home/pi/Pictures/IMG-%s.jpg' % dt)
    camera.stop_preview()
    #ledCapture.off()
    

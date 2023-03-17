import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
for x in range(3):
    GPIO.output(4, True)#relay = on
    print("on")
    time.sleep(3)
    GPIO.output(4, False)#relay = off
    print("off")
    time.sleep(3)
GPIO.cleanup()
    
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
while True:
  sw = input("input_status : ")
  if sw =='on':
    GPIO.output(4, True)#relay = on
    print('light = on ')
    time.sleep(0.5)
  elif sw =="off":
    GPIO.output(4, False)#relay = off
    print('light = off')
    time.sleep(0.5)
  else:
    print("___")
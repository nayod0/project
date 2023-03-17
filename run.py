
import RPi.GPIO as GPIO
import time
import datetime
import cv2
from gpiozero import Servo
from time import sleep
import os

myGPIO = 17
TRIG=18
ECHO=24
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT) # relay pin(4)
servo = Servo(myGPIO)
path = "/home/pi/Desktop/img"
dt = datetime.datetime.now()
dt = dt.strftime("%Y-%m-%d %H:%M:%S")



#_____________________loop_______________________________


while True:
    
    print("distance measurement in progress")
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG,False)
    print("waiting for sensor to settle")
    time.sleep(0.2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    
    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
    
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
    
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    print("distance:",distance,"cm")
    time.sleep(2)
#__________________camera_____________________
#     
#     if distance > 13 and distance < 25 :
#         
#         for i in range(1):
#             camera = cv2.VideoCapture(0)
#             dt = datetime.datetime.now()
#             dt = dt.strftime("%Y-%m-%d %H:%M:%S")
#             return_value, image = camera.read()
#             cv2.imwrite(dt+".ipg", image)
#             print("capture_img")
#             sleep(1)
#         del(camera)

    if distance > 4 and distance <13 :
        servo.min()
        sleep(0.5)
        for i in range(1):
            camera = cv2.VideoCapture(0)
            dt = datetime.datetime.now()
            dt = dt.strftime("%Y-%m-%d %H:%M:%S")
            return_value, image = camera.read()
            cv2.imwrite(os.path.join(path, dt+'.jpg'), image)
            print("cap_photo name:",dt)
            sleep(1)
        del(camera)
        
    if distance > 14 and distance < 18 :
        servo.mid()
        sleep(0.5)
        for i in range(1):
            camera = cv2.VideoCapture(0)
            dt = datetime.datetime.now()
            dt = dt.strftime("%Y-%m-%d %H:%M:%S")
            return_value, image = camera.read()
            cv2.imwrite(os.path.join(path, dt+'.jpg'), image)
            print("cap_photo name:",dt)
            sleep(1)
        del(camera)
    if distance > 19 and distance < 30 :
        servo.max()
        sleep(0.5)
        for i in range(1):
            camera = cv2.VideoCapture(0)
            dt = datetime.datetime.now()
            dt = dt.strftime("%Y-%m-%d %H:%M:%S")
            return_value, image = camera.read()
#             cv2.imwrite(dt+'.png', image)
            cv2.imwrite(os.path.join(path, dt+'.jpg'), image)
            print("cap_photo name:",dt)
            sleep(1)
        del(camera)
        
        
    
        
        
        
    
    




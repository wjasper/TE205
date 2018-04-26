import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
LED = 26


GPIO.setup(LED, GPIO.OUT)
p = GPIO.PWM(LED,50)                  # set duty cycle frequency to 50Hz
p.start(0)                            # set the duty cycle to 0%, ie. off
p.ChangeDutyCycle(trim_pot*100/1024)   

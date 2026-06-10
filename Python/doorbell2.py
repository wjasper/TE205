#! /usr/bin/python3

import os
import sys
import select
import RPi.GPIO as GPIO
import time

def Ring(channel):
    GPIO.remove_event_detect(channel)
    p.ChangeDutyCycle(0)   #Turn LED OFF
    os.system("cvlc --quiet Door-chime-sound.mp3 vlc://quit")
#   os.system("mpg321 -q -o alsa /home/pi/Doorbell/Door-chime-sound.mp3")
#   os.system("echo \"Answer the doorbell\" | mail -s \"Doorbell\" wjasper@ncsu.edu")
    GPIO.add_event_detect(2, GPIO.FALLING, Ring, bouncetime=200)
    p.ChangeDutyCycle(100) #Turn LED ON    

def Blink(n,delay=0.25):
  for i in range(n):
    p.ChangeDutyCycle(0)   #Turn LED OFF
    time.sleep(delay)
    p.ChangeDutyCycle(100) #Turn LED ON
    time.sleep(delay)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3, GPIO.OUT) # LED
p = GPIO.PWM(3,50)      # set duty cycle frequency to 50Hz
p.start(100)            # set the duty cycle to 0%, ie. off
GPIO.add_event_detect(2, GPIO.FALLING, Ring, bouncetime=200)
GPIO.output(3, True)
Blink(5)

while True:
  while sys.stdin in select.select([sys.stdin], [], [], 0) [0]:
    line = sys.stdin.readline()
    if line == "exit\n":
      p.stop()
#     GPIO.cleanup()
      sys.exit(0)
    elif line == "blink\n":
      msg = input("Enter number of times to blink: ")
      Blink(int(msg))
    elif line == "off\n":
      p.ChangeDutyCycle(0)
    elif line == "on\n":
      p.ChangeDutyCycle(100)
    elif line == "dim\n":
      for i in range(100):
        p.ChangeDutyCycle(i)
        time.sleep(.03)
      # p.ChangeFrequency(5)
      for i in range(10,110,10):
        p.ChangeDutyCycle(i)
        print("Duty Cycle = ",i,"%")
        time.sleep(3)
      p.ChangeFrequency(50)
      p.ChangeDutyCycle(100)                
    else:
      pass
  time.sleep(0.1)

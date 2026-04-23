#! /usr/bin/python3

# version 1 with polling

import os
import sys
import select
import RPi.GPIO
import time
import random

RPi.GPIO.setwarnings(False)
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(2, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)
RPi.GPIO.setup(3, RPi.GPIO.OUT)
RPi.GPIO.output(3, True)  #Turn LED On
chimes = ['Door-chime-sound.mp3', 'Horse.mp3', 'Geese.mp3', 'Sheep.mp3', 'Cow.mp3']

def Ring():
    RPi.GPIO.output(3, False) #Turn LED Off
    command = "mpg321 -q -o alsa " +  random.choice(chimes)
    os.system(command)
    while RPi.GPIO.input(2) == RPi.GPIO.LOW:
        pass
    RPi.GPIO.output(3, True)  #Turn LED On
#   os.system("echo \"Answer the doorbell\" | mail -s \"Doorbell\" wjasper@ncsu.edu")


def Blink(n,delay=0.25):
    for i in range(n):
        RPi.GPIO.output(3, False) #Turn LED Off
        time.sleep(delay)
        RPi.GPIO.output(3, True)  #Turn LED On
        time.sleep(delay)        

RPi.GPIO.output(3, True)
Blink(5)
while True:
    if RPi.GPIO.input(2) == RPi.GPIO.LOW:
        Ring()
    while sys.stdin in select.select([sys.stdin], [], [], 0) [0]:
        line = sys.stdin.readline()
        if line == "exit\n":
            RPi.GPIO.cleanup()
            exit(0)
        elif line == "blink\n":
            msg = input("Enter number of times to blink: ")
            Blink(int(msg))
        elif line == "off\n":
            RPi.GPIO.output(3, False)  #Turn LED Off
        elif line == "on\n":
            RPi.GPIO.output(3, True) #Turn LED On
        else:
            pass



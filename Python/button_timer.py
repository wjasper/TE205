#! /usr/bin/python3

import RPi.GPIO as GPIO
import time
import random
from timeit import default_timer as timer
import datetime

def Blink(n, delay=0.25):
    for i in range(n):
        GPIO.output(3, True)  # Turn LED ON
        time.sleep(delay)
        GPIO.output(3, False)  # Turn LED OFF
        time.sleep(delay)

def callback(channel):
    global end
    end = timer()
    GPIO.remove_event_detect(channel)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3, GPIO.OUT)  # LED
GPIO.output(3, False)

def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)
file_name = timeStamped('Reaction.txt')
file = open(file_name, 'w')
file.write('gender' + '	' + 'reaction' + '\n')
Reaction = []
Gender = []
nStudent = int(input('Please enter the number of participants: '))

for x in range(0, nStudent):
    gender = input('Please choose your gender: 1 for Female   2 for Male   3 for Not applicable' + '\n')
    if gender == '1':
        gender = 'Female'
    elif gender == '2':
        gender = 'Male'
    elif gender == '3':
        gender = 'Not applicable'
    Gender.append(gender)
    print('Press the button as soon as possible when you see the LED is on. Game \
          will start after the LED blinks three times.' + '\n')

    global start
    global end

    time.sleep(10)
    Blink(3)

    while True:
        turnOn = 5
        while (turnOn) > 0:
            if (turnOn) > 0:  # do turnOn
                GPIO.output(3, False)
                time.sleep(random.uniform(1, 4))
                GPIO.add_event_detect(2, GPIO.FALLING, callback, bouncetime=200)
                GPIO.output(3, True)
                start = timer()
                end = start
                time.sleep(2)
                GPIO.remove_event_detect(2)
                diff = end - start
                order = 6 - turnOn
                print('No.' + str(order) + ' try, ', diff)
                Reaction.append(diff)
                file.write(Gender[x] + '	' + str(Reaction[5*x+(order-1)]) + '\n')
                turnOn -= 1
        while True:
            answer = input('Press c to continue, or press q to quit. ')
            if (answer[0] == 'q' or answer[0] == 'Q' or answer[0] == 'c' or answer[0] == 'C') : break
        
        if (answer[0] == 'q' or answer[0] == 'Q'):
            file.close()
            print('All done. File written called ' + file_name + '. ')
            exit(0)
        elif (answer[0] == 'c' or answer[0] == 'C'):
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(3, GPIO.OUT)  # LED
            GPIO.output(3, False)
            break
            

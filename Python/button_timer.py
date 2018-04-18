#! /usr/bin/python3

import random
import RPi.GPIO as GPIO
import time
import os

#constants used for testing reflexes
lightOn = 1
lightOff = 2
BuzzerOn = 3
BuzzerOff = 4

piNum = 14 #The number of the Pi being used in the lab
LED = 19
button = 26
buzzer = 21
user = ""
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(button, GPIO.IN, GPIO.PUD_DOWN)
tests = [1,1,1,2,2,2,3,3,3,4,4,4]

def determineFilename(user):
    directory = "./results"
    target = "record" + str(piNum) + user + "_"
    if not os.path.exists(directory):
        os.makedirs(directory)

    listFiles = os.listdir(directory)
    
    relFiles = [k for k in listFiles if target in k]
    if relFiles:
        num = 1
        while(target + str(num) + ".txt" in relFiles):
            relFiles.remove(target + str(num) + ".txt")
            num += 1
        f = open(directory + "/" + target + str(num) + ".txt", "w+")
    else:
        f = open(directory + "/" + target + "1.txt", "w+")
    return f
    
def startTest(test):
    if test == 1:
        print("starting up - press the button when the LED turns on")
        for i in range(3):
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(0.25)
            GPIO.output(LED, GPIO.LOW)
            time.sleep(0.25)
    elif test == 2:
        print("starting up - press the button when the LED turns off")
        for i in range(3):
            GPIO.output(LED, GPIO.LOW)
            time.sleep(0.25)
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(0.25)
    elif test == 3:
        print("starting up - press the button when the buzzer turns on")
        for i in range(3):
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(0.25)
            GPIO.output(buzzer, GPIO.LOW)
            time.sleep(0.25)
    elif test == 4:
        print("starting up - press the button when the buzzer turns off")
        for i in range(3):
            GPIO.output(buzzer, GPIO.LOW)
            time.sleep(0.25)
            GPIO.output(buzzer, GPIO.HIGH)
            time.sleep(0.25)


def endTest(test):
    if test == 1:
        GPIO.output(LED, GPIO.LOW)
    elif test == 2:
        GPIO.output(LED, GPIO.LOW)
    elif test == 3:
        GPIO.output(buzzer, GPIO.LOW)
    elif test == 4:
        GPIO.output(buzzer, GPIO.LOW)

def endWait(test):
    if test == 1:
        GPIO.output(LED, GPIO.HIGH)
    elif test == 2:
        GPIO.output(LED, GPIO.LOW)
    elif test == 3:
        GPIO.output(buzzer, GPIO.HIGH)
    elif test == 4:
        GPIO.output(buzzer, GPIO.LOW)

def testReaction(test):
    startTest(test)
    time.sleep(random.random() * 2 + 2)
    if GPIO.input(button):
        print("cheater... wait until the signal to press the button")
        print("restarting")
        endTest(test)
        test = random.choice(tests)
        testReaction(test)
        return
    endWait(test)
    start = time.clock()
    while not GPIO.input(button):
        pass
    final = time.clock()
    GPIO.output(LED, GPIO.LOW)
    GPIO.output(buzzer, GPIO.LOW)
    result = final - start
    print('your response time was {0} seconds!'.format(result))
    tests.remove(test)
    if test == 1:
        test = "LED_ON"
    elif test == 2:
        test = "LED_OFF"
    elif test == 3:
        test = "BUZZ_ON"
    elif test == 4:
        test = "BUZZ_OFF"
    f.write("%s,%s,%s,%s\n" % (piNum, user, test, result))

user = input("please enter your name: ")
f = determineFilename(user)
f.write("board,user,test,time-elapsed\n")
while len(tests):
    test = random.choice(tests)
    testReaction(test)
print("testing complete")
GPIO.cleanup()
exit()

class PWM:
    pin = 0
    frequency = 0
    on = False
    duty = 0
    def __init__(self, channel, frequency):
        self.pin = channel
        self.frequency = frequency
    def start(self, duty):
        if not self.on:
            self.on = True
            self.duty = duty
            print(self.report())
        else:
            print("The light is still on, and this message is a BAD sign")
    def ChangeDutyCycle(self, duty):
        self.duty = duty
        print(self.report())
    def stop(self):
        self.on = False
        print(self.report())
    def report(self):
        if self.on:
            return "The light is on and the duty is %d" % self.duty
        elif self.duty > 100 or self.duty < 0:
            return "I think it might be broken"
        else:
            return "The light is not on"

import time

#this is the function you'll be modifying to get the PWM LED to obey all those commands
def process(p, cmd):
    if cmd == "on": #looks like the on command was already written for you!
        if not p.on:
            p.start(p.duty)
    #do we need code to turn it off as well?
    elif cmd.isdigit():
        cmd = int(cmd)
        #so they just typed a number! let's keep it 0-100, and change the duty cycle!
    #Off-On-Off, blink should be an easy string to recognize right here
    elif cmd == "pulse":
        num = input("Enter the number of times you would like to pulse the light:\n")
        #is the LED on?  maybe you should check that before cycling
        if num == "yes":
            while True:
                #write code to cycle the duty cycle here
        for i in range(int(num)):
            #write code to cycle the duty cycle here


LED = #write code here to instantiate a PWM object with pin 3 and 50 Hz
while True: #This is your main process
    process(led, input("next command:\n")) #no need to change anything here
    

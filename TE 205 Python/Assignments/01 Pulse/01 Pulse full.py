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

def process(p, cmd):
    if cmd == "on":
        if not p.on:
            p.start(p.duty)
    elif cmd == "off":
        if p.on:
            p.stop()
    elif cmd.isdigit():
        cmd = int(cmd)
        if cmd > 100:
            cmd = 100
        if cmd < 0:
            cmd = 0
        p.ChangeDutyCycle(cmd)
    elif cmd == "blink":
        p.stop()
        time.sleep(0.5)
        p.start(100)
        time.sleep(1)
        p.stop()
        time.sleep(0.5)
    elif cmd == "pulse":
        num = input("Enter the number of times you would like to pulse the light:\n")
        p.ChangeDutyCycle(0)
        if not p.on:
            p.start(0)
        if num == "yes":
            while True:
                for i in range(0,100,2):
                    p.ChangeDutyCycle(i)
                    time.sleep(0.02)
                for i in range(100,0,-2):
                    p.ChangeDutyCycle(i)
                    time.sleep(0.02)
        for i in range(int(num)):
            for i in range(0,100,2):
                p.ChangeDutyCycle(i)
                time.sleep(0.02)
            for i in range(100,0,-2):
                p.ChangeDutyCycle(i)
                time.sleep(0.02)
led = PWM(3,50)
while True:
    process(led, input("next command:\n"))
    

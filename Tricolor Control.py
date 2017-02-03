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
    def ChangeDutyCycle(self, duty):
        self.duty = duty
    def stop(self):
        self.on = False
    def status(self):
        if self.on:
            return self.duty
        return 0
################################################################################
#############Don't touch the stuff above this line##############################
import time

red = PWM(3,50)
green = PWM(5,50)
blue = PWM(7,50)

colors = [red, green, blue]
index = 0
colors[index].start(50)

while True:
    command = input("Enter a command please:\n")
    if command == "blue":
        for color in colors:
            color.stop()
        blue.start(75)
    #need commands to turn on red and green as well
    elif command == "1":
        #increase the index and turn on the new lights
    elif len(command) == 9 and command.isdigit():
        command = int(command)
        blue.ChangeDutyCycle(command % 1000)
        #complete the other two colors and light em up
    print("Red: %3d, Green: %3d, Blue: %3d" % (red.status(), green.status(), blue.status()))
        

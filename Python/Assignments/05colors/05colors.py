import time
import virtual
#   The virtual library comes with the class PWM which may
#   called as it is below.  The PWM has several defined functions:
#   it's constructor PWM(pin, freq) requires the pin and frequency
#   of the PWM mode.  Keep the duty cycle between 0-100.
#   .start(duty) starts the pwm cycle at the duty cycle specified
#   .ChangeDutyCycle(duty) changes the duty cycle
#   .stop() turns the PWM off.
#   The duty and 'on-ness' of the PWM can be checked with .duty and .on

#########################definitions go here##########################
def off(list):
    for c in list:
        c.stop()
        

###########################code starts here###########################

red = virtual.PWM(3, 50)
green = virtual.PWM(5, 50)
blue = virtual.PWM(7, 50)

colors = [red, green, blue]
index = 0

command = "red means go"
while command != "exit":
    command = input("Please enter a command:\n")
    if command == "blue":
        off(colors)
        index = 2
        colors[index].start(100)
    #the commands for red and green should also be set
    #make sure to add a function that transitions through as well!

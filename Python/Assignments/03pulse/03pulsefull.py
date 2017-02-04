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

#for example, this line creates a PWM class called x
x = virtual.PWM(3, 50)

#this line turns this PWM on with a duty cycle of 50
x.start(50)

command = "red means go"
while command != "exit":
    command = input("Please enter a command for the PWM system:\n")
    if command == "pulse":
        while True:
            for i in range(x.duty, 101, 1):
                x.ChangeDutyCycle(i)
                time.sleep(.02)
            for i in range(x.duty, -1, -1):
                x.ChangeDutyCycle(i)
                time.sleep(.02)

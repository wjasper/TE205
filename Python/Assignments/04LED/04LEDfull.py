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
def blink(pwm):
    pwm.stop()
    time.sleep(0.25)
    pwm.start(100)
    time.sleep(0.5)
    pwm.stop()
    time.sleep(0.25)

###########################code starts here###########################

x = virtual.PWM(3, 50)

command = "red means go"
while command != "exit":
    command = input("Please enter a command for the LED:\n")
    if command == "blink":
        blink(x)
    elif command.isnumeric():
        x.ChangeDutyCycle(int(command))

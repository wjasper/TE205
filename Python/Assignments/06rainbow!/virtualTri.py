pins = {}
class PWM:
    pin = 0
    frequency = 0
    on = False
    duty = 0
    def __init__(self, channel, frequency):
        self.pin = channel
        self.frequency = frequency
        pins[channel] = self
    def start(self, duty):
        if not self.on:
            self.on = True
            self.duty = duty
        else:
            print("The light is still on, \"good job\"")
    def ChangeDutyCycle(self, duty):
        self.duty = duty
    def stop(self):
        self.on = False
    def report(self):
        if self.duty > 100 or self.duty < 0:
            return "I think it might be broken, duty = %d" % self.duty
        elif self.on:
            return "The light is on and the duty is %d" % self.duty
        else:
            return "The light is off!"
colorPins = {3: 'red', 5: 'green', 7: 'blue'}

def report():
    p = False
    for pin in pins:
        if pin in colorPins:
            if pins[pin].on:
                p = True
                print("%s is on at a duty of %d" % (colorPins[pin], pins[pin].duty))
    if not p:
        print("Nothing is on...\n")

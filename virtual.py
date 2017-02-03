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
            print("The light is still on, \"good job\"")
    def ChangeDutyCycle(self, duty):
        self.duty = duty
        print(self.report())
    def stop(self):
        self.on = False
        print(self.report())
    def report(self):
        if self.duty > 100 or self.duty < 0:
            return "I think it might be broken, duty = %d" % self.duty
        elif self.on:
            return "The light is on and the duty is %d" % self.duty
        else:
            return "The light is off!"

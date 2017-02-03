#! /usr/bin/python3
#
# Raspberry Pi Rotary Encoder Class
# $Id: rotary_class.py,v 1.2 2014/01/31 13:34:48 bob Exp $
#
# Author : Bob Rathbone
# Site   : http://www.bobrathbone.com
#
# This class uses standard rotary encoder with push switch
# 
#

import RPi.GPIO as GPIO

class RotaryEncoder:

    CLOCKWISE = 1
    ANTICLOCKWISE = 2
    BUTTONDOWN = 3
    BUTTONUP = 4
    
    rotary_a = 0
    rotary_b = 0
    rotary_c = 0
    last_state = 0
    direction = 0

    # Initialize rotary encoder object
    # Pin C should be connected to ground.
    # Pin A & B are configured as DIO inputs with pull-up resistors enabled.
    # The switch is configred as a DIO input with a pull down resistor.
    def __init__(self, pinA, pinB, button, callback):
        self.pinA = pinA
        self.pinB = pinB
        self.button = button
        self.callback = callback

        GPIO.setmode(GPIO.BCM)
		
        # The following lines enable the internal pull-up resistors
        GPIO.setwarnings(False)
        GPIO.setup(self.pinA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.pinB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        # Add event detection to the GPIO inputs
        GPIO.add_event_detect(self.pinA, GPIO.BOTH, callback=self.switch_event, bouncetime=10)
        GPIO.add_event_detect(self.pinB, GPIO.BOTH, callback=self.switch_event, bouncetime=10)
        GPIO.add_event_detect(self.button, GPIO.BOTH, callback=self.button_event, bouncetime=200)

        return

    # Call back routine called by switch events
    def switch_event(self, switch):
        # Get pin A state
        if GPIO.input(self.pinA):
            self.rotary_a = 1
        else:
            self.rotary_a = 0

        # Get pin B state
        if GPIO.input(self.pinB):
            self.rotary_b = 1
        else:
            self.rotary_b = 0

        # Create bit sequence for current state
        self.rotary_c = self.rotary_a ^ self.rotary_b
        new_state = self.rotary_a*4 + self.rotary_b*2 + self.rotary_c

        # Get the difference between the new state and the previous state
        delta = (new_state - self.last_state) % 4

        # Store current state as last_state
        self.last_state = new_state
        event = 0

        if delta == 1:
            if self.direction == self.CLOCKWISE:
                # print("Clockwise")
                event = self.direction
            else:
                self.direction = self.CLOCKWISE
        elif delta == 3:
            if self.direction == self.ANTICLOCKWISE:
                # print("Anticlockwise")
                event = self.direction
            else:
                self.direction = self.ANTICLOCKWISE

        if event > 0:
            self.callback(event)

        return


    # Push button up event
    def button_event(self, button):
        if GPIO.input(button): 
            event = self.BUTTONUP 
        else:
            event = self.BUTTONDOWN 
        self.callback(event)
        return

    # Get a switch state
    def getSwitchState(self, switch):
        return  GPIO.input(switch)

# End of RotaryEncoder class


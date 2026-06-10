#!/usr/bin/python3

import time
import sys
import os
import RPi.GPIO
import pygame
import math
from array import array
from pygame.locals import *


MorseCode = {'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',
             'E': '.',    'F': '..-.', 'G': '--.',  'H': '....',
             'I': '..',   'J': '.---', 'K': '-.-',  'L': '.-..',
             'M': '--',   'N': '-.',   'O': '---',  'P': '.--.',
             'Q': '--.-', 'R': '.-.',  'S': '...',  'T': '-',
             'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-',
             'Y': '-.--', 'Z': '--..',

             '0': '-----',  '1': '.----',  '2': '..---',
             '3': '...--',  '4': '....-',  '5': '.....',
             '6': '-....',  '7': '--...',  '8': '---..',
             '9': '----.',

             '.': '.-.-.-',  ',': '--..--', ':': '---...',
             '?': '..--..',  '-': '-....-', '/': '-..-.',
             '(': '-.--.-',  ')': '-.--.-', '"': '.-..-.',
             '@': '.--.-.',  '=': '-...-',
            }

ONE_UNIT = 0.06

THREE_UNITS = 3 * ONE_UNIT
SEVEN_UNITS = 7 * ONE_UNIT

########## sound ##############
#pygame.mixer.pre_init(44100, -16, 1, 1024)
pygame.mixer.pre_init(22050, -16, 1, 1024)
pygame.init()

class ToneSound(pygame.mixer.Sound):
  def __init__(self, frequency, volume):
    self.frequency = frequency
    pygame.mixer.Sound.__init__(self, self.build_samples2())
    self.set_volume(volume)


  def build_samples(self):
    period = int(round(pygame.mixer.get_init()[0] / self.frequency))
    samples = array("h", [0]*period)
    amplitude = 2 ** (abs(pygame.mixer.get_init()[1]) - 1) - 1
    for time in range(period):
      if time < period / 2:
        samples[time] = amplitude
      else:
        samples[time] = -amplitude
    return samples


  def build_samples2(self):
    period = int(round(pygame.mixer.get_init()[0] / self.frequency))
    samples = array("i", [0]*period)
    amplitude = 2 ** (abs(pygame.mixer.get_init()[1]) - 1) - 1
    for time in range(period):
      samples[time] = int(amplitude*math.sin(2*math.pi*time/period))
    return samples
####################################
    
def verify(string):
  keys = MorseCode.keys()
  for char in string:
    if char.upper() not in keys and char != ' ':
      sys.exit('Error the charcter ' + char + ' cannot be translated to Morse Code')

def main():
  RPi.GPIO.setwarnings(False)
  RPi.GPIO.setmode(RPi.GPIO.BCM)
  RPi.GPIO.setup(3, RPi.GPIO.OUT)
  tone_obj = ToneSound(frequency = 1600, volume = 1.0)
  msg = input('Enter Message: ')
  verify(msg)
    
  for char in msg:
    if char == ' ':
      print(' '*7)
      time.sleep(SEVEN_UNITS)
    else:
      print(MorseCode[char.upper()])
      for char2 in MorseCode[char.upper()]:
        RPi.GPIO.output(3, True) # Turn LED On
        tone_obj.play(-1) #Turn sound on
        if char2 == '.':
          time.sleep(ONE_UNIT)
        else:
          time.sleep(THREE_UNITS)
        RPi.GPIO.output(3,False) #Turn LED OFF
        tone_obj.stop()    #Turn sound off
        time.sleep(ONE_UNIT)
    time.sleep(THREE_UNITS)
                    
if __name__ == "__main__":
    main()

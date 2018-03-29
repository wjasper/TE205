import time
import RPi.GPIO as g

LPin = 3 #sets the pin that the led is connected to

g.setmode(g.BCM) #chooses to specify pin by signal rather than pinout 
g.setup(LPin, g.OUT)

# sets up a PWM on the selected pin, the two arguments are
# the pin used and the refresh rate (in Hz).  40 is the minimum
# for the human eye to detect blinking normally.  Avoid multiples of 60.
x = g.PWM(LPin, 50)

dc = 50 #the duty cycle
x.start(dc) #begins the PWM at a duty cycle of 50% so on half the time

command = "red means go" #initializing user input outside of the loop

while command != "exit":
  command = input("enter a command: ")
  if command == "h":
    print("commands:")
    print("[integer] : sets the led to [integer] duty cycle")
    print("blink : causes the led to blink")
    print("bright : causes the led to brighten to max")
    print("fade : causes the led to dim until off")
    print("pulse : causes the led to brighten and dim")
    print("exit : ends the program and cleans up the channels")
    
  # "function" to handle blinking of light
  elif command == "blink":
    repeats = input("How many times would you like to blink?")
    for null in range(int(repeats)):
      dc = 100
      x.ChangeDutyCycle(dc)
      time.sleep(0.5)
      dc = 0
      x.ChangeDutyCycle(dc)
      time.sleep(0.5)
    dc = 50
    x.ChangeDutyCycle(dc)
  
  # "function" to handle brightening the light to full shine
  elif command == "bright":
    for i in range(dc, 101, 1):
        dc = i
        x.ChangeDutyCycle(dc)
        time.sleep(0.02)
        
  # "function" to handle dimming of light to fully dim
  elif command == "fade":
    for i in range(dc, -1, -1):
        dc = i
        x.ChangeDutyCycle(dc)
        time.sleep(0.02)
        
  # "function" to handle brightening and dimming the light in succession
  elif command == "pulse":
    repeats = input("How many times would you like to pulse?")
    for null in range(int(repeats)):
      for i in range(dc, 101, 1):
        dc = i
        x.ChangeDutyCycle(dc)
        time.sleep(0.02)
      for i in range(dc, -1, -1):
        dc = i
        x.ChangeDutyCycle(dc)
        time.sleep(0.02)
        
  # "function" that cleans the Rpi before exiting the program
  elif command == exit:
    g.cleanup()
  
  # "function" that handles entry of numbers
  else:
    try:
      dc = int(command)
      x.ChangeDutyCycle(dc)
    except ValueError:
      print("unrecognized command\n type h for help")
    
    
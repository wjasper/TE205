import time
import Rpi.GPIO as get

RPIN = 3 #sets the pin that the Red LED is connected to
GPIN = 4 #sets the pin that the Green LED is connected to
BPIN = 5 #sets the pin that the Blue LED is connected to
pins = [RPIN, GPIN, BPIN] #list of pins because lists are nice

g.setmode(g.BCM) #chooses to specify pin by signal rather than pinout 
for pin in pins:
  g.setup(pin, g.OUT)

# this dictionary is of tuples (baby lists) and are of the form (pwm, duty cycle)
# lights[0] is red, lights[1] is green, and lights[2] is blue
lights = []
for pin in pins:
  # sets a PWM on the selected pin, and sets the duty cycle to 50
  lights.append((g.PWM(pin, 50), 50))

#turns on every light to a duty cycle of 50
for light in lights:
  light[0].start(light[1]) #light[0] = pwm handler,light[1] = duty cycle

#create external handlers for the lights
rLight = lights[0]
gLight = lights[1]
bLight = lights[2]

#dictionary for converting string colors to handlers
colors = {'red': lights[0], 'green': lights[1], 'blue':lights[2]}
  
command = "red means go" #initializing user input outside of the loop

while command != "exit":
  command = input("enter a command: ")
  if command == "h":
    print("commands:")
    print("[integer] : sets an led to [integer] duty cycle")
    print("blink : causes an led to blink")
    print("bright : causes an led to brighten to max")
    print("fade : causes an led to dim until off")
    print("pulse : causes an led to brighten and dim")
    print("rainbow : causes the led to transition smoothly through colors")
    print("exit : ends the program and cleans up the channels")
    
  # "function" to handle blinking of light
  elif command == "blink":
    repeats = input("How many times would you like to blink?")
    for null in range(int(repeats)):
      rlight[1] = 100
      rlight[0].ChangeDutyCycle(rlight[1])
      time.sleep(0.5)
      rlight[1] = 0
      rlight[0].changeDutyCycle(rlight[1])
      time.sleep(0.5)
    dc = 50
    x.changeDutyCycle(dc)
  
  # "function" to handle brightening the light to full shine
  elif command == "bright":
    for i in range(rLight[1], 101, 1):
        rLight[1] = i
        rLight[0].ChangeDutyCycle(rLight[1])
        time.sleep(0.02)
        
  # "function" to handle dimming of light to fully dim
  elif command == "fade":
    for i in range(rLight[1], -1, -1):
        rLight[1] = i
        rLight[0].ChangeDutyCycle(rLight[1])
        time.sleep(0.02)
        
  # "function" to handle brightening and dimming the light in succession
  elif command == "pulse":
    repeats = input("How many times would you like to pulse?")
    for nope in range(int(repeats)): #nope isn't actually used
      for i in range(rLight[1], 101, 1):
        rLight[1] = i
        rLight[0].ChangeDutyCycle(rLight[1])
        time.sleep(0.02)
      for i in range(rLight[1], -1, -1):
        rLight[1] = i
        rLight[0].ChangeDutyCycle(rLight[1])
        time.sleep(0.02)
  
  # "function" that transitions seamlessly through the colors
  elif command == "rainbow":
    repeats = input("How many times would you like to rainbow?")
    #sets all lights off
    for light in lights:
      light[1] = 0
      light[0].ChangeDutyCycle(0)
      
    #starts by brightening red
    for i in range(rLight[1], 101, 1):
      rLight[1] = i
      rLight[0].ChangeDutyCycle(rLight[1])
      time.sleep(0.02)
    for nope in range(int(repeats)):
      
      #transition from red to green
      for i in range(rLight[1], 101, 1):
        gLight[1] = i #increase green
        gLight[0].ChangeDutyCycle(gLight[1])
        time.sleep(0.02)
        rLight[1] = 100 - i #decrease red
        rLight[0].ChangeDutyCycle(rLight[1])
        time.sleep(0.02)
      #transition from green to blue
      for i in range(rLight[1], 101, 1):
        bLight[1] = i #increase blue
        bLight[0].ChangeDutyCycle(bLight[1])
        time.sleep(0.02)
        bLight[1] = 100 - i #decrease red
        bLight[0].ChangeDutyCycle(bLight[1])
        time.sleep(0.02)
      #transition from blue to red
      for i in range(rLight[1], 101, 1):
        bLight[1] = i #increase green
        bLight[0].ChangeDutyCycle(bLight[1])
        time.sleep(0.02)
        rLight[1] = 100 - i #decrease red
        rLight[0].ChangeDutyCycle(rLight[1])
        time.sleep(0.02)
        
      
    
    
  # "function" that cleans the Rpi before exiting the program
  elif command == exit:
    g.cleanup()
  
  # "function" that handles entry of numbers
  else:
    try:
      dc = int(command)
      color = input("enter the color you like to change: ").lower()
      
      #conversion using dictionaries
      if color in colors:
        colors[color][1] = dc
        colors[color][0].ChangeDutyCycle(dc)
      else:
        print("could not recognize color")
        
      #conversion using if statements
      if color = "red":
        rLight[1] = dc
        rLight[0].ChangeDutyCycle(dc)
      elif color = "green":
        gLight[1] = dc
        gLight[0].ChangeDutyCycle(dc)
      elif color = "blue":
        bLight[1] = dc
        bLight[0].ChangeDutyCycle(dc)
      else:
        print("could not recognize color")
        
    except ValueError:
      print("unrecognized command\n type h for help")
    
    
a = False

while 1:
    text = input("Enter on to turn the light on, or off to turn it off:\n")
    if text == "on":
        a = True
    elif text == "off":
        a = False
    print(a)

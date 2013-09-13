
def revciph():

    message = raw_input("Please enter some text ")
    translate = ""

    i = len(message) -1

    while i >= 0:
        translate = translate + message[i]
        i = i -1

    print(translate)


revciph()

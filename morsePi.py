import  RPi.GPIO as GPIO
import time
from threading import Timer

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP)

def timeout():
    global buffer
    if(buffer != ""):
        letter = morse_to_letter(buffer)
        print (letter)
        buffer = ""
        output = 1

def timeout2():
    global output
    if(output == True):
        print (" ")

def morse_to_letter(arg):
    switcher = {
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
        "-..": "D",
        ".": "E",
        "..-.": "F",
        "--.": "G",
        "....": "H",
        "..": "I",
        ".---": "J",
        "-.-": "K",
        ".-..": "L",
        "--": "M",
        "-.": "N",
        "---": "O",
        ".--.": "P",
        "--.-": "Q",
        ".-.": "R",
        "...": "S",
        "-": "T",
        "..-": "U",
        "...-": "V",
        ".--": "W",
        "-..-": "X",
        "-.--": "Y",
        "--..": "Z",
        "-----": "0",
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9",
    }
    return switcher.get(arg, arg)

output = 0
buffer = ""
previous = "null"
start = 0
end = 0
duration = 0
t = Timer(2.0, timeout)
t2 = Timer(4.0, timeout2)

while True:

    inputValue = GPIO.input(18)

    # Morse switch is active
    if (inputValue == False and previous == "open" or inputValue == False and previous == "null"):
        t.cancel()
        t2.cancel()
        start = time.time()
        previous = "closed"
    
    # Morse switch is inactive
    if (inputValue != False and previous == "closed"):
        end = time.time()
        duration = end - start
        previous = "open"

        if (duration < 0.2):
                value = "."
        else:
                value = "-"

        buffer = buffer + value
        
        t = Timer(2.0, timeout)
        t.start()
        t2 = Timer(4.0, timeout2)
        t2.start()
    time.sleep(0.05)

GPIO.cleanup(18)
import  RPi.GPIO as GPIO
import time
from threading import Timer

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP)

buffer = ""
previous = "null"
start = 0
end = 0
duration = 0
character = "null"

def timeout():
    global buffer
    if(buffer != ""):
        letter = morse_to_letter(buffer)
        print letter
        buffer = ""

t = Timer(2.0, timeout)

def morse_to_letter(arg):
    switcher = {
        ".-": "A (.-)",
        "-...": "B (-...)",
        "-.-.": "C (-.-.)",
        "-..": "D (-..)",
        ".": "E (.)",
        "..-.": "F (..-.)",
        "--.": "G (--.)",
        "....": "H (....)",
        "..": "I (..)",
        ".---": "J (.---)",
        "-.-": "K (-.-)",
        ".-..": "L (.-..)",
        "--": "M (--)",
        "-.": "N (-.)",
        "---": "O (---)",
        ".--.": "P (.--.)",
        "--.-": "Q (--.-)",
        ".-.": "R (.-.)",
        "...": "S (...)",
        "-": "T (-)",
        "..-": "U (..-)",
        "...-": "V (...-)",
        ".--": "W (.--)",
        "-..-": "X (-..-)",
        "-.--": "Y (-.--)",
        "--..": "Z (--..)",
        "-----": "0 (-----)",
        ".----": "1 (.----)",
        "..---": "2 (..---)",
        "...--": "3 (...--)",
        "....-": "4 (....-)",
        ".....": "5 (.....)",
        "-....": "6 (-....)",
        "--...": "7 (--...)",
        "---..": "8 (---..)",
        "----.": "9 (----.)",
    }
    return switcher.get(arg, arg)

while True:

    inputValue = GPIO.input(18)

    if (inputValue == False and previous == "open" or inputValue == False and previous == "null"):
        start = time.time()
        end = 0
        duration = 0
        previous = "closed"
    if (inputValue != False and previous == "closed" or inputValue != False and previous == "null"):
        t.cancel
        end = time.time()
        duration = end - start

        if (previous != "null"):
            if (duration < 0.25):
                    buffer = ".%s" % (buffer)
            else:
                    buffer = "-%s"% (buffer)
        previous = "open"
        t = Timer(3.0, timeout)
        t.start()
    time.sleep(0.05)

GPIO.cleanup(18)
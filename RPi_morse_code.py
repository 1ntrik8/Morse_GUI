# Leigh Rowell
# ID: 219309149
# SIT210 - 5.3D
# RPi Morse Code using GUI

from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import time
RPi.GPIO.setmode(RPi.GPIO.BCM)

# Hardware
led = LED(14)

# GUI Definitions
win=Tk()
win.title("SIT210 - 5.3D")
win.geometry("250x90")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = 'bold')

# Variables
unitTime = 0.25				# single time unit in seconds...
dotTime = unitTime 			# time period for LED to illuminate, representing a dot.
dashTime = unitTime * 3 		# time period for LED to illuminate, representing a dash.
nextFlashPause = unitTime		# time period to delay between dot/dash in a single character.
nextCharPause = unitTime * 3	 	# time period to pause between letters.
nextWordPause = unitTime * 7 		# time period to pause between words.

# Event functions
def wait(waitTime):
    time.sleep(waitTime)

def dot():
    led.on()
    wait(dotTime)
    led.off()
def dash():
    led.on()
    wait(dashTime)
    led.off()
def nextChar():
    wait(nextCharPause)
def nextWord():
    wait(nextWordPause)
def nextFlash():
    wait(nextFlashPause)


# Letter functions
def A():
    dot()
    nextFlash()
    dash()
def B():
    dash()
    nextFlash()
    dot()
    nextFlash()
    dot()
    nextFlash()
    dot()
def C():
    dash()
    nextFlash()
    dot()
    nextFlash()
    dash()
    nextFlash()
    dot()
def D():
    dash()
    nextFlash()
    dot()
    nextFlash()
    dot()
def E():
    dot()
def F():
    dot()
    nextFlash()
    dot()
    nextFlash()
    dash()
    nextFlash()
    dot()
def G():
    dash()
    nextFlash()
    dash()
    nextFlash()
    dot()
def H():
    dot()
    nextFlash()
    dot()
    nextFlash()
    dot()
    nextFlash()
    dot()
def I():
    dot()
    nextFlash()
    dot()
def J():
    dot()
    nextFlash()
    dash()
    nextFlash()
    dash()
    nextFlash()
    dash()
def K():
    dash()
    nextFlash()
    dot()
    nextFlash()
    dash()
def L():
    dot()
    nextFlash()
    dash()
    nextFlash()
    dot()
    nextFlash()
    dot()
def M():
    dash()
    nextFlash()
    dash()
def N():
    dash()
    nextFlash()
    dot()
def O():
    dash()
    nextFlash()
    dash()
    nextFlash()
    dash()
def P():
    dot()
    nextFlash()
    dash()
    nextFlash()
    dash()
    nextFlash()
    dot()
def Q():
    dash()
    nextFlash()
    dash()
    nextFlash()
    dot()
    nextFlash()
    dash()
def R():
    dot()
    nextFlash()
    dash()
    nextFlash()
    dot()
def S():
    dot()
    nextFlash()
    dot()
    nextFlash()
    dot()
def T():
    dash()
def U():
    dot()
    nextFlash()
    dot()
    nextFlash()
    dash()
def V():
    dot()
    nextFlash()
    dot()
    nextFlash()
    dot()
    nextFlash()
    dash()
def W():
    dot()
    nextFlash()
    dash()
    nextFlash()
    dash()
def X():
    dash()
    nextFlash()
    dot()
    nextFlash()
    dot()
    nextFlash()
    dash()
def Y():
    dash()
    nextFlash()
    dot()
    nextFlash()
    dash()
    nextFlash()
    dash()
def Z():
    dash()
    nextFlash()
    dash()
    nextFlash()
    dot()
    nextFlash()
    dot()
def Space():
    wait(unitTime * 3)
def NewLine():
    dot()
    nextFlash()
    dash()
    nextFlash()
    dot()
    nextFlash()
    dash()


def close():
    RPi.GPIO.cleanup()
    win.destroy()

def morseSwitch(arg):
    # Set up a dictionary of letters to functions.
    mSwitch = {
        'a': A,
        'b': B,
        'c': C,
        'd': D,
        'e': E,
        'f': F,
        'g': G,
        'h': H,
        'i': I,
        'j': J,
        'k': K,
        'l': L,
        'm': M,
        'n': N,
        'o': O,
        'p': P,
        'q': Q,
        'r': R,
        's': S,
        't': T,
        'u': U,
        'v': V,
        'w': W,
        'x': Y,
        'z': Z,
        ' ': Space
        }
    # Create lambda function from the letter function..
    morseFunc = mSwitch.get(arg, lambda: "Invalid Entry")
    # Call the function.
    morseFunc()

def run():
    textString = str(textBox.get().lower())
    for character in textString:
        morseSwitch(character)
        nextChar()

## widgets
# GUI items:
textBox = tkinter.Entry(win)
textBox.pack()

runButton = Button(win, text = "Run Morse Code", command = run, height = 1, width = 12)
runButton.pack()

exitButton = Button(win, text = "Exit", command = close, height = 1, width = 12)
exitButton.pack()

win.protocol("WM_DELETE_WINDOW", close) # Close cleanly when clicking window X..

win.mainloop() # Loop forever and keep GUI running.
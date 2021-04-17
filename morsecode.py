import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

led = 8
buzzer = 12

GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(buzzer, GPIO.OUT, initial=GPIO.LOW)

MORSE_CODE = { ' ':' ', 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..',
	'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..',
	'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.',
	'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...',
	'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
	'Y':'-.--', 'Z':'--..', ',':'---..', '.':'.-.-.-',
	'?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.',
	')':'-.--.-'
}

import time

def encrypt(text):
	for letter in text:
		for element in MORSE_CODE[letter.upper()]:
			if element == '.':
				GPIO.output(led, GPIO.HIGH); GPIO.output(buzzer, GPIO.HIGH)
				time.sleep(0.1)
				GPIO.output(led, GPIO.LOW); GPIO.output(buzzer, GPIO.LOW)
				time.sleep(0.1) # Each dot or dash is followed by a blank period
			elif element == '-':
				GPIO.output(led, GPIO.HIGH); GPIO.output(buzzer, GPIO.HIGH)
				time.sleep(0.3) # Duration of dash is 3 times the dot
				GPIO.output(led, GPIO.LOW); GPIO.output(buzzer, GPIO.LOW)
				time.sleep(0.1) # Each dot or dash is followed by a blank period
			else:
				time.sleep(0.4) # Space between words is 7 dots duration
		time.sleep(0.3) # Space between letters is 3 dots duration

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("morsecode.py")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Enter text").grid(column=1, row=1)

text = StringVar()
textbox = ttk.Entry(mainframe, textvariable=text)
textbox.grid(column=1, row=2)
textbox.focus()

button = ttk.Button(mainframe, text="Convert", command=lambda:encrypt(text.get()))
button.grid(column=1, row=3)

root.mainloop()

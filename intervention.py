import RPi.GPIO as GPIO
from time import sleep
import datetime
import subprocess

# !IMPORTANT! assign unique name to device
deviceName = testDevice

# setup GPIO
# GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(21, GPIO.IN)
GPIO.setup(27, GPIO.IN)

buttonA = GPIO.input(23)
buttonB = GPIO.input(24)
buttonC = GPIO.input(25)
buttonD = GPIO.input(26)
#phoneButton = GPIO.input(27)
#stopButton = GPIO.input(27)
phoneButton = True

GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

# filenames
questionA = 'question_a.mp3'
questionB = 'question_b.mp3'
questionC = 'question_c.mp3'
questionD = 'question_d.mp3'

record = None

def StartRecord():
	global record
	record = subprocess.Popen([], shell=True)

def StopRecord():

def PlayRecord():


while True:
	while(phoneButton == True):
		if(buttonA == GPIO.HIGH):
			
		elif(buttonB == GPIO.HIGH):
		 	
		elif(buttonC == GPIO.HIGH):
		 	
		elif(buttonD == GPIO.HIGH):
		 	
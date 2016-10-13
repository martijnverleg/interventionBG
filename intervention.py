import RPi.GPIO as GPIO
from time import sleep
import datetime
import subprocess

# !IMPORTANT! assign unique name to device
deviceName = "testDevice"

# setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(21, GPIO.IN)
GPIO.setup(27, GPIO.IN)

buttonA = GPIO.input(12)
buttonB = GPIO.input(16)
buttonC = GPIO.input(18)
buttonD = GPIO.input(21)
#phoneButton = GPIO.input(27)
stopButton = GPIO.input(27)
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
userChoice = None

def StartRecord():
	global record
	record = subprocess.Popen(["arecord sound.wav"], shell=True)

def StopRecord():
	record.terminate()
	subprocess.Popen(["pkill aplay"], shell=True)

def PlayIntro():
	subprocess.Popen(["aplay sound.wave"], shell=True)

def PlayQuestion(question):
	subprocess.Popen(["aplay %s.wave"], shell=True) % question

def ChangeFileName(choice):
	currentTime = datetime.datetime.now().strftime ("%m%d_%H%M%S")
	fileName = "%s_%s_%s.wav" % (deviceName, choice, currentTime)
	subprocess.Popen(["mv record.wav %s"], shell=True) % fileName

while True:
	while(phoneButton == True):
		StartRecord()
		PlayIntro()

		if(buttonA == GPIO.HIGH):
			PlayQuestion(questionA)
			userChoice = A
		elif(buttonB == GPIO.HIGH):
		 	PlayQuestion(questionB)
		 	userChoice = B
		elif(buttonC == GPIO.HIGH):
		 	PlayQuestion(questionC)
		 	userChoice = C
		elif(buttonD == GPIO.HIGH):
		 	PlayQuestion(questionD)
		 	userChoice = D

		StopRecord()
		ChangeFileName(userChoice)
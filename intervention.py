import RPi.GPIO as GPIO
import time
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
questionA = 'question_a.wav'
questionB = 'question_b.wav'
questionC = 'question_c.wav'
questionD = 'question_d.wav'

record = None


def StartRecord():
	global record
	record = subprocess.Popen(["arecord -D plughw:1,0 record.wav"], shell=True)

def StopRecord():
	record.terminate()
	time.sleep(1)
	subprocess.Popen(["pkill aplay"], shell=True)

def PlayIntro():
	subprocess.Popen(["aplay -D plughw1:,0 intro.wav"], shell=True)

def PlayQuestion(question):
	command = "aplay -D plughw1:,0 %s" % question
	subprocess.Popen([command], shell=True) 

def ChangeFileName(choice):
	currentTime = datetime.datetime.now().strftime ("%m%d_%H%M%S")
	fileName = "%s_%s_%s.wav" % (deviceName, choice, currentTime)
	command = "mv record.wav %s" % fileName
	subprocess.Popen([command], shell=True)

while True:
	while(phoneButton == True):
		StartRecord()
		PlayIntro()
		userChoice = None

		if(buttonA == GPIO.HIGH):
			PlayQuestion(questionA)
			userChoice = "A"
		elif(buttonB == GPIO.HIGH):
		 	PlayQuestion(questionB)
		 	userChoice = "B"
		elif(buttonC == GPIO.HIGH):
		 	PlayQuestion(questionC)
		 	userChoice = "C"
		elif(buttonD == GPIO.HIGH):
		 	PlayQuestion(questionD)
		 	userChoice = "D"

		StopRecord()
		ChangeFileName(userChoice)
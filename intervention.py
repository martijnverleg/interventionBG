import RPi.GPIO as GPIO
import time
import datetime
import subprocess

# !IMPORTANT! assign unique name to device
deviceName = "testDevice"

# setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.cleanup
"""
GPIO.setwarnings(False)
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
"""
# filenames
questionA = 'question_a.wav'
questionB = 'question_b.wav'
questionC = 'question_c.wav'
questionD = 'question_d.wav'

record = None

GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



def StartRecord():
	global record
	record = subprocess.Popen(["arecord -D plughw:1,0 record.wav"], shell=True)
	time.sleep(2)

def StopRecord():
	record.terminate()
	time.sleep(1)
	subprocess.Popen(["pkill arecord"], shell=True)
	time.sleep(1)

def PlayIntro():
	subprocess.Popen(["aplay intro.wav"], shell=True)

def PlayQuestion(question):
	command = "aplay %s" % question
	subprocess.Popen([command], shell=True) 

def ChangeFileName(choice):
	currentTime = datetime.datetime.now().strftime ("%m%d_%H%M%S")
	fileName = "%s_%s_%s.wav" % (deviceName, choice, currentTime)
	command = "mv record.wav %s" % fileName
	subprocess.Popen([command], shell=True)

def Blink(amount, pin, delay):
	for x in range (0, amount):
		GPIO.output(pin, 1)
		time.sleep(delay)
		GPIO.output(pin, 0)
		time.sleep(delay)

while True:
	buttonA = GPIO.input(23)
	buttonB = GPIO.input(16)
	
	if(buttonA == True):
		Blink(3, 12, 0.5)


"""
while True:
	while(phoneButton == True):
		StartRecord()
		PlayIntro()
		userChoice = None

		print(buttonA)
		print(buttonB)
		print(buttonC)
		print(buttonD)

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
	
		GPIO.cleanup()
"""
import RPi.GPIO as GPIO
import time
import datetime
import subprocess

# !IMPORTANT! assign unique name to device
deviceName = "testDevice"

# setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
"""
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

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
"""
while True:
	buttonA = GPIO.input(23)
	buttonB = GPIO.input(16)
	
	if(buttonA == False):
		GPIO.output(18, 1)
	elif(buttonA == True):
		GPIO.output(18, 0)

	if(buttonB == False):
		GPIO.output(12, 1)
	elif(buttonB == True):
		GPIO.output(12, 0)

	time.sleep(0.1)
"""
while True:
	#phoneButton = GPIO.input(27)
	phoneButton = True
	
	while(phoneButton == True):
		buttonA = GPIO.input(23)
		buttonB = GPIO.input(16)

		"""
		buttonA = GPIO.input(12)
		buttonB = GPIO.input(16)
		buttonC = GPIO.input(18)
		buttonD = GPIO.input(21)
		stopButton = GPIO.input(27)
		"""

		StartRecord()
		PlayIntro()
		userChoice = None
		waitForInput = True

		while waitForInput == True:
			print("waiting for input...")
			if(buttonA == False):
				PlayQuestion(questionA)
				userChoice = "A"
				Blink(3, 18, 0.5)
				waitForInput = False
			elif(buttonB == False):
			 	PlayQuestion(questionB)
			 	userChoice = "B"
			 	Blink(3, 12, 0.5)
			 	waitForInput = False
			"""
			elif(buttonC == GPIO.HIGH):
			 	PlayQuestion(questionC)
			 	userChoice = "C"
			 	Blink(3, 12, 0.5)
			 	waitForInput = False
			elif(buttonD == GPIO.HIGH):
			 	PlayQuestion(questionD)
			 	userChoice = "D"
			 	Blink(3, 12, 0.5)
			 	waitForInput = False
			"""

		StopRecord()
		ChangeFileName(userChoice)
	
		#GPIO.cleanup()
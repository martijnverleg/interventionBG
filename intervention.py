import RPi.GPIO as GPIO
import time
import datetime
import subprocess

# !IMPORTANT! assign unique name to device
deviceName = "veiligheid"

# !IMPORTANT! max recording time in seconds
maxRecordTime = 300

inPinA = 12
inPinB = 16
inPinC = 20
inPinD = 21
outPinA = 6
outPinB = 13
outPinC = 19
outPinD = 26
phonePin = 18
stopPin = 17

# setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(inPinA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(inPinB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(inPinC, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(inPinD, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(phonePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(stopPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(outPinA, GPIO.OUT)
GPIO.setup(outPinB, GPIO.OUT)
GPIO.setup(outPinC, GPIO.OUT)
GPIO.setup(outPinD, GPIO.OUT)

# filenames
questionA = 'question_a.wav'
questionB = 'question_b.wav'
questionC = 'question_c.wav'
questionD = 'question_d.wav'

record = None

def StartRecord():
	global record
	record = subprocess.Popen(["arecord -D plughw:1,0 record.wav"], shell=True)
	time.sleep(2)

def StopRecord():
	record.terminate()
	time.sleep(1)
	subprocess.Popen(["pkill arecord"], shell=True)
	time.sleep(1)

def PlayIntro(folder):
	command = "aplay %s/intro.wav" % folder
	subprocess.Popen([command], shell=True)

	if(folder == "jezelf"): 
		time.sleep(60)
		Blink(3, outPinA, 0.333)
		GPIO.output(outPinA, 1)
		Blink(3, outPinB, 0.333)
		GPIO.output(outPinB, 1)
		Blink(3, outPinC, 0.333)
		GPIO.output(outPinC, 1)
		Blink(3, outPinD, 0.333)
		GPIO.output(outPinD, 1)
	elif(folder == "samenleving"):
		time.sleep(82)
		Blink(3, outPinA, 0.333)
		GPIO.output(outPinA, 1)
		Blink(3, outPinB, 0.333)
		GPIO.output(outPinB, 1)
		Blink(3, outPinC, 0.333)
		GPIO.output(outPinC, 1)
		Blink(3, outPinD, 0.333)
		GPIO.output(outPinD, 1)
	elif(folder == "vrijheid"):
		time.sleep(80)
		Blink(3, outPinA, 0.333)
		GPIO.output(outPinA, 1)
		Blink(3, outPinB, 0.333)
		GPIO.output(outPinB, 1)
		Blink(3, outPinC, 0.333)
		GPIO.output(outPinC, 1)
		Blink(3, outPinD, 0.333)
		GPIO.output(outPinD, 1)
	elif(folder == "zekerheid"):
		time.sleep(62)
		Blink(3, outPinA, 0.333)
		GPIO.output(outPinA, 1)
		Blink(3, outPinB, 0.333)
		GPIO.output(outPinB, 1)
		Blink(3, outPinC, 0.333)
		GPIO.output(outPinC, 1)
		Blink(3, outPinD, 0.333)
		GPIO.output(outPinD, 1)

def PlayQuestion(folder, question):
	subprocess.Popen(["pkill aplay"], shell=True)
	time.sleep(0.1)
	command = "aplay %s/%s" % (folder, question)
	subprocess.Popen([command], shell=True)

def PlayOutro(folder):
	command = "aplay %s/outro.wav" % folder
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
	phoneButton = GPIO.input(phonePin)

	while(phoneButton == True):
		GPIO.output(outPinA, 1)
		GPIO.output(outPinB, 1)
		GPIO.output(outPinC, 1)
		GPIO.output(outPinD, 1)
		
		userChoice = None
		waitForInput = True
		isRecording = True
		startTime = time.time()
		runTime = 0

		StartRecord()
		PlayIntro(deviceName)

		while waitForInput == True:
			buttonA = GPIO.input(inPinA)
			buttonB = GPIO.input(inPinB)
			buttonC = GPIO.input(inPinC)
			buttonD = GPIO.input(inPinD)

			if(buttonA == False):
				PlayQuestion(deviceName, questionA)
				userChoice = "A"
				Blink(3, outPinA, 0.5)
				GPIO.output(outPinA, 1)
				waitForInput = False

			elif(buttonB == False):
			 	PlayQuestion(deviceName, questionB)
			 	userChoice = "B"
			 	Blink(3, outPinB, 0.5)
			 	GPIO.output(outPinB, 1)
			 	waitForInput = False

			elif(buttonC == False):
			 	PlayQuestion(deviceName, questionC)
			 	userChoice = "C"
			 	Blink(3, outPinC, 0.5)
			 	GPIO.output(outPinC, 1)
			 	waitForInput = False

			elif(buttonD == False):
			 	PlayQuestion(deviceName, questionD)
			 	userChoice = "D"
			 	Blink(3, outPinD, 0.5)
			 	GPIO.output(outPinD, 1)
			 	waitForInput = False

		while isRecording == True: 
			runTime = int(float(time.time() - startTime))
			stopButton = GPIO.input(stopPin)
			if(stopButton == False):
				StopRecord()
				isRecording = False
			elif(runTime > maxRecordTime):
				StopRecord()
				isRecording = False

		PlayOutro(deviceName)

		ChangeFileName(userChoice)

		phoneButton = False
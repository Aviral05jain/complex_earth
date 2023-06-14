import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24, GPIO.IN)
GPIO.setup(23, GPIO.IN)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
while 1:
	a=GPIO.input(24)
	b=GPIO.input(23)
	print("THE VALUE OF PIN 24 IS= %d" %a)
	print("THE VALUE OF PIN 23 IS= %d" %b)
	print("--------------------")
	time.sleep(1)
	if a==0:
		print("sadi value is 0 24 pin switch1 is ON ")
		GPIO.output(17,1)
		time.sleep(.2)		
		GPIO.output(17,0)
		time.sleep(.2)
		GPIO.output(17,1)
		time.sleep(.2)		
		GPIO.output(17,0)
		time.sleep(.2)
	elif b==0:
		print("sadi value is 0 24 pin switch1 is ON ")
		GPIO.output(27,1)
		time.sleep(.2)		
		GPIO.output(27,0)
		time.sleep(.2)
		GPIO.output(27,1)
		time.sleep(.2)		
		GPIO.output(27,0)
		time.sleep(.2)
									
	else:
		print("no switch pressed")
		GPIO.output(22,1)
		time.sleep(.2)		
		GPIO.output(22,0)
		time.sleep(.2)
		GPIO.output(22,1)
		time.sleep(.2)		
		GPIO.output(22,0)
		time.sleep(.2)	


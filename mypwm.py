import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
x = GPIO.PWM(17,50)
x.start(0)
while 1:
	x.ChangeDutyCycle(5)
	time.sleep(1)
	x.ChangeDutyCycle(10)
	time.sleep(4)	
	x.ChangeDutyCycle(80)
	time.sleep(1)
	x.ChangeDutyCycle(99)
	time.sleep(1)		
x.stop()
GPIO.cleanup()
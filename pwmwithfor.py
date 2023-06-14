import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.output(17,0)
GPIO.output(27,0)
GPIO.output(22,0)
x = GPIO.PWM(17,50)
y = GPIO.PWM(27,50)
z = GPIO.PWM(22,50)
x.start(5)
y.start(5)
z.start(5)
while 1:
	x.start(5)
	for i in range(0,100,5):
		x.ChangeDutyCycle(i)
		print (i)
		time.sleep(0.2)
	x.stop()
	y.start(5)
	for j in range(0,100,5):
		y.ChangeDutyCycle(j)
		print (j)
		time.sleep(0.2)	
	y.stop()
	z.start(5)
	for k in range(0,100,5):
		z.ChangeDutyCycle(k)
		print (k)
		time.sleep(0.2)			
	z.stop()
x.stop()
y.stop()
z.stop()
GPIO.cleanup()
import RPi.GPIO as gp	
import time
gp.setmode(gp.BCM)
b = [17,27,22,5,6,13,19]  #list
for i in range (7):
	print (" pin %d is output "  %b[i])
	gp.setup(b[i], gp.OUT)

while True:
	gp.output(17,1)
	gp.output(27,1)
	gp.output(22,1)
	gp.output(5,0)
	gp.output(6,0)
	gp.output(13,0)
	gp.output(19,0)
	time.sleep(1)
	gp.output(17,0)
	gp.output(27,0)
	gp.output(22,0)
	gp.output(5,1)
	gp.output(6,1)
	gp.output(13,1)
	gp.output(19,1)
	time.sleep(1)

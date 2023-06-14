import RPi.GPIO as gp	
import time
gp.setmode(gp.BCM)
b = [17,27,22,5,6,13,19]  #list
for i in range (7):
	print (" pin %d is output "  %b[i])
	gp.setup(b[i], gp.OUT)

while True:
	for i in range (7):
		print(i)
		print ("our pin %d "  %b[i])
		gp.output(b[i],1)
		time.sleep(0.3)
	for i in range (7):
		print(i)
		print ("our pin %d "  %b[i])
		gp.output(b[i],0)
		time.sleep(0.3)
	for i in range (6,0,-1):
		print(i)
		print ("our pin %d "  %b[i])
		gp.output(b[i],1)
		time.sleep(0.3)					
	for i in range (6,0,-1):
		print(i)
		print ("our pin %d "  %b[i])
		gp.output(b[i],0)
		time.sleep(0.3)

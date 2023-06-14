from w1thermsensor import W1ThermSensor
from time import sleep 
Dhami = W1ThermSensor()

while 1:
	mytemp = gna.get_temperature()
	print (mytemp)
	sleep(2)


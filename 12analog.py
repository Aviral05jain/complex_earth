import time
import Netmaxiot
while 1:
	read=Netmaxiot.analogRead(0)
	print("the reading is = %d"%read)
	chd=read*4.88757
	print("----------------")
	print("the reading is = %0.3f mV"%chd)
	time.sleep(2)
    
	

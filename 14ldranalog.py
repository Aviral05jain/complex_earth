import time
import Netmaxiot
while 1:
	read1=Netmaxiot.analogRead(0)
	read2=Netmaxiot.analogRead(1)
	print("the reading is = %d"%read1)
	print("the reading is = %d"%read2)
	vol1=read1*4.887586
	vol2=read2*4.887586
	print("----------------")
	print("the reading c1 is = %0.3f mV"%vol1)
	print("the reading c2 is = %0.3f mV"%vol2)
	light=vol2/5000
	light=light*100
	print("----------------")
	print("----------------")
	print("the room light is = %0.3f percent"%light)
	time.sleep(2)
	print("----------------")
	print("----------------")
	

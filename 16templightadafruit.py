from Adafruit_IO import Client
###################################
import time
import Netmaxiot
user = "netmaxworkshop"
key = "aio_LEFc50upAUxDguGXVr8XTIesJNwp"
io = Client(user,key)  
#################################
tempi = io.feeds("tempx")
lighti = io.feeds("lightx")

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
	temp=vol1/10
	print("----------------")
	print("----------------")
	print("the temp is = %0.3f *C"%temp)	
	time.sleep(2)
	print("----------------")
	print("----------------")
	io.send(tempi.key,temp)
	io.send(lighti.key,light)
	print("-value sent-- to io cloud")
	time.sleep(6)


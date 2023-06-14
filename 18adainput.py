from Adafruit_IO import Client
import time
import Netmaxiot
user = "netmaxworkshop"
key = "aio_LEFc50upAUxDguGXVr8XTIesJNwp"
io = Client(user,key)
Netmaxiot.pinMode(2,"OUTPUT")
Netmaxiot.pinMode(3,"OUTPUT")
s1 = io.feeds('sw1')
s2 = io.feeds('sw2')
while 1:
	data1 =io.receive(s1.key)
	data2 =io.receive(s2.key)
	print("-------------------")
	print("cloud ka data")
	print("-------------------")
	print("-------------------")
	print(data1)
	print("-------------------")
	print("-------------------")
	x= int(data1.value)
	if x==1: 
		Netmaxiot.digitalWrite(2,1)
	else :
		Netmaxiot.digitalWrite(2,0)
		



from Adafruit_IO import Client
import time
import Netmaxiot
user = "netmaxworkshop"
key = "aio_LEFc50upAUxDguGXVr8XTIesJNwp"
io = Client(user,key)
##################################3
Netmaxiot.pinMode(2,"OUTPUT")
Netmaxiot.pinMode(3,"OUTPUT")
##########################
s1 = io.feeds('sw1')  
s2 = io.feeds('sw2')

while 1:
	data1 =io.receive(s1.key) # string data  "value:'1'" 
	data2 =io.receive(s2.key)
	print ("-----------")
	print ("-----------")
	print ("data ay gaya-- ")
	print ("-----------")
	print ("-----------")
	print (data1)
	print ("-----------")
	print ("-----------")
	print (data2)
	print ("-----------")
	print ("-----------")
	print ("-----------")
	time.sleep(2)
	x= int(data1.value)
	z= int(data2.value)
	if (x==1):
		Netmaxiot.digitalWrite(2,1)
	else :
		Netmaxiot.digitalWrite(2,0)
	if (z==1):
		Netmaxiot.digitalWrite(3,1)
	else :
		Netmaxiot.digitalWrite(3,0)
	time.sleep(2)				
# char int double float boolen 


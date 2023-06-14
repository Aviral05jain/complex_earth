from Adafruit_IO import Client
import RPi.GPIO as GPIO
import dht11
###################################
import time
import Netmaxiot
####################3
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  
GPIO.cleanup()
#############
mydht = dht11.DHT11(pin=25)
dtemp=0
dhum=0
user = "netmaxworkshop"
key = "aio_LEFc50upAUxDguGXVr8XTIesJNwp"
io = Client(user,key)  
#################################
tempi = io.feeds("tempx")
lighti = io.feeds("lightx")
dtempi = io.feeds("dtempx")
dhumi = io.feeds("dhumx")
while 1:
	result = mydht.read()
	time.sleep(2)
	if result.is_valid():
		dtemp=result.temperature
		dhum=result.humidity
		print("T: %0.2f C" %dtemp)
		print("H: %0.1f percent" %dhum)
	else:
		print("E:no %d dht11 off" % result.error_code)
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
	time.sleep(5)
	print("----------------")
	print("----------------")
	io.send(tempi.key,temp)
	io.send(lighti.key,light)
	io.send(dtempi.key,dtemp)
	io.send(dhumi.key,dhum)
	print("-value sent-- to io cloud")
	time.sleep(12)


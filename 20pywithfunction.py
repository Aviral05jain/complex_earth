import time
import Netmaxiot

def pinsetout():
	Netmaxiot.pinMode(2,"OUTPUT")
	Netmaxiot.pinMode(3,"OUTPUT")
	Netmaxiot.pinMode(4,"OUTPUT")
	Netmaxiot.pinMode(5,"OUTPUT")
	Netmaxiot.pinMode(6,"OUTPUT")
	Netmaxiot.pinMode(7,"OUTPUT")

def myvalue():
	print("this is my first function")
	Netmaxiot.digitalWrite(2,1)
	Netmaxiot.digitalWrite(3,1)
	Netmaxiot.digitalWrite(4,1)
	Netmaxiot.digitalWrite(5,1)
	Netmaxiot.digitalWrite(6,1)
	Netmaxiot.digitalWrite(7,1)
	print ("2 on")
	time.sleep(.1)
	Netmaxiot.digitalWrite(2,0)
	Netmaxiot.digitalWrite(3,0)
	Netmaxiot.digitalWrite(4,0)
	Netmaxiot.digitalWrite(5,0)
	Netmaxiot.digitalWrite(6,0)
	Netmaxiot.digitalWrite(7,0)
	print ("2 off")
	time.sleep(.1)

def myvalue2():
	print("this is my first function")
	Netmaxiot.digitalWrite(2,1)
	Netmaxiot.digitalWrite(3,0)
	Netmaxiot.digitalWrite(4,1)
	Netmaxiot.digitalWrite(5,0)
	Netmaxiot.digitalWrite(6,1)
	Netmaxiot.digitalWrite(7,0)
	print ("2 on")
	time.sleep(.1)
	Netmaxiot.digitalWrite(2,0)
	Netmaxiot.digitalWrite(3,1)
	Netmaxiot.digitalWrite(4,0)
	Netmaxiot.digitalWrite(5,1)
	Netmaxiot.digitalWrite(6,0)
	Netmaxiot.digitalWrite(7,1)
	print ("2 off")
	time.sleep(.1)

print("starting program")
time.sleep(1)
pinsetout()

while 1:
	myvalue()
	time.sleep(1)
	myvalue2()
	time.sleep(1)



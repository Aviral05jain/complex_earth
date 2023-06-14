import time
import Netmaxiot
mylist = [4,3,2,9,8,5,6,7]  #list
for i in range (8):
	print (" pin %d is output "  %mylist[i])
	Netmaxiot.pinMode(mylist[i],"OUTPUT")
for i in range (8):
	print (" pin %d is 0 "  %mylist[i])
	Netmaxiot.digitalWrite(mylist[i],0)

time.sleep(1)

try:
	while 1:
		for i in range(5):
			for i in range (8):
				#print (" pin %d is 1 "  %mylist[i])
				Netmaxiot.digitalWrite(mylist[i],1)
				time.sleep(0.01)
			print("on")
			time.sleep(1)
			for i in range (8):
				#print (" pin %d is 0 "  %mylist[i])
				Netmaxiot.digitalWrite(mylist[i],0)
				time.sleep(0.01)
			time.sleep(1)	
			print("off")
		time.sleep(3)		
		print("off")
		for i in range(0,255,2):
			Netmaxiot.analogWrite(3,i)
			time.sleep(0.05)
		for i in range(255,0,-2):
			Netmaxiot.analogWrite(3,i)
			time.sleep(0.05)	
		for i in range(0,255,2):
			Netmaxiot.analogWrite(5,i)
			time.sleep(0.05)
		for i in range(255,0,-2):
			Netmaxiot.analogWrite(5,i)
			time.sleep(0.05)
		for i in range(0,255,2):
			Netmaxiot.analogWrite(6,i)
			time.sleep(0.05)
		for i in range(0,255,2):
			Netmaxiot.analogWrite(9,i)
			time.sleep(0.05)
		for i in range(255,0,-2):
			Netmaxiot.analogWrite(9,i)
			time.sleep(0.05)
except KeyboardInterrupt:	# Turn LED off before stopping
	for i in range (8):
		Netmaxiot.digitalWrite(mylist[i],0)
		time.sleep(0.01)
	print ("you pressed Control + C byeeeee --:) ")


import time
import Netmaxiot 
Netmaxiot.pinMode(2,"OUTPUT")
Netmaxiot.pinMode(3,"OUTPUT")
Netmaxiot.pinMode(4,"OUTPUT")
while 1:
    Netmaxiot.digitalWrite(2,1)		# Send HIGH to switch on LED
    Netmaxiot.digitalWrite(3,1)
    Netmaxiot.digitalWrite(4,1)    
    print ("LED ON!-----:)")
    time.sleep(0.1)

    Netmaxiot.digitalWrite(2,0)     # Send HIGH to switch on LED
    Netmaxiot.digitalWrite(3,0)
    Netmaxiot.digitalWrite(4,0)  	# Send LOW to switch off LED
    print ("LED OFF!------:(")
    time.sleep(0.1)

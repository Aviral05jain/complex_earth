import time
import Netmaxiot
Netmaxiot.pinMode(5,"OUTPUT")
Netmaxiot.pinMode(6,"OUTPUT")
time.sleep(1)
i = 0
while True:
    Netmaxiot.analogWrite(5,i)
    i = i + 1
    time.sleep(.5)
    if i > 255:
        i= 0
    print (i)
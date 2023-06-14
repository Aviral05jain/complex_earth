import RPi.GPIO as GPIO
import dht11
from w1thermsensor import W1ThermSensor
from time import sleep
#############################
##########
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  #  board bcm 
GPIO.cleanup()
#############kidaan
mydht = dht11.DHT11(pin=25)
sensor = W1ThermSensor()
while 1:
    x = sensor.get_temperature()
    result = mydht.read()
    print("dht-T: %0.1f C" %result.temperature)
    print("dht-H: %0.1f P" %result.humidity)    
    print("-----------")
    print ("Ds-Temp=%0.3f"%x)
    sleep(6)
    print("-----------")
    print("-----------")

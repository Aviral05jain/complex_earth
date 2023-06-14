import RPi.GPIO as GPIO
import dht11
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  
GPIO.cleanup()
atul = dht11.DHT11(pin=25)
while 1:
    result = atul.read()
    print("T: %0.1f C" %result.temperature)
    print("H: %0.1f percent" % result.humidity)
    time.sleep(8)
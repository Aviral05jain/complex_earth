import RPi.GPIO as GPIO
import dht11
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  
GPIO.cleanup()

mydht = dht11.DHT11(pin=25)

while 1:
    result = mydht.read()
    if result.is_valid():
        x=result.temperature
        print("T: %0.2f C" %x)
        print("H: %0.1f percent" % result.humidity)
    else:
        print("Error:no %d sada senaor nahin challa" % result.error_code)

    time.sleep(7)
    
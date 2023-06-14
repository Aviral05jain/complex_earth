#BBFF-yYIAilDF2jQyo4AKhQXTC7Ss8rqd07
import RPi.GPIO as GPIO
import dht11
import time
import requests
import Netmaxiot 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  
GPIO.cleanup()
mydht = dht11.DHT11(pin=25)
def sendvalue():
    result = mydht.read()
    tx=result.temperature
    hx=result.humidity
    a = Netmaxiot.analogRead(1)
    lx = (a/5000)*100
    li=round(lx,2)
    print("light is ",li,"percent")
###########LDR
###########LM 35
    c = Netmaxiot.analogRead(0)
    d=(c*4.8875)
    tempx=d/10
    tempu=round(tempx,2)
    print("temp of lm35 is ",tempu)
    time.sleep(2)
    payload = {'temp':tempu,'light':li,'humidity':hx,'dhtemp':tx}
    return payload
while True:
        try:
            r = requests.post('http://things.ubidots.com/api/v1.6/devices/rpi/?token=BBFF-YCR86UHGJaPT62uP775ZSOHJoBTkPJ', data=sendvalue())
            print('sending to ubidots ')
            print (sendvalue())
        except:
            print('sending Failed--(:')
            pass          
        time.sleep(7)


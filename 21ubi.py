#BBFF-yYIAilDF2jQyo4AKhQXTC7Ss8rqd07
import time
import requests
import Netmaxiot 
def sendvalue():
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
    payload = {'temp':tempu,'light':li}
    return payload
while True:
        try:
            r = requests.post('http://things.ubidots.com/api/v1.6/devices/rpi/?token=BBFF-YCR86UHGJaPT62uP775ZSOHJoBTkPJ', data=sendvalue())
            print('sending to ubidots ')
            print (sendvalue())
        except:
            print('sending Failed--(:')
            pass          
        time.sleep(3)


#BBFF-YCR86UHGJaPT62uP775ZSOHJoBTkPJ
#########################
import time
import requests
import Netmaxiot 
def chd():
    a = Netmaxiot.analogRead(0)
    b=a*4.887
    lx = (b/5000)*100 #4.00988789878
    li=round(lx,1)
    print("light is ",li,"percent")
    payload = {'light':li}
    return payload
while 1:
    try:
        r = requests.post('http://things.ubidots.com/api/v1.6/devices/rpi/?token=BBFF-YCR86UHGJaPT62uP775ZSOHJoBTkPJ', data=chd())
        print('sending to ubidots ')
        print (chd())
    except:
        print('sending Failed--(:')
        pass          
    time.sleep(4)
from ubidots import ApiClient
import time
import Netmaxiot
Netmaxiot.pinMode(2,"OUTPUT")
Netmaxiot.pinMode(3,"OUTPUT")
api = ApiClient(token='BBFF-YCR86UHGJaPT62uP775ZSOHJoBTkPJ')
while 1:
    varx = api.get_variable('62de57af6ddfef06569c00eb')
    value= varx.get_values(1)
    print (value[0]['value'])
    if value[0]['value']==1.0:
        print ("Switch is ON")
        Netmaxiot.digitalWrite(2,1)
        time.sleep(1)
    else:
        print ("Switch is OFF")
        Netmaxiot.digitalWrite(2,0)
        time.sleep(1)
    print ("ubi data get")            
    time.sleep(4)
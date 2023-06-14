from ubidots import ApiClient
import time
api = ApiClient(token='BBFF-ArPW6WmjixXhnA3B3If23ufwgqj1Hb')
my_variable = api.get_variable('62df952aa82f830619c0aa30')
while True:
    my_variable = api.get_variable('62df952aa82f830619c0aa30')
    value= my_variable.get_values(1)
    button = int(value[0]['value'])
    print (button)
   

    if button==1:
        print ("Switch is ON")
    else:
        print ("Switch is OFF")
    
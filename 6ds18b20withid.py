from w1thermsensor import W1ThermSensor
for sensor in W1ThermSensor.get_available_sensors():
    print("---")
    print("Sen ID %s has Temp= %.3f" %(sensor.id, sensor.get_temperature()))
    print(" ")
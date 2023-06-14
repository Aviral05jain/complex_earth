import RPi.GPIO as gp 
from time import sleep 
gp.setmode(gp.BCM)
### kiddan janab
gp.setup(17, gp.OUT)
gp.setup(27, gp.OUT)
gp.setup(22, gp.OUT)

gp.output(17, 1)
gp.output(27, 1)
gp.output(22, 1)
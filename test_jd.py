from can_jd import *
import numpy as np

port = 'can1'
id = 10

can_jd = CANJD(port, id)


while True:
    r = can_jd.get_accel()
    print(r.T)
    #print(round(x,2), round(y,2), can_jd.slope_resolution)



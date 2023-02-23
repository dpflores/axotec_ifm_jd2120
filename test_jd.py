from can_jd import *
import numpy as np

import time

port = 'can1'
id = 10

can_jd = CANJD(port, id)


while True:
    speed = can_jd.get_speed_stimation()
    accel = can_jd.get_accel()
    print(np.round(accel.T,1))



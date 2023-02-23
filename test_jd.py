from can_jd import *
import numpy as np

import time

port = 'can1'
id = 10

can_jd = CANJD(port, id)


while True:
    start = time.time()
    r = can_jd.get_accel()
    end = time.time()
    print(end - start)
    # print(np.round(r.T,2),np.linalg.norm(r))
    
    #speed = can_jd.get_speed_stimation()



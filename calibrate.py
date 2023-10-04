from can_jd import *
import time
# CAN
port = 'can1'
id = 10
can_jd = CANJD(port, id)


SAMPLES = 10 

print("Calibrating...")

can_jd.calibrate_xy(SAMPLES)

print("Calibration done!")

from can_jd import *

port = 'can1'
id = 10

can_jd = CANJD(port, id)

while True:
    x,y = can_jd.get_slopes()
    print(round(x,2), round(y,2), can_jd.slope_resolution)



from can_jd import *

# CAN
port = 'can1'
id = 10
can_jd = CANJD(port, id)

# Acclerations
while True:

    x_angle, y_angle = can_jd.get_slopes()

    print(f'{{"x_angle":{round(x_angle,4)}, "y_angle":{round(y_angle,4)}}}')

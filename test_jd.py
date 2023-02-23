from can_jd import *
import numpy as np

port = 'can1'
id = 10

can_jd = CANJD(port, id)

g_vector = np.array([0, 0, -9.81]).T

def rotation(thetax_deg, thetay_deg, g_vector):
    thetax = -thetax_deg*np.pi/180
    Rx = np.array([[1, 0, 0],
                  [0, np.cos(thetax), -np.sin(thetax)],
                  [0, np.sin(thetax), np.cos(thetax)]])

    thetay = thetay_deg*np.pi/180
    Ry = np.array([[np.cos(thetay), 0, np.sin(thetay)],
                  [0, 1, 0],
                  [-np.sin(thetay), 0, np.cos(thetay)]])

    g_rotated = Ry@Rx@g_vector
    return g_rotated

while True:
    x,y = can_jd.get_slopes()

    g_rot = rotation(x,y,g_vector)

    print(g_rot.T)
    #print(round(x,2), round(y,2), can_jd.slope_resolution)



import canopen
import numpy as np

# Cargar archivo de configuración de dispositivo CANopen
g = 9.81

accel_resolution = g/1000
gyro_resolution = 0.1       # degrees/s

g_vector = np.array([0,0,-g]).T

slope_resolutions = {"10":0.01,"100":0.1,"1000":1}

class CANJD():
    def __init__(self, port='can1', node_id=10):
        network = canopen.Network()
        network.connect(bustype='socketcan', channel=port)
        self.node = network.add_node(node_id, 'JD2xxx_v1.0.eds')
        self.slope_resolution = slope_resolutions[str(self.node.sdo[0x6000].raw)]
        

    def get_accel(self):
        x = self.node.sdo[0x3403].raw * accel_resolution
        y = self.node.sdo[0x3404].raw * accel_resolution
        z = self.node.sdo[0x3405].raw * accel_resolution
        return x,y,z

    def get_gyro(self):
        x = self.node.sdo[0x3400].raw * gyro_resolution 
        y = self.node.sdo[0x3401].raw * gyro_resolution 
        z = self.node.sdo[0x3402].raw * gyro_resolution 
        return x,y,z

    def get_slopes(self):
        x = self.node.sdo[0x6010].raw * self.slope_resolution
        y = self.node.sdo[0x6020].raw * self.slope_resolution
        return x,y





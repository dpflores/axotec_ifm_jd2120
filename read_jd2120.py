import canopen

import math

# Cargar archivo de configuración de dispositivo CANopen
network = canopen.Network()
network.connect(bustype='socketcan', channel='can1')
node_id = 10

node = network.add_node(node_id, 'JD2xxx_v1.0.eds')
for obj in node.object_dictionary.values():
    print('0x%X: %s' % (obj.index, obj.name))
    if isinstance(obj, canopen.objectdictionary.Record):
        for subobj in obj.values():
            print('  %d: %s' % (subobj.subindex, subobj.name))




# X Y SLOPE
while True:
    x_slope = node.sdo[0x6010].raw

    y_slope = node.sdo[0x6020].raw

    print(round(x_slope,2), round(y_slope,2))



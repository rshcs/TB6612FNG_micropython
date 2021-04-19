
from time import sleep as delay
import fng

m1 = fng.Fng(14, 0, 2)
m2 = fng.Fng(12, 13, 15)

m1.write(0, 'cw')
m2.write(0, 'cw')
delay(1)

m1.write(300, 'cw')
delay(2)
m2.write(300, 'cw')
delay(2)
m1.write(0, 'cw')
m2.write(0, 'cw')
delay(1)
m1.write(300, 'ccw')
delay(2)
m2.write(300, 'ccw')
delay(2)
m1.write(0, 'cw')
m2.write(0, 'cw')
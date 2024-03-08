from sense_hat import SenseHat
import time
from time import sleep
sense = SenseHat()

colors = [
(255, 0, 0),
(255, 127, 0),
(255, 255, 0),
(0, 255, 0),
(0, 0, 255),
(75, 0, 130),
(159, 0, 255),
(255, 255, 255)
]

sense.clear()

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    
    x = round(x,1)
    y = round(y,1)
    z = round(z,1)
    
    if (x < 0 and y == 0):
        sense.clear()
        for x in range(7,-1,-1):
            for i in range(7,-1,-1):
                sense.set_pixel(x, i, colors[x])
            time.sleep(0.1)
            sense.clear()

    elif (x > 0 and y == 0):
        sense.clear()
        for x in range (8):
            for i in range (8):
                sense.set_pixel(x, i, colors[x])
            time.sleep(0.1)
            sense.clear()

    if (y < 0 and x == 0):
        sense.clear()
        for x in range (7,-1,-1):
            for i in range(7,-1,-1):
                sense.set_pixel(i, x, colors[x])
            time.sleep(0.1)
            sense.clear()

    elif (y > 0 and x == 0):
        sense.clear()
        for x in range (8):
            for i in range(8):
                sense.set_pixel(i, x, colors[x])
            time.sleep(0.1)
            sense.clear()
            
    if z == 1:
        sense.show_message("Up")
    elif z == -1:
        sense.show_message("Down")
        
    print("x = {0}, y = {1}, z = {2}".format(x, y, z))


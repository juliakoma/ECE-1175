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

x=0
i=0

sense.clear()

while True:
    for col in range(14):
        for row in range(col + 1):
            if row < 8 and col - row < 8:
                sense.set_pixel(row, col - row , colors[i])
        time.sleep(0.1)
        i+=1
        
        if i >= 8:
            i = 0
            
        sense.clear()
        

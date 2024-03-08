from sense_hat import SenseHat
import time
sense = SenseHat()

r = (255, 0, 0)
o = (255, 127, 0)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 255)
i = (75, 0, 130)
v = (159, 0, 255)
e = (0, 0, 0)

image1 = [
e,e,e,e,e,e,e,e,
r,e,e,r,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,r,e,e,e,
e,e,e,e,r,e,e,e,
r,r,r,r,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e]

image2 = [
e,e,e,e,e,e,e,e,
e,r,e,e,r,e,e,e,
e,e,e,e,e,e,e,e,
r,e,e,e,e,r,e,e,
r,e,e,e,e,r,e,e,
e,r,r,r,r,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e]

image3 = [
e,e,e,e,e,e,e,e,
e,e,r,e,e,r,e,e,
e,e,e,e,e,e,e,e,
e,r,e,e,e,e,r,e,
e,r,e,e,e,e,r,e,
e,e,r,r,r,r,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e]

image4 = [
e,e,e,e,e,e,e,e,
e,e,e,r,e,e,r,e,
e,e,e,e,e,e,e,e,
e,e,r,e,e,e,e,r,
e,e,r,e,e,e,e,r,
e,e,e,r,r,r,r,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e]

image5 = [
e,e,e,e,e,e,e,e,
e,e,e,e,r,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,r,e,e,e,e,
e,e,e,r,e,e,e,e,
e,e,e,e,r,r,r,r,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e]

while True:
    
    sense.set_pixels(image1)
    time.sleep(1)
    sense.set_pixels(image2)
    time.sleep(1)
    sense.set_pixels(image3)
    time.sleep(1)
    sense.set_pixels(image4)
    time.sleep(1)
    sense.set_pixels(image5)
    time.sleep(1)




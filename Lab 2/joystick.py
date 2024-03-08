from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
r = (255, 0, 0)
o = (255, 127, 0)
y = (255, 255, 0)
g = (0, 255, 0)
b = (0, 0, 255)
i = (75, 0, 130)
v = (159, 0, 255)
e = (0, 0, 0)

while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)
    
        if event.direction == "middle" and event.action == "released":
            t = sense.get_temperature()
            t = round(t, 1)
            msg = "Temperature = {0}".format(t)
            sense.show_message(msg, scroll_speed = 0.05)
        if event.direction == "left" and event.action == "released":
            p = sense.get_pressure()
            p = round(p, 1)
            msg = "Pressure = {0}".format(p)
            sense.show_message(msg, scroll_speed = 0.05)
        if event.direction == "right" and event.action == "released":
            h = sense.get_humidity()
            h = round(h, 1)
            msg = "Humidity = {0}".format(h)
            sense.show_message(msg, scroll_speed = 0.05)
        if event.direction == "up" and event.action == "released":
            image = [
            e,e,e,e,e,e,e,e,
            e,e,r,e,e,r,e,e,
            e,e,e,e,e,e,e,e,
            e,r,e,e,e,e,r,e,
            e,r,e,e,e,e,r,e,
            e,e,r,r,r,r,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e]
            sense.set_pixels(image)
        if event.direction == "down" and event.action == "released":
            image = [
            e,e,e,e,e,e,e,e,
            e,e,r,e,e,r,e,e,
            e,e,e,e,e,e,e,e,
            e,e,r,r,r,r,e,e,
            e,r,e,e,e,e,r,e,
            e,r,e,e,e,e,r,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e]
            sense.set_pixels(image)


    

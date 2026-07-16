#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks import nxtdevices

ev3 = EV3Brick()
ev3.light.on(Color.ORANGE)

# Make sure your sensor is physically plugged into Port 1!
brightness = nxtdevices.LightSensor(Port.S1)

while True:
    ev3.screen.print(brightness.ambient())
    wait(1000)

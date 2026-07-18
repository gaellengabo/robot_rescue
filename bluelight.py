#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.ev3devices import LightSensor

color = ColorSensor(Port.S4)

while True:
  screen.print(color.rgb())
  wait(1000)

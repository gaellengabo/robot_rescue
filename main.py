#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.ev3devices import LightSensor

ev3 = EV3Brick()
ev3.light.on(Color.ORANGE)

brightness = LightSensor(Port.S1)

while True:
  screen.print(brightness.reflection())
  wait(1000)

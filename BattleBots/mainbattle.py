#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

ev3 = EV3Brick()

ev3.light.on(Color.ORANGE)
while Button.CENTER not in ev3.buttons.pressed():
    wait(10)
ev3.light.on(Color.GREEN)
ev3.speaker.beep()
wait(5000)


#PUT YOUR CODE HERE  Delete mine

ev3.light.on(Color.RED)
wait(5000)

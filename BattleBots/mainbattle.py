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

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

ultrasonic = UltrasonicSensor(Port.S1)

DETECTION_DISTANCE = 76

BLACK_VALUE = 0    
WHITE_VALUE = 35

while True:
    dist = ultrasonic.distance()

    if dist < DETECTION_DISTANCE:
        left_motor.run(700)
        right_motor.run
        (700)
    else:
        left_motor.run(300)
        
        right_motor.run(-300)

    wait(20)

#try to be able to detect other ultrasonic sensors
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks import nxtdevices

ev3 = EV3Brick()
ev3.light.on(Color.ORANGE)

left_motor = Motor(Port.A)   
right_motor = Motor(Port.D)  

line_sensor = nxtdevices.LightSensor(Port.S1)
color_sensor = ColorSensor(Port.S4)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

BLACK_VALUE = 0    
WHITE_VALUE = 35
SETPOINT = (BLACK_VALUE + WHITE_VALUE) / 2

KP = 3.0        
BASE_SPEED = 27

RED_MIN = 6
RED_MAX = 8
GREEN_MIN = 1
GREEN_MAX = 3
BLUE_MIN = 0
BLUE_MAX = 2

while True:
    brightness = line_sensor.reflection()
    color = color_sensor.rgb()

    ev3.screen.clear()
    ev3.screen.print(brightness)

    if color[0] >= RED_MIN and color[0] <= RED_MAX and color[1] >= GREEN_MIN and color[1] <= GREEN_MAX and color[2] >= BLUE_MIN and color[2] <= BLUE_MAX:
        ev3.speaker.beep(frequency=800, duration=150)
        print("Yay eve! {}".format(color))
        break


    # normal line following
    error = SETPOINT - brightness
    turn_rate = KP * error
    robot.drive(BASE_SPEED, turn_rate)
    
    wait(10)

robot.stop(Stop.BRAKE)

#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks import nxtdevices

ev3 = EV3Brick()
ev3.light.on(Color.ORANGE)

left_motor = Motor(Port.A)   
right_motor = Motor(Port.D)  
line_sensor = nxtdevices.LightSensor(Port.S1)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

BLACK_VALUE = 7     
WHITE_VALUE = 25     
SETPOINT = (BLACK_VALUE + WHITE_VALUE) / 2

KP = 2.0             
BASE_SPEED = 100

while True:
    brightness = line_sensor.reflection()

    screen.clear()
    screen.print(brightness)

    # Proportional error formula from worksheet
    error = SETPOINT - brightness
    
    # Calculate turn speed based on how far off the line edge the robot is
    turn_rate = KP * error
    
    # Execute movement
    robot.drive(BASE_SPEED, turn_rate)
    
    wait(10)

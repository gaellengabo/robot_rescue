#we need to find the white and black values
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

ev3 = EV3Brick()

left_motor = Motor(Port.A)   
right_motor = Motor(Port.D)  
line_sensor = ColorSensor(Port.S1)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

BLACK_VALUE = 7     
WHITE_VALUE = 25     
SETPOINT = (BLACK_VALUE + WHITE_VALUE) / 2
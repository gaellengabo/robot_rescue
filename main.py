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

KP = 1.5             
BASE_SPEED = 100

while True:
    brightness = line_sensor.reflection()
    
    # Proportional error formula from worksheet
    error = SETPOINT - brightness
    
    # Calculate turn speed based on how far off the line edge the robot is
    turn_rate = KP * error
    
    # Execute movement
    robot.drive(BASE_SPEED, turn_rate)
    
    wait(10)
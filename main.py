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

black_value = 7     
white_value = 25     
setpoint = (black_value + white_value) / 2

kp = 1.4             
base_speed = 100

while True:
    brightness = line_sensor.reflection()
    
    # Proportional error formula from worksheet
    error = setpoint - brightness
    
    # Calculate turn speed based on how far off the line edge the robot is
    turn_rate = kp * error
    
    # Execute movement
    robot.drive(base_speed, turn_rate)
    
    wait(10)
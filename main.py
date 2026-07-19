
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
color_sensor = ev3devices.ColorSensor(Port.S4)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

BLACK_VALUE = 7     
WHITE_VALUE = 25
BLUE_R = 0
BLUE_B = 100
BLUE_G = 0
SETPOINT = (BLACK_VALUE + WHITE_VALUE) / 2

KP = 3.1             
BASE_SPEED = 56

while True:
    brightness = line_sensor.reflection()
    color = color_sensor.rgb()

    ev3.screen.clear()
    ev3.screen.print(brightness)

    # Proportional error formula from worksheet
    error = SETPOINT - brightness
    
    # Calculate turn speed based on how far off the line edge the robot is
    turn_rate = KP * error
    
    # Execute movement
    robot.drive(BASE_SPEED, turn_rate)
    
    wait(10)

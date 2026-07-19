#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

ev3 = EV3Brick()
ev3.light.on(Color.ORANGE)

left_motor = Motor(Port.A)   
right_motor = Motor(Port.D)  

line_sensor = ColorSensor(Port.S1)
color_sensor = ColorSensor(Port.S4)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

BLACK_VALUE = 7     
WHITE_VALUE = 25
SETPOINT = (BLACK_VALUE + WHITE_VALUE) / 2

KP = 3.1             
BASE_SPEED = 56

while True:
    brightness = line_sensor.reflection()
    r, g, b = color_sensor.rgb()

    ev3.screen.clear()
    ev3.screen.print(brightness)

    if b >= 9 and r <= 6 and g <= 6: 
        ev3.speaker.beep(frequency=800, duration=150)
        print("Blue detected! RGB: ({}, {}, {})".format(r, g, b))

    if brightness >= 24:
        ev3.speaker.beep(frequency=400, duration=100)
        robot.drive(0, 120) 
        wait(100) 
        continue

    # norml line following
    error = SETPOINT - brightness
    turn_rate = KP * error
    robot.drive(BASE_SPEED, turn_rate)
    
    wait(10)
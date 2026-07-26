#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.nxtdevices import LightSensor, UltrasonicSensor
from pybricks.parameters import Port, Color, Button
from pybricks.robotics import DriveBase
from pybricks.tools import wait

ev3 = EV3Brick()

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

ultrasonic = UltrasonicSensor(Port.S2)
front_sensor = LightSensor(Port.S4) 
back_sensor = ColorSensor(Port.S1)

WHITE_BORDER_THRESHOLD = 35  
OPPONENT_DISTANCE = 400 

ev3.light.on(Color.YELLOW)

while Button.CENTER not in ev3.buttons.pressed():
    wait(10)

ev3.light.on(Color.RED)
ev3.speaker.beep()
wait(5000) 
ev3.light.on(Color.GREEN)

while True:
    front_val = front_sensor.reflection()
    back_val = back_sensor.reflection()
    dist = ultrasonic.distance()

    if front_val > WHITE_BORDER_THRESHOLD:
        robot.straight(-150)
        robot.turn(90)

    elif back_val > WHITE_BORDER_THRESHOLD:
        robot.straight(150)

    elif dist < OPPONENT_DISTANCE:
        robot.drive(speed=700, turn_rate=0)

    else:
        robot.drive(speed=0, turn_rate=120)

    wait(5)
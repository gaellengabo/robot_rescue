#!/usr/bin/env pybricks-pycurry
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

ev3 = EV3Brick()
ev3.light.on(Color.ORANGE)
ev3.speaker.beep()

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=114)

left_motor.run_target(200, 360)
wait(500)

right_motor.run_target(200, 360)
wait(500)

robot.straight(200)
wait(500)

robot.straight(-200)
wait(500)

robot.turn(90)
wait(500)

robot.turn(-90)
wait(500)

ev3.light.off()
ev3.speaker.beep(frequency=800, duration=500)
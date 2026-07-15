#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize the EV3 brick
ev3 = EV3Brick()

# Initialize the motors
# Adjust Port.A or Port.D depending on where your left and right motors are plugged in
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

# Define robot dimensions
# Change wheel diameter (in mm) and axle track (distance between wheels in mm)
WHEEL_DIAMETER = 56
AXLE_TRACK = 114

# Set up the DriveBase
robot = DriveBase(left_motor, right_motor, wheel_diameter=WHEEL_DIAMETER, axle_track=AXLE_TRACK)

# Write your program here
ev3.speaker.beep(frequency=1000, duration=200)

# Drive forward 500 mm, then stop
robot.straight(500)
robot.stop(Stop.BRAKE)

# Wait for 1 second
wait(1000)

# Turn 90 degrees to the right
robot.turn(90)
robot.stop(Stop.BRAKE)

# Play a sound to indicate the program is finished
ev3.speaker.say("Task complete!")

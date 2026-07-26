#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.nxtdevices import LightSensor
from pybricks.parameters import Port, Color, Button
from pybricks.tools import wait

ev3 = EV3Brick()

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

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
        left_motor.run(-700)
        right_motor.run(-700)
        wait(500)
        
        left_motor.run(500)
        right_motor.run(-500)
        wait(350)

    elif back_val > WHITE_BORDER_THRESHOLD:
        left_motor.run(700)
        right_motor.run(700)
        wait(500)

    elif dist < OPPONENT_DISTANCE:
        left_motor.run(800)
        right_motor.run(800)

    else:
        left_motor.run(300)
        right_motor.run(-300)

    wait(10)
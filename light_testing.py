from pybricks.ev3devices import Motor, LightSensor

brightness = LightSensor(Port.S1)

while True:
  screen.print(brightness.reflection())
  wait(1000)

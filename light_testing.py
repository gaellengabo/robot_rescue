from pybricks.ev3devices import Motor, LightSensor

brightness = LightSensors(Port.1)

while True:
  screen.print(brightness.reflection())
  wait(1000)

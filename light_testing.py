from pybricks.ev3devices import Motor, LightSensor

brightness = LightSensors(Port.A)

while True:
  screen.print(brightness.reflection())
  wait(1000)

from pybricks.ev3devices import Motor, LightSensor

brightness = LightSensors(Port.A)

while True:
  screen.print(brightness)
  wait(1000)

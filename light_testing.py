from pybricks.ev3devices import Motor, ColorSensor

brightness = LightSensors(Port.A)

while True:
  screen.print(brightness)
  wait(1000)

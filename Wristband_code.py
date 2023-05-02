#This is where the code for the wristband goes
#needed imports
from gpiozero import DistanceSensor, InputDevice, OutputDevice
from machine import Pin

p0 = Pin(2, Pin.OUT)

p0.value(0)
p0.value(1)


class Pin.Pin(id, mode=Pin.OUT, pull=1, value=1)
#input/pre-video processing. subject to change
#note to self: find out how to send video to the hub if it is needed
ultrasonic = DistanceSensor(echo=1, trigger=3)
while true:
  distance = ultrasonic.distance
  concern_distance = 1.22
  def output_no_concern():
    print("All is good!")
  alert_distance = 0.80
  def output_concern():
    for 2:
      Pin.on()
  def output_alert():
    for 4:
      Pin.on()
  def calculate_vibration(distance):
    vibration = (((distance - 0.02) * -1) / (4 - 0.02)) + 1
    return vibration
  vibration = calculate_vibration(distance)
  motor.value = vibration

  
#Output/post-video processing
while distance >= 0:
  if distance >= concern_distance:
    output_no_concern();
  elseif distance > alert_distance:
    output_concern();
  else:
    output_alert();

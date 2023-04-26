#This is where the code for the wristband goes
#needed imports
from gpiozero import DistanceSensor, InputDevice, OutputDevice
#input/pre-video processing. subject to change
#note to self: find out how to send video to the hub if it is needed
ultrasonic = DistanceSensor(echo=4, trigger=7)
while true:
  distance = ultrasonic.distance
  concern_distance = 1.22
  def output_no_concern():
    
  alert_distance = 0.80
  def output_concern():
    
  def output_alert():
    
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

#This is where the code for the wristband goes
#input/pre-video processing. subject to change
#note to self: find out how to send video to the hub if it is needed




#Output/post-video processing
distance = 
concern_distance = 
output_no_concern = 
alert_distance = 
output_concern = 
output_alert = 
while distance >= 0:
  if distance >= concern_distance:
    output_no_concern;
  elseif distance > alert_distance:
    output_concern
  else:
    output_alert

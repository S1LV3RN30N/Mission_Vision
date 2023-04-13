#This is where the code for the wristband goes
while distance <= alert_range:
  if distance <= concern_range:
    output_concern
  else:
    outut_alert

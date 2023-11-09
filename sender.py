#! /usr/bin/env python3
import time
from pymavlink import mavutil
from pymavlink.mavutil import mavlink
from pymavlink.dialects.v10.ardupilotmega import MAVLink_global_position_int_message

# Create a connection to Process B (assuming it's listening on a specific port)
master = mavutil.mavlink_connection('udpout:localhost:14550')  # Example UDP connection to localhost:14550
# Send messages in a loop
h = 0
while True:
    # Create your MAVLink message here
    msg = MAVLink_global_position_int_message(0,0,0,h,0,0,0,0,0)
    print(msg)

    # Send the message
    master.mav.send(msg)

    # Wait for a while before sending the next message
    time.sleep(1)  # Sending a message every 1 second in this example
    h += 1

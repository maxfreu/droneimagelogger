#! /usr/bin/env python3
from time import sleep
from pymavlink import mavutil
from uuid import uuid4

# Create a connection to listen for incoming messages
# master = mavutil.mavlink_connection('/dev/ttyXXXX')
master = mavutil.mavlink_connection('udpin:localhost:14550')  # Example UDP input on port 14550

fname = f"/home/max/{str(uuid4())[:6]}_positions.csv"

# Receive and process messages in a loop
with open(fname, "w") as f:
    f.write(", ".join(['time_boot_ms', 'lat', 'lon', 'alt', 'relative_alt', 'vx', 'vy', 'vz', 'hdg'])  + "\n")
    while True:
        # Wait for a message to be received
        msg = master.recv_msg()

        # Check if a specific message type is received
        if msg is not None and msg.get_type() == 'GLOBAL_POSITION_INT':
            # Process the received message
            # Extract data from the message using msg.field1, msg.field2, etc.
            print("Received message:", msg)
            content = list(msg.to_dict().values())[1:]
            f.write(str(content)[1:-1] + "\n")
            f.flush()

        sleep(0.001)

#%%


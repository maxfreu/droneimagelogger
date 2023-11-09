#! /usr/bin/env python3
from time import sleep
from pymavlink import mavutil

# Create a connection to listen for incoming messages
master = mavutil.mavlink_connection('udpin:localhost:14550')  # Example UDP input on port 14550

# Receive and process messages in a loop
while True:
    # Wait for a message to be received
    msg = master.recv_msg()

    # Check if a specific message type is received
    if msg is not None and msg.get_type() == 'GLOBAL_POSITION_INT':
        # Process the received message
        # Extract data from the message using msg.field1, msg.field2, etc.
        print("Received message:", msg)

    sleep(0.001)

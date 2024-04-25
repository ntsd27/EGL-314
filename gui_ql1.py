import subprocess
import time 
import osc_client

# Replace with the IP address of your relay Raspberry Pi
RELAY_PI_IP = "192.168.1.101"
RELAY_PORT = 2000  # Port to send OSC messages to the relay Pi

def ql1_fader_control(channel, increment):
  """
  This function sends OSC messages to adjust the fader level of a specific channel on the QL1 mixer.

  Args:
      channel: The channel number (0-indexed).
      increment: The amount to increase or decrease the fader level (positive for increase, negative for decrease).
  """
  global RELAY_PI_IP, RELAY_PORT
  addr = "/fader"  # Address for fader control messages
  message = [channel, increment]  # Message format: [channel, increment]
  send_message(RELAY_PI_IP, RELAY_PORT, addr, message)

def run_command(command):
  # (unchanged from original code)

if __name__ == "__main__":
  # (unchanged from original code, remove demo commands)
  pass

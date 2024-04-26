import subprocess
import time 
import osc_client

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
    text = 'python3 command.py '
    config = text + command
    print(config)
    try:
        output = subprocess.check_output(config, shell=True)
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:

if __name__ == "__main__":
  # (unchanged from original code, remove demo commands)
  pass

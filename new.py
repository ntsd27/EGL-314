import tkinter as tk
from pythonosc import udp_client

# OSC Client configuration
client = udp_client.SimpleUDPClient("192.168.1.128", 49280)  # Replace "QL1_IP" with your mixer's IP

# Volume levels (initially 50)
person1_volume = 50
person2_volume = 50
person3_volume = 50

def volume_change(person, change):
  global person1_volume, person2_volume, person3_volume
  if person == "person1":
    person1_volume = min(max(person1_volume + change, 0), 100)
    send_osc_message(f"/ch/1/level", person1_volume)  # Send OSC for Person 1 (Channel 1)
  elif person == "person2":
    person2_volume = min(max(person2_volume + change, 0), 100)
    send_osc_message(f"/ch/2/level", person2_volume)  # Send OSC for Person 2 (Channel 2)
  elif person == "person3":
    person3_volume = min(max(person3_volume + change, 0), 100)
    send_osc_message(f"/ch/3/level", person3_volume)  # Send OSC for Person 3 (Channel 3)
  print(f"Person 1: {person1_volume}, Person 2: {person2_volume}, Person 3: {person3_volume}")

def send_osc_message(address, value):
  # Function to send OSC messages to QL1 Mixer
  client.send_message(address, value)

def reset_volumes():
  global person1_volume, person2_volume, person3_volume
  person1_volume = 50
  person2_volume = 50
  person3_volume = 50
  send_osc_message(f"/ch/1/level", person1_volume)  # Reset OSC for Person 1
  send_osc_message(f"/ch/2/level", person2_volume)  # Reset OSC for Person 2
  send_osc_message(f"/ch/3/level", person3_volume)  # Reset OSC for Person 3


main = tk.Tk()
main.title("Volume Control")  # Set window title

# Padding for elements
padx = 10
pady = 5

# Person 1 Volume Buttons
person1_label = tk.Label(main, text="Person 1 Volume")
person1_label.grid(row=1, column=1, padx=padx, pady=pady)
person1_up_button = tk.Button(main, text="Up", command=lambda: volume_change("person1", 5))
person1_up_button.grid(row=2, column=1, padx=padx)
person1_down_button = tk.Button(main, text="Down", command=lambda: volume_change("person1", -5))
person1_down_button.grid(row=4, column=1, padx=padx)

# Person 2 Volume Buttons
person2_label = tk.Label(main, text="Person 2 Volume")
person2_label.grid(row=1, column=3, padx=padx, pady=pady)
person2_up_button = tk.Button(main, text="Up", command=lambda: volume_change("person2", 5))
person2_up_button.grid(row=2, column=3, padx=padx)
person2_down_button = tk.Button(main, text="Down", command=lambda: volume_change("person2", -5))
person2_down_button.grid(row=4, column=3, padx=padx)

# Master Volume Buttons
person3_label = tk.Label(main, text="Master Volume")
person3_label.grid(row=1, column=5, padx=padx, pady=pady)
person3_up_button = tk.Button(main, text="Up", command=lambda: volume_change("master", 5))
person3_up_button.grid(row=2, column=5, padx=padx)
person3_down_button = tk.Button(main, text="Down", command=lambda: volume_change("master", -5))
person3_down_button.grid(row=4, column=5, padx=padx)

# Reset Button
reset_button = tk.Button(main, text="Reset", command=reset_volumes)
reset_button.grid(row=6, column=3, columnspan=1, padx=padx, pady=pady)


import tkinter as tk
import pythonosc
import osc_client

def ql1():
    receive_ip = "192.168.01.128"
    receive_port = 49280
    addr = "/print"
    message = "HELLOOOOOOOOOOOO" 

    send_message(receive_ip,receive_port,addr,message)
	
	
def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)

		print("Message sent successfully.")
	except:
		print("Message not sent")

def volume_change():
  if person == "person1":
    command = 'set MIXER:Current/InCh/Fader/Level 0 0 1000'

  elif person == "person2":
    command = 'set MIXER:Current/InCh/Fader/Level 1 0 1000'

  elif person == "person3":
    command = 'set MIXER:Current/InCh/Fader/Level 2 0 1000'

def reset_volumes():
  command = 'set MIXER:Current/InCh/Fader/Level 0 0 500'
  command = 'set MIXER:Current/InCh/Fader/Level 1 0 500'
  command = 'set MIXER:Current/InCh/Fader/Level 2 0 500'

main = tk.Tk()
main.title("Volume Control")  # Set window title

# Padding for elements
padx = 10
pady = 5

# Person 1 Volume Buttons
person1_label = tk.Label(main, text="Person 1 Volume")
person1_label.grid(row=1, column=1, padx=padx, pady=pady))
person1_up_button.grid(row=2, column=1, padx=padx)
person1_down_button = tk.Button(main, text="Down", command=l: )
person1_down_button.grid(row=4, column=1, padx=padx)

# Person 2 Volume Buttons
person2_label = tk.Label(main, text="Person 2 Volume")
person2_label.grid(row=1, column=3, padx=padx, pady=pady)
person2_up_button = tk.Button(main, text="Up", command=lambda: volume_change("person2", 5))
person2_up_button.grid(row=2, column=3, padx=padx)
person2_down_button = tk.Button(main, text="Down", command=lambda: volume_change("person2", -5))
person2_down_button.grid(row=4, column=3, padx=padx)

# Master Volume Buttons
master_label = tk.Label(main, text="Master Volume")
master_label.grid(row=1, column=5, padx=padx, pady=pady)
master_up_button = tk.Button(main, text="Up", command=lambda: volume_change("master", 5))
master_up_button.grid(row=2, column=5, padx=padx)
master_down_button = tk.Button(main, text="Down", command=lambda: volume_change("master", -5))
master_down_button.grid(row=4, column=5, padx=padx)

# Reset Button
reset_button = tk.Button(main, text="Reset", command=reset_volumes)
reset_button.grid(row=6, column=3, columnspan=1, padx=padx, pady=pady)

main.mainloop()
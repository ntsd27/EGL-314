import tkinter as tk
from pythonosc import udp_client


# Initialize OSC client
client = udp_client.SimpleUDPClient("192.168.1.128", 49820)  # Replace IP address and port with your mixer's IP and port

# Volume levels (initially 0dB)
person1_volume = 0
person2_volume = 0
person3_volume = 0

def volume_change(person, change):
    global person1_volume, person2_volume, person3_volume
    if person == "person1":
        person1_volume = min(max(person1_volume + change, 0), 100)  # Clamp between 0 and 100
        client.send_message("/person1/volume", person1_volume)
    elif person == "person2":
        person2_volume = min(max(person2_volume + change, 0), 100)
        client.send_message("/person2/volume", person2_volume)
    elif person == "person3":
        person3_volume = min(max(person3_volume + change, 0), 100)
        client.send_message("/person3/volume", person3_volume)

def reset_volumes():
    global person1_volume, person2_volume, person3_volume
    person1_volume = 0
    person2_volume = 0
    person3_volume = 0
    client.send_message("/person1/volume", 0)
    client.send_message("/person2/volume", 0)
    client.send_message("/person3/volume", 0)

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

# Person 3 Volume Buttons
person3_label = tk.Label(main, text="Person 3 Volume")
person3_label.grid(row=1, column=5, padx=padx, pady=pady)
person3_up_button = tk.Button(main, text="Up", command=lambda: volume_change("person3", 5))
person3_up_button.grid(row=2, column=5, padx=padx)
person3_down_button = tk.Button(main, text="Down", command=lambda: volume_change("person3", -5))
person3_down_button.grid(row=4, column=5, padx=padx)

# Reset Button
reset_button = tk.Button(main, text="Reset", command=reset_volumes)
reset_button.grid(row=6, column=3, columnspan=1, padx=padx, pady=pady)

main.mainloop()


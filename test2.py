import tkinter as tk
from pythonosc import udp_client

class MixerControlApp:
    def __init__(self, master):
        self.master = master
        master.title("Mixer Control")

        self.mixer_ip = '192.168.1.100'  # Change to QL1 mixer's IP address
        self.mixer_port = 10023  # Change to QL1 mixer's OSC port

        self.label_person1 = tk.Label(master, text="Person 1")
        self.label_person1.pack()

        self.label_person2 = tk.Label(master, text="Person 2")
        self.label_person2.pack()

        self.volume_up_button = tk.Button(master, text="Volume Up", command=self.volume_up)
        self.volume_up_button.pack()

        self.volume_down_button = tk.Button(master, text="Volume Down", command=self.volume_down)
        self.volume_down_button.pack()

        self.mute_button = tk.Button(master, text="Mute", command=self.toggle_mute)
        self.mute_button.pack()

    def volume_up(self):
        self.send_osc_message("/channel/volume", 1.0)

    def volume_down(self):
        self.send_osc_message("/channel/volume", -1.0)

    def toggle_mute(self):
        self.send_osc_message("/channel/mute", 1)

    def send_osc_message(self, address, value):
        client = udp_client.SimpleUDPClient(self.mixer_ip, self.mixer_port)
        client.send_message(address, value)

root = tk.Tk()
app = MixerControlApp(root)
root.mainloop()

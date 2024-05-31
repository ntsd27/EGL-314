import tkinter as tk
from pythonosc import udp_client, osc_message_builder
import time

main=tk.Tk()

#destroy ensures that when navigating from one page to another, every element in the navigated page is destroyed

def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)

		print("Message sent successfully.")
	except:
		print("Message not sent")

LAPTOP_IP = "192.168.1.103"		# send to laptop w grandMA3
PORT = 8000                     # laptop w grandMA3 port number
addr = "/gma3/cmd"

def MA3_Fader1Up():
    if __name__ == "__main__":
        send_message(LAPTOP_IP, PORT, addr, "FaderMaster Page 1.201 At 100")

def MA3_Fader1Down():
    if __name__ == "__main__":
        send_message(LAPTOP_IP, PORT, addr, "FaderMaster Page 1.201 At 0")
        
def MA3_Fader2Up():
    if __name__ == "__main__":
        send_message(LAPTOP_IP, PORT, addr, "FaderMaster Page 1.202 At 100")

def MA3_Fader2Down():
    if __name__ == "__main__":
        send_message(LAPTOP_IP, PORT, addr, "FaderMaster Page 1.202 At 0")
        
def MA3_Fader1Go():
    if __name__ == "__main__":
        send_message(LAPTOP_IP, PORT, addr, "Go Fader 201")

def MA3_Fader2Go():
    if __name__ == "__main__":
        send_message(LAPTOP_IP, PORT, addr, "Go Fader 202")

main.title("MA3 Control")

MA3PageFader1Up=tk.Button(main,text="Sequence 1 Up",font="20",command=MA3_Fader1Up)
MA3PageFader2Up=tk.Button(main,text="Sequence 2 Up",font="20",command=MA3_Fader2Up)
MA3PageFader1Label=tk.Label(main,text="Fader 1", font="20")
MA3PageFader2Label=tk.Label(main,text="Fader 2", font="20")
MA3PageFader1Down=tk.Button(main,text="Sequence 1 Down",font="20",command=MA3_Fader1Down)
MA3PageFader2Down=tk.Button(main,text="Sequence 2 Down",font="20",command=MA3_Fader2Down)
MA3PageFader1Go=tk.Button(main,text="Sequence 1 Go ",font="20",command=MA3_Fader1Go)
MA3PageFader2Go=tk.Button(main,text="Sequence 2 Go",font="20",command=MA3_Fader2Go)

MA3PageFader1Up.grid(row=1, column=0)
MA3PageFader2Up.grid(row=1, column=1)
MA3PageFader1Label.grid(row=0, column=0)
MA3PageFader2Label.grid(row=0, column=1)
MA3PageFader1Down.grid(row=3, column=0)
MA3PageFader2Down.grid(row=3, column=1)
MA3PageFader1Go.grid(row=4, column=0)
MA3PageFader2Go.grid(row=4, column=1)

main.mainloop()

import tkinter as tk
from pythonosc import udp_client

def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)

		print("Message sent successfully.")
	except:
		print("Message not sent")

# FOR INFO: IP address and port of the receiving Raspberry Pi
PI_A_ADDR = "192.168.1.103"		# wlan ip
PORT = 8000

def marker_1():
	global PI_A_ADDR
	global PORT
	addr = "/action/40161"
	msg = float(1)
	send_message(PI_A_ADDR, PORT, addr, msg)
	
def marker_2():
	global PI_A_ADDR
	global PORT
	addr = "/action/40162"
	msg = float(1)
	send_message(PI_A_ADDR, PORT, addr, msg)
	
def marker_3():
	global PI_A_ADDR
	global PORT
	addr = "/action/40163"
	msg = float(1)
	send_message(PI_A_ADDR, PORT, addr, msg)
	
def marker_4():
	global PI_A_ADDR
	global PORT
	addr = "/action/40164"
	msg = float(1)
	send_message(PI_A_ADDR, PORT, addr, msg)
	
def playstop():
	global PI_A_ADDR
	global PORT
	addr = "/action/40044"
	msg = float(1)
	send_message(PI_A_ADDR, PORT, addr, msg)
	



main = tk.Tk()
main.title('Music Control')

Snapshot1_label = tk.Button(main,text= "Snapshot 1",background= 'blue', foreground= 'white', command= marker_1, font= ("Helvetica",20))
Snapshot2_label = tk.Button(main,text= "Snapshot 2",background= 'green', foreground= 'white', command= marker_2, font= ("Helvetica",20))
Snapshot3_label = tk.Button(main,text= "Snapshot 3",background= 'purple', foreground= 'white', command= marker_3, font= ("Helvetica",20))
Snapshot4_label = tk.Button(main,text= "Snapshot 4",background= 'red', foreground= 'white',command= marker_4, font= ("Helvetica",20))
action_label = tk.Button(main,text= "Play/Pause", background='orange' , foreground= 'white',command= playstop, font= ("Helvetica",20))

Snapshot1_label.grid(row = 0, column= 0)
Snapshot2_label.grid(row = 0, column= 2)
Snapshot3_label.grid(row = 2, column= 0)
Snapshot4_label.grid(row = 2, column= 2)
action_label.grid(row = 1, column= 1)

main.mainloop()
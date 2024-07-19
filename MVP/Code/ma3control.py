from pythonosc import udp_client, osc_message_builder

def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)

		print("Message sent successfully.")
	except:
		print("Message not sent")

LAPTOP_IP = "192.168.254.30"		# send to laptop w grandMA3
MA_PORT = 8888                     # laptop w grandMA3 port number
addr1 = "/gma3/cmd"

def point():
	global LAPTOP_IP
	global MA_PORT
	global addr1
	msg = "Go+ Sequence 53"
	send_message(LAPTOP_IP, MA_PORT, addr1, msg)
	

def correct():
	global LAPTOP_IP
	global MA_PORT
	global addr1
	msg = "Go+ Sequence 52"
	send_message(LAPTOP_IP, MA_PORT, addr1, msg)
	

def wrong():
	global LAPTOP_IP
	global MA_PORT
	global addr1
	msg = "Go+ Sequence 51"
	send_message(LAPTOP_IP, MA_PORT, addr1, msg)

def split3():
    global LAPTOP_IP
    global MA_PORT
    global addr1
    msg = "Go+ Sequence 57"
    send_message(LAPTOP_IP, MA_PORT, addr1, msg)

def middle():
    global LAPTOP_IP
    global MA_PORT
    global addr1
    msg = "Go+ Sequence 58"
    send_message(LAPTOP_IP, MA_PORT, addr1, msg)
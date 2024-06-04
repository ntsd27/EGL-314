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

PI_A_ADDR = "192.168.1.103"		# wlan ip
PORT = 8000

def play_pause():
    global PI_A_ADDR
    global PORT
    addr = "/action/40044"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def demohigh():
    global PI_A_ADDR
    global PORT
    addr = "/action/40161"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def demolow():
    global PI_A_ADDR
    global PORT
    addr = "/action/40162"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def high():
    demohigh()
    play_pause()
    main.after(1500,play_pause)

def low():
    demolow()
    play_pause()
    main.after(1500,play_pause)

def combi1():
    code2
    play_pause
    main.after(4000,code5)
    main.after(4000,code7)
    main.after(3500,play_pause)

def combi2():
    code1
    play_pause
    main.after(4500,code4)
    main.after(4000,code9)
    main.after(4000,play_pause)

def combi3():
    code3
    play_pause
    main.after(4000,code0)
    main.after(5000,code6)
    main.after(4000,play_pause)

def combi4():
    code8
    play_pause
    main.after(4000,code2)
    main.after(4000,code4)
    main.after(4000,play_pause)

def combi5():
    code0
    play_pause
    main.after(5000,code0)
    main.after(5000,code0)
    main.after(5000,play_pause)
def code0():
    global PI_A_ADDR
    global PORT
    addr = "/action/40163"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def code1():
    global PI_A_ADDR
    global PORT
    addr = "/action/40164"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def code2():
    global PI_A_ADDR
    global PORT
    addr = "/action/40165"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def code3():
    global PI_A_ADDR
    global PORT
    addr = "/action/40166"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def code4():
    global PI_A_ADDR
    global PORT
    addr = "/action/40167"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def code5():
    global PI_A_ADDR
    global PORT
    addr = "/action/40168"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def code6():
    global PI_A_ADDR
    global PORT
    addr = "/action/40169"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def code7():
    global PI_A_ADDR
    global PORT
    addr = "/action/40160"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def code8():
    global PI_A_ADDR
    global PORT
    addr = "/action/41251"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def code9():
    global PI_A_ADDR
    global PORT
    addr = "/action/41252"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)
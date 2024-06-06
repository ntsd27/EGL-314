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

PI_A_ADDR = "192.168.254.30"		# wlan ip
PORT = 4869

def play():
    global PI_A_ADDR
    global PORT
    addr = "/action/1007"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def pause():
    global PI_A_ADDR
    global PORT
    addr = "/action/1008"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def demohigh():
    global PI_A_ADDR
    global PORT
    addr = "/action/41259"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def demolow():
    global PI_A_ADDR
    global PORT
    addr = "/action/41260"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def demowind():
     global PI_A_ADDR
     global PORT
     addr = "/marker/30"
     msg = float(1)
     send_message(PI_A_ADDR,PORT,addr,msg)

def high():
    demohigh()
    play()
    main.after(1500, pause)

def low():
    demolow()
    play()
    main.after(1500,pause)

def wind():
     demowind()
     play()
     main.after(1500,pause)

def combi1():
    code2()
    play()
    main.after(6000,code5)
    main.after(12000,code7)
    main.after(18000,pause)

def combi2():
    code1()
    play()
    main.after(4500,code4)
    main.after(4000,code9)
    main.after(4000,pause)


def combi3():
    code3()
    play()
    main.after(4000,code0)
    main.after(5000,code6)
    main.after(4000,pause)


def combi4():
    code8()
    play()
    main.after(4000,code2)
    main.after(4000,code4)
    main.after(4000,pause)

def combi5():
    code0()
    play()
    main.after(5000,code0)
    main.after(5000,code0)
    main.after(5000,pause)

def code0():
    global PI_A_ADDR
    global PORT
    addr = "/action/41262"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def code1():
    global PI_A_ADDR
    global PORT
    addr = "/action/41269"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def code2():
    global PI_A_ADDR
    global PORT
    addr = "/action/41270"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def code3():
    global PI_A_ADDR
    global PORT
    addr = "/marker/34"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def code4():
    global PI_A_ADDR
    global PORT
    addr = "/marker/35"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def code5():
    global PI_A_ADDR
    global PORT
    addr = "/marker/36"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def code6():
    global PI_A_ADDR
    global PORT
    addr = "/marker/37"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def code7():
    global PI_A_ADDR
    global PORT
    addr = "/marker/38"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def code8():
    global PI_A_ADDR
    global PORT
    addr = "/marker/39"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def code9():
    global PI_A_ADDR
    global PORT
    addr = "/marker/40"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)


def win():
    global PI_A_ADDR
    global PORT
    addr = "/marker/41"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)


def lose():
    global PI_A_ADDR
    global PORT
    addr = "/marker/42"
    msg = float(1)
    send_message(PI_A_ADDR,PORT,addr,msg)

def intro():
     global PI_A_ADDR
     global PORT
     addr = "/marker/43"
     msg = float(1)
     send_message(PI_A_ADDR, PORT, addr, msg)

marker_functions = [combi1, combi2, combi3, combi4, combi5]

main = tk.Tk()

marker1 = tk.Button(main, text="3", command=combi1)
marker1.pack(pady=5)

marker1 = tk.Button(main, text="4", command=code4)
marker1.pack(pady=5)
marker1 = tk.Button(main, text="5", command=code5)
marker1.pack(pady=5)
marker1 = tk.Button(main, text="6", command=code6)
marker1.pack(pady=5)
marker1 = tk.Button(main, text="7", command=code7)
marker1.pack(pady=5)
marker1 = tk.Button(main, text="8", command=code8)
marker1.pack(pady=5)
marker1 = tk.Button(main, text="9", command=code9)
marker1.pack(pady=5)
marker1 = tk.Button(main, text="0", command=code0)
marker1.pack(pady=5)
marker1 = tk.Button(main, text="win", command=win)
marker1.pack(pady=5)
marker1 = tk.Button(main, text="lose", command=lose)
marker1.pack(pady=5)
marker1 = tk.Button(main, text="whoosh", command=wind)
marker1.pack(pady=5)
marker1 = tk.Button(main, text="intro", command=intro)
marker1.pack(pady=5)

main.mainloop()
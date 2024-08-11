import tkinter as tk
from PIL import Image, ImageTk
from pythonosc import udp_client
import random
import ma3control

def send_message(receiver_ip, receiver_port, address, message):
    try:
        # Create an OSC client to send messages
        client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

        # Send an OSC message to the receiver
        client.send_message(address, message)

        print(f"Message sent to {receiver_ip}:{receiver_port} - Address: {address}, Message: {message}")
    except:
        print(f"Failed to send message to {receiver_ip}:{receiver_port} - Address: {address}, Message: {message}")

PI_A_ADDR = "192.168.254.30"        # wlan ip
PORT = 4869

LAPTOP_IP = "192.168.254.229"
MA_PORT = 8888

LISA_IP = "192.168.254.30"
LISA_PORT = 8880

def whooo1():
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/49/azim"
    msg = float(180)
    send_message(LISA_IP,LISA_PORT,addr,msg) 

def whooo2():
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/50/azim"
    msg = float(180)
    send_message(LISA_IP,LISA_PORT,addr,msg)  

def whooo3():
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/51/azim"
    msg = float(180)
    send_message(LISA_IP,LISA_PORT,addr,msg)  

def whooo4():
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/52/azim"
    msg = float(180)
    send_message(LISA_IP,LISA_PORT,addr,msg)  

def whooo5():
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/52/azim"
    msg = float(180)
    send_message(LISA_IP,LISA_PORT,addr,msg)   


def one1pan7():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/49/azim"
    msg = float(-117.47)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def one2pan7():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/50/azim"
    msg = float(-117.47)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def one3pan7():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/51/azim"
    msg = float(-117.47)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def one4pan7():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/52/azim"
    msg = float(-117.47)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def one5pan7():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/53/azim"
    msg = float(-117.47)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def one1pan8():  #one = number code, 1 = speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/49/azim"
    msg = float(-88.85)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def one2pan8():  #one = number code, 1 = speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/50/azim"
    msg = float(-88.85)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def one3pan8():  #one = number code, 1 = speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/51/azim"
    msg = float(-88.85)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def one4pan8():  #one = number code, 1 = speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/52/azim"
    msg = float(-88.85)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def one5pan8():  #one = number code, 1 = speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/53/azim"
    msg = float(-88.85)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def one1pan9():  #one = number code, 1 = speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/49/azim"
    msg = float(-57.38)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def one2pan9():  #one = number code, 1 = speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/50/azim"
    msg = float(-57.38)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def one3pan9():  #one = number code, 1 = speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/51/azim"
    msg = float(-57.38)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def one4pan9():  #one = number code, 1 = speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/52/azim"
    msg = float(-57.38)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def one5pan9():  #one = number code, 1 = speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/53/azim"
    msg = float(-57.38)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def two1pan10():  #one = number code, 1 = speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/49/azim"
    msg = float(-27.47)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def two2pan10():  #one = number code, 1 = speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/50/azim"
    msg = float(-27.47)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def two3pan10():  #one = number code, 1 = speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/51/azim"
    msg = float(-27.47)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def two4pan10():  #one = number code, 1 = speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/52/azim"
    msg = float(-27.47)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def two5pan10():  #one = number code, 1 = speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/53/azim"
    msg = float(-27.47)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def two1pan11():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/49/azim"
    msg = float(0)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def two2pan11():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/50/azim"
    msg = float(0)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def two3pan11():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/51/azim"
    msg = float(0)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def two4pan11():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/52/azim"
    msg = float(0)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def two5pan11():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/53/azim"
    msg = float(0)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def two1pan12():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/49/azim"
    msg = float(27.63)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def two2pan12():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/50/azim"
    msg = float(27.63)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def two3pan12():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/51/azim"
    msg = float(27.63)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def two4pan12():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/52/azim"
    msg = float(27.63)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def two5pan12():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/53/azim"
    msg = float(27.63)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def three1pan1():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/49/azim"
    msg = float(59.04)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def three2pan1():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/50/azim"
    msg = float(59.04)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def three3pan1():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/51/azim"
    msg = float(59.04)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def three4pan1():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/52/azim"
    msg = float(59.04)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def three5pan1():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/53/azim"
    msg = float(59.04)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def three1pan2():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/49/azim"
    msg = float(90)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def three2pan2():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/50/azim"
    msg = float(90)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def three3pan2():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/51/azim"
    msg = float(90)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def three4pan2():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/52/azim"
    msg = float(90)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def three5pan2():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/53/azim"
    msg = float(90)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def three1pan3():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/49/azim"
    msg = float(118.37)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def three2pan3():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/50/azim"
    msg = float(118.37)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def three3pan3():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/51/azim"
    msg = float(118.37)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def three4pan3():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/52/azim"
    msg = float(118.37)
    send_message(LISA_IP,LISA_PORT,addr,msg)

def three5pan3():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/53/azim"
    msg = float(118.37)
    send_message(LISA_IP,LISA_PORT,addr,msg)




def play():
    global PI_A_ADDR
    global PORT
    addr = "/action/1007"
    msg = float(1)
    send_message(PI_A_ADDR, PORT, addr, msg)

def pause():
    global PI_A_ADDR
    global PORT
    addr = "/action/1008"
    msg = float(1)
    send_message(PI_A_ADDR, PORT, addr,  msg)

def demohigh():
    global PI_A_ADDR
    global PORT
    addr = "/action/41259"
    msg = float(1)
    send_message(PI_A_ADDR, PORT, addr, msg)

def demolow():
    global PI_A_ADDR
    global PORT
    addr = "/action/41260"
    msg = float(1)
    send_message(PI_A_ADDR, PORT, addr, msg)

def demowind():
     global PI_A_ADDR
     global PORT
     addr = "/marker/32"
     msg = float(1)
     send_message(PI_A_ADDR,PORT,addr,msg)

def democombi():
     global PI_A_ADDR
     global PORT
     addr = "/marker/33"
     msg = float(1)
     send_message(PI_A_ADDR,PORT,addr,msg)

def high():
    demohigh()
    play()
    main.after(1500, pause)

def low():
    demolow()
    play()
    main.after(1500, pause)

def wind():
     demowind()
     play()
     main.after(1500,pause)

def demo():
    democombi()
    play()
    main.after(20500,pause)

# Define the preset combinations
preset_combinations = [
    [5, 5, 5],
    [2, 7, 5],
    [1, 5, 4],
    [3, 0, 5],
    [0, 2, 4]
]

def combi1():
    global PI_A_ADDR
    global PORT
    addr = "/action/41269"
    msg = float(1)
    send_message(PI_A_ADDR, PORT, addr, msg)

def combi2():
    global PI_A_ADDR
    global PORT
    addr = "/action/41270"
    msg = float(1)
    send_message(PI_A_ADDR, PORT, addr, msg)

def combi3():
    global PI_A_ADDR
    global PORT
    addr = "/marker/36"
    msg = float(1)
    send_message(PI_A_ADDR, PORT, addr, msg)

def combi4():
    global PI_A_ADDR
    global PORT
    addr = "/marker/37"
    msg = float(1)
    send_message(PI_A_ADDR, PORT, addr, msg)

def combi5():
    global PI_A_ADDR
    global PORT
    addr = "/marker/38"
    msg = float(1)
    send_message(PI_A_ADDR, PORT, addr, msg)

def win():
    global PI_A_ADDR
    global PORT
    addr = "/marker/39"
    msg = float(1)
    send_message(PI_A_ADDR, PORT, addr, msg)

def lose():
    global PI_A_ADDR
    global PORT
    addr = "/marker/40"
    msg = float(1)
    send_message(PI_A_ADDR, PORT, addr, msg)

def intro():
     global PI_A_ADDR
     global PORT
     addr = "/marker/41"
     msg = float(1)
     send_message(PI_A_ADDR, PORT, addr, msg)

def playcombi1():
    combi1()
    play()
    main.after(12000,one1pan8) #H
    main.after(13000,three1pan1) #H 
    main.after(14000,three1pan3) #L
    main.after(15500,two1pan12) #H
    main.after(16500,two1pan12) #L
    main.after(18000,three1pan2) #H
    main.after(19000,one1pan7) #L
    main.after(20500,three1pan1) #L
    main.after(22000,one1pan9) #H
    main.after(23500,one1pan8) #L
    main.after(25500,two1pan11) #H 
    main.after(27000,two1pan11) #L
    main.after(28500,whooo1)

    main.after(30500,one1pan8)
    main.after(31500,three1pan1)
    main.after(32500,three1pan3)
    main.after(34000,two1pan12)
    main.after(35000,two1pan12)
    main.after(36500,three1pan2)
    main.after(37500,one1pan7)
    main.after(39000,three1pan1)
    main.after(40500,one1pan9)
    main.after(42000,one1pan8)
    main.after(43500,two1pan11)
    main.after(44500,two1pan11)
    main.after(46000,whooo1)

    main.after(48000,one1pan8)
    main.after(49500,three1pan1)
    main.after(51000,three1pan3)
    main.after(52500,two1pan12)
    main.after(53500,two1pan12)
    main.after(55000,three1pan2)
    main.after(56000,one1pan7)
    main.after(57500,three1pan1)
    main.after(59000,one1pan9)
    main.after(60000,one1pan8)
    main.after(61500,two1pan11)
    main.after(63000,two1pan11)
    main.after(64500,whooo1)
    
    #main.after(70000, pause)

   #main.after(70000, pause)

def playcombi2():
    combi2()
    play()
    main.after(13000,one2pan8) #H
    main.after(14000,one2pan7) #H
    main.after(15000,three2pan3) #H
    main.after(16000,two2pan11) #H
    main.after(17500,two2pan10) #L
    main.after(19000,three2pan1) #L
    main.after(20500,one2pan9) #L
    main.after(22000,three2pan2) #H
    main.after(23000,three2pan3) #L
    main.after(24500,one2pan9) #H
    main.after(25500,two2pan11) #L
    main.after(27000,two2pan10) #L
    main.after(28500,whooo2)

    main.after(31000,one2pan8)
    main.after(32000,one2pan7)
    main.after(33000,three2pan3)
    main.after(34000,two2pan11)
    main.after(35500,two2pan10)
    main.after(37000,three2pan1)
    main.after(38500,one2pan9)
    main.after(40000,three2pan2)
    main.after(41000,three2pan3)
    main.after(42500,one2pan9)
    main.after(43500,two2pan11)
    main.after(45000,two2pan10)
    main.after(46500,whooo2)

    main.after(49000,one2pan8)
    main.after(50000,one2pan7)
    main.after(51000,three2pan3)
    main.after(52000,two2pan11)
    main.after(53500,two2pan10)
    main.after(55000,three2pan1)
    main.after(56500,one2pan9)
    main.after(58000,three2pan2)
    main.after(59000,three2pan3)
    main.after(60500,one2pan9)
    main.after(61500,two2pan11)
    main.after(63000,two2pan10)
    main.after(64500,whooo2)
    #main.after(70000, pause)

def playcombi3():
    combi3()
    play()
    main.after(13000,three3pan1) #H
    main.after(14000,two3pan11) #H
    main.after(15000,three3pan3) #L
    main.after(16500,one3pan9) #H
    main.after(17500,two3pan12) #L
    main.after(19000,one3pan8) #H
    main.after(20000,one3pan9) #H
    main.after(21000,three3pan2) #H
    main.after(22000,three3pan3) #H
    main.after(23000,one3pan7) #L
    main.after(24500,two3pan11) #H
    main.after(25500,two3pan10) #L
    main.after(27000,whooo3)

    main.after(31000,three3pan1)
    main.after(32000,two3pan11)
    main.after(33000,three3pan3)
    main.after(34500,one3pan9)
    main.after(35500,two3pan12)
    main.after(37000,one3pan8)
    main.after(38000,one3pan9)
    main.after(39000,three3pan2)
    main.after(40000,three3pan3)
    main.after(41000,one3pan7)
    main.after(42500,two3pan11)
    main.after(43500,two3pan10)
    main.after(45000,whooo3)

    main.after(49500,three3pan1)
    main.after(50500,two3pan11)
    main.after(51500,three3pan3)
    main.after(53000,one3pan9)
    main.after(54000,two3pan12)
    main.after(55500,one3pan8)
    main.after(56500,one3pan9)
    main.after(57500,three3pan2)
    main.after(58500,three3pan3)
    main.after(59500,one3pan7)
    main.after(61000,two3pan11)
    main.after(62000,two3pan10)
    main.after(63500,whooo3)
    #main.after(70000,pause)

def playcombi4():
    combi4()
    play()
    main.after(12500,two4pan12) # H
    main.after(14000,one4pan9) #H
    main.after(15000,one4pan7) #H 
    main.after(16000,three4pan3) #H
    main.after(17000,two4pan11) #H
    main.after(18000,three4pan1) #L
    main.after(19500,one4pan8) #L
    main.after(20500,three4pan2) #H
    main.after(22000,three4pan3) #L
    main.after(23000,one4pan8) #L
    main.after(24000,two4pan11) #H
    main.after(25000,two4pan10) #H
    main.after(26000,whooo4)

    main.after(28000,two4pan12)
    main.after(29500,one4pan9)
    main.after(30500,one4pan7)
    main.after(31500,three4pan3)
    main.after(32500,two4pan11)
    main.after(33500,three4pan1)
    main.after(35000,one4pan8)
    main.after(36000,three4pan2)
    main.after(37500,three4pan3)
    main.after(38500,one4pan8)
    main.after(39500,two4pan11)
    main.after(40500,two4pan10)
    main.after(41500,whooo4)

    main.after(43500,two4pan12)
    main.after(45000,one4pan9)
    main.after(46000,one4pan7)
    main.after(47000,three4pan3)
    main.after(48000,two4pan11)
    main.after(49000,three4pan1)
    main.after(50000,one4pan8)
    main.after(51500,three4pan2)
    main.after(52500,three4pan3)
    main.after(54000,one4pan8)
    main.after(55000,two4pan11)
    main.after(56000,two4pan10)
    main.after(57000,whooo4)
    #main.after(70000,pause)

def playcombi5():
    combi5()
    play()
    main.after(12500,one4pan8) #L 
    main.after(14000,two4pan11) #H 
    main.after(15000,three4pan3) #H
    main.after(16000,one4pan9) #H
    main.after(17000,two4pan12) #H
    main.after(18000,three4pan2) #L
    main.after(19500,one4pan8) #H
    main.after(20500,two4pan11) #L
    main.after(22000,three4pan3) #H
    main.after(23000,one4pan8) #H
    main.after(24000,two4pan11) #H
    main.after(25000,three4pan3) #H
    main.after(26000,whooo4)

    main.after(28000,one4pan8)
    main.after(29500,two4pan11)
    main.after(30500,three4pan3)
    main.after(31500,one4pan9)
    main.after(32500,two4pan12)
    main.after(33500,three4pan2)
    main.after(35000,one4pan8)
    main.after(36000,two4pan11)
    main.after(37500,three4pan3)
    main.after(38500,one4pan8)
    main.after(39500,two4pan11)
    main.after(40500,three4pan3)
    main.after(41500,whooo4)

    main.after(43500,one4pan8)
    main.after(45000,two4pan11)
    main.after(46000,three4pan3)
    main.after(47000,one4pan9)
    main.after(48000,two4pan12)
    main.after(49000,three4pan2)
    main.after(50000,one4pan8)
    main.after(51500,two4pan11)
    main.after(52500,three4pan3)
    main.after(54000,one4pan8)
    main.after(55000,two4pan11)
    main.after(56000,three4pan3)
    main.after(57000,whooo4)
    #main.after(70000,pause)

def playcombi5():
    combi5()
    play()
    main.after(12500,one5pan8)
    main.after(13500,three5pan1)
    main.after(14500,three5pan3)
    main.after(15500,two5pan11)
    main.after(16500,two5pan12)
    main.after(17500,one5pan7)
    main.after(19000,three5pan2)
    main.after(20500,two5pan10)
    main.after(21500,two5pan11)
    main.after(23000,three5pan2)
    main.after(24500,one5pan7)
    main.after(25500,one5pan9)
    main.after(26500,whooo5)

    main.after(28500,one5pan8)
    main.after(29500,three5pan1)
    main.after(30500,three5pan3)
    main.after(31500,two5pan11)
    main.after(32500,two5pan12)
    main.after(33500,one5pan7)
    main.after(35000,three5pan2)
    main.after(36500,two5pan10)
    main.after(37500,two5pan11)
    main.after(39000,three5pan2)
    main.after(40500,one5pan7)
    main.after(41500,one5pan9)
    main.after(42500,whooo5)

    main.after(44500,one5pan8)
    main.after(45500,three5pan1)
    main.after(46500,three5pan3)
    main.after(47500,two5pan11)
    main.after(48500,two5pan12)
    main.after(49500,one5pan7)
    main.after(51000,three5pan2)
    main.after(52500,two5pan10)
    main.after(53500,two5pan11)
    main.after(55000,three5pan2)
    main.after(56500,one5pan7)
    main.after(57500,one5pan9)
    main.after(58500,whooo5)
    #main.after(70000,pause)

osc_msg_list = [playcombi1,playcombi2,playcombi3,playcombi4]

def high1():
    one1pan8()
    high()

def low1():
    one1pan8()
    low()

def high2():
    two1pan11()
    high()

def low2():
    two1pan11()
    low()

def high3():
    three1pan3()
    high()

def low3():
    three1pan3()
    low()

def whodemo():
    whooo1()
    wind()


# Variable to keep track of the current index
#current_index = None
# Counter to track the number of repetitions
#repetition_counter = 0
# Flag to indicate if the correct combination is entered
correct_combination_entered = False

# Function to play the current choice and handle repetitions
def play_current_choice():
    global correct_combination_entered #repetition_counter

    if correct_combination_entered:
        return  # Stop the function if the correct combination is entered

    if current_index is not None:
        osc_msg_list[current_index]()  # Call the function at current_index

    #repetition_counter += 1

    #if repetition_counter < 3:  # Check if the function has been called less than 3 times
        # Schedule the function to run again after a set interval (e.g., 20 seconds)
        #main.after(20000, play_current_choice)

#def stop_repetitive_function():
    #try:
        #main.after_cancel(play_current_choice)
    #except:
        #pass

# Function to choose a random item and start the repetition process
def choose_random_item():
    global current_index, repetition_counter, correct_combination_entered
    current_index = random.randint(0, len(osc_msg_list) - 1)
    #repetition_counter = 0  # Reset the repetition counter
    correct_combination_entered = False  # Reset the flag for new choice
    play_current_choice()

# Create the main window
main = tk.Tk()
main.title("Number Combination Lock")
main.geometry("600x600")
main.configure(bg = '#786239')
main.after(1000, lambda: main.attributes('-fullscreen', True))
# Set the window size

# Initialize the number labels
number_labels = []


# Function to increment the number and cycle back to 0 after reaching 9
def increment_number(idx):
    current_number = int(number_labels[idx]["text"])  # Get the current number from the label
    current_number = (current_number + 1) % 10  # Increment and cycle back to 0
    number_labels[idx].config(text=str(current_number))  # Update the label with the new value

# Function to decrement the number and cycle back to 9 after reaching 0
def decrement_number(idx):
    current_number = int(number_labels[idx]["text"])  # Get the current number from the label
    current_number = (current_number - 1) if current_number > 0 else 9  # Decrement and cycle back to 9
    number_labels[idx].config(text=str(current_number))  # Update the label with the new value

# Function to check if the current combination is correct
def check_combination():
    global correct_combination_entered

    current_combination = [int(label["text"]) for label in number_labels]
    if current_combination in preset_combinations:
        correct_combination_entered = True  # Set the flag
        result_label.config(text="Correct Combination Entered!", fg="green", bg="white", font=("Arial", 16, "bold"))
        main.after(100,pause)
        main.after(100,ma3control.clear)
        main.after(500, win)
        main.after(500, play)
        main.after(500, ma3control.correct)
        main.after(5600, ma3control.clear)
        main.after(5900, reset_to_start_page)
        main.after(5950, ma3control.split3)
        main.after(6000, pause)

    else:
        result_label.config(text="Incorrect Combination. Try Again.", fg="red", bg="white", font=("Arial", 16, "bold"))
        ma3control.wrong()

# Function to start the countdown before showing the number lock page
def start_countdown():
    main.after(0,choose_random_item)
    countdown_label.grid()
    countdown(10)

# Function to handle the countdown
def countdown(seconds):

    if seconds > 0:
        countdown_label.config(text=str(seconds))
        main.after(1000, countdown, seconds-1)
    else:
        countdown_label.config(text="Go!")
        main.after(1000, show_number_lock_page)

# Function to show the number lock page
def show_number_lock_page():
    start_game_timer()
    countdown_label.grid_forget()
    start_page.place_forget()
    number_lock_page.place(relx=0.5, rely=0.5, anchor="center")

# Function to start the game timer
def start_game_timer():
    game_timer_label.config(text="60", font=("Arial", 24))
    game_timer_label.pack()
    game_timer(90)

# Function to handle the game timer
def game_timer(seconds):
    global game_timer_id
    if seconds > 0:
        game_timer_label.config(text=str(seconds))
        game_timer_id = main.after(1000, game_timer, seconds-1)
    else:
        game_timer_label.pack_forget()
        result_label.config(text="Time's up! You have lost the game.", fg="red", bg="white", font=("Arial", 16, "bold"))
        main.after(100,ma3control.wrong)
        main.after(500,lose)
        main.after(500,play)
        main.after(2500,ma3control.clear)
        main.after(3000, reset_to_start_page)
        main.after(3000,ma3control.split3)
        main.after(3000,pause)

# Function to reset to the start page
def reset_to_start_page():
    main.after_cancel(game_timer_id)  # Cancel any ongoing game timer
    number_lock_page.place_forget()
    start_page.place(relx=0.5, rely=0.5, anchor="center")
    result_label.config(text="")
    for label in number_labels:
        label.config(text="0")
    countdown_label.grid_forget()  # Hide countdown label for reset
    countdown_label.config(text="")  # Clear countdown label text
    game_timer_label.grid_forget()

# Create frames for different pages
start_page = tk.Frame(main, bg="#a07d48")
number_lock_page = tk.Frame(main, bg="#a07d48")

start_button = tk.Button(start_page, text="Start", command=start_countdown, width=10, height=2, font=("Arial", 16))
button1 = tk.Button(start_page, text="High1", command=high1, width=10, height=2, font=("Arial", 16), bg = "Blue")
button2 = tk.Button(start_page, text="Low1", command=low1, width=10, height=2, font=("Arial", 16), bg = "Blue")
button3 = tk.Button(start_page, text="High2", command=high2, width=10, height=2, font=("Arial", 16), bg = "Yellow")
button4 = tk.Button(start_page, text="Low2", command=low2, width=10, height=2, font=("Arial", 16), bg = "Yellow")
button5 = tk.Button(start_page, text="High3", command=high3, width=10, height=2, font=("Arial", 16), bg = "Red")
button6 = tk.Button(start_page, text="Low3", command=low3, width=10, height=2, font=("Arial", 16), bg = "Red")
button7 = tk.Button(start_page, text="Wind", command=whodemo, width=10, height=2, font=("Arial", 16))

# Arrange the buttons using grid
start_button.grid(row=0, column=0, columnspan=2, pady=10)
button1.grid(row=1, column=0, padx=5, pady=5)
button2.grid(row=1, column=1, padx=5, pady=5)
button3.grid(row=2, column=0, padx=5, pady=5)
button4.grid(row=2, column=1, padx=5, pady=5)
button5.grid(row=3, column=0, padx=5, pady=5)
button6.grid(row=3, column=1, padx=5, pady=5)
button7.grid(row=4, column=0, columnspan=2, pady=5)

# Define the countdown label
countdown_label = tk.Label(start_page, text="", font=("Arial",24))
countdown_label.grid(row=5,column = 0,columnspan=2,pady=10)
# Center the start page in the window
start_page.place(relx=0.5, rely=0.5, anchor="center")

# Number lock page widgets
number_frame = tk.Frame(number_lock_page)
number_frame.pack(pady=18)

colors = ["blue","yellow","red"]

for i in range(3):
    increment_button = tk.Button(number_frame, text="+", command=lambda idx=i: increment_number(idx), width=5, height=2, font=("Arial", 16),bg = colors[i])
    increment_button.grid(row=i, column=0, pady=5)

    number_label = tk.Label(number_frame, text="0", font=("Arial", 24),bg = colors[i])
    number_label.grid(row=i, column=1, padx=10)
    number_labels.append(number_label)

    decrement_button = tk.Button(number_frame, text="-", command=lambda idx=i: decrement_number(idx), width=5, height=2, font=("Arial", 16),bg = colors[i])
    decrement_button.grid(row=i, column=2, pady=5)

# Create result label
result_label = tk.Label(number_lock_page, text="", font=("Arial", 16), width=30, height=2)
result_label.pack(pady=10)

# Create game timer label
game_timer_label = tk.Label(number_lock_page, text="", font=("Arial", 24))

# Create check button
check_button = tk.Button(number_lock_page, text="Check Combination", command=check_combination, width=20, height=3, font=("Arial", 16))
check_button.pack(pady=10)

# Start the main loop
main.mainloop()


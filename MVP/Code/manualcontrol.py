import tkinter as tk
from pythonosc import udp_client

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
addr1 = "/gma3/cmd"

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



def clear():
    global LAPTOP_IP
    global MA_PORT
    global addr1
    msg = "Off MyRunningSequence"
    send_message(LAPTOP_IP, MA_PORT, addr1, msg)

def point():
    global LAPTOP_IP
    global MA_PORT
    global addr1
    msg = "Go+ Sequence 54"
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

def correct():
    global LAPTOP_IP
    global MA_PORT
    global addr1
    msg = "Go+ Sequence 51"
    send_message(LAPTOP_IP, MA_PORT, addr1, msg)


def wrong():
    global LAPTOP_IP
    global MA_PORT
    global addr1
    msg = "Go+ Sequence 52"
    send_message(LAPTOP_IP, MA_PORT, addr1, msg)


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
    main.after(12000,one1pan8)
    main.after(13000,two1pan11)
    main.after(14000,three1pan3)
    main.after(15500,one1pan9)
    main.after(16500,two1pan12)
    main.after(18000,three1pan2)
    main.after(19000,one1pan8)
    main.after(20500,two1pan11)
    main.after(22000,three1pan3)
    main.after(23500,one1pan8)
    main.after(25500,two1pan11)
    main.after(27000,three1pan3)
    main.after(28500,whooo1)

    main.after(30500,one1pan8)
    main.after(31500,two1pan11)
    main.after(32500,three1pan3)
    main.after(34000,one1pan9)
    main.after(35000,two1pan12)
    main.after(36500,three1pan2)
    main.after(37500,one1pan8)
    main.after(39000,two1pan11)
    main.after(40500,three1pan3)
    main.after(42000,one1pan8)
    main.after(43500,two1pan11)
    main.after(44500,three1pan3)
    main.after(46000,whooo1)

    main.after(48000,one1pan8)
    main.after(49500,two1pan11)
    main.after(51000,three1pan3)
    main.after(52500,one1pan9)
    main.after(53500,two1pan12)
    main.after(55000,three1pan2)
    main.after(56000,one1pan8)
    main.after(57500,two1pan11)
    main.after(59000,three1pan3)
    main.after(60000,one1pan8)
    main.after(61500,two1pan11)
    main.after(63000,three1pan3)
    main.after(64500,whooo1)
    
    #main.after(70000, pause)

def playcombi2():
    combi2()
    play()
    main.after(13000,one2pan8)
    main.after(14000,two2pan11)
    main.after(15000,three2pan3)
    main.after(16000,one2pan9)
    main.after(17500,two2pan12)
    main.after(19000,three2pan2)
    main.after(20500,one2pan7)
    main.after(22000,two2pan11)
    main.after(23000,three2pan3)
    main.after(24500,one2pan8)
    main.after(25500,two2pan11)
    main.after(27000,three2pan1)
    main.after(28500,whooo2)

    main.after(31000,one2pan8)
    main.after(32000,two2pan11)
    main.after(33000,three2pan3)
    main.after(34000,one2pan9)
    main.after(35500,two2pan12)
    main.after(37000,three2pan2)
    main.after(38500,one2pan8)
    main.after(40000,two2pan11)
    main.after(41000,three2pan3)
    main.after(42500,one2pan8)
    main.after(43500,two2pan11)
    main.after(45000,three2pan3)
    main.after(46500,whooo2)

    main.after(49000,one2pan8)
    main.after(50000,two2pan11)
    main.after(51000,three2pan3)
    main.after(52000,one2pan9)
    main.after(53500,two2pan12)
    main.after(55000,three2pan2)
    main.after(56500,one2pan8)
    main.after(58000,two2pan11)
    main.after(59000,three2pan3)
    main.after(60500,one2pan8)
    main.after(61500,two2pan11)
    main.after(63000,three2pan3)
    main.after(64500,whooo2)
    #main.after(70000, pause)

def playcombi3():
    combi3()
    play()
    main.after(13000,one3pan8)
    main.after(14000,two3pan11)
    main.after(15000,three3pan3)
    main.after(16500,one3pan9)
    main.after(17500,two3pan12)
    main.after(19000,three3pan2)
    main.after(20000,one3pan8)
    main.after(21000,two3pan11)
    main.after(22000,three3pan3)
    main.after(23000,one3pan8)
    main.after(24500,two3pan11)
    main.after(25500,three3pan3)
    main.after(27000,whooo3)

    main.after(31000,one3pan8)
    main.after(32000,two3pan11)
    main.after(33000,three3pan3)
    main.after(34500,one3pan9)
    main.after(35500,two3pan12)
    main.after(37000,three3pan2)
    main.after(38000,one3pan8)
    main.after(39000,two3pan11)
    main.after(40000,three3pan3)
    main.after(41000,one3pan8)
    main.after(42500,two3pan11)
    main.after(43500,three3pan3)
    main.after(45000,whooo3)

    main.after(49500,one3pan8)
    main.after(50500,two3pan11)
    main.after(51500,three3pan3)
    main.after(53000,one3pan9)
    main.after(54000,two3pan12)
    main.after(55500,three3pan2)
    main.after(56500,one3pan8)
    main.after(57500,two3pan11)
    main.after(58500,three3pan3)
    main.after(59500,one3pan8)
    main.after(61000,two3pan11)
    main.after(62000,three3pan3)
    main.after(63500,whooo3)
    #main.after(70000,pause)

def playcombi4():
    combi4()
    play()
    main.after(12500,one4pan8)
    main.after(14000,two4pan11)
    main.after(15000,three4pan3)
    main.after(16000,one4pan9)
    main.after(17000,two4pan12)
    main.after(18000,three4pan2)
    main.after(19500,one4pan8)
    main.after(20500,two4pan11)
    main.after(22000,three4pan3)
    main.after(23000,one4pan8)
    main.after(24000,two4pan11)
    main.after(25000,three4pan3)
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
    main.after(13500,two5pan11)
    main.after(14500,three5pan3)
    main.after(15500,one5pan9)
    main.after(16500,two5pan12)
    main.after(17500,three5pan2)
    main.after(19000,one5pan8)
    main.after(20500,two5pan11)
    main.after(21500,three5pan3)
    main.after(23000,one5pan8)
    main.after(24500,two5pan11)
    main.after(25500,three5pan3)
    main.after(26500,whooo5)

    main.after(28500,one5pan8)
    main.after(29500,two5pan11)
    main.after(30500,three5pan3)
    main.after(31500,one5pan9)
    main.after(32500,two5pan12)
    main.after(33500,three5pan2)
    main.after(35000,one5pan8)
    main.after(36500,two5pan11)
    main.after(37500,three5pan3)
    main.after(39000,one5pan8)
    main.after(40500,two5pan11)
    main.after(41500,three5pan3)
    main.after(42500,whooo5)

    main.after(44500,one5pan8)
    main.after(45500,two5pan11)
    main.after(46500,three5pan3)
    main.after(47500,one5pan9)
    main.after(48500,two5pan12)
    main.after(49500,three5pan2)
    main.after(51000,one5pan8)
    main.after(52500,two5pan11)
    main.after(53500,three5pan3)
    main.after(55000,one5pan8)
    main.after(56500,two5pan11)
    main.after(57500,three5pan3)
    main.after(58500,whooo5)
    #main.after(70000,pause)

main = tk.Tk()
main.title("Number Combination Lock")
main.geometry("600x600")


malabel = tk.Label(main, text= 'Lighting')
malabel.grid(row=0, column= 1)

clear = tk.Button(main, text= 'Clear', command= clear)
clear.grid(row=1, column= 1)

malabel = tk.Button(main, text= 'Lighting', command= point)
malabel.grid(row=2, column= 1)

correctbutton = tk.Button(main, text= 'Correct', command= correct)
correctbutton.grid(row=3, column= 1)

wrongbutton = tk.Button(main, text= 'Wrong', command= wrong)
wrongbutton.grid(row=4, column= 1)

sidebutton = tk.Button(main, text= '3 Sides', command= split3)
sidebutton.grid(row=5, column= 1)

gatherbutton = tk.Button(main, text= 'Gather', command= middle)
gatherbutton.grid(row=6, column= 1)

dawlabel = tk.Label(main, text= 'Audio')
dawlabel.grid(row=0, column= 4)

combi1button = tk.Button(main, text= 'Combi1', command= playcombi1)
combi1button.grid(row=1, column= 4)

combi2button = tk.Button(main, text= 'Combi2', command= playcombi2)
combi2button.grid(row=2, column= 4)

combi3button = tk.Button(main, text= 'Combi3', command= playcombi3)
combi3button.grid(row=3, column= 4)

combi4button = tk.Button(main, text= 'Combi4', command= playcombi4)
combi4button.grid(row=4, column= 4)

combi5button = tk.Button(main, text= 'Combi5', command= playcombi5)
combi5button.grid(row=5, column= 4)

introbutton = tk.Button(main, text= 'Intro', command= intro)
introbutton.grid(row=6, column= 4)

playbutton = tk.Button(main, text= 'Play', command= play)
playbutton.grid(row=7, column= 4)

introbutton = tk.Button(main, text= 'Pause', command= pause)
introbutton.grid(row=8, column= 4)

main.mainloop()
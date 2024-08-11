## <p align=center>Final Demostration
</p>

<p align=center>All the resources fully required to give a complete demostration, which basically means a full working demostration of our staion, Art of Hearing</p>

## Overview
> This repository contains all the assests,codes and others for our Station 3 - Art Of Hearing.

>In this Final Demostration, there will be a master station which will be shared among all teams, which in the venue, there are 12 speakers in the venue.

>In this station, there will be 3 participants standing at each side of the room, each participants have to listen to the beat that correspond to their side of the room, to get a number and then come together to crack open the combination of the lock.

>Sound cue represent the secret ninja code that every ninja has learnt.When combined, the 4 sound cue together a code will be created which then can be deciphered into a number to input into the lock

>There is also a treasure chest full of secrets of the richest man in the village through this: 




## References
For the hardware and software connections, please consult the following: 

1. [Backlog 1 Sprint 1](../Backlog%201%20Sprint%201/) - Sending OSC Messages to GrandMA3


2. [Backlog 2 Sprint 1](../Backlog%202%20Sprint%201/) - Reaper and L-ISA Control Using OSC Commands

3. [Backlog 2 Sprint 2](../Backlog%202%20Sprint%201/) - Game

4. [MVP](../MVP/) - Laser Show

## Hardware and Software Setup

### Hardware Setup
> For the hardware setup, there are no changes made, hence refer to [POC](../POC/README.md) for the set up of hardware.



### System Diagram
```mermaid
graph TD
A[Raspberry Pi] --OSC--> V[Master Laptop]-->B[Reaper DAW] <--DANTE VSC--> C[L-ISA Processor] <--Spatial Meta Data--> D[L-ISA Controller]<--LAN DANTE--> E[Yamaha QL1] <--LAN DANTE--> F[Amplifier] --Speaker Cable to Euroblock(4P)--> I[Speakers]
V --OSC--> G[GrandMA3] <--SCAN--> H[Moving Lights
Ayrton Mistral,MagicBlade,Minipanel,Showliner ePar]

Y --OSC--> V

Y[Laptop GUI] -- OSC--> Z[Raspberry Pi - Laser Master]
Z --OSC--> N[Raspberry Pi - Laser Slave 1]
Z --OSC--> X[Raspberry Pi - Laser Slave 2]
Z --OSC--> W[Raspberry Pi - Laser Slave 3]
Z --OSC--> J[Raspberry Pi - Laser Slave 4]
Z --OSC--> K[Raspberry Pi - Neopixel LED Strip]

N --GPIO--> L[Relay Module]
X --GPIO--> Q[Relay Module]
W --GPIO--> P[Relay Module]
J --GPIO--> R[Relay Module]
L --> O[Laser Module]
Q --> O
P --> O
R --> O
```
>In this system diagram, for any equipments used in the sending of OSC commands <b>MUST</b> be on the same network,including all the IP Addresses of the Raspberry PI.

### Software SetUp
><b>L-ISA</b>
> 1. On the L-ISA OSC page, change the Raspberry PI to "OSC-ADM" format, as the OSC control commands are more precise, allowing specific degress for accurate placement on the speakers.

<img src = "./Media Assests/LISAOSC.png">

### Hardware SetUp
> For the hardware set up of the treasure chest, this is what it looks like: 

<img src = "./Media Assests/displaysetup.jpg">

>There are ample space to store both the powerbank and the raspberry Pi with ample amount of slack.


## Media Assests
> Included in the MVP Demostration are: 
>
>[Legend Board](./Media%20Assests/legendboard.jpg)- Poster with the number Comibinations for the participants to refer to

<img src = "./Media Assests/legendboard.jpg">

>[Master File](./Master%20Files/) - Contains all the software used for the MVP, which includes:
> 1. [GrandMA3](./Master%20Files/MasterShowfile_EGL314_MVP_FINAL.show) Master file
> 2. [REAPER](./Master%20Files/314MAINREAPER_POC_FINAL.rpp) Master file
> 3. [L-ISA](./Master%20Files/MAINFILE%20POC_FINAL%20-%20copy.lisa) Master file

## Explanation
> Classified into 2 different folders, for easier differentiation and explantion: 
>1. Code
>2. Laser

### Code
> In the [game.py](./Code/game.py), upon running the program, the start page GUI appears as below: 
<img src = "./Media Assests/new start.png">
>There are mainly 5 buttons for demo, which mainly: 

>1. <b>Start</b> - To start and begin the game

>2. <b>High 1</b> - Plays the High sound on speaker 2

>3. <b>Low 1</b> - Plays the Low sound on speaker 2

>4. <b>High 2</b> -Plays the High sound on speaker  11

>5. <b>Low 2</b> - Plays the Low sound on speaker 11

>6. <b>High 3</b> - Plays the High sound on speaker 8

>7. <b>Low 3</b> - Plays the High sound on speaker 8

>8. <b>Wind</b> - Plays the Whoosh sound on speaker 5

>For reference, this is a picture of the speakers placement and numbers. 
<img src = './Media Assests/SpeakerPlacement.png'> 

>For Blue side, it is speakers 1-3.
>
>For Yellow side, it is speakers 10-12.
>
>For Red side, it is speakers 7-9.

#### Begin of Game

> When the game begins, this GUI is shown instead: 
<img src = './Media Assests/new lock.png'>
>The functions here include: 

> 1. <b>Number Combinations</b> - Pressing the '+'or '-' button will increase or decrease the current number shown respectively, able to loop to '9' when pressing '-' when the number is 0.

> 2. <b>Check Combination</b> - When participants has input a number combination, pressing the button wil check if the numbers the particiapants has inputted is the correct combination as what they heard on the speakers, there will 2 scenarios that can happen, mainly:
> 1. <b>Winning Scenario</b> - The combination entered is correct and participants win the game.
> 2. <b>Losing Scenario</b> - The combination entered is wrong, causing the lights to turn red, while participatns are able to try for a different combination as long as the time does not run out.

> Participants at each of their side of the speakers must listen for their corresponding beats coming form their side of the speakers, decipher it into a number and input the number according to their color on the number lock.

> When participants run out of time, they are  brought back to the start page. This allows for multiple attempts in one smooth gameplay which requires little maintence or rerunning of the program

> The Main Game contains all the functions for sending OSC messages to REAPER and L-ISA.

> [manualcontrol.py](./Code/manualcontrol.py) - allows for manual control of all the functions, audio and lighting wise. 
<img src = './Media Assests/manualcontrol.png'>

> The functions include:
> 1. <b>Clear</b>  - Clears any sequences on the GrandMA3  running on the GrandMA3 software
> 2. <b>Face Light</b> - Runs a sequence on the GrandMA3 that points light to the front of our station for one of us to start presenting. 
> 3. <b>Correct</b> - Runs a sequence on the GrandMA3  for when the correct combination has been entered
> 4. <b>Wrong</b> - Runs a sequence on the GrandMA3  for when the incorrect combination has been entered
> 5. <b>3 Sides</b> - Runs a sequence on the GrandMA3  for the 3 participants to stand in to listen for the sound beats. 
> 6. <b>Gather</b> - Runs a sequence on the GrandMA3 which creates a light in the middle of the room for participants to gather 
> 7. <b>Combi 1-5</b> - Plays the commbination number beats
> 8. <b>Play</b> - Plays the timeline on Reaper
> 9. <b>Pause</b> - Pauses the timeline on Reaper
> 10. <b>Correct</b> - Plays the timeline on Reaper of the correct comibination and on GrandMA3
> 11. <b>Wrong</b> - Plays the timeline on Reaper of the wrong comibination and on GrandMA3

>[ma3control.py](./Code/ma3control.py)- contains all the functions to send OSC mesages to GrandMA3 

>Let's further break down the codes in [game.py](./Code/game.py):

```
PI_A_ADDR = "192.168.254.30"        # wlan ip
PORT = 4869

LAPTOP_IP = "192.168.254.229"
MA_PORT = 8888

LISA_IP = "192.168.254.30"
LISA_PORT = 8880
```
> PI_A_ADDR, PORT is the IP Address and Port number for REAPER.
> LAPTOP_ADDR, MA_PORT is the IP Address and Port number for GrandMA3.
> LISA_ADDR, LISA_PORT is the IP Address and Port number for L-ISA Controller.

```
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
```
> Controls the 'Wind' sound during the gameplay to play to speaker 5.

>From line 64-377, are the OSC commands to pan the sounds to each speakers, for each set 5 combination. Will take one example: 
```

def one1pan7():  #[one,1,1] = position of number, combi,speaker
    global LISA_IP
    global LISA_PORT
    addr = "/adm/obj/49/azim"
    msg = float(-117.47)
    send_message(LISA_IP,LISA_PORT,addr,msg)
```
> the one1pan7 function meant that this function control the first number in combination 1 to pan to speaker 7 when needed.
```
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
```
> Each function sends OSC commands to REAPER to travel to the specified marker on the REAPER Timeline. Seen from Line 382-422 and 453-507.

```
def high():
    demohigh()
    play()
    main.after(1500, pause)
```
>Calls the function demohigh to travel to the specified marker and plays the timeline, afterwards when 1.5s has passed, pauses the timeline on Reaper. Same logic applies to line 424-442 and 509-786.

```
def play_current_choice():
    global correct_combination_entered #repetition_counter

    if correct_combination_entered:
        return  # Stop the function if the correct combination is entered

    if current_index is not None:
        osc_msg_list[current_index]()

def choose_random_item():
    global current_index, repetition_counter, correct_combination_entered
    current_index = random.randint(0, len(osc_msg_list) - 1)
    #repetition_counter = 0  # Reset the repetition counter
    correct_combination_entered = False  # Reset the flag for new choice
    play_current_choice()
```
> Function to choose any function at random from Combi1-5.
```
main.after(1000, lambda: main.attributes('-fullscreen', True))
```
>Makes the GUI Fullscreen.

```
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
```
>Creates the scencarios and functions for Incorrect and Winning Combinations.

```
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

```
>Creates a timer for 60 seconds, which is the game duration, and the Lose Scenario

```
start_button = tk.Button(start_page, text="Start", command=start_countdown, width=10, height=2, font=("Arial", 16))
start_button.pack(pady=10)

button1 = tk.Button(start_page, text="High", command=high, width=10, height=2, font=("Arial", 16))
button1.pack(pady=5)

button2 = tk.Button(start_page, text="Low", command=low, width=10, height=2, font=("Arial", 16))
button2.pack(padx=5)

button3 = tk.Button(start_page, text= "Wind",command=wind, width=10, height=2, font=("Arial", 16))
button3.pack(pady=5)

button4 = tk.Button(start_page, text= "Demo",command=demo, width=10, height=2, font=("Arial", 16))
button4.pack(pady=5)

countdown_label = tk.Label(start_page, text="", font=("Arial", 24))
countdown_label.pack()

# Center the start page in the window
start_page.place(relx=0.5, rely=0.5, anchor="center")

# Number lock page widgets
number_frame = tk.Frame(number_lock_page)
number_frame.pack(pady=18)

for i in range(3):
    increment_button = tk.Button(number_frame, text="+", command=lambda idx=i: increment_number(idx), width=5, height=2, font=("Arial", 16))
    increment_button.grid(row=i, column=0, pady=5)

    number_label = tk.Label(number_frame, text="0", font=("Arial", 24))
    number_label.grid(row=i, column=1, padx=10)
    number_labels.append(number_label)

    decrement_button = tk.Button(number_frame, text="-", command=lambda idx=i: decrement_number(idx), width=5, height=2, font=("Arial", 16))
    decrement_button.grid(row=i, column=2, pady=5)

# Create result label
result_label = tk.Label(number_lock_page, text="", font=("Arial", 16), width=30, height=2)
result_label.pack(pady=10)

# Create game timer label
game_timer_label = tk.Label(number_lock_page, text="", font=("Arial", 24))

# Create check button
check_button = tk.Button(number_lock_page, text="Check Combination", command=check_combination, width=20, height=3, font=("Arial", 16))
check_button.pack(pady=10)
```
>Lastly, the placements of all the different buttons and widgets, labels.

## Laser

> For reference, the speakers number in the room: 

<img src = "./Media Assests/SpeakerPlacement.png">

>For My team,only speaker 5  are our responsibility to maintain the condition and set up of the lasers.
>
> For hardware setup, see: [Backlog 3 Sprint 1](../Backlog%203%20Sprint%201/B3S1.md).
>
>For the laser show, there are only 3 codes required which are:
>
> 1. [lasershow.py](./Laser/lasershow.py) - the main GUI to start the laser show sequence.
> 2. [osclaser_server_V2.py](./Laser/osclaser_server_V2.py) - To be run on Master PI to send OSC commands received to other slave PIs.
> 3. [osclaser_trigger_V2.py](./Laser/osclaser_trigger_V2.py) - To be run on slave PI to turn on the laser module for the respective speakers.
>
>Due to the addition of another neo pixel in the balloon, and now there are also lighting sequences happening during the laser show.
>
> [lasershow.py](./Laser/lasershow.py) - when running the code, this is what is shown: 
<img src = './Media Assests/lasergui.png'>
><b>Start Show</b> - Starts the whole laser sequence show with music and lighting sequence.
>
><b>MUSIC Only</b> - Only plays the music used for the laser show.
>
><b>All laser on</b> - Sends OSC messages to turn on all the lasers.
>
><b>All laser Off</b> - Sends OSC messages to turn off all the lasers.
>
><b>Neo Pixel</b> - Only plays the neo pixel functions in both the truss and the balloon.
>
><b>Stop Show</b> - Stops the Reaper and the lighting sequence on the GrandMA3.

> In this code, take note of the following:
```
# Set the IP and port of the OSC server (the Raspberry Pi running your NeoPixel control code)
SERVER_IP = "192.168.254.242"  # Change to your RPi's IP address
SERVER_PORT = 2005

#Set the IP and port for the second neopixel in the balloon
SERVER_IP2 = "192.168.254.102"  # Change to your RPi's IP address
SERVER_PORT2 = 2006

client = udp_client.SimpleUDPClient(SERVER_IP, SERVER_PORT)
client2 = udp_client.SimpleUDPClient(SERVER_IP2, SERVER_PORT2)

PI_A_ADDR = "192.168.254.49"  # Laser control RPi IP address
DAW_A_ADDR = "192.168.254.30" #DAW IP
PORT_LASER = 2000
PORT_DAW = 4869 #DAW PORT
addr = "/print"
LAPTOP_IP = "192.168.254.229"
MA_PORT = 8888
addr1 = "/gma3/cmd"
```
>Make sure to change the respective IP Addresses and port number accordingly to the IP Addresses of the software. Port number must be different from one another. We wil take a look at each function on the respective softwares. 
>
><b>REAPER</b>
```
def play():
    global DAW_A_ADDR
    global PORT_DAW
    addr1 = "/action/1007"
    msg = float(1)
    send_message(DAW_A_ADDR,PORT_DAW,addr1,msg)

def pause():
    global DAW_A_ADDR
    global PORT_DAW
    addr1 = "/action/1008"
    msg = float(1)
    send_message(DAW_A_ADDR,PORT_DAW,addr1,msg)

def gomusic():
    global DAW_A_ADDR
    global PORT_DAW
    addr1 = "/marker/65"
    msg = float(1)
    send_message(DAW_A_ADDR,PORT_DAW,addr1,msg)
```
> <b>play</b> - Plays the timeline on Reaper

> <b>pause</b> - Pauses the timeline on Reaper

> <b>gomusic</b> - There is a marker created on the reaper timeline for Team E's laser music, this function just sends OSC to Reaper to allow it to travel to that marker.

><b>Neo Pixel</b>
```
# Truss Neopixel
def send_color_array(colors):
    address = "/color_array"
    flattened_colors = [color for rgb in colors for color in rgb]
    client.send_message(address, flattened_colors)
    print(f"Sent color array: {flattened_colors}")

def send_brightness(brightness):
    client.send_message("/brightness", brightness)
    print(f"Sent brightness {brightness}")

def send_off():
    client.send_message("/off", [])
    print("Sent off message")

# Ballon Neopixel
def send_color_array2(colors):
    address = "/color_array"
    flattened_colors = [color for rgb in colors for color in rgb]
    client2.send_message(address, flattened_colors)
    print(f"Sent color array: {flattened_colors}")

def send_brightness2(brightness):
    client2.send_message("/brightness", brightness)
    print(f"Sent brightness {brightness}")

def send_off2():
    client2.send_message("/off", [])
    print("Sent off message")

```

><b>send_color_array(colors)</b> - Sends OSC message to the Raspberry PI running Neo Pixel on the truss. r,g,b represents the color code which can be customised for the neo pixel to display different colors.
>
><b>send_brightness</b> - sends OSC message to the Raspbery PI running Neo Pixel to control the brightness of the Neo Pixel on the truss. 0.1 being the lowest brightness, and 1 being the highest brightness.
>
><b>send_off</b> - sends OSC message to the Raspberry PI running Neo Pixel on the Truss to turn off.
>
><b>send_color_array2(colors)</b> - Sends OSC message to the Raspberry PI running Neo Pixel in the balloon. r,g,b represents the color code which can be customised for the neo pixel to display different colors.
>
><b>send_brightness2</b> - sends OSC message to the Raspbery PI running Neo Pixel to control the brightness of the Neo Pixel in the balloon. 0.1 being the lowest brightness, and 1 being the highest brightness.
>
><b>send_off2</b> - sends OSC message to the Raspberry PI running Neo Pixel in the balloon to turn off.
>
><b>Laser Functions</b> - There are only 2 functions given to turn on and turn off the lasers.
```

def laseron():
    lasers = ["2,1,1","2,2,1","5,1,1","5,2,1","8,1,1","8,2,1","11,1,1","11,2,1"]
    for laser in lasers:
        send_message(PI_A_ADDR,PORT_LASER,addr,laser)

def laseroff():
    lasers = ["2,1,0","2,2,0","5,1,0","5,2,0","8,1,0","8,2,0","11,1,0","11,2,0"]
    for laser in lasers:
        send_message(PI_A_ADDR,PORT_LASER,addr,laser)
```
>These functions prints the message using For Loop function, and sends each message in the list 'lasers' to send to the Master PI, which then sends out to the specifc Raspberry PI to control the lasers.

>Next, are the functions for the Neo Pixels:

```
def set_all_pixels_color(color):
    # Create an array with the same color for all 170 pixels
    colors = [color] * 170

    # Send the color array to the NeoPixels
    send_color_array(colors)
```
> This function sets all the pixels of the neo pixel in the truss to be one color.

```
def set_section_colors(section1_color, section2_color, section3_color):
    # Define the sections
    section1_end = 57
    section2_end = 113

    colors = [(0, 0, 0)] * 170
    # Set colors for each section
    for i in range(170):
        if i < section1_end:
            colors[i] = section1_color
        elif i < section2_end:
            colors[i] = section2_color
        else:
            colors[i] = section3_color
    send_color_array(colors)
```
> This function splits the 170 pixels in the neo pixel on the truss into three different sections, mainly from pixel 1-57, 58-113 and 114-170, and allows for indivdual section controls of the color.

```
def create_rainbow_colors(num_pixels):
    # Define the RGB colors for a simple rainbow
    rainbow_colors = [
        (255, 0, 0),    # Red
        (255, 127, 0),  # Orange
        (255, 255, 0),  # Yellow
        (0, 255, 0),    # Green
        (0, 0, 255),    # Blue
        (75, 0, 130),   # Indigo
        (148, 0, 211)   # Violet
    ]
    
    # Calculate the number of pixels per color
    num_colors = len(rainbow_colors)
    pixels_per_color = num_pixels // num_colors
    remainder_pixels = num_pixels % num_colors
    
    colors = []
    
    for i, color in enumerate(rainbow_colors):
        count = pixels_per_color
        if i < remainder_pixels:
            count += 1
        colors.extend([color] * count)
    
    return colors

def display_rainbow(num_pixels):
    colors = create_rainbow_colors(num_pixels)
    send_color_array2(colors)
```
>Creates a rainbow on the neopixel in the balloon

```
def wave_transition():
    num_pixels_170 = 170
    num_pixels_101 = 101
    interval = 13/num_pixels_170

    # Create a wave pattern for the 170-pixel strip
    for offset in range(num_pixels_170):
        colors_170 = [(50, 205, 50)] * num_pixels_170
        for i in range(offset, offset + 10):
            if i < num_pixels_170:
                colors_170[i] = (75, 0, 130)  # Red wave

        send_color_array(colors_170)
        time.sleep(interval)

    # Transition the wave to the 101-pixel strip
    colors_101 = colors_170[:num_pixels_101]
    send_color_array2(colors_101)
```
>Creates a wave transition from the neo pixel in the truss all the way to the neo pixel in the balloon.

```
delay_pixel = 13/170
def onebyone():
    colors = [(0,0,0)] * 170
    for i in range(170):
        colors[i] = (255,255,255)
        send_color_array(colors)
        time.sleep(delay_pixel)
    send_off()
```
>This function creates a function where each pixels after a delay lights up one by one in 13 seconds before turning everything off

```
def strobe_pink(duration=6, interval=0.1):
    num_pixels_170 = 170
    num_pixels_101 = 101
    end_time = time.time() + duration

    pink_color = (255, 105, 180)
    off_color = (0, 0, 0)

    while time.time() < end_time:
        # Strobe on with pink color
        colors_170 = [pink_color] * num_pixels_170
        colors_101 = [pink_color] * num_pixels_101
        send_color_array(colors_170)
        send_color_array(colors_101)
        time.sleep(interval)

        # Strobe off
        colors_170 = [off_color] * num_pixels_170
        colors_101 = [off_color] * num_pixels_101
        send_color_array(colors_170)
        send_color_array(colors_101)
        time.sleep(interval)

    send_off(client)
    send_off(client2)
```
>This function makes both the neo pixel in the truss and in the balloon strobe pink for 6 seconds.
```
    BPM = 113  # Set the BPM of the songdef wave_transition()
    strobe_duration = 11  # Total strobe duration in seconds
    delay_per_flash = 60 / BPM  # Calculate delay between flashes based on BPM
    strobe_colors = [(0, 0, 255), (255, 0, 0), (0, 255, 0)]  # Blue, Red, Green

    end_time = time.time() + strobe_duration
    while time.time() < end_time:
        for color in strobe_colors:
            if time.time() >= end_time:
                break
            colors = [color] * 170  # Set all pixels to the current strobe color
            send_color_array(colors)
            time.sleep(delay_per_flash) 
        send_off()
```
>This function makes the neo pixel in the truss strobes blue,red, green for 11 seconds.
```
delay_pixel2 = 13/170
def reverse_pixel_off(delay_pixel=0.1):
    num_pixels_170 = 170

    # Start with all pixels lit (e.g., white)
    colors = [(255, 255, 255)] * num_pixels_170
    send_color_array(colors)

    # Turn off each pixel one by one from the end to the beginning
    for i in range(num_pixels_170 - 1, -1, -1):
        colors[i] = (0, 0, 0)
        send_color_array(colors)
        time.sleep(delay_pixel2)
    send_off()
```
>Lastly, this function lights all the pixels in the neo pixel in the truss, before turning each pixel individually until all the pixels has been turned off, for a duration of 13 seconds.

><b>GrandMA3</b>
```
def lightstart():
    global LAPTOP_IP
    global MA_PORT
    global addr1
    msg = "Go+ Sequence 87"
    send_message(LAPTOP_IP, MA_PORT, addr1, msg)

def lightmid():
    global LAPTOP_IP
    global MA_PORT
    global addr1
    msg = "Go+ Sequence 89"
    send_message(LAPTOP_IP, MA_PORT, addr1, msg)


def offsequence():
    global LAPTOP_IP
    global MA_PORT
    global addr1
    msg = "Off MyRunningSequence"
```
><b>lightstart</b> - This function starts the sequence for the laser show, where each cue in the sequence has been aligned to sync with the music perfectly.
><b>lightmid</b> - This function points a light near the middle of the room to present the certificate for completing our showcase.
><b>offsequence</b> - This function clears the sequence currently running.

>[osclaser_server_V2.py](./Laser/osclaser_server_V2.py) - In this code, take note of the following:
```
receiver_ip = "192.168.254.49" # Team A
receiver_port = 2000
```
> Change the receiver_ip and receiver_port accordingly to the IP Address of the Master PI. In this project scenario, we will be using '192.168.254.49' as the IP Address. 

```
    if 1 <= spk <= 3:
       send_addr = "IP Address" #Team C
       send_port = 2001
    elif 4 <= spk <= 6:
      send_addr = "IP Address" #Team E
      send_port = 2002
    elif 7 <= spk <= 9:
      send_addr = "IP Address" #Team B
      send_port = 2003
    elif 10 <= spk <= 12:
      send_addr = "IP Address" #Team F
      send_port = 2004
```
> When the Master PI receives OSC messages sent from each team respective PIs, according to the first number in the message received, will then send the message to the respective team Pis. For example, one of the messages the Master Pi may receive is "1,2,1", where since the first number is the speaker number, hence it will send the message to Team C's Slave Pi.

>[osclaser_trigger_V2.py](./Laser/osclaser_trigger_V2.py) - To be run on the respective Slave PIs to turn on/off the laser modules. 

```
r1_c1 = 21
r1_c2 = 20
r2_c1 = 26
r2_c2 = 19
r3_c1 = 3
r3_c2 = 2
```

>Intialising the GPIO pins where each relay module are connected 

```
GPIO.setmode(GPIO.BCM)
GPIO.setup(r1_c1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(r1_c2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(r2_c1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(r2_c2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(r3_c1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(r3_c2, GPIO.OUT, initial=GPIO.HIGH)
```

>Making each laser to turn off at the start when running the code, as they are arranged on normally open connections.

```
receiver_ip = "192.168.254.101" # IP address of your Pi
receiver_port = 2002 # Team C: 2001, Team E: 2002, Team B: 2003, Team F: 2004
```
> Change the receiver_ip and receiver_port IP Address respectively, howeger in this case we wil be using Team Es' Raspberry Pi IP Address.

```
        elif spk == 6: # Change according to spk number (refer to S536 drawing)
            if channel == 1:
                if value == 1:
                    GPIO.output(r3_c1, GPIO.LOW)
                    print("Relay 3 channel 1 turned ON")
                elif value == 0:
                    GPIO.output(r3_c1, GPIO.HIGH)
                    print("Relay 3 channel 1 turned OFF")
            elif channel == 2:
                if value == 1:
                    GPIO.output(r3_c2, GPIO.LOW)
                    print("Relay 3 channel 2 turned ON")
                elif value == 0:
                    GPIO.output(r3_c2, GPIO.HIGH)
                    print("Relay 3 channel 2 turned OFF")

```
> When the slave Pi receives a message from Master Pi, it will send the command to turn on which channels in the relay module. For example, when the Slave PI receives "6,2,1", it will turn on laser channel 2 on speaker 6.

```
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/trigger", control_relay) 

server = osc_server.ThreadingOSCUDPServer((receiver_ip, receiver_port), dispatcher)
print("serving on {}".format(server.server_address))
```
> Start a server on the Slave PI to listen to OSC commands given by Master PI 
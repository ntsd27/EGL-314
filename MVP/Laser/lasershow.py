from pythonosc import udp_client
import time
import tkinter as tk





def send_message(receiver_ip, receiver_port, address, message):
    try:
        client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
        client.send_message(address, message)
        print(f"Message '{message}' sent successfully to {receiver_ip}:{receiver_port}.")
    except Exception as e:
        print(f"Failed to send message '{message}' to {receiver_ip}:{receiver_port}. Error: {e}")

def send_color(receiver_ip, receiver_port, r, g, b):
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
    client.send_message("/color", [r, g, b])

def send_brightness(receiver_ip, receiver_port, brightness):
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
    client.send_message("/brightness", [brightness])

# FOR INFO: IP address and port of the receiving Raspberry Pi
PI_A_ADDR = "192.168.254.49"  # Laser control RPi IP address
DAW_A_ADDR = "192.168.254.30" #DAW IP
NEO_PIXEL_ADDR = "192.168.254.242"  # NeoPixel RPi IP address
PORT_LASER = 2000
PORT_PIXEL = 2005
PORT_DAW = 4869 #DAW PORT
addr = "/print"

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



# Pattern: Turn on all lasers on the right side (speakers 1, 2, 3)
def turn_on_right():
    messages = [
        "1,1,1", "1,2,1", "2,1,1", "2,2,1", "3,1,1", "3,2,1"
    ]
    for message in messages:
        send_message(PI_A_ADDR, PORT_LASER, addr, message)
    send_color(NEO_PIXEL_ADDR, PORT_PIXEL, 255, 0, 0)  # Red color for right side
    time.sleep(0.5)
    send_brightness(NEO_PIXEL_ADDR, PORT_PIXEL, 0.25)

# Pattern: Turn on all lasers on the back side (speakers 4, 5, 6)
def turn_on_back():
    messages = [
        "4,1,1", "4,2,1", "5,1,1", "5,2,1", "6,1,1", "6,2,1"
    ]
    for message in messages:
        send_message(PI_A_ADDR, PORT_LASER, addr, message)
    send_color(NEO_PIXEL_ADDR, PORT_PIXEL, 255, 0, 0)  # Green color for back side
    time.sleep(0.5)
    send_brightness(NEO_PIXEL_ADDR, PORT_PIXEL, 0.50)

# Pattern: Turn on all lasers on the left side (speakers 7, 8, 9)
def turn_on_left():
    messages = [
        "7,1,1", "7,2,1", "8,1,1", "8,2,1", "9,1,1", "9,2,1"
    ]
    for message in messages:
        send_message(PI_A_ADDR, PORT_LASER, addr, message)
    send_color(NEO_PIXEL_ADDR, PORT_PIXEL, 255, 0, 0)  # Blue color for left side
    time.sleep(0.5)
    send_brightness(NEO_PIXEL_ADDR, PORT_PIXEL, 0.75)

def turn_corner():
    messages = ["1,1,1","1,2,1","3,1,1","3,2,1","4,1,1","4,2,1","6,1,1","6,2,1",
                "7,1,1","7,2,1","9,1,1","9,2,1","12,1,1"]
    for message in messages:
        send_message(PI_A_ADDR, PORT_LASER, addr, message)
    send_color(NEO_PIXEL_ADDR, PORT_PIXEL, 255, 0, 0)
    time.sleep(0.5)
    send_brightness(NEO_PIXEL_ADDR, PORT_PIXEL, 1)

def turn_corneroff():
    messages = ["1,1,0","1,2,0","3,1,0","3,2,0","4,1,0","4,2,0","6,1,0","6,2,0",
                "7,1,0","7,2,0","9,1,0","9,2,0","12,1,0"]
    for message in messages:
        send_message(PI_A_ADDR, PORT_LASER, addr, message)
    send_color(NEO_PIXEL_ADDR, PORT_PIXEL, 0, 0, 0)
    time.sleep(0.5)
    send_brightness(NEO_PIXEL_ADDR, PORT_PIXEL, 0)

def turn_middleoff():
    messages = ["2,1,0","2,2,0","5,1,0","5,2,0",
                "8,1,0","8,2,0","11,1,0"]
    for message in messages:
        send_message(PI_A_ADDR, PORT_LASER, addr, message)
    send_color(NEO_PIXEL_ADDR, PORT_PIXEL, 0, 0, 0)
    time.sleep(0.5)
    send_brightness(NEO_PIXEL_ADDR, PORT_PIXEL, 0)

def turn_middle():
    messages = ["2,1,1","2,2,1","5,1,1","5,2,1",
                "8,1,1","8,2,1","11,1,1"]
    for message in messages:
        send_message(PI_A_ADDR, PORT_LASER, addr, message)
    send_color(NEO_PIXEL_ADDR, PORT_PIXEL, 128, 0, 0)
    time.sleep(0.5)
    send_brightness(NEO_PIXEL_ADDR, PORT_PIXEL, 0.5)

def sequenceon():
    messages = [
        "1,1,1", "1,2,1", "2,1,1", "2,2,1", "3,1,1", "3,2,1", "4,1,1", "4,2,1", 
        "5,1,1", "5,2,1", "6,1,1", "6,2,1", "7,1,1", "7,2,1", "8,1,1", "8,2,1", 
        "9,1,1", "9,2,1", "11,1,1", "12,1,1"
    ]
    for message in messages:
        send_message(PI_A_ADDR, PORT_LASER, addr, message)
        time.sleep(sequence_beat)
    send_color(NEO_PIXEL_ADDR, PORT_PIXEL, 0, 0, 255)
    time.sleep(0.5)
    send_brightness(NEO_PIXEL_ADDR, PORT_PIXEL, 0.75)

def sequenceoff():
    messages = [
        "1,1,0", "1,2,0", "2,1,0", "2,2,0", "3,1,0", "3,2,0", "4,1,0", "4,2,0", 
        "5,1,0", "5,2,0", "6,1,0", "6,2,0", "7,1,0", "7,2,0", "8,1,0", "8,2,0", 
        "9,1,0", "9,2,0", "11,1,0", "12,1,0"
    ]
    for message in messages:
        send_message(PI_A_ADDR, PORT_LASER, addr, message)
        time.sleep(sequence_beat)
    send_color(NEO_PIXEL_ADDR, PORT_PIXEL, 0, 0, 0)
    time.sleep(0.5)
    send_brightness(NEO_PIXEL_ADDR, PORT_PIXEL, 0)

# Pattern: Turn on all lasers on the front side (speakers 10, 11, 12)
def turn_on_front():
    messages = [
        "10,1,1", "10,2,1", "11,1,1", "12,1,1",
    ]
    for message in messages:
        send_message(PI_A_ADDR, PORT_LASER, addr, message)
    send_color(NEO_PIXEL_ADDR, PORT_PIXEL, 255, 255, 0)  # Yellow color for front side
    time.sleep(0.5)
    send_brightness(NEO_PIXEL_ADDR, PORT_PIXEL, 0.25)

def star():
    messages = [
        "4,1,1", "4,2,1","6,1,1", "6,2,1",  "9,1,1", "9,2,1","1,1,1", "1,2,1",  "11,1,1"
        ]
    for message in messages:
        send_message(PI_A_ADDR, PORT_LASER, addr, message)
        time.sleep(star_beat)
    send_color(NEO_PIXEL_ADDR, PORT_PIXEL, 255, 255, 0)
    time.sleep(0.5)
    send_brightness(NEO_PIXEL_ADDR, PORT_PIXEL, 1)




# Off pattern: Turn off all lasers and set NeoPixel to black
def off_pattern():
    messages = [
        "1,1,0", "1,2,0", "2,1,0", "2,2,0", "3,1,0", "3,2,0", "4,1,0", "4,2,0", 
        "5,1,0", "5,2,0", "6,1,0", "6,2,0", "7,1,0", "7,2,0", "8,1,0", "8,2,0", 
        "9,1,0", "9,2,0", "10,1,0", "10,2,0", "11,1,0", "11,2,0", "12,1,0", "12,2,0"
    ]
    for message in messages:
        send_message(PI_A_ADDR, PORT_LASER, addr, message)
    send_color(NEO_PIXEL_ADDR, PORT_PIXEL, 0,0,0)  # Turn off NeoPixel
    print("All lasers turned off.")

def playdaw():
    gomusic()
    play()
    main.after(30000,pause)

# Calculate the duration of each beat
bpm = 92
beat_duration = 60 / bpm
sequence_beat= beat_duration / 20
star_beat = beat_duration / 9

def start_show():
    playdaw()
    mainshow()

def allon():
    turn_on_back()
    turn_on_front()
    turn_on_right()
    turn_on_left()

# Main loop to run the show
def mainshow():
    turn_on_right()
    time.sleep(beat_duration)  # Adjust timing based on the song's structure
    turn_on_back()
    time.sleep(beat_duration)  # Adjust timing based on the song's structure
    turn_on_left()
    time.sleep(beat_duration)  # Adjust timing based on the song's structure
    turn_on_front()
    time.sleep(beat_duration)  # Adjust timing based on the song's structure
    off_pattern()
    time.sleep(beat_duration)  # Adjust timing based on the song's structure
    sequenceon()
    sequenceoff()
    turn_corner()
    time.sleep(beat_duration)
    turn_corneroff()
    time.sleep(beat_duration)
    turn_middle()
    time.sleep(beat_duration)
    turn_middleoff()
    off_pattern()
    time.sleep(beat_duration)
    star()
    time.sleep(beat_duration)
    off_pattern()
    turn_on_back()
    turn_on_left()
    turn_on_back()
    turn_on_right()
    off_pattern()
    turn_on_left()
    turn_on_right()
    off_pattern()
    turn_corner()
    time.sleep(beat_duration)
    turn_corner()
    time.sleep(beat_duration)
    sequenceon()
    sequenceoff()
    star()
    time.sleep(beat_duration)
    off_pattern()
    star()
    time.sleep(beat_duration)
    sequenceon()
    time.sleep(beat_duration)
    sequenceoff() 
    turn_corner()
    turn_middle()
    time.sleep(beat_duration)
    off_pattern()
    print("Laser show finished.")

main = tk.Tk()
main.title("Laser Show Controller")

start_button = tk.Button(main,command=start_show, text= 'Start Show')
start_button.grid(row = 0, column= 0)

music_button = tk.Button(main,command=playdaw, text= 'MUSIC Only')
music_button.grid(row = 0, column= 1)

laseron_button = tk.Button(main,command=allon, text= 'All laser On')
laseron_button.grid(row = 0, column= 2)

main.mainloop()

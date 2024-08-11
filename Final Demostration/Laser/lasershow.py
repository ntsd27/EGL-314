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

# Set the IP and port of the OSC server (the Raspberry Pi running your NeoPixel control code)
SERVER_IP = "192.168.254.242"  # Change to your RPi's IP address
SERVER_PORT = 2005

#Set the IP and port for the second pi
SERVER_IP2 = "192.168.254.102"  # Change to your RPi's IP address
SERVER_PORT2 = 2006

# Create an OSC client
client = udp_client.SimpleUDPClient(SERVER_IP, SERVER_PORT)
client2 = udp_client.SimpleUDPClient(SERVER_IP2, SERVER_PORT2)

################################# Functions DO NOT TOUCH!!!!############################################################################

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


# FOR INFO: IP address and port of the receiving Raspberry Pi
PI_A_ADDR = "192.168.254.49"  # Laser control RPi IP address
DAW_A_ADDR = "192.168.254.30" #DAW IP
PORT_LASER = 2000
PORT_DAW = 4869 #DAW PORT
addr = "/print"
LAPTOP_IP = "192.168.254.229"
MA_PORT = 8888
addr1 = "/gma3/cmd"

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
    send_message(LAPTOP_IP, MA_PORT, addr1, msg)

def laseron():
    lasers = ["2,1,1","2,2,1","5,1,1","5,2,1","8,1,1","8,2,1","11,1,1","11,2,1"]
    for laser in lasers:
        send_message(PI_A_ADDR,PORT_LASER,addr,laser)

def laseroff():
    lasers = ["2,1,0","2,2,0","5,1,0","5,2,0","8,1,0","8,2,0","11,1,0","11,2,0"]
    for laser in lasers:
        send_message(PI_A_ADDR,PORT_LASER,addr,laser)


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

def playdaw():
    gomusic()
    play()

def set_all_pixels_color(color):
    # Create an array with the same color for all 170 pixels
    colors = [color] * 170

    # Send the color array to the NeoPixels
    send_color_array(colors)

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

delay_pixel = 13/170

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
        send_color_array(colors_101
        time.sleep(interval)

    send_off(client)
    send_off(client2)

def onebyone():
    colors = [(0,0,0)] * 170
    for i in range(170):
        colors[i] = (255,255,255)
        send_color_array(colors)
        time.sleep(delay_pixel)
    send_off()

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

    wave_transition()
    strobe_pink()
    set_section_colors((0,0,0),(0,0,0),(0,0,0))
    time.sleep(1.0)
    set_section_colors((255, 0, 0),(0,0,0),(255,0,255))
    time.sleep(1.0)
    set_section_colors((0,0,0),(255,255,0),(0, 255, 0))
    time.sleep(1.0)
    set_section_colors((0, 255, 0),(255,0,0),(255,0,0))
    time.sleep(1.0)
    set_section_colors((0,0,255),(0,0,0),(255, 255, 0))
    time.sleep(1.0)
    set_section_colors((0,255,0),(255,0,255),(255, 255, 255))
    time.sleep(1.0)
    set_all_pixels_color((255,255,0))
    display_rainbow(101)
    colors = [(0,0,0)] * 170
    send_color_array2(colors)
    send_color_array(colors)
    reverse_pixel_off()

def start():
    playdaw()
    lightstart()
    main.after(60000,stop)
    main.after(60000,lightmid)
    colors = [(0,0,0)] * 170
    for i in range(170):
        colors[i] = (255,255,255)
        send_color_array(colors)
        time.sleep(delay_pixel)
    send_off()
    laseron()
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
    laseroff()
    wave_transition()
    laseron()
    strobe_pink()
    laseroff()
    set_section_colors((0,0,0),(0,0,0),(0,0,0))
    time.sleep(1.0)
    set_section_colors((255, 0, 0),(0,0,0),(255,0,255))
    time.sleep(1.0)
    set_section_colors((0,0,0),(255,255,0),(0, 255, 0))
    time.sleep(1.0)
    set_section_colors((0, 255, 0),(255,0,0),(255,0,0))
    time.sleep(1.0)
    set_section_colors((0,0,255),(0,0,0),(255, 255, 0))
    time.sleep(1.0)
    set_section_colors((0,255,0),(255,0,255),(255, 255, 255))
    time.sleep(1.0)
    set_all_pixels_color((255,255,0))
    display_rainbow(101)
    colors = [(0,0,0)] * 170
    send_color_array2(colors)
    send_color_array(colors)
    reverse_pixel_off()






# Calculate the duration of ea+ch beat
def start_show():
    playdaw()
    onebyone()
    colors = [(0, 255, 0)] * 170  # Red, Green, Blue sections
    send_color_array(colors)
    send_off()
    colors = [(0, 0, 255)] * 170 
    send_color_array(colors)
    time.sleep(1)
    send_brightness2(0.05)
    time.sleep(1)
    send_brightness2(0.6)
    time.sleep(1)
    colors = [(255,0,0)]*170
    send_color_array2(colors)
        
    time.sleep(0.5)
    send_off2()
    send_off()

def stop():
    pause()
    offsequence()



# Main loop to run the show

main = tk.Tk()
main.title("Laser Show Controller")

start_button = tk.Button(main,command=start, text= 'Start Show')
start_button.grid(row = 0, column= 0)

music_button = tk.Button(main,command=playdaw, text= 'MUSIC Only')
music_button.grid(row = 0, column= 1)

laseron_button = tk.Button(main,command=laseron, text= 'All laser On')
laseron_button.grid(row = 0, column= 2)

laseroff_button = tk.Button(main,command=laseroff, text= 'All laser Off')
laseroff_button.grid(row = 0, column= 3)

neopixel_button = tk.Button(main,command=onebyone, text= 'Neo Pixel')
neopixel_button.grid(row = 0, column= 4)

stopshow_button = tk.Button(main,command=stop, text= 'Stop Show')
stopshow_button.grid(row = 0, column= 5)

main.mainloop()
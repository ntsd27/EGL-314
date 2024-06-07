import subprocess
import time
import socket
import sys 
import tkinter as Tk

from pythonosc import udp_client

def run_command(command):
    text = 'python3 command.py '
    config = text + command
    print(config)
    try:
        output = subprocess.check_output(config, shell=True)
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.returncode}, {e.output.decode('utf-8')}")

def run_recall(command):
    text = 'python3 recall.py '
    config = text + command
    print(config)
    try:
        output = subprocess.check_output(config, shell=True)
        print(output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.returncode}, {e.output.decode('utf-8')}")

def send_message(receiver_ip, receiver_port, address, message):
    try:
        # Create an OSC client to send messages
        client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

        # Send an OSC message to the receiver
        client.send_message(address, message)

        print("Message sent successfully.")
    except:
        print("Message not sent")

def volume_up1():
    command = 'set MIXER:Current/InCh/Fader/Level 0 0 1000'
    run_command(command)
    time.sleep(1)

def volume_up2():
    command = 'set MIXER:Current/InCh/Fader/Level 1 0 1000'
    run_command(command)
    time.sleep(1)


def toggle_mute1():
    command = 'set MIXER:Current/InCh/Fader/On  0 0 0'
    run_command(command)
    time.sleep(1)

def toggle_mute2():
    command = 'set MIXER:Current/InCh/Fader/On  1 0 0'
    run_command(command)
    time.sleep(1)

def toggle_unmute1():
    command = 'set MIXER:Current/InCh/Fader/On  0 0 1'
    run_command(command)
    time.sleep(1)

def toggle_unmute2():
    command = 'set MIXER:Current/InCh/Fader/On  1 0 1'
    run_command(command)
    time.sleep(1)

def volume_down1():
    command = 'set MIXER:Current/InCh/Fader/Level 0 0 0'
    run_command(command)
    time.sleep(1)

def volume_down2():
    command = 'set MIXER:Current/InCh/Fader/Level 1 0 0'
    run_command(command)
    time.sleep(1)




def send_osc():
    # Define OSC message parameters and send OSC message
    PI_A_ADDR = "192.168.1.128"  # IP address of the receiving Raspberry Pi
    PORT = 49820  # Port of the receiving Raspberry Pi

    addr = "/print"
    msg = "salutations from pi_B"
    send_message(PI_A_ADDR, PORT, addr, msg)

main = Tk.Tk()
main.title("Audio Mixer Control")

person1_label = Tk.Label(main, text="Person 1 Volume")
person1_label.grid(row=1, column=1,)
person1_up_button = Tk.Button(main, text = 'Up', command = volume_up1)
person1_up_button.grid(row=2, column=1)
person1_down_button = Tk.Button(main, text="Down", command=volume_down1 )
person1_down_button.grid(row=4, column=1)

# Person 2 Volume Buttons
person2_label = Tk.Label(main, text="Person 2 Volume")
person2_label.grid(row=1, column=3)
person2_up_button = Tk.Button(main, text="Up", command=volume_up2)
person2_up_button.grid(row=2, column=3)
person2_down_button = Tk.Button(main, text="Down", command=volume_down2)
person2_down_button.grid(row=4, column=3,)

person2_umute = Tk.Button(main, text="Person 2 unmute", command=toggle_unmute2)
person2_umute.grid(row=6, column=3)
person1_mute = Tk.Button(main, text="Person 1 mute", command=toggle_mute1)
person1_mute.grid(row=5, column = 1)
person2_mute = Tk.Button(main, text="Person 2 mute", command=toggle_mute2)
person2_mute.grid(row=5, column = 3)
person1_unmute = Tk.Button(main, text="Person 1 unmute", command=toggle_unmute1)
person1_unmute.grid(row=6, column = 1)

main.mainloop()


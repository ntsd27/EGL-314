import tkinter as tk
from tkinter import messagebox
import RPi.GPIO as GPIO

# Define GPIO pins
pins = {
    'Laser 1': 21,
    'Laser 2': 20,
    'Laser 3': 26,
    'Laser 4': 19,
    'Laser 5': 3,
    'Laser 6': 2
}

# Setup GPIO
GPIO.setmode(GPIO.BCM)
for pin in pins.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Toggle function
def toggle_laser(laser):
    pin = pins[laser]
    GPIO.output(pin, not GPIO.input(pin))

# Turn all lasers on
def all_on():
    for pin in pins.values():
        GPIO.output(pin, GPIO.LOW)

# Turn all lasers off
def all_off():
    for pin in pins.values():
        GPIO.output(pin, GPIO.HIGH)

# Create GUI
root = tk.Tk()
root.title("Laser Control")

# Laser buttons
for laser in pins.keys():
    button = tk.Button(root, text=laser, command=lambda l=laser: toggle_laser(l))
    button.pack(pady=5)

# All on/off buttons
all_on_button = tk.Button(root, text="All On", command=all_on)
all_on_button.pack(pady=5)

all_off_button = tk.Button(root, text="All Off", command=all_off)
all_off_button.pack(pady=5)

# Cleanup GPIO on exit
def on_closing():
    GPIO.cleanup()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Start GUI loop
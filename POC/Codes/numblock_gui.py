import tkinter as tk
from PIL import Image, ImageTk
from pythonosc import udp_client
import random
import ma3control
import dawcontrol

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

LAPTOP_IP = "192.168.254.30"
MA_PORT = 8888


# Define the preset combinations
preset_combinations = [
    [2, 5, 7],
    [1, 4, 9],
    [3, 0, 6],
    [8, 2, 4],
    [0, 0, 0]
]


osc_msg_list = [dawcontrol.combi1, dawcontrol.combi2, dawcontrol.combi3, dawcontrol.combi4, dawcontrol.combi5]

# Variable to keep track of the current index
current_index = None
# Counter to track the number of repetitions
repetition_counter = 0
# Flag to indicate if the correct combination is entered
correct_combination_entered = False

# Function to play the current choice and handle repetitions
def play_current_choice():
    global repetition_counter, correct_combination_entered

    if correct_combination_entered:
        return  # Stop the function if the correct combination is entered

    if current_index is not None:
        osc_msg_list[current_index]()  # Call the function at current_index

    repetition_counter += 1

    if repetition_counter < 3:  # Check if the function has been called less than 3 times
        # Schedule the function to run again after a set interval (e.g., 20 seconds)
        main.after(20000, play_current_choice)

def stop_repetitive_function():
    try:
        main.after_cancel(play_current_choice)
    except:
        pass

# Function to choose a random item and start the repetition process
def choose_random_item():
    global current_index, repetition_counter, correct_combination_entered
    current_index = random.randint(0, len(osc_msg_list) - 1)
    repetition_counter = 0  # Reset the repetition counter
    correct_combination_entered = False  # Reset the flag for new choice
    play_current_choice()

# Create the main window
main = tk.Tk()
main.title("Number Combination Lock")
main.geometry("500x500")
main.after(50,ma3control.point)
main.after(50, ma3control.point)
main.after(5000,dawcontrol.intro)
main.after(5000,dawcontrol.play)
main.after(40000,dawcontrol.pause)
# Set the window size

# Initialize the number labels
number_labels = []

# Load the image for the background
image = Image.open("padlock picture.png")  # Replace with the path to your image
image = image.resize((350, 350))  # Resize the image if needed
background_image = ImageTk.PhotoImage(image)

# Create a label to display the background image
background_label = tk.Label(main, image=background_image)
background_label.place(x=0, y=2, relwidth=1, relheight=1)

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
        ma3control.clear()
        main.after(500, dawcontrol.win)
        main.after(500, dawcontrol.play)
        main.after(500, ma3control.correct)
        main.after(7500, reset_to_start_page)
        main.after(7500, ma3control.clear)
        main.after(7500, dawcontrol.pause)
        stop_repetitive_function()

    else:
        result_label.config(text="Incorrect Combination. Try Again.", fg="red", bg="white", font=("Arial", 16, "bold"))
        ma3control.wrong()

# Function to start the countdown before showing the number lock page
def start_countdown():
    main.after(5000, choose_random_item)
    countdown_label.pack()
    countdown(3)

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
    countdown_label.pack_forget()
    start_page.place_forget()
    number_lock_page.place(relx=0.5, rely=0.5, anchor="center")

# Function to start the game timer
def start_game_timer():
    game_timer_label.config(text="60", font=("Arial", 24))
    game_timer_label.pack()
    game_timer(60)

# Function to handle the game timer
def game_timer(seconds):
    global game_timer_id
    if seconds > 0:
        game_timer_label.config(text=str(seconds))
        game_timer_id = main.after(1000, game_timer, seconds-1)
    else:
        game_timer_label.pack_forget()
        result_label.config(text="Time's up! You have lost the game.", fg="red", bg="white", font=("Arial", 16, "bold"))
        ma3control.wrong()
        lose()
        play()
        main.after(3000, reset_to_start_page)
        main.after(3000, ma3control.clear)
        main.after(3000,ma3control.point)
        main.after(3000,dawcontrol.pause)

# Function to reset to the start page
def reset_to_start_page():
    main.after_cancel(game_timer_id)  # Cancel any ongoing game timer
    number_lock_page.place_forget()
    start_page.place(relx=0.5, rely=0.7, anchor="center")
    result_label.config(text="")
    for label in number_labels:
        label.config(text="0")
    countdown_label.pack_forget()  # Hide countdown label for reset
    countdown_label.config(text="")  # Clear countdown label text
    game_timer_label.pack_forget()

# Create frames for different pages
start_page = tk.Frame(main, bg="#a07d48")
number_lock_page = tk.Frame(main, bg="#a07d48")

# Start page widgets
start_button = tk.Button(start_page, text="Start", command=start_countdown)
start_button.pack(pady=10)

button1 = tk.Button(start_page, text="High", command=high)
button1.pack(pady=5)

button2 = tk.Button(start_page, text="Low", command=low)
button2.pack(pady=5)

button3 = tk.Button(start_page, text= "Wind",command=wind)
button3.pack(pady=5)

countdown_label = tk.Label(start_page, text="", font=("Arial", 24))
countdown_label.pack()

# Center the start page in the window
start_page.place(relx=0.5, rely=0.7, anchor="center")

# Number lock page widgets
number_frame = tk.Frame(number_lock_page)
number_frame.pack(pady=18)

for i in range(3):
    increment_button = tk.Button(number_frame, text="+", command=lambda idx=i: increment_number(idx))
    increment_button.grid(row=i, column=0, pady=5)

    number_label = tk.Label(number_frame, text="0", font=("Arial", 24))
    number_label.grid(row=i, column=1, padx=10)
    number_labels.append(number_label)

    decrement_button = tk.Button(number_frame, text="-", command=lambda idx=i: decrement_number(idx))
    decrement_button.grid(row=i, column=2, pady=5)

# Create result label
result_label = tk.Label(number_lock_page, text="", font=("Arial", 16))
result_label.pack(pady=10)

# Create game timer label
game_timer_label = tk.Label(number_lock_page, text="", font=("Arial", 24))

# Create check button
check_button = tk.Button(number_lock_page, text="Check Combination", command=check_combination)
check_button.pack(pady=10)

# Start the main loop
main.mainloop()

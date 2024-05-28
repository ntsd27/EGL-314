import tkinter as tk
from PIL import Image, ImageTk

# Define the preset combinations
preset_combinations = [
    [2, 5, 7],
    [1, 4, 9],
    [3, 0, 6],
    [8, 2, 4],
    [0, 0, 0]
]

# Create the main window
main = tk.Tk()
main.title("Number Combination Lock")

# Initialize the number labels
number_labels = []

# Load the image for the background
image = Image.open("padlock picture.png")  # Replace with the path to your image
image = image.resize((800, 800), Image.LANCZOS)  # Resize the image if needed
background_image = ImageTk.PhotoImage(image)

# Create a label to display the background image
background_label = tk.Label(main, image=background_image)
background_label.pack(fill="both", expand=True)

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
    current_combination = [int(label["text"]) for label in number_labels]
    if current_combination in preset_combinations:
        result_label.config(text="Correct Combination Entered!", fg="green")
    else:
        result_label.config(text="Incorrect Combination!", fg="red")

# Function to start the countdown and flip to the number lock page
def start_countdown():
    countdown_label.config(text="5", font=("Arial", 24))
    countdown_label.grid(row=3, column=0)  # Grid the countdown label
    countdown(5)

def countdown(seconds):
    if seconds > 0:
        countdown_label.config(text=str(seconds))
        main.after(1000, countdown, seconds-1)
    else:
        countdown_label.grid_forget()  # Ungrid the countdown label
        show_number_lock_page()

def show_number_lock_page():
    start_page.pack_forget()
    number_lock_page.pack()

# Start page widgets
start_page = tk.Frame(main)

start_button = tk.Button(start_page, text="Start", command=start_countdown)
start_button.grid(row=0, column=0, pady=10)

play_high_button = tk.Button(start_page, text="Play High", command=lambda: print("Play High clicked"))
play_high_button.grid(row=1, column=0, pady=10)

play_low_button = tk.Button(start_page, text="Play Low", command=lambda: print("Play Low clicked"))
play_low_button.grid(row=2, column=0, pady=10)

countdown_label = tk.Label(start_page, text="", font=("Arial", 24))
countdown_label.grid(row=3, column=0, pady=10)

# Number lock page widgets
number_lock_page = tk.Frame(main)

number_frame = tk.Frame(number_lock_page)
number_frame.place(relx=0.5, rely=0.5, anchor="center")

for i in range(3):
    increment_button = tk.Button(number_frame, text="+", command=lambda idx=i: increment_number(idx))
    increment_button.grid(row=i, column=0)

    number_label = tk.Label(number_frame, text="0", font=("Arial", 24))
    number_label.grid(row=i, column=1)
    number_labels.append(number_label)

    decrement_button = tk.Button(number_frame, text="-", command=lambda idx=i: decrement_number(idx))
    decrement_button.grid(row=i, column=2)

check_button = tk.Button(number_lock_page, text="Check Combination", command=check_combination)
check_button.place(relx=0.5, rely=0.8, anchor="center")

result_label = tk.Label(number_lock_page, text="", font=("Arial", 16))
result_label.place(relx=0.5, rely=0.9, anchor="center")

# Show the start page initially
start_page.pack()

# Run the main loop
main.mainloop()

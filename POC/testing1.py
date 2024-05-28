import tkinter as tk

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
        result_label.config(text="Correct Combination Entered!", fg="green", bg="white", font=("Arial", 16, "bold"))
    else:
        result_label.config(text="Incorrect Combination!", fg="red", bg="white", font=("Arial", 16, "bold"))

# Function to start the countdown
def start_countdown():
    countdown_label.config(text="5", font=("Arial", 24),bg= "yellow")
    countdown_label.pack()
    countdown(5)

# Function to handle the countdown
def countdown(seconds):
    if seconds > 0:
        countdown_label.config(text=str(seconds))
        main.after(1000, countdown, seconds-1)
    else:
        countdown_label.pack_forget()
        show_number_lock_page()

# Function to show the number lock page
def show_number_lock_page():
    start_page.pack_forget()
    number_lock_page.pack()

# Create frames for different pages
start_page = tk.Frame(main)
number_lock_page = tk.Frame(main)

# Start page widgets
start_button = tk.Button(start_page, text="Start", command=start_countdown)
start_button.pack(pady=20)

button1 = tk.Button(start_page, text="Button 1")
button1.pack(pady=5)

button2 = tk.Button(start_page, text="Button 2")
button2.pack(pady=5)

countdown_label = tk.Label(start_page, text="", font=("Arial", 24))

start_page.pack()

# Number lock page widgets
number_frame = tk.Frame(number_lock_page)
number_frame.pack(pady=20)

for i in range(3):
    increment_button = tk.Button(number_frame, text="+", command=lambda idx=i: increment_number(idx))
    increment_button.grid(row=i, column=0, pady=5)

    number_label = tk.Label(number_frame, text="0", font=("Arial", 24))
    number_label.grid(row=i, column=1, padx=10)
    number_labels.append(number_label)

    decrement_button = tk.Button(number_frame, text="-", command=lambda idx=i: decrement_number(idx))
    decrement_button.grid(row=i, column=2, pady=5)

check_button = tk.Button(number_lock_page, text="Check Combination", command=check_combination)
check_button.pack(pady=10)

result_label = tk.Label(number_lock_page, text="", font=("Arial", 16), width=30, height=2)
result_label.pack(pady=10)

# Run the main loop
main.mainloop()

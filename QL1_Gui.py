import tkinter as tk

# Volume levels (initially 50)
person1_volume = 50
person2_volume = 50
master_volume = 50

def volume_change(person, change):
  global person1_volume, person2_volume, master_volume
  if person == "person1":
    person1_volume = min(max(person1_volume + change, 0), 100)  # Clamp between 0 and 100
  elif person == "person2":
    person2_volume = min(max(person2_volume + change, 0), 100)
  elif person == "master":
    master_volume = min(max(master_volume + change, 0), 100)
    # Update person volumes proportionally
    volume_diff = person1_volume - person2_volume
    person1_volume = master_volume + volume_diff / 2
    person2_volume = master_volume - volume_diff / 2
  print(f"Person 1: {person1_volume}, Person 2: {person2_volume}, Master: {master_volume}")  # Update display (optional)

def reset_volumes():
  global person1_volume, person2_volume, master_volume
  person1_volume = 50
  person2_volume = 50
  master_volume = 50

main = tk.Tk()
main.title("Volume Control")  # Set window title

# Padding for elements
padx = 10
pady = 5

# Person 1 Volume Buttons
person1_label = tk.Label(main, text="Person 1 Volume")
person1_label.grid(row=1, column=1, padx=padx, pady=pady)
person1_up_button = tk.Button(main, text="Up", command=lambda: volume_change("person1", 5))
person1_up_button.grid(row=2, column=1, padx=padx)
person1_down_button = tk.Button(main, text="Down", command=lambda: volume_change("person1", -5))
person1_down_button.grid(row=4, column=1, padx=padx)

# Person 2 Volume Buttons
person2_label = tk.Label(main, text="Person 2 Volume")
person2_label.grid(row=1, column=3, padx=padx, pady=pady)
person2_up_button = tk.Button(main, text="Up", command=lambda: volume_change("person2", 5))
person2_up_button.grid(row=2, column=3, padx=padx)
person2_down_button = tk.Button(main, text="Down", command=lambda: volume_change("person2", -5))
person2_down_button.grid(row=4, column=3, padx=padx)

# Master Volume Buttons
master_label = tk.Label(main, text="Master Volume")
master_label.grid(row=1, column=5, padx=padx, pady=pady)
master_up_button = tk.Button(main, text="Up", command=lambda: volume_change("master", 5))
master_up_button.grid(row=2, column=5, padx=padx)
master_down_button = tk.Button(main, text="Down", command=lambda: volume_change("master", -5))
master_down_button.grid(row=4, column=5, padx=padx)

# Reset Button
reset_button = tk.Button(main, text="Reset", command=reset_volumes)
reset_button.grid(row=6, column=3, columnspan=1, padx=padx, pady=pady)

main.mainloop()
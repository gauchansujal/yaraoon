import tkinter as tk
from tkinter import ttk

def search_buses():
    # Placeholder function for searching buses
    departure_location = departure_entry.get()
    arrival_location = arrival_entry.get()
    print(f"Searching for buses from {departure_location} to {arrival_location}")

# Create the main window
root = tk.Tk()
root.title("Bus Management System")

# Create and set the window size
window_width = 1440
window_height = 1024
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create a Canvas for the green rectangle
canvas = tk.Canvas(root, width=1440, height=144, bg="green", highlightthickness=0)
canvas.pack()

# Create labels and entry fields for departure and arrival
departure_label = ttk.Label(root, text="Departure From:")
departure_label.place(x=20, y=200)
departure_entry = ttk.Entry(root)
departure_entry.place(x=150, y=200)

arrival_label = ttk.Label(root, text="Arrival To:")
arrival_label.place(x=20, y=250)
arrival_entry = ttk.Entry(root)
arrival_entry.place(x=150, y=250)

# Create the "Search for Buses" button
search_button = ttk.Button(root, text="Search for Buses", command=search_buses)
search_button.place(x=300, y=300)

# Create the buttons with corner radius using the 'padding' option
button_radius = 6

button1 = ttk.Button(root, text="Button 1", style="Yellow.TButton")
button1.place(x=616, y=65)

button2 = ttk.Button(root, text="Button 2", style="Yellow.TButton")
button2.place(x=815, y=65)

button3 = ttk.Button(root, text="Button 3", style="Yellow.TButton")
button3.place(x=1007, y=65)

button4 = ttk.Button(root, text="Button 4", style="Blue.TButton")
button4.place(x=1197, y=62)

# Create the small circle using Canvas
white_circle = canvas.create_oval(4, 8, 140, 133, fill="white")

# Create a custom style for the buttons with yellow color
root.style = ttk.Style()
root.style.configure("Yellow.TButton", background="yellow", borderwidth=0, paddings=(5, 15, 5, 15), relief="flat", anchor="center")

# Create a custom style for the blue button
root.style.configure("Blue.TButton", background="blue", borderwidth=0, paddings=(5, 15, 5, 15), relief="flat", anchor="center")

# Start the Tkinter event loop
root.mainloop()

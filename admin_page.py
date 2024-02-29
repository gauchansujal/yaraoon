import tkinter as tk
from tkinter import ttk

# Dummy data for demonstration
users = ["Admin", "User1", "User2"]
buses = ["Bus1", "Bus2", "Bus3"]

def manage_users():
    # Implement user management logic here
    print("Managing Users")

def manage_buses():
    # Implement bus management logic here
    print("Managing Buses")

def manage_tickets():
    # Implement ticket management logic here
    print("Managing Tickets")

# Create main window
root = tk.Tk()
root.title("Admin Page")
root.geometry("1200x1000")  # Set the size of the main window

# Create a frame to hold all the widgets
main_frame = ttk.Frame(root,)
main_frame.grid(row=0, column=0, padx=10, pady=10)

# Create tabs
tab_control = ttk.Notebook(main_frame)

# Users tab
users_tab = ttk.Frame(tab_control)
tab_control.add(users_tab, text="Users")

# Create a frame to center the label
users_label_frame = ttk.Frame(users_tab)
users_label_frame.pack(expand=True)

users_label = tk.Label(users_label_frame, text="User Management")
users_label.pack(expand=True, anchor=tk.CENTER)

users_listbox = tk.Listbox(users_tab, height=5, selectmode=tk.SINGLE)
for user in users:
    users_listbox.insert(tk.END, user)
users_listbox.pack()

manage_users_button = tk.Button(users_tab, text="Manage User", command=manage_users)
manage_users_button.pack()

# Buses tab
buses_tab = ttk.Frame(tab_control)
tab_control.add(buses_tab, text="Buses")

buses_label = tk.Label(buses_tab, text="Bus Management")
buses_label.pack()

buses_listbox = tk.Listbox(buses_tab, height=5, selectmode=tk.SINGLE)
for bus in buses:
    buses_listbox.insert(tk.END, bus)
buses_listbox.pack()

manage_buses_button = tk.Button(buses_tab, text="Manage Bus", command=manage_buses)
manage_buses_button.pack()

# Tickets tab
tickets_tab = ttk.Frame(tab_control)
tab_control.add(tickets_tab, text="Tickets")

tickets_label = tk.Label(tickets_tab, text="Ticket Management")
tickets_label.pack()

manage_tickets_button = tk.Button(tickets_tab, text="Manage Ticket", command=manage_tickets)
manage_tickets_button.pack()

tab_control.pack(expand=1, fill="both")

root.mainloop()

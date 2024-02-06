from tkinter import*
from tkinter import messagebox

# def check_login():
#     email = entry_email.get()
#     password = entry_password.get()

#     # Replace the following with your actual authentication logic
#     if email == "admin@example.com" and password == "password":
#         messagebox.showinfo("Login Successful", "Welcome, {}".format(email))
#     else:
#         messagebox.showerror("Login Failed", "Invalid email or password")

# Create the main window
root = Tk()
root.title("Login Page")

# Create and place a frame
frame = Frame(root, width=450, height=662, bg="white")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Create and place widgets inside the frame
signin = Label(frame, text="Sign In", font=("Helvetica", 20, "bold"))
signin.grid(row=0, column=0, columnspan=2, pady=20)

#email button
def temp_email(e):
    Email.delete(0,"end")

Email=Entry(frame, bg="white")
Email.insert(0, "Email id.")
Email.grid(padx=2, pady=3)
Email.bind("<FocusIn>", temp_email)

#password button
def temp_password(e):
    password.delete(0,"end")

password=Entry(frame, bg="white")
password.insert(0, "Password")
password.grid(padx=2, pady=3)
password.bind("<FocusIn>", temp_password)

#log in button
btn_login = Button(frame, text="Login", bg="#F50707")
btn_login.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()

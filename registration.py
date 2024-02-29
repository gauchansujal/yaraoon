from tkinter import *
from tkinter import messagebox
import mysql.connector
import re

# Validation function for phone number
def validate_phone_number(username_val):
    # Check if the username_val contains only digits and has exactly 10 digits
    if re.match(r'^\d{10}$', username_val):
        return True
    else:
        return False
# Validation function for name
def validate_name(name_val):
    # Check if the name_val contains only letters
    if re.match(r'^[a-zA-Z\s]+$', name_val):
        return True
    else:
        return False
   
def register_user():
    name_val = name.get()
    username_val = username.get()
    password_val = password.get()
    repassword_val = repassword.get()

    # Check if any field is empty
    if not name_val or not username_val or not password_val or not repassword_val:
        messagebox.showerror("Error", "All fields must be filled")
        return
    
    # Validate data
    if password_val != repassword_val:
        messagebox.showerror("Error", "Passwords do not match")
        return
    
    # Validate phone number
    if not validate_phone_number(username_val):
        messagebox.showerror("Error", "Invalid phone number. Please enter a 10-digit numeric value.")
        return
    
    #validate name
    if not validate_name(name_val):
        messagebox.showerror("Error", "Invalid name. Please enter only letters.")
        return
    
    # Connect to MySQL database
    connection = mysql.connector.connect(
        host='localhost',
        user='pma',  
        password='Yug12345',  
        database='user_management'  
    )

    # Create cursor
    cursor = connection.cursor()

    # Insert data into the database
    insert_query = "INSERT INTO users (name, username, password) VALUES (%s, %s, %s)"
    data = (name_val, username_val, password_val)
    try:
        cursor.execute(insert_query, data)
        connection.commit()
        messagebox.showinfo("Success", "User registered successfully")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to register user: {error}")
    finally:
        # Close cursor and connection
        cursor.close()
        connection.close()

        root.destroy()
        import Login



root = Tk()
root.title('Login')
root.geometry('700x500+300+150')
root.configure(bg="#fff")
root.resizable(False, False)

frame = Frame(root, bg="black", bd=0)
frame.pack(expand=True, fill=BOTH)

#signup
heading = Canvas(frame, width=150, height=50, bg="black", highlightthickness=0)
heading.place(relx=0.5, rely=0.04, anchor="n")
heading.create_text(75, 25, text='Sign up', fill="#0775F5", font=('Microsoft YaHei UI Light', 23, 'bold','underline'), anchor='center')

#text
heading2 = Canvas(frame, width=280, height=100, bg="black", highlightthickness=0)
heading2.place(relx=0.5, rely=0.15, anchor="n")
heading2.create_text(140, 20, text='create an account to enjoy all the services', fill="white", font=('Microsoft YaHei UI Light', 12), anchor='n')
heading2.create_text(140, 40, text='with out any ads for free', fill="white", font=('Microsoft YaHei UI Light', 12), anchor='n')


#------------namestorage------------
def on_name_select(event):
    selected_name = name.get()
    save_selected_name(selected_name)

def save_selected_name(selected_name):
    with open("selected_name.txt", "w") as file:
        file.write(selected_name)

# entername
def temp_name(e):
    name.delete(0, "end")

name = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 16))
name.place(relx=0.5, rely=0.37, anchor="n")
name.insert(0, 'Enter your Name')

name.bind("<FocusIn>", temp_name)  
name.bind("<KeyRelease>", on_name_select)

#numberstorage
def on_user_select(event):
    selected_user = username.get()
    save_selected_user(selected_user)

def save_selected_user(selected_user):
    with open("selected_num.txt", "w") as file:
        file.write(selected_user)

#enternumber
def temp_username(e):
    username.delete(0, "end")

username = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 16))
username.place(relx=0.5, rely=0.45, anchor="n")
username.insert(0, 'Enter your phoneno.')
username.bind("<FocusIn>", temp_username)
username.bind("<KeyRelease>", on_user_select)

#enterpassword
def temp_password(e):
    password.delete(0, "end")

password = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 16))
password.place(relx=0.5, rely=0.53, anchor="n")
password.insert(0, 'Create password')
password.bind("<FocusIn>", temp_password)

#retype password
def temp_repassword(e):
    repassword.delete(0, "end")

repassword = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 16))
repassword.place(relx=0.5, rely=0.61, anchor="n")
repassword.insert(0, 'Re-type your password')
repassword.bind("<FocusIn>", temp_repassword)

#create account
create_btn = Button(frame, width=10,text="Create Account", fg='black', bg='red', font=('Microsoft YaHei UI Light', 20), border=0,command=register_user)
create_btn.place(relx=0.5, rely=0.70, anchor="n")

# Already Have An Account? Text
already_text = Label(frame, text="Already Have An Account?", fg="white", bg="black", font=('Microsoft YaHei UI Light', 12))
already_text.place(relx=0.46, rely=0.80, anchor="n")

    
# Sign in Button
def back():
    result=messagebox.showinfo("login","If you already have an account, Click ok")
    root.destroy()
    import Login
    
signin_btn = Button(frame, text="Sign in", fg='black', bg='blue', font=('Microsoft YaHei UI Light', 12), border=0, command=back)
signin_btn.place(relx=0.63, rely=0.80, anchor="n")

root.mainloop()

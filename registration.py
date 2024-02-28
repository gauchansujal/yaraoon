from tkinter import *
from tkinter import messagebox
import mysql.connector

def register_user():
    username_val = username.get()
    password_val = password.get()
    repassword_val = repassword.get()

    # Validate data
    if password_val != repassword_val:
        messagebox.showerror("Error", "Passwords do not match")
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
    insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    data = (username_val, password_val)
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


root = Tk()
root.title('Login')
root.geometry('700x500+300+150')
root.configure(bg="#fff")

frame = Frame(root, bg="#53D3D1", bd=0)
frame.pack(expand=True, fill=BOTH)

#signup
heading = Canvas(frame, width=150, height=50, bg="#53D3D1", highlightthickness=0)
heading.place(relx=0.5, rely=0.04, anchor="n")
heading.create_text(75, 25, text='Sign up', fill="#0775F5", font=('karla', 23, 'bold','underline'), anchor='center')

#text
heading2 = Canvas(frame, width=350, height=100, bg="#53D3D1", highlightthickness=0)
heading2.place(relx=0.5, rely=0.15, anchor="n")
heading2.create_text(149, 20, text='  create an account to enjoy all the services', fill="black", font=('karla', 12), anchor='n')
heading2.create_text(140, 40, text='with out any ads for free', fill="black", font=('karla', 12), anchor='n')

#enternumber
def temp_username(e):
    username.delete(0, "end")

username = Entry(frame, width=25, fg='black', border=0, bg="white", font=('karla', 16))
username.place(relx=0.5, rely=0.35, anchor="n")
username.insert(0, 'Enter your email/phone')
username.bind("<FocusIn>", temp_username)

#enterpassword
def temp_password(e):
    password.delete(0, "end")

password = Entry(frame, width=25, fg='black', border=0, bg="white", font=('karla', 16))
password.place(relx=0.5, rely=0.43, anchor="n")
password.insert(0, 'Create password')
password.bind("<FocusIn>", temp_password)

#retype password
def temp_repassword(e):
    repassword.delete(0, "end")

repassword = Entry(frame, width=25, fg='black', border=0, bg="white", font=('karla', 16))
repassword.place(relx=0.5, rely=0.51, anchor="n")
repassword.insert(0, 'Re-type your password')
repassword.bind("<FocusIn>", temp_repassword)

#create account
create_btn = Button(frame, width=18,text="Create Account", fg='black', bg='#079FF5', font=('karla', 20), border=0,command=register_user)
create_btn.place(relx=0.5, rely=0.60, anchor="n")

# Already Have An Account? Text
already_text = Label(frame, text="Already Have An Account?", fg="black", bg="#53D3D1", font=('karla', 12))
already_text.place(relx=0.44, rely=0.75, anchor="n")

    
# Sign in Button
def back():
    result=messagebox.askyesno('',"Are you sure you want to choose this route ")
    if result:
        print("user clicked yes")
        root.destroy()
        import log_in
       
    else:
        print("user clicked no")

signin_btn = Button(frame, text="Sign in", fg="black", bg='#53D3D1', font=('karla', 12,'underline'), border=0,activebackground="black", command=back)
signin_btn.place(relx=0.62, rely=0.75, anchor="n")

root.mainloop()
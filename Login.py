from tkinter import *
from tkinter import messagebox
import mysql.connector

def authenticate_user():
    entered_username = username.get()
    entered_password = password.get()

    # Connect to MySQL database
    connection = mysql.connector.connect(
        host='localhost',
        user='pma',  
        password='Yug12345',  
        database='user_management'
    )

    # Create cursor
    cursor = connection.cursor()


    # Check if the entered credentials exist in the database
    select_query = "SELECT * FROM users WHERE username = %s AND password = %s"
    data = (entered_username, entered_password)
    cursor.execute(select_query, data)
    user = cursor.fetchone()

    # Close cursor and connection
    cursor.close()
    connection.close()

    if user:
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password")
    root.destroy()
    import first


root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)


img = PhotoImage(file='./driver.png')
Label(root,image=img,bg="white").place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in', fg="#57a1f8", bg="white", font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=160,y=5)

#usernamebutton
def temp_username(e):
    username.delete(0,"end")

username = Entry(frame,width=30,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',14))
username.place(x=50,y=80)
username.insert(0,'Email id./Phone')
username.bind("<FocusIn>", temp_username)

Frame(frame,width=295,height=2,bg='black').place(x=43,y=107)

#passwordbutton
def temp_password(e):
    password.delete(0,"end")
    password.config(show="*")
password = Entry(frame,width=30,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',14))
password.place(x=50,y=150)
password.insert(0,'Password')
password.bind("<FocusIn>", temp_password)

Frame(frame,width=295,height=2,bg='black').place(x=43,y=177)

#signinbutton
Button(frame,width=30,pady=2,text='Sign in',bg='#57a1f8',fg='black',border=0, command=authenticate_user).place(x=45,y=204)

#signupbutton
def back():
    import registration


sign_up = Button(frame,width=6,text='New here?', border=0,bg='white' ,cursor='hand',fg='#57a1f8',command=back)
sign_up.place(x=255,y=250)

root.mainloop()





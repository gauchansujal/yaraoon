from tkinter import *
from tkinter import messagebox

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
    username.config(show="*")

username = Entry(frame,width=30,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',14))
username.place(x=50,y=80)
username.insert(0,'Email id.')
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
Button(frame,width=30,pady=2,text='Sign in',bg='#57a1f8',fg='black',border=0).place(x=45,y=204)
forgot=Button(frame,text="Forgot password?",width=10,fg='black',bg='white',font=('Microsoft YaH UI Light',9))
forgot.place(x=250,y=235)

#signupbutton
label=Label(frame,text='New here?',width=10,fg='black',bg='white',font=('Microsoft YaH UI Light',12,'underline'))
label.place(x=135,y=273)
sign_up= Button(frame,width=6,text='Sign up', border=0,bg='white' ,cursor='hand',fg='#57a1f8')
sign_up.place(x=215,y=270)



root.mainloop()

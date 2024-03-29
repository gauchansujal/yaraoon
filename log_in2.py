from tkinter import *
from tkinter import messagebox

win=Tk()
win.title('Login')
win.geometry('925x500+300+200')
win.configure(bg="#fff")
win.resizable(False,False)

img = PhotoImage(file='driver.png')
Label(win,image=img,bg="white").place(x=50,y=50)

frame=Frame(win,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in', fg="#57a1f8", bg="white", font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=160,y=5)

#usernamebuttons
username = Entry(frame,width=30,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',14))
username.place(x=50,y=80)
username.insert(0,'Email id.')
Frame(frame,width=295,height=2,bg='black').place(x=43,y=107)

#passwordbutton
password = Entry(frame,width=30,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',14))
password.place(x=50,y=150)
password.insert(0,'Password')
Frame(frame,width=295,height=2,bg='black').place(x=43,y=177)
#insidebaki

def back():
    win.destroy()
    import second

#signinbutton
Button(frame,width=50,pady=2,text='Sign in',bg='#57a1f8',fg='black',border=0,command=back).place(x=23,y=(204))
forgot=Button(frame,text="Forgot password?",width=20,fg='black',bg='white',border=0,font=('Microsoft YaH UI Light',9),command=back)
forgot.place(x=125,y=235)

#signupbutton
sign_up= Button(frame,width=10,text='New here?', border=0,bg='white',font=('Microsoft YaH UI Light',10,'underline') ,cursor='hand2',fg='black')
sign_up.place(x=215,y=270)

win.mainloop()
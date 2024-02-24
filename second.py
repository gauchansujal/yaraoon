from tkinter import *
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import messagebox


root = Tk()

root.geometry("1200x1000")



frame = Frame(root, bg="#024c6e", highlightbackground="black", highlightthickness=2, bd=2,height=100)
frame.pack(expand=TRUE, fill=BOTH)


image_path = r"bus_12.png"
image= PhotoImage(file = image_path)
 

desired_width = 100
desired_height = 50

resized_image = image.subsample(int(image.width()/desired_width), int(image.height()/desired_height))


label = Label(frame, bg="#024c6e",  width=desired_width, height=100, image = resized_image, anchor=W)
label.pack(side = TOP, expand=False, fill=BOTH)
label.pack_propagate(False)
label.pack(pady=7)

def login2():
    root.destroy()
    import log_in2
    

button = Button(label, text="sign in",height=10,width=15,bg="#0094FF",cursor = "hand2",font=('Inter',10,"bold"),command=login2)
button.pack(side=RIGHT,pady=25)


def popup(): 
    messagebox.showinfo("contac us", "987635925924")
b3_button=Button(label, text="contact us",height=10,width=15, bg="#D3D3D3",cursor = "  hand2",font=('Inter',10,"bold"), command=popup)
b3_button.pack(side=RIGHT,  padx=(0,30),pady=25)

def aboutus_popup():
    messagebox.showinfo("About Us","we are bus travel")
b2_button = Button(label, text="about us", height=10,width=15,bg="#D3D3D3",cursor = "  hand2",font=('Inter',10,"bold"),command=aboutus_popup)
b2_button.pack(side=RIGHT, padx=(0,30),pady=25)

def service_showinfo():
    messagebox.showinfo("Service","We provide the best services for you")
button = Button(label, text="service",height=10,width=15, bg="#D3D3D3",cursor = "  hand2",font=('Inter',10,"bold"), command=service_showinfo)
button.pack(side=RIGHT, padx=(0,30),pady=25)



# we have created 2nd frame here  to put the label on it and then add scrollbar to this frame



second_label = Label(frame,  width=500, height=500, bg="#024c6e",anchor=CENTER)
second_label.pack(side = TOP, expand=False, fill=BOTH) 

message=Message(second_label,text="Choose  Bus",bg="#024c6e",fg="black", width=500,font=("Poppins", 40, "bold"))
message.pack (side=TOP,padx=100)

# adding calendar  to the frame

message=Message(second_label,text="Date",bg="#024c6e",font=("Poppins", 16, "bold"))
message.pack(side=LEFT,padx=5, pady=1)

cal=DateEntry(second_label ,selectmode='day')

cal.pack(side=LEFT,padx=10,pady=1) 


def change():
    result=messagebox.askyesno("Log out","Are you sure you want to log out?")
    if result:
        print("User clicked OK")
        root.destroy()
        import first
        
    else:
        print("User clicked Cancel")


# CREATINGG BUTTON

desired_width2 = 150
desired_height2 = 50 

frame1 = Frame(frame, width= desired_width, height= desired_height ,bg="#024c6e", highlightbackground="black", highlightthickness=0)
frame1.pack( padx=(50,50), pady=100)


message_label= Label(frame1, width=desired_width, bg="#024c6e",height=desired_height,borderwidth=1,anchor=CENTER)
message_label.pack(side = TOP, expand=False, fill=BOTH)

bus_message=Message(message_label,text="Bus type", font=("Poppins", 20, "bold"),fg="black",bg="#024c6e", width=desired_width)
bus_message.pack(side=LEFT,padx=(350,550),pady=8)

departure_message=Message(message_label,text="Departure", font=("Poppins", 20, "bold"),fg="black",bg="#024c6e", width=500)
departure_message.pack(side=LEFT, padx=0, pady=8, anchor=CENTER)

fare_message=Message(message_label,text="Fare", font=("Poppins", 20, "bold"),fg="black",bg="#024c6e", width=desired_width)
fare_message.pack(side=RIGHT,padx=(150),pady=8)


# creating first label for button
button_label=Label(frame1, width=desired_width, height=desired_height,bg="#FBECEB",highlightbackground="black",highlightthickness=1)
button_label.pack(side = TOP, expand=False, fill=BOTH)
 
bus_button=Button(button_label,text="Tourist travels ", bg='#FBECEB', fg='black', height=5, width=100,borderwidth=0, activebackground="#FBECEB")
bus_button.pack(side=LEFT,padx=(35,0),pady=1)

bus2_button=Button(button_label,text="6:30 PM", bg='#FBECEB', fg='black', height=5, width=100,borderwidth=0, activebackground="#FBECEB")
bus2_button.pack(side=LEFT,padx=0,pady=8)

bus3_button=Button(button_label,text="rs:650", bg='#FBECEB', fg='black', height=5, width=100,borderwidth=0, activebackground="#FBECEB")
bus3_button.pack(side=RIGHT,padx=(0,35),pady=8)

# creating second label for button
second_button= Label(frame1, width=desired_width, height=desired_height,bg="#FBECEB",highlightbackground="black",highlightthickness=1)
second_button.pack(side = TOP, expand=False, fill=BOTH)

bus4_button=Button(second_button,text="Legend Gorkha ", bg='#FBECEB', fg='black', height=5, width=100,borderwidth=0, activebackground="#FBECEB")
bus4_button.pack(side=LEFT,padx=(35,0),pady=8)

bus5_button=Button(second_button,text="4:00 PM", bg='#FBECEB', fg='black', height=5, width=100,borderwidth=0, activebackground="#FBECEB")
bus5_button.pack(side=LEFT,padx=0,pady=8)

bus6_button=Button(second_button,text="rs:10000", bg='#FBECEB', fg='black', height=5, width=100,borderwidth=0, activebackground="#FBECEB")
bus6_button.pack(side=RIGHT,padx=(0,35),pady=8)

# creating third label for button
third_button= Label(frame1, width=desired_width, height=desired_height,bg="#FBECEB",highlightbackground="black",highlightthickness=1)
third_button.pack(side = TOP, expand=False, fill=BOTH)

bus7_button=Button(third_button,text="Nepal travels ", bg='#FBECEB', fg='black', height=5, width=100,borderwidth=0, activebackground="#FBECEB")
bus7_button.pack(side=LEFT,padx=(35,0),pady=8)

bus8_button=Button(third_button,text="12:30 PM", bg='#FBECEB', fg='black', height=5, width=100,borderwidth=0, activebackground="#FBECEB")
bus8_button.pack(side=LEFT,padx=0,pady=8)

bus9_button=Button(third_button,text="rs.700", bg='#FBECEB', fg='black', height=5, width=100,borderwidth=0, activebackground="#FBECEB")
bus9_button.pack(side=RIGHT,padx=(0,35),pady=8)

fourth_button= Label(frame1,bg='#024c6e', width=desired_width, height=desired_height)
fourth_button.pack(side = TOP, expand=False, fill=BOTH)

def buy():
    messagebox.showinfo("Ticket","Are you sure you want to book this Bus")
    root.destroy()
    import bus
buy_button=Button( fourth_button,text="Buy ticket", bg='#53D3D1', fg='black', height=5, width=30, padx=5, pady=5, command=buy)
buy_button.pack(side=RIGHT)

#---------------------------------------creating a button for change in plan-------------------------
def change():
    result=messagebox.askyesno("Log out","Are you sure you want to log out?")
    if result:
        print("User clicked OK")
        root.destroy()
        import first
        
    else:
        print("User clicked Cancel")

change_button = Button(fourth_button, text="change in plan?", bg="#FEB249",height=5, width=30,cursor = "hand2",padx=5, pady=5,command=change,activebackground="red")
change_button.pack(side=RIGHT)

root.mainloop()
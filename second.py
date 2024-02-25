from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


root = Tk()

root.geometry("1200x1000")



frame = Frame(root, bg="#53D3D1", highlightbackground="black", highlightthickness=2, bd=2,height=100)
frame.pack(expand=TRUE, fill=BOTH)


image_path = r"bus_12.png"
image= PhotoImage(file = image_path)
 

desired_width = 100
desired_height = 50

resized_image = image.subsample(int(image.width()/desired_width), int(image.height()/desired_height))


label = Label(frame, bg="#53D3D1",  width=desired_width, height=100, image = resized_image, anchor=W)
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



second_label = Label(frame,  width=500, height=500, bg="#53D3D1",anchor=CENTER)
second_label.pack(side = TOP, expand=False, fill=BOTH) 

message=Message(second_label,text="Choose  Bus",bg="#53D3D1",fg="black", width=500,font=("Poppins", 40, "bold"))
message.pack (side=TOP,padx=100)


def change():
    result=messagebox.askyesno("Log out","Are you sure you want to log out?")
    if result:
        print("User clicked OK")
        root.destroy()
        import first
        
    else:
        print("User clicked Cancel")


#-------------------------------------CREATINGG BUTTON--------------------------------------------

desired_width2 = 150
desired_height2 = 50 

frame1 = Frame(frame, width= desired_width, height= desired_height ,bg="#53D3D1", highlightbackground="black", highlightthickness=0)
frame1.pack( padx=(50,50), pady=75)


message_label= Label(frame1, width=desired_width, bg="#53D3D1",height=desired_height,borderwidth=1)
message_label.pack(side = TOP, anchor=CENTER,expand=False, fill=BOTH)

bus_message=Message(message_label,text="Bus type", font=("Poppins", 20, "bold"),fg="black",bg="#53D3D1", width=250)
bus_message.pack(side=LEFT,padx=(100,200),pady=8)

departure_message=Message(message_label,text="Departure", font=("Poppins", 20, "bold"),fg="black",bg="#53D3D1", width=250)
departure_message.pack(side=LEFT, padx=20, pady=8, anchor=CENTER)

fare_message=Message(message_label,text="Fare", font=("Poppins", 20, "bold"),fg="black",bg="#53D3D1", width=250)
fare_message.pack(side=RIGHT,padx=(100,160),pady=8)


# ----------------------------------------creating first label for button----------------------------------
button_label=Label(frame1, width=desired_width, height=desired_height,bg="#002447",highlightbackground="black",highlightthickness=1)
button_label.pack(side = TOP)
 
bus_button=Button(button_label,text="Tourist travels ", bg='#002447', fg="white",font=("Poppins", 14,"bold") ,height=3, width=30,borderwidth=0, activebackground="#002447")
bus_button.pack(side=LEFT,padx=(35,0),pady=1)

bus2_button=Button(button_label,text="6:30 PM", bg='#002447', fg="white",font=("Poppins", 14,"bold") ,height=3, width=30,borderwidth=0, activebackground="#002447")
bus2_button.pack(side=LEFT,padx=0,pady=8)

bus3_button=Button(button_label,text="rs:650", bg='#002447', fg="white",font=("Poppins", 14,"bold") ,height=3, width=30,borderwidth=0, activebackground="#002447")
bus3_button.pack(side=LEFT,padx=(0,35),pady=8)

# ---------------------------------------creating second label for button--------------------------------------------
second_button= Label(frame1, width=desired_width, height=desired_height,bg="#002447",highlightbackground="black",highlightthickness=1)
second_button.pack(side = TOP)

bus4_button=Button(second_button,text="Legend Gorkha ", bg='#002447', fg="white",font=("Poppins", 14,"bold") ,height=3, width=30,borderwidth=0, activebackground="#002447")
bus4_button.pack(side=LEFT,padx=(35,0),pady=8)

bus5_button=Button(second_button,text="4:00 PM", bg='#002447', fg="white",font=("Poppins", 14,"bold") ,height=3, width=30,borderwidth=0, activebackground="#002447")
bus5_button.pack(side=LEFT,padx=0,pady=8)

bus6_button=Button(second_button,text="rs:7500", bg='#002447', fg="white",font=("Poppins", 14,"bold") ,height=3, width=30,borderwidth=0, activebackground="#002447")
bus6_button.pack(side=RIGHT,padx=(0,35),pady=8)

# ----------------------------------------creating third label for button------------------------------------------------------
third_button= Label(frame1, width=desired_width, height=desired_height,bg="#002447",highlightbackground="black",highlightthickness=1)
third_button.pack(side = TOP)

bus7_button=Button(third_button,text="Nepal travels ", bg='#002447', fg="white",font=("Poppins", 14,"bold") ,height=3, width=30,borderwidth=0, activebackground="#002447")
bus7_button.pack(side=LEFT,padx=(35,0),pady=8)

bus8_button=Button(third_button,text="12:30 PM", bg='#002447', fg="white",font=("Poppins", 14,"bold") ,height=3, width=30,borderwidth=0, activebackground="#002447")
bus8_button.pack(side=LEFT,padx=0,pady=8)

bus9_button=Button(third_button,text="rs.700", bg='#002447', fg="white",font=("Poppins", 14,"bold") ,height=3, width=30,borderwidth=0, activebackground="#002447")
bus9_button.pack(side=RIGHT,padx=(0,35),pady=8)

fourth_button= Label(frame1,bg='#53D3D1', width=desired_width, height=desired_height)
fourth_button.pack(side = TOP, expand=False, fill=BOTH)
#-------------------------buying ticket------------------------------------------------
def buy():
    result=messagebox.askyesno("Ticket","Are you sure you want to book this Bus")
    if result:
        print("User clicked OK")
        root.destroy()
        import bus
        
    else:
        print("User clicked Cancel")

buy_button=Button( fourth_button,text="Buy ticket", bg='red', fg="black", font=("Poppins", 14,"bold") ,height=3, width=16,  command=buy)
buy_button.pack(side=RIGHT,anchor=CENTER)

#---------------------------------------creating a button for change in plan-------------------------
def change():
    result=messagebox.askyesno("change","Are you sure you want to change plan?")
    if result:
        print("User clicked OK")
        root.destroy()
        import first
        
    else:
        print("User clicked Cancel")

change_button = Button(fourth_button, text="change in plan?", bg="#FEB249",cursor = "hand2",font=("Poppins", 14,"bold") ,height=3, width=16,command=change,activebackground="red")
change_button.pack(side=RIGHT)

root.mainloop()
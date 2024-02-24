from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


root = Tk()
root.geometry("1200x1000")

my_img= ImageTk.PhotoImage(Image.open("Seat.png"))
frame = Frame(root, highlightbackground="black", highlightthickness=2, bd=2)
frame.pack(expand=TRUE, fill=BOTH)



image_path = r"bus_12.png"
image = PhotoImage(file = image_path)

desired_width = 100
desired_height = 50

resized_image = image.subsample(int(image.width()/desired_width), int(image.height()/desired_height))
label = Label(frame, bg='#4aa9ed',  width=desired_width, height=100, image = resized_image, anchor=W)
label.pack(side = TOP, expand=False, fill=BOTH)
label.pack_propagate(False)
label.pack(pady=7)

def logout():
    result=messagebox.askokcancel("Log out","Are you sure you want to log out?")
    if result:
        print("User clicked OK")
        root.destroy()
    import log_in2
    

button = Button(label, text="Log out",height=10,width=15,bg="#0094FF",cursor = "hand2",font=('Inter',10,"bold"),command=logout)
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


#------------------------------creating new frame ---------------------------
f = Frame(frame, width= 1295, height=500, highlightbackground="black", bd=0)
f.pack( side= TOP, fill=Y)

label = Label(f, bg='white',  width=500, height=300, anchor=CENTER)
label.pack(side = TOP, expand=False, fill=BOTH,pady=(10,150))

message_label=Label(label,bg='black',  width=500, height=5, anchor=N)
message_label.pack(side=TOP, fill=BOTH,)

ticket_message=Message(message_label,text="Ticket Details ",font=('Inka',29,'bold'), background="black",fg="white",width=500,anchor=N)
ticket_message.pack(padx=1,fill=BOTH)


detail_label=Label(label,bg='#43F4FF', height=100,width=50, highlightbackground="black", highlightthickness=2, bd=0)
detail_label.pack(side=LEFT, fill=Y) 


date=Label(detail_label,text="Date:",bg='#43F4FF',font=('Helvetica', 12)).grid(row=1, column=1)
date_message=Message(detail_label,text="Ticket Details ",font=('Helvetica',12,'underline'), background="#43F4FF",fg="black",width=500).grid(row=1, column=2)


bus=Label(detail_label,text="Bus No. :",bg='#43F4FF',font=('Helvetica', 12)).grid(row=2, column=1)
bus_message=Message(detail_label,text="Ticket Details ",font=('Helvetica',12,'underline'), background="#43F4FF",fg="black",width=500).grid(row=2, column=2)

age=Label(detail_label,text="Age:",bg='#43F4FF',font=('Helvetica', 12)).grid(row=3, column=1)
age_message=Message(detail_label,text="Ticket Details ",font=('Helvetica',12,'underline'), background="#43F4FF",fg="black",width=500).grid(row=3, column=2)

#--------------------------------------here we make new tiket label------------------------------------------------------

fare=Label(detail_label,text="Fare Rs. :",bg='#43F4FF',font=('Helvetica', 12)).grid(row=4, column=1)
fare_message=Message(detail_label,text="Ticket Details ",font=('Helvetica',12,'underline'), background="#43F4FF",fg="black",width=500).grid(row=4, column=2)

serial=Label(detail_label,text="S. NO:",bg='#43F4FF',font=('Helvetica', 12)).grid(row=5, column=1)
serial_message=Message(detail_label,text="Ticket Details ",font=('Helvetica',12,'underline'), background="#43F4FF",fg="black",width=500).grid(row=5, column=2)

pass_label=Label(label,bg='#43F4FF',  width=desired_width, height=100,highlightbackground="black", highlightthickness=2, bd=0)
pass_label.pack(side=RIGHT, fill=Y,expand=YES)


pass_message=Message(pass_label,text="BOARDING PASS ",font=('Imprint MT Shadow',20,'bold'), background="#43F4FF",fg="black",width=500).grid(row=1, column=2)

name_message=Message(pass_label,text="Name",font=('Inka',12), background="#43F4FF",fg="#1814D4",width=500).grid(row=2, column=1)


ticket_number_message=Message(pass_label,text="Ticket ",font=('Inka',12), background="#43F4FF",fg="#1814D4",width=500).grid(row=2, column=2)


fare_base_message=Message(pass_label,text="Fare base ",font=('Inka',12), background="#43F4FF",fg="#1814D4",width=500).grid(row=2, column=3)

issue_message=Message(pass_label,text="Isused by ",font=('Inka',12), background="#43F4FF",fg="#1814D4",width=500).grid(row=2, column=4)


from_message=Message(pass_label,text="From ",font=('Inka',12), background="#43F4FF",fg="#1814D4",width=500).grid(row=3, column=1)


Bus_date_message=Message(pass_label,text="Date ",font=('Inka',12), background="#43F4FF",fg="#1814D4",width=500).grid(row=3, column=2)


bus_time_message=Message(pass_label,text="Time ",font=('Inka',12), background="#43F4FF",fg="#1814D4",width=500).grid(row=3, column=3)

bus_seat_message=Message(pass_label,text="Seat ",font=('Inka',12), background="#43F4FF",fg="#1814D4",width=500).grid(row=3, column=4)

bus_ticket_message=Message(pass_label,text="Ticket number ",font=('Inka',12), background="#43F4FF",fg="#1814D4",width=500).grid(row=3, column=4)

to_message=Message(pass_label,text="To ",font=('Inka',12), background="#43F4FF",fg="#1814D4",width=500).grid(row=4, column=1)

reaching_date_message=Message(pass_label,text="Date ",font=('Inka',12), background="#43F4FF",fg="#1814D4",width=500).grid(row=4, column=2)

reaching_time_message=Message(pass_label,text="Seat ",font=('Inka',12), background="#43F4FF",fg="#1814D4",width=500).grid(row=4, column=3)

#-------------------------------here wwe are adding qr photo to scan  --------------------------
image_path_2= r"qr.png"
image2 = PhotoImage(file = image_path_2)

desired_width2 = 100
desired_height2 = 100

resized_image2 = image2.subsample(int(image2.width()/desired_width2), int(image2.height()/desired_height2))

qr_img= Label(pass_label, image = resized_image2,background="#43F4FF" ).grid(row=5 ,column=4)

btn_label=Label(frame,width=100,height=100,anchor=SE)
btn_label.pack(side=RIGHT,padx=70,pady=100)
#-------------------asking user how do they want to save passs--------------------------
def email():
    result=messagebox.askyesno('Email', "Do You Want to send pass in your email")
    if result:
        print("User clicked OK")
    
    else:
        print("User clicked Cancel")

send_button=Button(btn_label, text="Send it to email",font=("Helvetica",16,"bold"),background="#1893ED",fg="white",command=email)
send_button.pack(side=LEFT,padx=0,pady=50)

def download():
    result=messagebox.askyesnocancel("Download","Do You Want To Download The Pass?")
    if result:
        print("User clicked OK")
    else:
        print("User clicked Cancel")
download_button=Button(btn_label,text="Download",font=("Helvetica",16,"bold"),background="#1893ED",fg="white")
download_button.pack(side=RIGHT,padx=10,pady=50)

root.mainloop()
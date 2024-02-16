from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


root = Tk()
root.geometry("1200x1000")

my_img= ImageTk.PhotoImage(Image.open("Seat.png"))
frame = Frame(root, highlightbackground="black", highlightthickness=2, bd=2)
frame.pack(expand=TRUE, fill=BOTH)



image_path = r"bus.png"
image = PhotoImage(file = image_path)

desired_width = 100
desired_height = 50

resized_image = image.subsample(int(image.width()/desired_width), int(image.height()/desired_height))

label = Label(frame, bg='#4aa9ed',  width=desired_width, height=desired_height, image = resized_image, anchor=W)
label.pack(side = TOP, expand=False, fill=BOTH)
label.pack_propagate(False)
label.pack(pady=7)

def logout():
    result=messagebox.showinfo("Log out","are you sure you want to log out?")
    if result:
        print("User clicked OK")
    else:
        print("User clicked Cancel")
    root.destroy()
    import log_in
   
button = Button(label, text="log out", bg="#D3D3D3",cursor = " hand2",command=logout)
button.pack(side=RIGHT)

def popup(): 
    messagebox.showinfo("contac us", "987635925924")
b3_button=Button(label, text="contact us", bg="#D3D3D3",cursor = "  hand2", command=popup)
b3_button.pack(side=RIGHT,  padx=(0,30))

def aboutus_popup():
    messagebox.showinfo("About Us","we are bus travel")
b2_button = Button(label, text="about us", bg="#D3D3D3",cursor = "  hand2",command=aboutus_popup)
b2_button.pack(side=RIGHT, padx=(0,30))

def service_showinfo():
    messagebox.showinfo("Service","We provide the best services for you")
button = Button(label, text="service", bg="#D3D3D3",cursor = "  hand2", command=service_showinfo)
button.pack(side=RIGHT, padx=(0,30))

f = Frame(frame, width= 1295, height=100, highlightbackground="black", bd=0)
f.pack( side= TOP, fill=Y,padx=100)

label = Label(f, bg='white',  width=500, height=300, anchor=CENTER)
label.pack(side = TOP, expand=False, fill=BOTH,pady=(10,150))

message_label=Label(label,bg='black',  width=500, height=5, anchor=N)
message_label.pack(side=TOP, fill=Y)

ticket_message=Message(message_label,text="Ticket Details ",font=('Inka',29,'bold'), background="black",fg="white",width=500,anchor=N)
ticket_message.pack(padx=1,fill=BOTH)


detail_label=Label(label,bg='#43F4FF', height=100,width=120, highlightbackground="black", highlightthickness=2, bd=0)
detail_label.pack(side=LEFT, fill=Y) 


date=Label(detail_label,text="Date:",bg='#43F4FF',font=('Helvetica', 12)).grid(row=1, column=1)
date_message=Message(detail_label,text="Ticket Details ",font=('Helvetica',12,'underline'), background="#43F4FF",fg="black",width=500).grid(row=1, column=2)


bus=Label(detail_label,text="Bus No. :",bg='#43F4FF',font=('Helvetica', 12)).grid(row=2, column=1)
bus_message=Message(detail_label,text="Ticket Details ",font=('Helvetica',12,'underline'), background="#43F4FF",fg="black",width=500).grid(row=2, column=2)

age=Label(detail_label,text="Age:",bg='#43F4FF',font=('Helvetica', 12)).grid(row=3, column=1)
age_message=Message(detail_label,text="Ticket Details ",font=('Helvetica',12,'underline'), background="#43F4FF",fg="black",width=500).grid(row=3, column=2)

fare=Label(detail_label,text="Fare Rs. :",bg='#43F4FF',font=('Helvetica', 12)).grid(row=4, column=1)
fare_message=Message(detail_label,text="Ticket Details ",font=('Helvetica',12,'underline'), background="#43F4FF",fg="black",width=500).grid(row=4, column=2)

serial=Label(detail_label,text="S. NO:",bg='#43F4FF',font=('Helvetica', 12)).grid(row=5, column=1)
serial_message=Message(detail_label,text="Ticket Details ",font=('Helvetica',12,'underline'), background="#43F4FF",fg="black",width=500).grid(row=5, column=2)

pass_label=Label(label,bg='#43F4FF',  width=desired_width, height=100,highlightbackground="black", highlightthickness=2, bd=0)
pass_label.pack(side=RIGHT, fill=Y)


pass_message=Message(pass_label,text="BOARDING PASS ",font=('Imprint MT Shadow',37,'bold'), background="#43F4FF",fg="black",width=500).grid(row=1, column=2)

name_message=Message(pass_label,text="Name \n miraj",font=('Inka',18), background="#43F4FF",fg="#1814D4").grid(row=2, column=1)


ticket_number_message=Message(pass_label,text="Ticket \n one way ",font=('Inka',18), background="#43F4FF",fg="#1814D4").grid(row=2, column=2)


fare_base_message=Message(pass_label,text="Fare base \n adult",font=('Inka',18), background="#43F4FF",fg="#1814D4").grid(row=2, column=3)

issue_message=Message(pass_label,text="Isused by \n national bus",font=('Inka',18), background="#43F4FF",fg="#1814D4").grid(row=2, column=4)


from_message=Message(pass_label,text="From \n national bus",font=('Inka',18), background="#43F4FF",fg="#1814D4").grid(row=3, column=1)

root.mainloop()
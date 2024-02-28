from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


root = Tk()
root.geometry("1200x1000")

my_img= ImageTk.PhotoImage(Image.open("Seat.png"))
frame = Frame(root,bg="#53D3D1", highlightbackground="black", highlightthickness=2, bd=2)
frame.pack(expand=TRUE, fill=BOTH)



image_path = r"bus_12.png"
image = PhotoImage(file = image_path)

desired_width = 100
desired_height = 50

resized_image = image.subsample(int(image.width()/desired_width), int(image.height()/desired_height))
label = Label(frame, bg='#53D3D1',  width=desired_width, height=100, image = resized_image, anchor=W)
label.pack(side = TOP, expand=False, fill=BOTH)
label.pack_propagate(False)
label.pack(pady=7)

def logout():
    result=messagebox.askokcancel("Log out","Are you sure you want to log out?")
    if result:
        print("User clicked OK")
        root.destroy()
        import log_in2
    else:
        print("user clicked cancle")


button = Button(label, text="Log out",height=10,width=15,bg="#0094FF",cursor = "hand2",font=('Inter',10,"bold"),command=logout)
button.pack(side=RIGHT,pady=25)


def message_popup(): 
    messagebox.showinfo("contac us", "Please get in touch with us right away if you have any issues with this app. Contact us at\n +977 985511133.")
b3_button=Button(label, text="contact us",height=10,width=15, bg="#D3D3D3",cursor = " hand2",font=('Inter',10,"bold"), command=message_popup)
b3_button.pack(side=RIGHT,  padx=(0,30),pady=25)

def aboutus_popup():
    messagebox.showinfo("About Us","We are travel bus; we are the first travel agency in Nepal where you may purchase a ticket to reserve a bus and travel at an affordable price throughout Nepal. By offering practical and reasonably priced bus reservation services, Travel Bus is transforming the travel sector in Nepal and facilitating individuals' exploration of the natural beauty of our nation.")
b2_button = Button(label, text="about us", height=10,width=15,bg="#D3D3D3",cursor = "  hand2",font=('Inter',10,"bold"),command=aboutus_popup)
b2_button.pack(side=RIGHT, padx=(0,30),pady=25)

def service_showinfo():
    messagebox.showinfo("Service","At Travel Bus, we take pride in offering the best bus reservation service in Nepal. Our software is designed to cater to the needs of both locals and visitors, providing a seamless and convenient way to schedule buses for their travels across the country.")
button = Button(label, text="service",height=10,width=15, bg="#D3D3D3",cursor = "  hand2",font=('Inter',10,"bold"), command=service_showinfo)
button.pack(side=RIGHT, padx=(0,30),pady=25)



#------------------------------creating new frame ---------------------------
f = Frame(frame, bg="#53D3D1",width= 1295, height=500, highlightbackground="black", bd=0)
f.pack( side= TOP, fill=Y)

label = Label(f, bg='#53D3D1',  width=500, height=300, anchor=CENTER)
label.pack(side = TOP, expand=False, fill=BOTH,pady=(40,0))

message_label=Label(label,bg='black',  width=500, height=5, anchor=N)
message_label.pack(side=TOP, fill=BOTH,)

ticket_message=Message(message_label,text="Ticket Details ", font=("Poppins", 20,"bold"), background="black",fg="white",width=500,anchor=N)
ticket_message.pack(padx=1,fill=BOTH)


detail_label=Label(label,bg='white', height=100,width=50, highlightbackground="black", highlightthickness=2, bd=0)
detail_label.pack(side=LEFT, fill=Y) 


date=Label(detail_label,text="Date:",bg='white', font=("Poppins", 14,"bold")).grid(row=1, column=1)
date_message=Message(detail_label,text="Ticket Details ", font=("Poppins", 14,"bold",'underline'), background="white",fg="black",width=500).grid(row=1, column=2)


bus=Label(detail_label,text="Bus No. :",bg='white', font=("Poppins", 14,"bold")).grid(row=2, column=1)
bus_message=Message(detail_label,text="Ticket Details ", font=("Poppins", 14,"bold",'underline'), background="white",fg="black",width=500).grid(row=2, column=2)

age=Label(detail_label,text="Age:",bg='white', font=("Poppins", 14,"bold")).grid(row=3, column=1)
age_message=Message(detail_label,text="Ticket Details ", font=("Poppins", 14,"bold",'underline'), background="white",fg="black",width=500).grid(row=3, column=2)

#--------------------------------------here we make new tiket label------------------------------------------------------

fare=Label(detail_label,text="Fare Rs. :",bg='white', font=("Poppins", 14,"bold")).grid(row=4, column=1)
fare_message=Message(detail_label,text="Ticket Details ", font=("Poppins", 14,"bold",'underline'), background="white",fg="black",width=500).grid(row=4, column=2)

serial=Label(detail_label,text="S. NO:",bg='white', font=("Poppins", 14,"bold")).grid(row=5, column=1)
serial_message=Message(detail_label,text="Ticket Details ", font=("Poppins", 14,"bold",'underline'), background="white",fg="black",width=500).grid(row=5, column=2)

pass_label=Label(label,bg='white',  width=desired_width, height=100,highlightbackground="black", highlightthickness=2, bd=0)
pass_label.pack(side=RIGHT, fill=Y,expand=YES)


pass_message=Message(pass_label,text="Bus Ticket ",font=('poppins',20,'bold'), background="white",fg="black",width=500).grid(row=1, column=2)

name_message=Message(pass_label,text="Name", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=2, column=1)
name2_message=Message(pass_label,text=":Name", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=3, column=1)

ticket_number_message=Message(pass_label,text="Ticket ", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=2, column=2)
ticket2_message=Message(pass_label,text=":Name", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=3, column=2)

fare2_base_message=Message(pass_label,text="Fare base ", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=2, column=3)
fare2_base_message=Message(pass_label,text=":Fare base ", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=3, column=3)

issue2_message=Message(pass_label,text="Isused by ", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=2, column=4)
issue2_message=Message(pass_label,text=":Isused by ", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=3, column=4)

from_message=Message(pass_label,text="From ", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=4, column=1)
from2_message=Message(pass_label,text=":From ", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=5, column=1)

Bus_date_message=Message(pass_label,text="Date ", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=4, column=2)
Bus2_date_message=Message(pass_label,text=":Date ", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=5, column=2)

bus_time_message=Message(pass_label,text="Time ", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=4, column=3)
bus2_time_message=Message(pass_label,text=":Time ", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=5, column=3)

bus_seat_message=Message(pass_label,text="Seat ", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=4, column=4)
bus2_seat_message=Message(pass_label,text=":Seat ", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=5, column=4)

bus_ticket_message=Message(pass_label,text="Ticket number ", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=4, column=4)
bus2_ticket_message=Message(pass_label,text=":Ticket number ", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=5, column=4)

to_message=Message(pass_label,text="To ", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=6, column=1)
to_message=Message(pass_label,text="To ", font=(":Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=7, column=1)

reaching_date_message=Message(pass_label,text="Date ", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=6, column=2)
reaching_date_message=Message(pass_label,text=":Date ", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=7, column=2)

reaching_time_message=Message(pass_label,text="Seat ", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=6, column=3)
reaching_time_message=Message(pass_label,text=":Seat ", font=("Poppins", 14,"bold"), background="white",fg="black",width=500).grid(row=7, column=3)

#-------------------------------here wwe are adding qr photo to scan  --------------------------
image_path_2= r"qr.png"
image2 = PhotoImage(file = image_path_2)

desired_width2 = 100
desired_height2 = 100

resized_image2 = image2.subsample(int(image2.width()/desired_width2), int(image2.height()/desired_height2))

qr_img= Label(pass_label, image = resized_image2,background="white" ).grid(row=9 ,column=4)
#-------------------asking user how do they want to save passs--------------------------
btn_label=Label(f,bg="#53D3D1",width=100,height=100)
btn_label.pack(side=RIGHT)
def download():
    result=messagebox.askyesnocancel("Download","Do You Want To Download The Pass?")
    if result:
        print("User clicked OK")
    else:
        print("User clicked Cancel")
download_button=Button(btn_label,text="Download",bg="#FEB249",cursor = "hand2",font=("Poppins", 14,"bold") ,height=3, width=16,command=download,activebackground="red")
download_button.pack(side=RIGHT,anchor=CENTER)

def email():
    result=messagebox.askokcancel('Email', "Your pass have been send to your provided email address \n Thank you!!")
    if result:
        print("User clicked OK")
    
    else:
        print("User clicked Cancel")

send_button=Button(btn_label, text="Send it to email", bg="#FEB249",cursor = "hand2",font=("Poppins", 14,"bold") ,height=3, width=16,command=email,activebackground="red")
send_button.pack(side=RIGHT)


root.mainloop()
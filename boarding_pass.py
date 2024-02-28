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


Name=Label(detail_label,text="Name:",bg='white', font=("Poppins", 14,"bold")).grid(row=1, column=1)
Name_message=Message(detail_label,text="Ticket Details ", font=("Poppins", 14,"bold",'underline'), background="white",fg="black",width=500).grid(row=1, column=2)

seatmo=Label(detail_label,text="seat no:",bg='white', font=("Poppins", 14,"bold")).grid(row=2, column=1)
seatmo_message=Message(detail_label,text="Ticket Details ", font=("Poppins", 14,"bold",'underline'), background="white",fg="black",width=500).grid(row=2, column=2)

Destination=Label(detail_label,text="Destination:",bg='white', font=("Poppins", 14,"bold")).grid(row=4, column=1)
Destination_message=Message(detail_label,text="Ticket Details ", font=("Poppins", 14,"bold",'underline'), background="white",fg="black",width=500).grid(row=4, column=2)

Date=Label(detail_label,text="Date:",bg='white', font=("Poppins", 14,"bold")).grid(row=5, column=1)
Date_message=Message(detail_label,text="Ticket Details ", font=("Poppins", 14,"bold",'underline'), background="white",fg="black",width=500).grid(row=5, column=2)

Phone=Label(detail_label,text="Phone:",bg='white', font=("Poppins", 14,"bold")).grid(row=1, column=4)
Phone_message=Message(detail_label,text="Ticket Details ", font=("Poppins", 14,"bold",'underline'), background="white",fg="black",width=500).grid(row=1, column=5)


Bus=Label(detail_label,text="Bus:",bg='white', font=("Poppins", 14,"bold")).grid(row=2, column=4)
Bus_message=Message(detail_label,text="Ticket Details ", font=("Poppins", 14,"bold",'underline'), background="white",fg="black",width=500).grid(row=2, column=5)


price=Label(detail_label,text="price:",bg='white', font=("Poppins", 14,"bold")).grid(row=2, column=4)
price_message=Message(detail_label,text="Ticket Details ", font=("Poppins", 14,"bold",'underline'), background="white",fg="black",width=500).grid(row=2, column=5)



#-------------------------------here wwe are adding qr photo to scan  --------------------------
image_path_2= r"qr.png"
image2 = PhotoImage(file = image_path_2)

desired_width2 = 100
desired_height2 = 100

resized_image2 = image2.subsample(int(image2.width()/desired_width2), int(image2.height()/desired_height2))

qr_img= Label(detail_label, image = resized_image2,background="white" ).grid(row=9 ,column=4)
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
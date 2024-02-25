from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry


root = Tk()
root.geometry("1200x1000")

frame = Frame(root,bg="#024c6e", highlightbackground="black", highlightthickness=2, bd=2)
frame.pack(expand=TRUE, fill=BOTH)



image_path = r"bus_12.png"
image = PhotoImage(file = image_path)

desired_width = 100
desired_height = 75

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
b3_button=Button(label, text="contact us",height=10,width=15, bg="#D3D3D3",cursor = " hand2",font=('Inter',10,"bold"), command=popup)
b3_button.pack(side=RIGHT,  padx=(0,30),pady=25)

def aboutus_popup():
    messagebox.showinfo("About Us","we are bus travel")
b2_button = Button(label, text="about us", height=10,width=15,bg="#D3D3D3",cursor = "  hand2",font=('Inter',10,"bold"),command=aboutus_popup)
b2_button.pack(side=RIGHT, padx=(0,30),pady=25)

def service_showinfo():
    messagebox.showinfo("Service","We provide the best services for you")
button = Button(label, text="service",height=10,width=15, bg="#D3D3D3",cursor = "  hand2",font=('Inter',10,"bold"), command=service_showinfo)
button.pack(side=RIGHT, padx=(0,30),pady=25)

#--------------------------creating a frame for payment--------------------------------------

payment_frame=Frame(frame,bg="#024c6e",width=1000,height=1000)
payment_frame.pack(expand=False, fill=BOTH)

payment_message=Message(payment_frame,text="Here, you can select any payment option to purchase a ticket." ,font=('Inter',35,"bold"),bg="#024c6e",fg='white',width=700)
payment_message.pack()


payment_label = Label(payment_frame, bg="#024c6e",  width=desired_width, height=100)
payment_label.pack(side = LEFT, expand=False, fill=BOTH,pady=100)
payment_label.pack_propagate(False)
payment_label.pack(pady=7)

image_esewa = PhotoImage(file="esewa.png")

esewa_button = Button(payment_label, text="Pay with Esewa", font=('Inter', 10, "bold"), bg="#FBECEB", image=image_esewa, width=400,height=85,fg='black', pady=10,compound=LEFT)
esewa_button.pack(side=TOP, pady=10)

khalti_button=Button(payment_label,text="Pay with Khatlti",font=('Inter',10,"bold"),bg="#FBECEB",fg='black',width=50,height=5,pady=10)
khalti_button.pack(side=TOP,pady=10)

khalti_button=Button(payment_label,text="Pay with Master Card",font=('Inter',10,"bold"),bg="#FBECEB",fg='black',width=50,height=5,pady=10)
khalti_button.pack(side=TOP,pady=10)


root.mainloop()
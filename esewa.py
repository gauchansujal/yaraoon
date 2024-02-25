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
    

button = Button(label, text="sign in",height=10,width=15,bg="#0094FF",cursor = "hand2",font=('poppins',10,"bold"),command=login2)
button.pack(side=RIGHT,pady=25)


def popup(): 
    messagebox.showinfo("contac us", "987635925924")
b3_button=Button(label, text="contact us",height=10,width=15, bg="#D3D3D3",cursor = "  hand2",font=('poppins',10,"bold"), command=popup)
b3_button.pack(side=RIGHT,  padx=(0,30),pady=25)

def aboutus_popup():
    messagebox.showinfo("About Us","we are bus travel")
b2_button = Button(label, text="about us", height=10,width=15,bg="#D3D3D3",cursor = "  hand2",font=('poppins',10,"bold"),command=aboutus_popup)
b2_button.pack(side=RIGHT, padx=(0,30),pady=25)

def service_showinfo():
    messagebox.showinfo("Service","We provide the best services for you")
button = Button(label, text="service",height=10,width=15, bg="#D3D3D3",cursor = "  hand2",font=('poppins',10,"bold"), command=service_showinfo)
button.pack(side=RIGHT, padx=(0,30),pady=25)


esewa_frame = Frame(frame, bg="#024c6e", highlightbackground="black", height=100)
esewa_frame.pack(expand=TRUE, fill=BOTH)

image_esewa = PhotoImage(file="esewa2.png")

esewa_label = Label(esewa_frame, bg="black",  width=desired_width, height=75, image=image_esewa,anchor=W)
esewa_label.pack(side = TOP, expand=False, fill=BOTH,padx=10)

esewa_2label = Label(esewa_frame, bg="#3FC90F",  width=desired_width, height=2, text="Please Pay Here.",font=("Poppins", 20,"bold"),fg="white", anchor=CENTER)
esewa_2label.pack(side = TOP, expand=False, fill=BOTH,padx=10)


image_esewaQR = PhotoImage(file="esewaQR.png")

esewaQR_label = Label(esewa_frame, bg="#024c6e",  width=desired_width, height=500, image=image_esewaQR,anchor=CENTER)
esewaQR_label.pack(side = TOP, expand=False, fill=BOTH,padx=10)

esewa_3label = Label(esewa_frame, bg="#024c6e",  width=desired_width, height=2, text="Please don’t forget to write your name in remarks.",font=("Poppins", 20,"bold"),fg="black", anchor=CENTER)
esewa_3label.pack(side = TOP, expand=False, fill=BOTH,padx=10)


root.mainloop()
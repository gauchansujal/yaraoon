from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry


root = Tk()
root.geometry("1200x1000")

frame = Frame(root,bg="#53D3D1", highlightbackground="black", highlightthickness=2, bd=2)
frame.pack(expand=TRUE, fill=BOTH)



image_path = r"bus_12.png"
image = PhotoImage(file = image_path)

desired_width = 100
desired_height = 75

resized_image = image.subsample(int(image.width()/desired_width), int(image.height()/desired_height))

label = Label(frame, bg="#53D3D1",  width=desired_width, height=100, image = resized_image, anchor=W)
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
b3_button=Button(label, text="contact us",height=10,width=15, bg="#D3D3D3",cursor = " hand2",font=('poppins',10,"bold"), command=popup)
b3_button.pack(side=RIGHT,  padx=(0,30),pady=25)

def aboutus_popup():
    messagebox.showinfo("About Us","we are bus travel")
b2_button = Button(label, text="about us", height=10,width=15,bg="#D3D3D3",cursor = "  hand2",font=('poppins',10,"bold"),command=aboutus_popup)
b2_button.pack(side=RIGHT, padx=(0,30),pady=25)

def service_showinfo():
    messagebox.showinfo("Service","We provide the best services for you")
button = Button(label, text="service",height=10,width=15, bg="#D3D3D3",cursor = "  hand2",font=('poppins',10,"bold"), command=service_showinfo)
button.pack(side=RIGHT, padx=(0,30),pady=25)

#--------------------------creating a frame for payment--------------------------------------  

payment_frame=Frame(frame,bg="#53D3D1",width=1000,height=1000)
payment_frame.pack(expand=False, fill=BOTH)

payment_message=Message(payment_frame,text="Here, you can select any payment option to purchase a ticket." ,font=('poppins',35,"bold"),bg="#53D3D1",fg='white',width=700)
payment_message.pack()


payment_label = Label(payment_frame, bg="#53D3D1",  width=desired_width, height=100)
payment_label.pack(side = LEFT, expand=False, fill=BOTH,pady=100)
payment_label.pack_propagate(False)
payment_label.pack(pady=7)
#---------------------------creating esewa buttons-----------------------------------------------

def esewa_payment():
    result=messagebox.askokcancel("Paymetn","Are you sure you ?")
    if result:
        print("User clicked OK")
        root.destroy()
        import esewa
             
    else:
        print("User clicked Cancel")

    
image_esewa = PhotoImage(file="esewa.png")

esewa_button = Button(payment_label, text="Pay with Esewa", font=('poppins', 10, "bold"), bg="#FBECEB", image=image_esewa, width=400,height=85,fg='black',pady=10,compound=LEFT,command=esewa_payment)
esewa_button.pack(side=TOP, pady=10)

#---------------------------creating khalti buttons-------------------------------------------------------

def khalti_payment():
    result=messagebox.askokcancel("Paymetn","Are you sure you ?")
    if result:
        print("User clicked OK")
        root.destroy()
        import khalti
         
    else:
        print("User clicked Cancel")

image_Khalti = PhotoImage(file="Khalti.png")
khalti_button=Button(payment_label,text="Pay with Khatlti",font=('poppins',10,"bold"),bg="#FBECEB",image=image_Khalti, width=400,height=85,fg='black', pady=10,compound=LEFT,command=khalti_payment)
khalti_button.pack(side=TOP,pady=10)

image_mastercard= PhotoImage(file="mastercard.png")
khalti_button=Button(payment_label,text="Pay with Master Card",font=('poppins',10,"bold"),bg="#FBECEB",image=image_mastercard, width=400,height=85,fg='black', pady=10,compound=LEFT)
khalti_button.pack(side=TOP,pady=10)


root.mainloop()
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

#--------------------------------------creating khalti frame-----------------------------------------------------------------------------

khalti_frame = Frame(frame, bg="#024c6e", height=100)
khalti_frame.pack(expand=TRUE, fill=BOTH)

image_khalti = PhotoImage(file="khalti1.png")

desired_1width=100
desired_1height=50


x_1subsample_factor = max(int(image_khalti.width()/desired_1width), 1)
y_1subsample_factor = max(int(image_khalti.height()/desired_1height), 1)

resized_1image = image_khalti.subsample(x_1subsample_factor, y_1subsample_factor)

khalti_label = Label(khalti_frame, bg="white",  width=desired_width, height=75, image=resized_1image,anchor=W)
khalti_label.pack(side = TOP, expand=False, fill=BOTH,padx=10)

khalti_2label = Label(khalti_frame ,bg="#5C2E91",  width=desired_width, height=2, text="Please Pay Here.",font=("Poppins", 20,"bold"),fg="white", anchor=CENTER)
khalti_2label.pack(side = TOP, expand=False, fill=BOTH,padx=10)


image_khaltiQR  = PhotoImage(file="khalti12.jpg")

desired_2width=250
desired_2height=400


x_subsample_factor = max(int(image_khaltiQR.width()/desired_2width), 1)
y_subsample_factor = max(int(image_khaltiQR.height()/desired_2height), 1)

resized_2image = image_khaltiQR.subsample(x_subsample_factor, y_subsample_factor)

khalti_3label = Label(khalti_frame, bg="#024c6e", width=desired_2width, height=desired_2height, image=resized_2image)
khalti_3label.pack(side=TOP, expand=False, fill=BOTH, padx=10)

esewa_4label = Label(khalti_frame, bg="#024c6e", width=desired_1width, height=2, text="Please don’t forget to write your name in remarks.", font=("Poppins", 20, "bold"), fg="black")
esewa_4label.pack(side=TOP, expand=False, fill=BOTH, padx=10)


#----------------creating update buttons------------------------------------
buttons_label = Label(khalti_frame, bg="#024c6e",  width=desired_width, height=75,anchor=CENTER)
buttons_label.pack(side = TOP,padx=10)
#------------------------creating esewa button--------------------------------
def esewa_payment():
    result=messagebox.askokcancel("Paymetn","Are you sure you ?")
    if result:
        print("User clicked OK")
        root.destroy()
        import esewa
             
    else:
        print("User clicked Cancel")

    
image_esewa = PhotoImage(file="esewa.png")

esewa_button = Button(buttons_label, bg="#FBECEB", image=image_esewa, width=150,height=75,fg='black',pady=10,compound=LEFT,command=esewa_payment)
esewa_button.pack(side=LEFT)
#--------------------------------creating message------------------------------
or_message=Message(buttons_label,text="OR",font=('poppins',14,"bold"),bg="#024c6e",fg='black')
or_message.pack(side=LEFT)
#-----------------------creating update button for mastercard---------------------
def mastercard_payment():
    result=messagebox.askokcancel("Paymetn","Are you sure you ?")
    if result:
        print("User clicked OK")
        root.destroy()
        import mastercard
    else:
        print("User clicked Cancel")

image_mastercard= PhotoImage(file="mastercard.png")
mastercard_button=Button(buttons_label,bg="#FBECEB",image=image_mastercard, width=150,height=75,fg='black', pady=10,command=mastercard_payment)
mastercard_button.pack(side=LEFT,pady=10)

#-------------------------------creating conformation button--------------------------------

def boarding_pass():
    result=messagebox.askokcancel("Paymetn","Are you sure you ?")
    if result:
        print("User clicked OK")
        root.destroy()
        import boarding_pass
    else:
        print("User clicked Cancel")

confrim_button=Button(buttons_label,bg="#FBECEB",text="CONFRIM", width=15,height=3,fg='black', font=("Poppins", 14,"bold"),command=boarding_pass)
confrim_button.pack(side=RIGHT,padx=(150,0))
root.mainloop()
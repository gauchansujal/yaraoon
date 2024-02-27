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
    

button = Button(label, text="sign in",height=10,width=15,bg="#0094FF",cursor = "hand2",font=('poppins',10,"bold"),command=login2)
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



#--------------------------creating a frame for payment--------------------------------------

esewa_frame = Frame(frame, bg="#53D3D1", highlightbackground="black", height=100)
esewa_frame.pack(expand=TRUE, fill=BOTH)

image_esewa = PhotoImage(file="esewa2.png")

esewa_label = Label(esewa_frame, bg="black",  width=desired_width, height=75, image=image_esewa,anchor=W)
esewa_label.pack(side = TOP, expand=False, fill=BOTH,padx=10)

esewa_2label = Label(esewa_frame, bg="#3FC90F",  width=desired_width, height=2, text="Please Pay Here.",font=("Poppins", 20,"bold"),fg="white", anchor=CENTER)
esewa_2label.pack(side = TOP, expand=False, fill=BOTH,padx=10)


image_esewaQR = PhotoImage(file="esewaQR.png")

esewaQR_label = Label(esewa_frame, bg="#53D3D1",  width=desired_width, height=500, image=image_esewaQR,anchor=CENTER)
esewaQR_label.pack(side = TOP, expand=False, fill=BOTH,padx=10)

esewa_3label = Label(esewa_frame, bg="#53D3D1",  width=desired_width, height=2, text="Please don’t forget to write your name in remarks.",font=("Poppins", 20,"bold"),fg="black", anchor=CENTER)
esewa_3label.pack(side = TOP, expand=False, fill=BOTH,padx=10)

#----------------creating update buttons----------------------------
buttons_label = Label(esewa_frame, bg="#53D3D1",  width=desired_width, height=75)
buttons_label.pack(side = TOP,padx=10)

def khalti_payment():
    result=messagebox.askokcancel("payment","Are you sure you ?")
    if result:
        print("User clicked OK")
        root.destroy()
        import khalti
         
    else:
        print("User clicked Cancel")


image_khalti = PhotoImage(file="khalti1.png")

desired_1width=100
desired_1height=50


x_1subsample_factor = max(int(image_khalti.width()/desired_1width), 1)
y_1subsample_factor = max(int(image_khalti.height()/desired_1height), 1)

resized_1image = image_khalti.subsample(x_1subsample_factor, y_1subsample_factor)

khalti_button=Button(buttons_label,image=resized_1image, bg="white",width=150,height=75,fg='black',compound=LEFT,command=khalti_payment)
khalti_button.pack(side=LEFT,pady=10)

#--------------------------------creating message------------------------------
or_message=Message(buttons_label,text="OR",font=('poppins',14,"bold"),bg="#53D3D1",fg='black')
or_message.pack(side=LEFT)
#----------------------creating update button for fonepay---------------------
def fonepay_payment():
    result=messagebox.askokcancel("payment","Are you sure you ?")
    if result:
        print("User clicked OK")
        root.destroy()
        import fonepay
    else:
        print("User clicked Cancel")

image_fonepay= PhotoImage(file="fonepay.png")
fonepay_button=Button(buttons_label,bg="#FBECEB",image=image_fonepay, width=150,height=75,fg='black', pady=10,command=fonepay_payment)
fonepay_button.pack(side=LEFT,pady=10)

#----------------------creating conformation button---------------------
def boarding_pass():
    result=messagebox.askokcancel("payment","Are you sure you ?")
    if result:
        print("User clicked OK")
        root.destroy()
        import boarding_pass
    else:
        print("User clicked Cancel")

confrim_button=Button(buttons_label,bg="#FBECEB",text="CONFRIM", width=15,height=3,fg='black', font=("Poppins", 14,"bold"),command=boarding_pass)
confrim_button.pack(side=RIGHT,padx=(150,0))
root.mainloop()
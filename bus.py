from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, Button
from tkinter import ttk



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

label = Label(frame, bg="#53D3D1",  width=desired_width, height=100, image = resized_image, anchor=W)
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
        print("User clicked Cancel")

    

button = Button(label, text="Log out",height=10,width=9,bg="#0094FF",cursor = "hand2",font=('Inter',10,"bold"),command=logout)
button.pack(side=RIGHT,pady=25)

def message_popup(): 
    messagebox.showinfo("contac us", "Please get in touch with us right away if you have any issues with this app. Contact us at\n +977 985511133.")
b3_button=Button(label, text="contact us",height=10,width=9, bg="#D3D3D3",cursor = " hand2",font=('Inter',10,"bold"), command=message_popup)
b3_button.pack(side=RIGHT,  padx=(0,30),pady=25)

def aboutus_popup():
    messagebox.showinfo("About Us","We are travel bus; we are the first travel agency in Nepal where you may purchase a ticket to reserve a bus and travel at an affordable price throughout Nepal. By offering practical and reasonably priced bus reservation services, Travel Bus is transforming the travel sector in Nepal and facilitating individuals' exploration of the natural beauty of our nation.")
b2_button = Button(label, text="about us", height=10,width=9,bg="#D3D3D3",cursor = "  hand2",font=('Inter',10,"bold"),command=aboutus_popup)
b2_button.pack(side=RIGHT, padx=(0,30),pady=25)

def service_showinfo():
    messagebox.showinfo("Service","At Travel Bus, we take pride in offering the best bus reservation service in Nepal. Our software is designed to cater to the needs of both locals and visitors, providing a seamless and convenient way to schedule buses for their travels across the country.")
button = Button(label, text="service",height=10,width=9, bg="#D3D3D3",cursor = "  hand2",font=('Inter',10,"bold"), command=service_showinfo)
button.pack(side=RIGHT, padx=(0,30),pady=25)

text_frame=Frame(frame,width=500, height= 5,bg="#53D3D1")
text_frame.pack(side=TOP,expand=True,fill=BOTH)

message_text=Message(text_frame, bg="#53D3D1",text="Choose your seat for your long travel!! ",font=('Inter',40,"bold"),width=500)
message_text.pack(side=TOP)
#------------------------------creating new frame ---------------------------

f = Frame(frame, width= 500, height=500,bg="#53D3D1", highlightbackground="black", highlightthickness=2, bd=0)
f.pack( side= TOP, fill=Y ,padx=100)

#---------------------------------creating bus seat so that user can pick your seat--------------------------------------------------------------

label2 = Label(f, bg="#53D3D1",  width=500, height=desired_height)
label2.pack(side = TOP, expand=False, fill=BOTH)
label2.pack_propagate(False)
label2.pack(pady=7)


def choose(text):
    result=messagebox.askokcancel("",f"Are you sure you want to choose this seat {text}")
    if result:
        print("User clicked OK")
        combo.set(text)
    else:
        print("User clicked Cancel")
   
seat_text1="A7"
seat_indicator1=Label(label2,bg="red" ,height=5,width=9,text="ok").grid(row=1,column=0)
seat1_button = Button(label2, text="A7", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text1)).grid(row=1,column=0)


seat_text2="A6"
seat_indicator2=Label(label2, bg="red",height=5,width=9, text="").grid(row=1,column=2)
seat2_button = Button(label2, text="A6", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text2)).grid(row=1,column=2)


seat_text3="A5"
seat_indicator3=Label(label2,bg="red",height=5,width=9, text="").grid(row=1,column=3)
seat3_button = Button(label2, text="A5", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text3)).grid(row=1,column=3)


seat_text3="A4"
seat_indicator4=Label(label2, bg="red",height=5,width=9,text="").grid(row=1,column=4)
seat4_button = Button(label2, text="A4", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text4)).grid(row=1,column=4)


seat_text4="A3"
seat_indicator5=Label(label2,bg="red",height=5,width=9, text="").grid(row=1,column=5)
seat6_button = Button(label2, text="A3", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text4)).grid(row=1,column=5) 

seat_text41="A2"
seat_indicator6=Label(label2, bg="red",height=5,width=9,text="").grid(row=1,column=6)
seat7_button = Button(label2, text="A2", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text41)).grid(row=1,column=6)


seat_text5="A1"
seat_indicator6=Label(label2,bg="red",height=5,width=9, text="").grid(row=1,column=7)
seat8_button = Button(label2, text="A1", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text5)).grid(row=1,column=7) 

seat_text6="B7"
seat_indicator6=Label(label2, bg="red",height=5,width=9,text="").grid(row=2,column=0)
seatC_button = Button(label2, text="B7", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text6)).grid(row=2,column=0)


seat_text7="B6"
seat_indicator7=Label(label2, bg="red",height=5,width=9,text="").grid(row=2,column=2)
seatB2_button = Button(label2, text="B6", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text7)).grid(row=2,column=2)


seat_text8="B5"
seat_indicator8=Label(label2, bg="red",height=5,width=9,text="").grid(row=2,column=3)
seatC3_button = Button(label2, text="B5", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text8)).grid(row=2,column=3)


seat_text9="B4"
seat_indicator9=Label(label2, bg="red",height=5,width=9,text="").grid(row=2,column=4)
seatD4_button = Button(label2, text="B4", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text9)).grid(row=2,column=4)


seat_text11="B3"
seat_indicator10=Label(label2, bg="red",height=5,width=9,text="").grid(row=2,column=5)
seatE6_button = Button(label2, text="B3", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text11)).grid(row=2,column=5)


seat_text12="B2" 
seat_indicator11=Label(label2, bg="red",height=5,width=9,text="").grid(row=2,column=6)
seatF7_button = Button(label2, text="B2", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text12)).grid(row=2,column=6)

seat_text13="B1"
seat_indicator12=Label(label2, bg="red",height=5,width=9,text="").grid(row=2,column=7)
seatG8_button = Button(label2, text="B1", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text13)).grid(row=2,column=7)


seat_text14="E1!!! \n WE SUGGEST YOU TO CHOOSE THIS SEAT ONLY IF OTHER SEATS ARE UNAVAILABLE."
seat_indicator14=Label(label2, bg="red",height=5,width=9,text="").grid(row=3,column=0)
seatG9_button = Button(label2, text="C1", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text14)).grid(row=3,column=0)


seat_text9="D8"
seat_indicator9=Label(label2, bg="red",height=5,width=9,text="").grid(row=4,column=0)
seatB1_button = Button(label2, text="D8", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text9)).grid(row=4,column=0)


seat_text16="D7"
seat_indicator16=Label(label2, bg="red",height=5,width=9,text="").grid(row=4,column=2)
seatB2_button = Button(label2, text="D7", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text16)).grid(row=4,column=2)


seat_text17="D6"
seat_indicator17=Label(label2, bg="red",height=5,width=9,text="").grid(row=4,column=3)
seatB3_button = Button(label2, text="D6", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text17)).grid(row=4,column=3)


seat_text18="D5"
seat_indicator18=Label(label2, bg="red",height=5,width=9,text="").grid(row=4,column=4)
seatB4_button = Button(label2, text="D5", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text18)).grid(row=4,column=4)

seat_text19="D4"
seat_indicator19=Label(label2, bg="red",height=5,width=9,text="").grid(row=4,column=5)
seatB6_button = Button(label2, text="D4", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text19)).grid(row=4,column=5)


seat_text21="D3"
seat_indicator21=Label(label2, bg="red",height=5,width=9,text="").grid(row=4,column=6) 
seatB7_button = Button(label2, text="D3", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text21)).grid(row=4,column=6)


seat_text22="D2"
seat_indicator22=Label(label2, bg="red",height=5,width=9,text="").grid(row=4,column=7)
seatB8_button = Button(label2, text="D2", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text22)).grid(row=4,column=7)


seat_text23="D1"
seat_indicator23=Label(label2, bg="red",height=5,width=9,text="").grid(row=4,column=8)
seatB8_button = Button(label2, text="D1", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text23)).grid(row=4,column=8)

seat_text24="C8"
seat_indicator24=Label(label2, bg="red",height=5,width=9,text="").grid(row=5,column=0)
seatC1_button = Button(label2, text="C8", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text24)).grid(row=5,column=0)

seat_text25="C7"
seat_indicator25=Label(label2, bg="red",height=5,width=9,text="").grid(row=5,column=2)
seatC2_button = Button(label2, text="C7", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text25)).grid(row=5,column=2)



seat_text256="C6"
seat_indicator256=Label(label2, bg="red",height=5,width=9,text="").grid(row=5,column=3)
seatC3_button = Button(label2, text="C6", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text256)).grid(row=5,column=3)

seat_text26="C5"
seat_indicator26=Label(label2, bg="red",height=5,width=9,text="").grid(row=5,column=4)
seatC4_button = Button(label2, text="C5", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text26)).grid(row=5,column=4)


seat_text27="C4"
seat_indicator27=Label(label2, bg="red",height=5,width=9,text="").grid(row=5,column=5)
seatC6_button = Button(label2, text="C4", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text27)).grid(row=5,column=5) 


seat_text28="C3"
seat_indicator28=Label(label2, bg="red",height=5,width=9,text="").grid(row=5,column=6)
seatC7_button = Button(label2, text="C3", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text28)).grid(row=5,column=6)


seat_text29="C2"
seat_indicator29=Label(label2, bg="red",height=5,width=9,text="").grid(row=5,column=7)
seatC8_button = Button(label2, text="C2", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text29)).grid(row=5,column=7)


seat_text31="C1"
seat_indicator31=Label(label2, bg="red",height=5,width=9,text="").grid(row=5,column=8)
seatC9_button = Button(label2, text="C1", bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text31)).grid(row=5,column=8)




#------------------------------------------creating combo box-----------------------------------
frame2=Label(text_frame,bg="#53D3D1",  width=desired_width, height=desired_height)
frame2.pack(side = RIGHT, expand=False, fill=BOTH)
frame2.pack(pady=7)

ttk.Label(frame2, text = "Your seat :",background="#53D3D1" ,font = ("Poppins", 18,"bold"), ).pack()
combo = ttk.Combobox(frame2, values=[], state='readonly')
combo.pack()
def option_selected(event):
   
   selected_option = combo.get()
   print("You selected:", selected_option)
combo.bind("<<ComboboxSelected>>", option_selected)

def change():
    selected_option = combo.get()
    result=messagebox.askyesno("change",f"Are you sure you want Buy {selected_option} ?")
    if result:
        print("User clicked OK")
        root.destroy()
        import payment_method
    else:
        print("User clicked Cancel")

change_button = Button(frame2 ,text="Buy ticket?", bg="#FEB249",cursor = "hand2",font=("Poppins", 14,"bold") ,height=3, width=16,command=change,activebackground="red")
change_button.pack()
root.mainloop()


from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, Button



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
        import log_in
    else:
        print("User clicked Cancel")
   
logout_button = Button(label, text="log out", bg="#D3D3D3",cursor = " hand2",font=('Inter',10,"bold"),command=logout)
logout_button.pack(side=RIGHT)

def popup(): 
    messagebox.showinfo("contac us", "987635925924")
b3_button=Button(label, text="contact us", bg="#D3D3D3",cursor = "  hand2",font=('Inter',10,"bold"), command=popup)
b3_button.pack(side=RIGHT,  padx=(0,30))

def aboutus_popup():
    messagebox.showinfo("About Us","we are bus travel")
b2_button = Button(label, text="about us", bg="#D3D3D3",cursor = "  hand2",font=('Inter',10,"bold"),command=aboutus_popup)
b2_button.pack(side=RIGHT, padx=(0,30))

def service_showinfo():
    messagebox.showinfo("Service","We provide the best services for you")
serrive_button = Button(label, text="service", bg="#D3D3D3",cursor = "  hand2",font=('Inter',10,"bold"), command=service_showinfo)
serrive_button.pack(side=RIGHT, padx=(0,30))

f = Frame(frame, width= 500, height=500, highlightbackground="black", highlightthickness=2, bd=0)
f.pack( side= TOP, fill=Y, pady=100)

label = Label(f, bg='white',  width=desired_width, height=desired_height, anchor=CENTER)
label.pack(side = TOP, expand=False, fill=BOTH)


message=Message(label,text="choose your seat for your long travel!!",font=('Helvetica', 19,"bold"),width=500)
message.pack(side=TOP,padx=0, pady=1)

label2 = Label(f, bg='#43F4FF',  width=desired_width, height=desired_height, anchor=CENTER)
label2.pack(side = TOP, expand=False, fill=BOTH)
label2.pack_propagate(False)
label2.pack(pady=7)

#---------------------------------creating bus seat so that user can pick your seat--------------------------------------------------------------

click_seat= PhotoImage(file='Seat.png')
img_label= Label(image=click_seat)

def choose(text):
    result=messagebox.askokcancel("",f"Are you sure you want to choose this seat {text}")
    
    if result:
        print("User clicked OK")
        root.destroy()
        import boarding_pass
        
    else:
        print("User clicked Cancel")

seat_text1="A7"
seat1_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text1)).grid(row=1,column=0)

seat_text2="A6"
seat2_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text2)).grid(row=1,column=2)

seat_text3="A5"
seat3_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text3)).grid(row=1,column=3)


seat_text3="A4"
seat4_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text4)).grid(row=1,column=4)

seat_text4="A3"
seat6_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text4)).grid(row=1,column=5) 

seat_text41="A2"
seat7_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text41)).grid(row=1,column=6)

seat_text5="A1"
seat8_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text5)).grid(row=1,column=7) 


seat_text6="B7"
seatC_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text6)).grid(row=2,column=0)

seat_text7="B6"
seatB2_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text7)).grid(row=2,column=2)

seat_text8="B5"
seatC3_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text8)).grid(row=2,column=3)

seat_text9="B4"
seatD4_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text9)).grid(row=2,column=4)

seat_text11="B3"
seatE6_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text11)).grid(row=2,column=5)

seat_text12="B2" 
seatF7_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text12)).grid(row=2,column=6)

seat_text13="B1"
seatG8_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text13)).grid(row=2,column=7)


seat_text14="C1!!! \n WE SUGGEST YOU TO CHOOSE THIS SEAT ONLY IF OTHER SEATS ARE UNAVAILABLE."
seatG9_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text14)).grid(row=3,column=0)


seat_text15="D8"
seatB1_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text15)).grid(row=4,column=0)

seat_text16="D7"
seatB2_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text16)).grid(row=4,column=2)

seat_text17="D6"
seatB3_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text17)).grid(row=4,column=3)

seat_text18="D5"
seatB4_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text18)).grid(row=4,column=4)

seat_text19="D4"
seatB6_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text19)).grid(row=4,column=5)

seat_text21="D3" 
seatB7_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text21)).grid(row=4,column=6)

seat_text22="D2"
seatB8_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text22)).grid(row=4,column=7)

seat_text23="D1"
seatB8_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text23)).grid(row=4,column=8)

seat_text24="C8"
seatC1_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text24)).grid(row=5,column=0)

seat_text25="C7"
seatC2_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text25)).grid(row=5,column=2)

seat_text256="C6"
seatC3_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text256)).grid(row=5,column=3)

seat_text26="C5"
seatC4_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text26)).grid(row=5,column=4)

seat_text27="C4"
seatC6_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text27)).grid(row=5,column=5) 

seat_text28="C3"
seatC7_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text28)).grid(row=5,column=6)

seat_text29="C2"
seatC8_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text29)).grid(row=5,column=7)

seat_text31="C1"
seatC9_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text31)).grid(row=5,column=8)

# seat_text32="CANT USE THIS SEAT"
# seatC10_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=lambda:choose(seat_text32)).grid(row=5,column=9)

root.mainloop()


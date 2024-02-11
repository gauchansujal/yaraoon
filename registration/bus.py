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

f = Frame(frame, width= 500, height=500, highlightbackground="black", highlightthickness=2, bd=0)
f.pack( side= TOP, fill=Y)

label = Label(f, bg='white',  width=desired_width, height=desired_height, anchor=CENTER)
label.pack(side = TOP, expand=False, fill=BOTH)


message=Message(label,text="choose your seat for your long travell",width=500,)
message.pack(side=TOP,padx=100, pady=1)

label2 = Label(f, bg='#43F4FF',  width=desired_width, height=desired_height, anchor=CENTER)
label2.pack(side = TOP, expand=False, fill=BOTH)
label2.pack_propagate(False)
label2.pack(pady=7)



click_seat= PhotoImage(file='Seat.png')
img_label= Label(image=click_seat)
def choose():
    messagebox.showinfo("","are you sure you want to shoose this seat")
seat1_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=1,column=0)
seat2_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=1,column=2)
seat3_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=1,column=3)
seat4_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=1,column=4)
seat6_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=1,column=5) 
seat7_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=1,column=6)
seat8_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=1,column=7)

seatA1_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=2,column=0)
seatB2_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=2,column=2)
seatC3_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=2,column=3)
seatD4_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=2,column=4)
seatE6_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=2,column=5) 
seatF7_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=2,column=6)
seatG8_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=2,column=7)

seatG9_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=3,column=0)
seatG10_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=4,column=0)

seatB1_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=5,column=0)
seatB2_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=5,column=2)
seatB3_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=5,column=3)
seatB4_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=5,column=4)
seatB6_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=5,column=5) 
seatB7_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=5,column=6)
seatB8_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=5,column=7)

seatC1_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=6,column=0)
seatC2_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=6,column=2)
seatC3_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=6,column=3)
seatC4_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=6,column=4)
seatC6_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=6,column=5) 
seatC7_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=6,column=6)
seatC8_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=6,column=7)
seatC10_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=6,column=8)
seatC11_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=5,column=8)

message1=Message(label2,text="front side of bus",bg="#D3D3D3",width=500).grid(row=4,column=10)


root.mainloop()

from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox



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
   
button = Button(label, text="log out", bg="#D3D3D3",cursor = " hand2",font=('Inter',10,"bold"),command=logout)
button.pack(side=RIGHT)

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
button = Button(label, text="service", bg="#D3D3D3",cursor = "  hand2",font=('Inter',10,"bold"), command=service_showinfo)
button.pack(side=RIGHT, padx=(0,30))

f = Frame(frame, width= 500, height=500, highlightbackground="black", highlightthickness=2, bd=0)
f.pack( side= TOP, fill=Y, pady=100)

label = Label(f, bg='white',  width=desired_width, height=desired_height, anchor=CENTER)
label.pack(side = TOP, expand=False, fill=BOTH)


message=Message(label,text="choose your seat for your long travell",font=('Helvetica', 12),width=500)
message.pack(side=TOP,padx=0, pady=1)

label2 = Label(f, bg='#43F4FF',  width=desired_width, height=desired_height, anchor=CENTER)
label2.pack(side = TOP, expand=False, fill=BOTH)
label2.pack_propagate(False)
label2.pack(pady=7)

#---------------------------------creating bus seat so that user can pick your seat--------------------------------------------------------------

click_seat= PhotoImage(file='Seat.png')
img_label= Label(image=click_seat)

seat_buttons = {}

def choose():
    result=messagebox.askokcancel("","Are you sure you want to choose this seat")
    if result:
        print("User clicked OK")
        root.destroy()
        import boarding_pass
        
    else:
        print("User clicked Cancel")

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

seatB1_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=4,column=0)
seatB2_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=4,column=2)
seatB3_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=4,column=3)
seatB4_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=4,column=4)
seatB6_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=4,column=5) 
seatB7_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=4,column=6)
seatB8_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=4,column=7)
seatB8_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=4,column=8)

seatC1_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=5,column=0)
seatC2_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=5,column=2)
seatC3_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=5,column=3)
seatC4_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=5,column=4)
seatC6_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=5,column=5) 
seatC7_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=5,column=6)
seatC8_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=5,column=7)
seatC9_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=5,column=8)
seatC10_button = Button(label2, text="",image=click_seat, bg="#D3D3D3",cursor = "hand2",command=choose).grid(row=5,column=9)


message1=Message(label2,text="front side of bus",background="#D3D3D3",width=500).grid(row=4,column=10)


# # Example function to create and place buttons
# def create_button(row, column):
#     button = Button(root, text="", bg="#D3D3D3", cursor="hand2", command=choose, image=click_seat)
#     button.grid(row=row, column=column)
#     return button

# # Example loop to create and place buttons
# for row, row_label in enumerate(["1", "A", "B", "C"]):
#     for col, col_label in enumerate(["1", "2", "3", "4", "6", "7", "8", "9", "10"]):
#         # Create button with image
#         button = create_button(row + 1, col)
#         button.grid(width=50, height=50, compound='top')
#         # Store button in dictionary
#         seat_buttons[(row_label, col_label)] = button




root.mainloop()

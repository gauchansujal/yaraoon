from tkinter import *
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter import messagebox


root = Tk()

root.geometry("1200x1000")



frame = Frame(root, highlightbackground="black", highlightthickness=2, bd=1,height=100,relief="ridge")
frame.pack(expand=TRUE, fill=BOTH)


image_path = r"bussss.png"
image= PhotoImage(file = image_path)


desired_width = 100
desired_height = 50

resized_image = image.subsample(int(image.width()/desired_width), int(image.height()/desired_height))


label = Label(frame, bg='#4aa9ed',  width=desired_width, height=desired_height, image = resized_image, anchor=W)
label.pack(side = TOP, expand=False, fill=BOTH)
label.pack_propagate(False)
label.pack(pady=7)

def login2():
    root.destroy()
    import log_in2
    

button = Button(label, text="sign in", bg="#D3D3D3",cursor = "hand2",command=login2)
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



# we have created 2nd frame here  to put the label on it and then add scrollbar to this frame



second_label = Label(frame,  width=500, height=500, anchor=CENTER)
second_label.pack(side = TOP, expand=False, fill=BOTH) 

# adding calendar  to the frame

cal=DateEntry(second_label ,selectmode='day')

cal.pack(side=RIGHT,padx=5,pady=1) 

message=Message(second_label,text="Date")
message.pack(side=RIGHT,padx=1, pady=1)

def change():
    root.destroy()
    import first
   
change_button = Button(second_label, text="change in plan?", height=2, width=20,cursor = "hand2",command=change)
change_button.pack(anchor=CENTER, padx=(25, 183))

# creting third label

desired_width2 = 100
desired_height2 = 50 

frame1 = Frame(frame, width= desired_width, height= desired_height , highlightbackground="black", highlightthickness=2, bd=0)
frame1.pack( expand=True, fill=BOTH)


third_label= Label(frame1,  width=800, height=800)
third_label.place()

message=Message(third_label,text="Choose your bus",fg="black",bg="#0775F5", width=200,font=("Helvetica", 14, "bold"))
message.pack (side=LEFT,padx=100, pady=8)

# adding menu button

sort_button = Menubutton (third_label, text="sort by",fg="black",bg="#0775F5",cursor = "  hand2")
sort_button.menu=Menu(sort_button)
sort_button["menu"]=sort_button.menu

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()

sort_button.menu.add_checkbutton(label="maxinmum price to mini",variable=var1)
sort_button.menu.add_checkbutton(label="minimum price to maximum",variable=var2)
sort_button.menu.add_checkbutton(label="sort by time",variable=var3)
sort_button.menu.add_checkbutton(label="want taxo",variable=var4)
sort_button.pack(side=RIGHT, padx=10)

# CREATINGG BUTTON

message_label= Label(frame1, width=desired_width, height=desired_height,bg="red")
message_label.pack(side = TOP, expand=False, fill=BOTH)



bus_message=Message(message_label,text="Bus type", font=("Helvetica", 14, "bold"),fg="black", bg="red", width=desired_width)
bus_message.pack(side=LEFT,padx=150,pady=8)

departure_message=Message(message_label,text="Departure", font=("Helvetica", 14, "bold"),fg="black", bg="red", width=desired_width)
departure_message.pack(side=LEFT,padx=300,pady=8)

fare_message=Message(message_label,text="Fare", font=("Helvetica", 14, "bold"),fg="black", bg="red", width=desired_width)
fare_message.pack(side=LEFT,padx=300,pady=8)

button_label=Label(frame1, width=desired_width, height=desired_height,bg="red")
button_label.pack(side = TOP, expand=False, fill=BOTH)
 
bus_button=Button(button_label,text="", bg='black', fg='black', height=5, width=100, padx=5, pady=5)
bus_button.pack(side=LEFT,padx=150,pady=8)

# bus2_button=Button(button_label,text="hello world", bg='white', fg='black', height=5, width=200, padx=5, pady=5).grid(row=1, column=0,padx=100,pady=8)

# bus3_button=Button(button_label,text="hello world", bg='white', fg='black', height=5, width=200, padx=5, pady=5).grid(row=2, column=0,padx=100,pady=8)

# bus4_button=Button(button_label,text="hello world", bg='white', fg='black', height=5, width=200, padx=5, pady=5).grid(row=3, column=0,padx=100,pady=8)

# buy_button=Button( button_label,text="Buy ticket", bg='white', fg='black', height=5, width=30, padx=5, pady=5).grid(row=4, column=1,padx=50,pady=8)

root.mainloop()
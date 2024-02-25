from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

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
    

button = Button(label, text="sign in",height=10,width=15,bg="#0094FF",cursor = "hand2",font=('Inter',10,"bold"),command=login2)
button.pack(side=RIGHT,pady=25)


def message_popup(): 
    messagebox.showinfo("contac us", "987635925924")
b3_button=Button(label, text="contact us",height=10,width=15, bg="#D3D3D3",cursor = " hand2",font=('Inter',10,"bold"), command=message_popup)
b3_button.pack(side=RIGHT,  padx=(0,30),pady=25)

def aboutus_popup():
    messagebox.showinfo("About Us","we are bus travel")
b2_button = Button(label, text="about us", height=10,width=15,bg="#D3D3D3",cursor = "  hand2",font=('Inter',10,"bold"),command=aboutus_popup)
b2_button.pack(side=RIGHT, padx=(0,30),pady=25)

def service_showinfo():
    messagebox.showinfo("Service","We provide the best services for you")
button = Button(label, text="service",height=10,width=15, bg="#D3D3D3",cursor = "  hand2",font=('Inter',10,"bold"), command=service_showinfo)
button.pack(side=RIGHT, padx=(0,30),pady=25)

f = Frame(frame, width= 500, highlightbackground="black",highlightthickness=2, bd=2,height=500,bg="#53D3D1")
f.pack( side= RIGHT, fill=Y)

custom_font= ("Helvetica", 20)

#----------------------text-box----------------------------------------------------

b4 = Label(f, text="leaving from ?",bg="#53D3D1", font=custom_font)
b4.grid(row=0, column=0, padx=20, pady=22)

def temp_text(e):
    b4_entry.delete(1.0, "end-1c")

b4_entry = Text(f, width=30, height=2,highlightbackground="black",highlightthickness=2, bd=2)
b4_entry.grid( row=1, column=0, padx=40, pady=20)
b4_entry.insert(1.0,"Enter source city: \n (Eg:Kathmandu)")
b4_entry.bind("<FocusIn>",temp_text)


#-------------------------------------------second-text-box---------------------------------

b5 = Label(f, text="going destination",bg="#53D3D1", font=custom_font)
b5.grid(row=2, column=0, padx=40, pady=20)

def temp_2ndtext(e):
    b5_entry.delete(1.0, "end-1c")
b5_entry = Text(f, width=30, height=2,highlightbackground="black",highlightthickness=2, bd=2)
b5_entry.grid(row=3, column=0, padx=40, pady=20)
b5_entry.insert(1.0,"Enter Destination City:\n (Eg:Pokhara)")
b5_entry.bind("<FocusIn>",temp_2ndtext)

#-------------------------------------------date-time-text-box---------------------------------

b6 = Label(f, text="Travel Date",bg="#53D3D1", font=custom_font)
b6.grid(row=4, column=0, padx=40, pady=20)

def search():
    result=messagebox.askyesno('',"Are you sure you want to choose this route ")
    if result:
        print("user clicked yes")
        root.destroy()
        import second
       
    else:
        print("user clicked no")
   
b7 = Button(f, text="search Buses", bg="#4aa9ed", fg="black", width=12, font=custom_font,command=search)
b7.grid(row=7, column=0, padx=0, pady=40)

image_path_2= r"bus.png"
image = PhotoImage(file = image_path_2)

g = Frame(frame, width=500, height=500,bg="#53D3D1", highlightbackground="black")
g.pack(expand=TRUE, fill=BOTH)


rrr = Label(g, image=image,bg="#53D3D1")
rrr.pack()

root.mainloop()

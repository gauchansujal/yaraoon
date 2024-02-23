from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox



root = Tk()
root.geometry("1200x1000")

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

def login():
    result=messagebox.askyesno('log in',"Are you sure to Sign In?")
    root.destroy()
    import log_in
   
button = Button(label, text="sign in", bg="#D3D3D3",cursor = " hand2",command=login)
button.pack(side=RIGHT)

def popup(): 
    messagebox.showinfo("contac us", "If you find any bugs and face any probelnm then please then contact us on \n +977 987635925924")
    
b3_button=Button(label, text="contact us", bg="#D3D3D3",cursor = "  hand2", command=popup)
b3_button.pack(side=RIGHT,  padx=(0,30))

def aboutus_popup():
    messagebox.showinfo("About Us","we are bus travel!!!")
b2_button = Button(label, text="about us", bg="#D3D3D3",cursor = "  hand2",command= aboutus_popup)
b2_button.pack(side=RIGHT, padx=(0,30))

def service_showinfo():
    messagebox.showinfo("Service","We provide the best services for you")
button = Button(label, text="service", bg="#D3D3D3",cursor = "  hand2", command=service_showinfo)
button.pack(side=RIGHT, padx=(0,30))

f = Frame(frame, width= 500, height=500, highlightbackground="black", highlightthickness=2, bd=0)
f.pack( side= RIGHT, fill=Y)

custom_font= ("Helvetica", 20)

b4 = Label(f, text="leaving from ?", font=custom_font)
b4.grid(row=0, column=0, padx=20, pady=22)

b4_entry = Text(f, width=30, height=2)
b4_entry.grid( row=1, column=0, padx=40, pady=20)

b5 = Label(f, text="going destination", font=custom_font)
b5.grid(row=2, column=0, padx=40, pady=20)

b5_entry = Text(f, width=30, height=2)
b5_entry.grid(row=3, column=0, padx=40, pady=20)

b6 = Label(f, text="Travel Date", font=custom_font)
b6.grid(row=4, column=0, padx=40, pady=20)

b6_entry = Text(f, width=30, height=2, font= 20 )
b6_entry.grid(row=5, column=0, padx=40, pady=20)


b7 = Button(f, text="search Buses", background="blue", fg="black", width=10, font=custom_font)
b7.grid(row=7, column=0, padx=0, pady=40)


def search():
    result=messagebox.askyesno('',"Are you sure you want to choose this route ")
    if result:
        print("user clicked yes")
        root.destroy()
        import second
       
    else:
        print("user clicked no")
   
b7 = Button(f, text="search Buses", background="#4aa9ed", fg="black", width=10, font=custom_font,command=search)
b7.grid(row=7, column=0, padx=0, pady=40)

image_path_2= r"bus.png"
image = PhotoImage(file = image_path_2)

g = Frame(frame, width=500, height=500, highlightbackground="black", highlightthickness=2)
g.pack(expand=TRUE, fill=BOTH)



rrr = Label(g, image=image)
rrr.pack()

root.mainloop()

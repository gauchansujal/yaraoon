from tkinter import *
from tkinter import PhotoImage

root = Tk()
root.geometry("500x500")

frame = Frame(root, highlightbackground="black", highlightthickness=2, bd=2)
frame.pack(expand=TRUE, fill=BOTH)

image_path = r""
image = PhotoImage(file = image_path)

desired_width = 100
desired_height = 50

resized_image = image.subsample(int(image.width()/desired_width), int(image.height()/desired_height))

label = Label(frame, bg='#1069E5',  width=desired_width, height=desired_height, image = resized_image, anchor=W)
label.pack(side = TOP, expand=False, fill=BOTH)
label.pack_propagate(False)
label.pack(pady=7)

button5 = Button(label, text="Sign in", bg="#0094FF")
button5.pack(side=RIGHT, expand=False, padx=(0,30))

b3_button=Button(label, text="Contact us")
b3_button.pack(side=RIGHT, padx=(0,30))

b2_button = Button(label, text="About us")
b2_button.pack(side=RIGHT, padx=(0,30))

button = Button(label, text="Services")
button.pack(side=RIGHT, expand=False, padx=(0,30))

f = Frame(frame, width=300, height=100, highlightbackground="black", highlightthickness=2, bd=0)
f.pack(side=LEFT, expand=False, padx=(900,39))

b4 = Label(f, text="leaving from ?", font="bold_font")
b4.grid(row=0, column=0, padx=20, pady=20)

b4_entry = Entry(f, width=20)
b4_entry.grid( row=1, column=0, padx=40, pady=20)

b5 = Label(f, text="going destination", font="bold_font")
b5.grid(row=2, column=0, padx=40, pady=20)

b5_entry = Entry(f, width=20)
b5_entry.grid(row=3, column=0, padx=40, pady=20)

b6 = Label(f, text="Travel Date", font="bold_font")
b6.grid(row=4, column=0, padx=40, pady=20)

b6_entry = Entry(f, width=20)
b6_entry.grid(row=5, column=0, padx=40, pady=20)

b7 = Button(f, text="search Buses", background="#4aa9ed", fg="black", width=20)
b7.grid(row=7, column=0, padx=0, pady=40)


root.mainloop()

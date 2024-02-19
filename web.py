from tkinter import *
from PIL import Image, ImageTk
'''def convert_to_circular(image_path, size):
    original_image = Image.open(image_path)
    original_image = original_image.resize((size, size))
    
    circular_mask = Image.new('L', (size, size),0)
    draw = ImageDraw.Draw(circular_mask)
    draw.ellipse((0, 0,size, size), fill=225)

    circular_image = Image.new('RGBA',(size, size),(0,0,0,0))
    circular_image.paste(original_image, mask=circular_mask)

    return ImageTk.PhotoImage(circular_image)

def main():'''

root = Tk()
root.geometry("500x500")
frame = Frame(root, highlightbackground="black", highlightthickness=2, bd=2)
frame.pack(expand=TRUE, fill=BOTH)


image_path = r"C:\Users\Acer\Pictures\bus.png"
image = PhotoImage(file=image_path)
 



desired_width = 100
desired_height = 50

'''canvas = Canvas(frame, width= desired_width, height= desired_height, bg='#4aa9ed')
canvas.pack()

canvas.create_image(30, 0, anchor=NW, image=image)'''



resized_image = image.subsample(int(image.width()/desired_width), int(image.height()/desired_height))

label = Label(frame, bg='#4aa9ed',  width=desired_width, height=desired_height, image = resized_image, anchor=W)
label.pack(side = TOP, expand=False, fill=BOTH)
label.pack_propagate(False)
label.pack()

button = Button(label, text='sign up',bg='blue' ,font='bold')
button.pack( side=RIGHT, padx=(30,0)) 


b3_button=Button(label, text="contact us", font="bold")
b3_button.pack(side=RIGHT)
b2_button = Button(label, text="about us", font="bold")
b2_button.pack(side=RIGHT, padx=(0,30))

button = Button(label, text="service", font="bold")
button.pack(side=RIGHT, padx=(0,30))
 
f = Frame(frame, width= 500, height=500, highlightbackground="black", highlightthickness=2, bd=0)
f.pack( side= RIGHT, fill=Y)

custom_font= ("Helvetica", 14)

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

image_path_2= r"C:\Users\Acer\Pictures\hhhhh.png"
image = PhotoImage(file = image_path_2)

g = Frame(frame, width=500, height=500, highlightbackground="black", highlightthickness=2)
g.pack(expand=TRUE, fill=BOTH)

 

rrr = Label(g, image=image)
rrr.pack()

#white_circle = label.create_oval(4, 8, 140, 133, fill="black")

'''r = Frame(frame, height= =highlightthickness=1, highlightbackground='BLACK')
r.pack()'''
root.mainloop()

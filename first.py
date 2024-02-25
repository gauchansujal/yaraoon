from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

root = Tk()
root.geometry("1200x1000")

frame = Frame(root, highlightbackground="black", highlightthickness=2, bd=2)
frame.pack(expand=TRUE, fill=BOTH)


image_path = r"./logo.png"
image = PhotoImage(file = image_path)

desired_width = 100
desired_height = 75

resized_image = image.subsample(int(image.width()/desired_width), int(image.height()/desired_height))

label = Label(frame, bg='#4aa9ed',  width=desired_width, height=100, image = resized_image, anchor=W)
label.pack(side = TOP, expand=False, fill=BOTH)
label.pack_propagate(False)
label.pack(pady=7)

def login2():
    root.destroy()
    import Login
    

button = Button(label, text="sign in",height=10,width=15,bg="#0094FF",cursor = "hand2",font=('Inter',10,"bold"),command=login2)
button.pack(side=RIGHT,pady=25)


def popup(): 
    messagebox.showinfo("contac us", "987635925924")
b3_button=Button(label, text="contact us",height=10,width=15, bg="#D3D3D3",cursor = " hand2",font=('Inter',10,"bold"), command=popup)
b3_button.pack(side=RIGHT,  padx=(0,30),pady=25)

def aboutus_popup():
    messagebox.showinfo("About Us","we are bus travel")
b2_button = Button(label, text="about us", height=10,width=15,bg="#D3D3D3",cursor = "  hand2",font=('Inter',10,"bold"),command=aboutus_popup)
b2_button.pack(side=RIGHT, padx=(0,30),pady=25)

def service_showinfo():
    messagebox.showinfo("Service","We provide the best services for you")
button = Button(label, text="service",height=10,width=15, bg="#D3D3D3",cursor = "  hand2",font=('Inter',10,"bold"), command=service_showinfo)
button.pack(side=RIGHT, padx=(0,30),pady=25)

f = Frame(frame, width= 500, height=500, highlightbackground="black", highlightthickness=2, bd=0)
f.pack( side= RIGHT, fill=Y)

custom_font= ("Helvetica", 20)

#----------------------text-box----------------------------------------------------

b4 = Label(f, text="leaving from ?", font=custom_font)
b4.grid(row=0, column=0, padx=20, pady=22)

leaving=['Kathmandu','Pokhara','Birgunj','Biratnagar','Dhangadi','Bhairawa','Chitwan',]
b4_entry = ttk.Combobox(f, values=leaving,width=25, height=10)
b4_entry.set('Leaving from?')
b4_entry.grid( row=1, column=0, padx=40, pady=20)


#-------------------------------------------second-text-box---------------------------------

b5 = Label(f, text="going destination", font=custom_font)
b5.grid(row=2, column=0, padx=40, pady=20)

destination=['Pokhara','Birgunj','Biratnagar','Dhangadi','Bhairawa','Chitwan','Kathmandu']
b5_entry = ttk.Combobox(f,values=destination,width=25, height=10)
b5_entry.set('choose your destination')
b5_entry.grid(row=3, column=0, padx=40, pady=20)


#-------------------------------------------date-time-text-box---------------------------------

b6 = Label(f, text="Travel Date", font=custom_font)
b6.grid(row=4, column=0, padx=40, pady=20)

#datebutton
date=['2024/2/24','2024/2/25','2024/2/26','2024/2/27','2024/2/28','2024/2/29','2024/3/01','2024/3/02']
b6_entry = ttk.Combobox(f, values=date, width=25, height=10, font=20)
b6_entry.set('            -------Date-------')
b6_entry.grid(row=5, column=0, padx=40, pady=10)  

def search():
    leaving_from = b4_entry.get()
    going_destination = b5_entry.get()
    travel_date = b6_entry.get()

    if leaving_from == 'Leaving from?' or going_destination == 'Choose your destination' or travel_date == '            -------Date-------':
        messagebox.showerror("Error", "Please select valid options for Leaving from, Destination, and Travel Date.")
    elif leaving_from == going_destination:
        messagebox.showerror("Error", "Please choose different options for Leaving from and Destination.")
    else:
        result = messagebox.askyesno('', "Are you sure you want to choose this route?")
        if result:
            print("User clicked yes")

            # Insert data into the database
            connection = mysql.connector.connect(
                host='localhost',
                user='pma',
                password='Yug12345',
                database='route_management'
            )

            cursor = connection.cursor()

            # Use a try-except block to handle potential errors
            try:
                insert_query = "INSERT INTO routes (leaving_from, going_destination, travel_date) VALUES (%s, %s, %s)"
                data = (leaving_from, going_destination, travel_date)
                cursor.execute(insert_query, data)
                connection.commit()
                messagebox.showinfo("Success", "Route selected successfully!")
            except mysql.connector.Error as error:
                messagebox.showerror("Error", f"Failed to insert route into the database: {error}")
            finally:
                cursor.close()
                connection.close()

            root.destroy()
            import bus
        else:
            print("User clicked no")

   
b7 = Button(f, text="search Buses", background="#4aa9ed", fg="black", width=10, font=custom_font,command=search)
b7.grid(row=7, column=0, padx=0, pady=40)

image_path_2= r"bus.png"
image = PhotoImage(file = image_path_2)

g = Frame(frame, width=500, height=500, highlightbackground="black", highlightthickness=2)
g.pack(expand=TRUE, fill=BOTH)



rrr = Label(g, image=image)
rrr.pack()

root.mainloop()

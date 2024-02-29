from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector


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
    messagebox.showinfo("contac us", "Please get in touch with us right away if you have any issues with this app. Contact us at\n +977 985511133.")
b3_button=Button(label, text="contact us",height=10,width=15, bg="#D3D3D3",cursor = " hand2",font=('Inter',10,"bold"), command=message_popup)
b3_button.pack(side=RIGHT,  padx=(0,30),pady=25)

def aboutus_popup():
    messagebox.showinfo("About Us","We are travel bus; we are the first travel agency in Nepal where you may purchase a ticket to reserve a bus and travel at an affordable price throughout Nepal. By offering practical and reasonably priced bus reservation services, Travel Bus is transforming the travel sector in Nepal and facilitating individuals' exploration of the natural beauty of our nation.")
b2_button = Button(label, text="about us", height=10,width=15,bg="#D3D3D3",cursor = "  hand2",font=('Inter',10,"bold"),command=aboutus_popup)
b2_button.pack(side=RIGHT, padx=(0,30),pady=25)

def service_showinfo():
    messagebox.showinfo("Service","At Travel Bus, we take pride in offering the best bus reservation service in Nepal. Our software is designed to cater to the needs of both locals and visitors, providing a seamless and convenient way to schedule buses for their travels across the country.")
button = Button(label, text="service",height=10,width=15, bg="#D3D3D3",cursor = "  hand2",font=('Inter',10,"bold"), command=service_showinfo)
button.pack(side=RIGHT, padx=(0,30),pady=25)

f = Frame(frame, width= 500, highlightbackground="black",highlightthickness=2, bd=2,height=500,bg="#53D3D1")
f.pack( side= RIGHT, fill=Y)

custom_font= ("poppins", 20)

#----------------------datastorage-------------------------------------------------

#date
def on_date_select(event):
    selected_date = b6_entry.get()
    save_selected_date(selected_date)

def save_selected_date(selected_date):
    with open("selected_date.txt", "w") as file:
        file.write(selected_date)

#leaving
def on_leave_select(event):
    selected_leave = b4_entry.get()
    save_selected_leave(selected_leave)

def save_selected_leave(selected_leave):
    with open("leaving.txt", "w") as file:
        file.write(selected_leave)

#destination
def on_dest_select(event):
    selected_dest = b5_entry.get()
    save_selected_dest(selected_dest)

def save_selected_dest(selected_dest):
    with open("destination.txt", "w") as file:
        file.write(selected_dest)

#----------------------text-box----------------------------------------------------

b4 = Label(f, text="leaving from ?", bg="#53D3D1",font=custom_font, width=30, height=2)
b4.grid(row=0, column=0, padx=20)

leaving=['Kathmandu','Pokhara','Birgunj','Biratnagar','Dhangadi','Bhairawa','Chitwan',]
b4_entry = ttk.Combobox(f, values=leaving,width=25, height=20,state="readonly")
b4_entry.set('Leaving from?')
b4_entry.grid( row=1, column=0, padx=40)

b4_entry.bind("<<ComboboxSelected>>", on_leave_select)

#-------------------------------------------second-text-box---------------------------------

b5 = Label(f, text="going destination",bg="#53D3D1", font=custom_font, width=30, height=2)
b5.grid(row=2, column=0, padx=40)

destination=['Pokhara','Birgunj','Biratnagar','Dhangadi','Bhairawa','Chitwan','Kathmandu']
b5_entry = ttk.Combobox(f,values=destination,width=25, height=25,state="readonly")
b5_entry.set('choose your destination')

b5_entry.grid(row=3, column=0, padx=40)

b5_entry.bind("<<ComboboxSelected>>", on_dest_select)

#-------------------------------------------date-time-text-box---------------------------------

b6= Label(f, text="Travel Date",bg="#53D3D1",font=custom_font, width=30, height=2)
b6.grid(row=4, column=0, padx=40)

#datebutton
date=['2024/2/24','2024/2/25','2024/2/26','2024/2/27','2024/2/28','2024/2/29','2024/3/01','2024/3/02']
b6_entry = ttk.Combobox(f, values=date, width=25, height=10, font=20,state="readonly")
b6_entry.set('            -------Date-------')
b6_entry.grid(row=5, column=0, padx=40)  

b6_entry.bind("<<ComboboxSelected>>", on_date_select)


#-------database--------
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
            import second
        else:
            print("User clicked no")


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

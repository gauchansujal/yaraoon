from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

# Create a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="pma",
    password="Yug12345",
    database="travel_bus_payment"
)
cursor = conn.cursor()

# Execute the SQL code to create a 'payment_info' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS payment_info (
        id INT AUTO_INCREMENT PRIMARY KEY,
        phone_number VARCHAR(20) NOT NULL,
        password VARCHAR(100) NOT NULL,
        payment_value DECIMAL(10,2) NOT NULL
    )
''')

# Function to be called when the confirm button is clicked
def boarding_pass():
    phone_number = khalti_entry.get("1.0", "end-1c")
    password = khalti_password_entry.get("1.0", "end-1c")
    payment_value_str = khalit_payment_entry.get("1.0", "end-1c")

    # Check if any of the fields are blank
    if not phone_number or not password or not payment_value_str:
        messagebox.showwarning("Warning", "Please fill in all the fields.")
        return

    # Check if payment_value is a valid integer
    try:
        payment_value = int(payment_value_str)
    except ValueError:
        messagebox.showwarning("Warning", "Payment value must be a valid integer.")
        return

    # Check if payment_value is not less than 1000
    if payment_value < 1000:
        messagebox.showwarning("Warning", "Payment value must be at least 1000.")
        return

    # Insert the payment information into the database
    cursor.execute("INSERT INTO payment_info (phone_number, password, payment_value) VALUES (%s, %s, %s)",
                   (phone_number, password, payment_value))
    conn.commit()

    result = messagebox.askokcancel("Confirmation", "Are you sure you want to proceed?")
    if result:
        print("User clicked OK")
        root.destroy()
        import boarding_pass
    else:
        print("User clicked Cancel")

root = Tk()

root.geometry("1200x1000")



frame = Frame(root, bg="#53D3D1", highlightbackground="black", highlightthickness=2, bd=2,height=100)
frame.pack(expand=TRUE, fill=BOTH)


image_path = r"logo.png"
image= PhotoImage(file = image_path)
 

desired_width = 100
desired_height = 50

resized_image = image.subsample(int(image.width()/desired_width), int(image.height()/desired_height))


label = Label(frame, bg="#53D3D1",  width=desired_width, height=100, image = resized_image, anchor=W)
label.pack(side = TOP, expand=False, fill=BOTH)
label.pack_propagate(False)
label.pack(pady=7)

def login2():
    root.destroy()
    import Login
    

button = Button(label, text="sign in",height=10,width=15,bg="#0094FF",cursor = "hand2",font=('poppins',10,"bold"),command=login2)
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


#--------------------------------------creating khalti frame-----------------------------------------------------------------------------

khalti_frame = Frame(frame, bg="#53D3D1", height=100)
khalti_frame.pack(expand=TRUE, fill=BOTH)

image_khalti = PhotoImage(file="khalti1.png")

desired_1width=100
desired_1height=50


x_1subsample_factor = max(int(image_khalti.width()/desired_1width), 1)
y_1subsample_factor = max(int(image_khalti.height()/desired_1height), 1)

resized_1image = image_khalti.subsample(x_1subsample_factor, y_1subsample_factor)

khalti_label = Label(khalti_frame, bg="white",  width=desired_width, height=75, image=resized_1image,anchor=W)
khalti_label.pack(side = TOP, expand=False, fill=BOTH,padx=10)

khalti_2label = Label(khalti_frame ,bg="#5C2E91",  width=desired_width, height=2, text="Please Pay Here.",font=("Poppins", 20,"bold"),fg="white", anchor=CENTER)
khalti_2label.pack(side = TOP, expand=False, fill=BOTH,padx=10)


khaltilabel = Label(khalti_frame, bg="#53D3D1",  width=desired_width, height=500, anchor=CENTER)
khaltilabel.pack(side = TOP, expand=False, fill=Y,padx=10)

fonepay = Label(khaltilabel,bg="#53D3D1")
fonepay.grid(row=3,column=3, padx=40, pady=20)


def temp_1sttext(e):
    khalti_entry.delete(1.0, "end-1c")
khalti_entry = Text(fonepay, width=30, height=2,highlightbackground="#5C2E91",highlightthickness=2, bd=2)
khalti_entry.grid(row=3, column=6, padx=40, pady=20)
khalti_entry.insert(1.0,"Enter phone number")
khalti_entry.bind("<FocusIn>",temp_1sttext)


def temp_2ndtext(e):
    khalti_password_entry.delete(1.0, "end-1c")
khalti_password_entry= Text(fonepay, width=30, height=2,highlightbackground="#5C2E91",highlightthickness=2, bd=2)
khalti_password_entry.grid(row=3, column=9, padx=40, pady=20)
khalti_password_entry.insert(1.0,"Enter your your password")
khalti_password_entry.bind("<FocusIn>",temp_2ndtext)

def temp_3rdtext(e):
    khalit_payment_entry.delete(1.0, "end-1c")
khalit_payment_entry= Text(fonepay, width=30, height=2,highlightbackground="#5C2E91",highlightthickness=2, bd=2)
khalit_payment_entry.grid(row=3, column=12 , padx=40, pady=20)
khalit_payment_entry.insert(1.0,"Enter value")
khalit_payment_entry.bind("<FocusIn>",temp_3rdtext)



esewa_4label = Label(khalti_frame, bg="#53D3D1", width=desired_1width, height=2, text="Please don’t forget to write your name in remarks.", font=("Poppins", 20, "bold"), fg="black")
esewa_4label.pack(side=TOP, expand=False, fill=BOTH, padx=10)


#----------------creating update buttons------------------------------------
buttons_label = Label(khalti_frame, bg="#53D3D1",  width=desired_width, height=75,anchor=CENTER)
buttons_label.pack(side = TOP,padx=10)
#------------------------creating esewa button--------------------------------
def esewa_payment():
    result=messagebox.askokcancel("payment","Are you sure you ?")
    if result:
        print("User clicked OK")
        root.destroy()
        import esewa
             
    else:
        print("User clicked Cancel")

    
image_esewa = PhotoImage(file="esewa.png")

esewa_button = Button(buttons_label, bg="#FBECEB", image=image_esewa, width=150,height=75,fg='black',pady=10,compound=LEFT,command=esewa_payment)
esewa_button.pack(side=LEFT)
#--------------------------------creating message------------------------------
or_message=Message(buttons_label,text="OR",font=('poppins',14,"bold"),bg="#53D3D1",fg='black')
or_message.pack(side=LEFT)
#-----------------------creating update button for fonepay---------------------
def fonepay_payment():
    result=messagebox.askokcancel("payment","Are you sure you ?")
    if result:
        print("User clicked OK")
        root.destroy()
        import fonepay
    else:
        print("User clicked Cancel")

image_fonepay= PhotoImage(file="fonepay.png")
fonepay_button=Button(buttons_label,bg="white",image=image_fonepay, width=150,height=75,fg='black', pady=10,command=fonepay_payment)
fonepay_button.pack(side=LEFT,pady=10)

#-------------------------------creating conformation button--------------------------------



confrim_button=Button(buttons_label,bg="#FBECEB",text="CONFRIM", width=15,height=3,fg='black', font=("Poppins", 14,"bold"),command=boarding_pass)
confrim_button.pack(side=RIGHT,padx=(150,0))
root.mainloop()
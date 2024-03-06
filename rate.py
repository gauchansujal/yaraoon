from tkinter import *
from tkinter import messagebox

class StarRating(Frame):
    def __init__(self, master=None, num_stars=5):
        super().__init__(master, bg="#53D3D1")  # Set background color for the frame
        self.num_stars = num_stars
        self.rating = 0
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        heading_label = Label(self, text="Give Rating", font=("Arial", 20), bg="#53D3D1")
        heading_label.grid(row=0, column=0, columnspan=self.num_stars, pady=(10, 20))

        self.stars = []
        for i in range(1, self.num_stars + 1):
            star_button = Button(self, text="★", font=("Arial", 30),
                                  command=lambda i=i: self.on_star_click(i), bg="#53D3D1", border=0)
            star_button.grid(row=1, column=i-1, padx=3, pady=20)

            self.stars.append(star_button)

        submit_button = Button(self, text="Submit", command=self.submit_rating, height=3, width=10,
                               bg="green", fg="#000000")  # Red background, black text
        submit_button.grid(row=2, column=0, columnspan=self.num_stars, pady=(6, 2))

    def on_star_click(self, rating):
        self.rating = rating
        for i, star in enumerate(self.stars):
            if i < rating:
                star.config(fg="orange")  # Highlighted star
            else:
                star.config(fg="black")   # Unhighlighted star

    def submit_rating(self):
        messagebox.showinfo("Thank You!", f"Thank you for your feedback. You rated {self.rating} stars.")
        root.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Star Rating System")

    # Set window background color
    root.configure(bg="#53D3D1")

    # Set window size and position
    window_width = 500
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Make the window unresizable
    root.resizable(width=False, height=False)

    star_rating = StarRating(root, num_stars=5)

root.mainloop()

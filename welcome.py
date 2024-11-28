"""
Project : robot for devoteam
Module : intership test
Author : Ryan BERSIER
Start date: 28.11.24
Latest update: 08.10.24
Version : 0.1
"""

# Library
from tkinter import *
from tkinter import messagebox
import grid


def validate_input(value):
    try:
        number = int(value)
        if number < 0 or number > 10:
            raise ValueError
        return number
    except ValueError:
        return None


def submit_dimensions():
    wide_value = wide_entry.get()
    deep_value = deep_entry.get()

    wide = validate_input(wide_value)
    deep = validate_input(deep_value)

    if wide is None or deep is None:
        messagebox.showerror("Invalid Input", "Please enter numbers between 0 and 10 for both dimensions and don't send float numbers")
    else:
        home_page.destroy()
        grid.grid_page(wide, deep)



def welcome_page():
    global wide_entry, deep_entry, home_page
    # Create the window
    home_page = Tk()
    home_page.title("Welcome Page")
    height = 250
    width = 400
    home_page.geometry(f"{width}x{height}")

    # Background color.
    home_page.configure(background="grey")

    # Frame
    labelFrame = Frame(home_page, bg="grey")
    entryFrame = Frame(home_page, bg="grey")
    buttonFrame = Frame(home_page, bg="grey")

    labelFrame.pack(side=TOP, pady=10)
    entryFrame.pack(side=TOP, pady=10)
    buttonFrame.pack(side=TOP, pady=10)

    # Label
    lblWelcome = Label(labelFrame, text="Welcome to the Robot Controller", font=("Arial", 16), bg="grey")
    lblask = Label(labelFrame, text="Can you give me the dimensions of your grid please?", font=("Arial", 12), bg="grey")

    lblWelcome.pack(side=TOP)
    lblask.pack(side=TOP)

    # Entry labels and fields
    lblWide = Label(entryFrame, text="Wide (0-10):", font=("Arial", 12), bg="grey")
    lblDeep = Label(entryFrame, text="Deep (0-10):", font=("Arial", 12), bg="grey")

    wide_entry = Entry(entryFrame, font=("Arial", 12))
    deep_entry = Entry(entryFrame, font=("Arial", 12))

    lblWide.grid(row=0, column=0, padx=5, pady=5)
    wide_entry.grid(row=0, column=1, padx=5, pady=5)
    lblDeep.grid(row=1, column=0, padx=5, pady=5)
    deep_entry.grid(row=1, column=1, padx=5, pady=5)

    # Submit button
    btnSubmit = Button(buttonFrame, text="Submit", font=("Arial", 12), command=submit_dimensions)
    btnSubmit.pack(pady=10)

    # Launch window
    home_page.mainloop()


if __name__ == "__main__":
    welcome_page()
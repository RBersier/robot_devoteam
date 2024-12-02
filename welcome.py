"""
Project : robot for devoteam
Module : intership test
Author : Ryan BERSIER
Start date: 28.11.24
Latest update: 28.11.24
Version : 0.1
"""

from tkinter import *
from tkinter import messagebox
import grid

def validate_input(value):
    try:
        number = int(value)
        if number < 1 or number > 9:
            raise ValueError
        return number
    except ValueError:
        return None

def validate_position(x, y, wide, deep):
    try:
        x = int(x)
        y = int(y)
        if x < 0 or x > wide or y < 0 or y > deep:
            raise ValueError
        return x, y
    except ValueError:
        return None, None

def validate_polar(polar):
    if polar in ["N", "E", "S", "W"]:
        return polar
    return None

def submit_dimensions():
    wide_value = wide_entry.get()
    deep_value = deep_entry.get()
    x_value = x_entry.get()
    y_value = y_entry.get()
    polar_value = polar_entry.get()

    wide = validate_input(wide_value)
    deep = validate_input(deep_value)

    if wide is None or deep is None:
        messagebox.showerror("Invalid Input", "Please enter numbers between 1 and 9 for both dimensions and don't send float numbers")
        return

    x, y = validate_position(x_value, y_value, wide, deep)
    if x is None or y is None:
        messagebox.showerror("Invalid Position", "Please ensure x and y are within grid bounds and not negative.")
        return

    polar = validate_polar(polar_value)
    if polar is None:
        messagebox.showerror("Invalid Direction", "Polar must be one of the following: N, E, S, W.")
        return

    home_page.destroy()
    grid.grid_page(wide, deep, x-1, y-1, polar)

def welcome_page():
    global wide_entry, deep_entry, x_entry, y_entry, polar_entry, home_page
    # Create the window
    home_page = Tk()
    home_page.title("Welcome Page")
    height = 400
    width = 400
    home_page.geometry(f"{width}x{height}")

    # Background color.
    home_page.configure(background="grey")

    # Frame
    labelFrame = Frame(home_page, bg="grey")
    dimensionFrame = Frame(home_page, bg="grey")
    questionFrame = Frame(home_page, bg="grey")
    positionFrame = Frame(home_page, bg="grey")
    buttonFrame = Frame(home_page, bg="grey")

    labelFrame.pack(side=TOP, pady=10)
    dimensionFrame.pack(side=TOP, pady=10)
    questionFrame.pack(side=TOP, pady=10)
    positionFrame.pack(side=TOP, pady=10)
    buttonFrame.pack(side=TOP, pady=10)

    # Label
    lblWelcome = Label(labelFrame, text="Welcome to the Robot Controller", font=("Arial", 16), bg="grey")
    lblask = Label(labelFrame, text="Can you give me the dimensions of your grid please?", font=("Arial", 12), bg="grey")

    lblWelcome.pack(side=TOP)
    lblask.pack(side=TOP)

    # Entry labels and fields
    lblWide = Label(dimensionFrame, text="Wide (1-9):", font=("Arial", 12), bg="grey")
    lblDeep = Label(dimensionFrame, text="Deep (1-9):", font=("Arial", 12), bg="grey")

    wide_entry = Entry(dimensionFrame, font=("Arial", 12))
    deep_entry = Entry(dimensionFrame, font=("Arial", 12))

    lblWide.grid(row=0, column=0, padx=5, pady=5)
    wide_entry.grid(row=0, column=1, padx=5, pady=5)
    lblDeep.grid(row=1, column=0, padx=5, pady=5)
    deep_entry.grid(row=1, column=1, padx=5, pady=5)

    lblposition = Label(questionFrame, text="Can you give me the position of your robot?", font=("Arial", 12), bg="grey")
    lblposition.pack(side=TOP)

    lblx = Label(positionFrame, text="x:", font=("Arial", 12), bg="grey")
    lbly = Label(positionFrame, text="y:", font=("Arial", 12), bg="grey")
    lblpolar = Label(positionFrame, text="Polar (N, E, S, W):", font=("Arial", 12), bg="grey")

    x_entry = Entry(positionFrame, font=("Arial", 12))
    y_entry = Entry(positionFrame, font=("Arial", 12))
    polar_entry = Entry(positionFrame, font=("Arial", 12))

    lblx.grid(row=2, column=0, padx=5, pady=5)
    x_entry.grid(row=2, column=1, padx=5, pady=5)
    lbly.grid(row=3, column=0, padx=5, pady=5)
    y_entry.grid(row=3, column=1, padx=5, pady=5)
    lblpolar.grid(row=4, column=0, padx=5, pady=5)
    polar_entry.grid(row=4, column=1, padx=5, pady=5)

    # Submit button
    btnSubmit = Button(buttonFrame, text="Submit", font=("Arial", 12), command=submit_dimensions)
    btnSubmit.pack(pady=10)

    # Launch window
    home_page.mainloop()

if __name__ == "__main__":
    welcome_page()
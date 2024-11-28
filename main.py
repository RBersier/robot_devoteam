"""
Project : robot for devoteam
Module : intership test
Author : Ryan BERSIER
Start date: 28.11.24
Latest update: 08.10.24
Version : 0.1
"""

# librairy
from tkinter import *

def welcome_page():
    # Create the window
    home_page = Tk()
    home_page.title("Welcome page")
    height = 200
    width = 250
    home_page.geometry(f"{width}x{height}")

    # Background color.
    home_page.configure(background="grey")

    # Frame
    labelFrame = Frame(home_page, bg="grey")
    entryFrame = Frame(home_page, bg="grey")

    labelFrame.pack(side=TOP, pady=10)
    entryFrame.pack(side=TOP, pady=10)

    # Label
    lblWelcome = Label(labelFrame, text="Welcome to the Robot Controller", font=("Arial", 15))
    lblask = Label(labelFrame, text="", )


    # Entry

    # Launch window.
    home_page.mainloop()

if __name__ == "__main__":
    welcome_page()
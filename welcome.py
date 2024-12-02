"""
Project : robot for devoteam
Module : intership test
Author : Ryan BERSIER
Start date: 28.11.24
Latest update: 2.12.24
Version : 0.3
"""
from tkinter import *
from tkinter import messagebox
import grid


def validate_input(value):
    """
    Validates that the input is an integer between 1 and 9.

    :param value: Input value to validate.
    :return: The validated integer or None if invalid.
    """
    try:
        number = int(value)
        if number < 1 or number > 9:
            raise ValueError
        return number
    except ValueError:
        return None


def validate_position(x, y, width, depth):
    """
    Validates that the position (x, y) is within the grid boundaries.

    :param x: X-coordinate of the position.
    :param y: Y-coordinate of the position.
    :param width: Width of the grid.
    :param depth: Depth of the grid.
    :return: A tuple (x, y) or (None, None) if invalid.
    """
    try:
        x = int(x)
        y = int(y)
        if x < 0 or x > width or y < 0 or y > depth:
            raise ValueError
        return x, y
    except ValueError:
        return None, None


def validate_polar(polar):
    """
    Validates that the polar direction is one of 'N', 'E', 'S', or 'W'.

    :param polar: Input polar direction.
    :return: The validated polar direction or None if invalid.
    """
    if polar in ["N", "E", "S", "W"]:
        return polar
    return None


def submit_dimensions():
    """
    Handles the submission of grid dimensions and robot position. Validates the inputs and switches to the grid page.
    """
    width_value = width_entry.get()
    depth_value = depth_entry.get()
    x_value = x_entry.get()
    y_value = y_entry.get()
    polar_value = polar_entry.get().upper()

    width = validate_input(width_value)
    depth = validate_input(depth_value)

    if width is None or depth is None:
        messagebox.showerror("Invalid Input", "Please enter numbers between 1 and 9 for both dimensions. Do not use float numbers.")
        return

    x, y = validate_position(x_value, y_value, width, depth)
    if x is None or y is None:
        messagebox.showerror("Invalid Position", "Please ensure x and y are within grid bounds and not negative.")
        return

    polar = validate_polar(polar_value)
    if polar is None:
        messagebox.showerror("Invalid Direction", "Polar must be one of the following: N, E, S, W.")
        return

    home_page.destroy()
    grid.display_grid_page(width, depth, x-1, y-1, polar)


def welcome_page():
    """
    Initializes and displays the welcome page for the application.
    """
    global width_entry, depth_entry, x_entry, y_entry, polar_entry, home_page

    # Create the main window
    home_page = Tk()
    home_page.title("Welcome Page")
    height = 400
    width = 400
    home_page.geometry(f"{width}x{height}")

    # Set background color
    home_page.configure(background="grey")

    # Create frames
    label_frame = Frame(home_page, bg="grey")
    dimension_frame = Frame(home_page, bg="grey")
    question_frame = Frame(home_page, bg="grey")
    position_frame = Frame(home_page, bg="grey")
    button_frame = Frame(home_page, bg="grey")

    label_frame.pack(side=TOP, pady=10)
    dimension_frame.pack(side=TOP, pady=10)
    question_frame.pack(side=TOP, pady=10)
    position_frame.pack(side=TOP, pady=10)
    button_frame.pack(side=TOP, pady=10)

    # Add labels
    lbl_welcome = Label(label_frame, text="Welcome to the Robot Controller", font=("Arial", 16), bg="grey")
    lbl_ask = Label(label_frame, text="Can you give me the dimensions of your grid, please?", font=("Arial", 12), bg="grey")

    lbl_welcome.pack(side=TOP)
    lbl_ask.pack(side=TOP)

    # Add dimension input fields
    lbl_width = Label(dimension_frame, text="Width (1-9):", font=("Arial", 12), bg="grey")
    lbl_depth = Label(dimension_frame, text="Depth (1-9):", font=("Arial", 12), bg="grey")

    width_entry = Entry(dimension_frame, font=("Arial", 12))
    depth_entry = Entry(dimension_frame, font=("Arial", 12))

    lbl_width.grid(row=0, column=0, padx=5, pady=5)
    width_entry.grid(row=0, column=1, padx=5, pady=5)
    lbl_depth.grid(row=1, column=0, padx=5, pady=5)
    depth_entry.grid(row=1, column=1, padx=5, pady=5)

    # Add position input fields
    lbl_position = Label(question_frame, text="Can you give me the position of your robot?", font=("Arial", 12), bg="grey")
    lbl_position.pack(side=TOP)

    lbl_x = Label(position_frame, text="x:", font=("Arial", 12), bg="grey")
    lbl_y = Label(position_frame, text="y:", font=("Arial", 12), bg="grey")
    lbl_polar = Label(position_frame, text="Polar (N, E, S, W):", font=("Arial", 12), bg="grey")

    x_entry = Entry(position_frame, font=("Arial", 12))
    y_entry = Entry(position_frame, font=("Arial", 12))
    polar_entry = Entry(position_frame, font=("Arial", 12))

    lbl_x.grid(row=2, column=0, padx=5, pady=5)
    x_entry.grid(row=2, column=1, padx=5, pady=5)
    lbl_y.grid(row=3, column=0, padx=5, pady=5)
    y_entry.grid(row=3, column=1, padx=5, pady=5)
    lbl_polar.grid(row=4, column=0, padx=5, pady=5)
    polar_entry.grid(row=4, column=1, padx=5, pady=5)

    # Add submit button
    btn_submit = Button(button_frame, text="Submit", font=("Arial", 12), command=submit_dimensions)
    btn_submit.pack(pady=10)

    # Start the main event loop
    home_page.mainloop()


if __name__ == "__main__":
    welcome_page()

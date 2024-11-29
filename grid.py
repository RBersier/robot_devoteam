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

def grid_page(x, y):
    global gridFrame, orderFrame, windowGrid, entryOrder, rows, cols
    # Create the window
    windowGrid = Tk()
    windowGrid.title("Grid Page")
    height = x*110
    width = y*90
    if x <= 4:
        height = height + 100
    if y <= 2:
        width = width + 100
    windowGrid.geometry(f"{width}x{height}")

    # Background color.
    windowGrid.configure(background="grey")

    # Frames
    textFrame = Frame(windowGrid, bg="grey")
    gridFrame = Frame(windowGrid, bg="grey")
    orderFrame = Frame(windowGrid, bg="grey")

    textFrame.pack(side=TOP, pady=10)
    gridFrame.pack(side=TOP, pady=10)
    orderFrame.pack(side=TOP, pady=10)

    lbltitle = Label(textFrame, text="🤖 The robot grid 🤖", font=("Arial", 16), bg="grey")
    lbltitle.pack(side=TOP)

    entryOrder = Entry(orderFrame, font=("Arial", 12))
    btnOrder = Button(orderFrame, text="Submit", font=("Arial", 12), command=mouvement)

    entryOrder.pack(side=LEFT, padx=5)
    btnOrder.pack(side=LEFT, padx=5)

    rows, cols = x, y  # Grid size
    grid_tile(gridFrame, rows, cols)


def grid_tile(gridFrame, x, y):
    global tiles
    # Store tiles in a list for easy access
    tiles = []

    # Create all the tiles
    for i in range(x):
        row = []
        for j in range(y):
            # Each "tile" is a Label with a border
            tile = Label(gridFrame, text=f"({i},{j})", borderwidth=2, relief="solid", width=10, height=5, bg="white")
            tile.grid(row=i, column=j)
            row.append(tile)
        tiles.append(row)

    # Add the robot at the center position
    for i in range(x):
        for j in range(y):
            if not tiles[i][j] == "🤖":
                centerX, centerY = x // 2, y // 2
                tiles[centerX][centerY].configure(text="🤖", bg="lightblue")


def mouvement():
    order_value = entryOrder.get()
    separated_letters = list(order_value)
    side = 0

    # Define direction mapping
    directions = {
        0: ("N", (-1, 0)),
        1: ("E", (0, 1)),
        2: ("S", (1, 0)),
        3: ("W", (0, -1))
    }

    # Define the starting position
    pos_x, pos_y = rows // 2, cols // 2

    for letter in separated_letters:
        letter = letter.upper()

        if letter not in ["L", "F", "R"]:
            messagebox.showerror("Invalid Input", "Only 3 letters are available (L = Left, F = Front, R = Right)")
            return

        if letter == "L":
            side = (side + 1) % 4
        elif letter == "R":
            side = (side - 1) % 4
        elif letter == "F":
            _, (dx, dy) = directions[side]
            pos_x += dx
            pos_y += dy

        # Check for grid boundaries
        pos_x = max(0, min(rows - 1, pos_x))
        pos_y = max(0, min(cols - 1, pos_y))

        # Reinitialize the grid
        grid_tile(gridFrame, rows, cols)

        # Update the tiles
        for i in range(rows):
            for j in range(cols):
                tiles[i][j].configure(text=f"({i},{j})", bg="white")
        tiles[pos_x][pos_y].configure(text="🤖", bg="lightblue")

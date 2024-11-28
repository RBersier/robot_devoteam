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

def grid_page(x, y):
    global gridFrame, orderFrame, windowGrid
    # Create the window
    windowGrid = Tk()
    windowGrid.title("Grid Page")
    height = x*100
    width = y*100
    windowGrid.geometry(f"{width}x{height}")

    # Background color.
    windowGrid.configure(background="grey")

    # Frames
    gridFrame = Frame(windowGrid, bg="grey")
    orderFrame = Frame(windowGrid, bg="grey")

    gridFrame.pack(side=TOP, pady=10)
    orderFrame.pack(side=TOP, pady=10)
    rows, cols = x, y  # Grid size
    grid_tile(gridFrame, rows, cols)


def grid_tile(grid_frame, x, y):
    # Store tiles in a list for easy access
    tiles = []

    # Create all the tiles
    for i in range(x):
        row = []
        for j in range(y):
            # Each "tile" is a Label with a border
            tile = Label(grid_frame, text=f"({i},{j})", borderwidth=2, relief="solid", width=10, height=5, bg="white")
            tile.grid(row=i, column=j)
            row.append(tile)
        tiles.append(row)

    # Add the robot at the center position (or any desired position)
    center_x, center_y = x // 2, y // 2
    tiles[center_x][center_y].configure(text="🤖", bg="lightblue")




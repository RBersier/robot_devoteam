"""
Project : robot for devoteam
Module : intership test
Author : Ryan BERSIER
Start date: 28.11.24
Latest update: 29.11.24
Version : 0.2
"""
# Library
from tkinter import *
from tkinter import messagebox

def grid_page(x, y):
    global gridFrame, orderFrame, windowGrid, entryOrder, rows, cols, room_size, start_position
    # Create the window
    windowGrid = Tk()
    windowGrid.title("Grid Page")
    height = x * 110
    width = y * 90
    if x <= 4:
        height += 100
    if y <= 2:
        width += 100
    windowGrid.geometry(f"{width}x{height}")

    # Background color
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
    btnOrder = Button(orderFrame, text="Submit", font=("Arial", 12), command=submit_commands)

    entryOrder.pack(side=LEFT, padx=5)
    btnOrder.pack(side=LEFT, padx=5)

    rows, cols = x, y  # Grid size
    room_size = (x, y)
    start_position = (x // 2, y // 2, 'N')  # Default starting position
    grid_tile(gridFrame, rows, cols, start_position)

def grid_tile(gridFrame, x, y, start_position):
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

    # Clear previous robot position and add it at the new position
    for i in range(x):
        for j in range(y):
            tiles[i][j].configure(text=f"({i},{j})", bg="white")

    start_x, start_y, _ = start_position
    tiles[start_x][start_y].configure(text="🤖", bg="lightblue")

def submit_commands():
    global room_size, start_position

    commands = entryOrder.get().strip().upper()
    if not commands:
        messagebox.showerror("Invalid Input", "Please provide a sequence of commands (L, F, R).")
        return
    order = list(commands)
    # Valider les commandes
    for i in range(len(order)):
        if not (order[i] == "L" or order[i] == "F" or order[i] == "R"):
            messagebox.showerror("Invalid Input", "Only L, F, R commands are allowed.")
            return
    try:
        # Execute the movement
        result = mouvement(room_size, start_position, commands)
        x, y, orientation = result.split()

        # Update starting position for further movements
        start_position = (int(x), int(y), str(orientation))

        # Display final position
        messagebox.showinfo("Position", f"The final position of the robot is:\n{x} {y} {orientation}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def mouvement(room_size, start_position, commands):
    # Room dimensions
    width, height = room_size

    # Starting position and orientation
    x, y, orientation = start_position

    # Map orientations to index and vice versa
    orientations = ['N', 'E', 'S', 'W']
    direction_index = orientations.index(orientation)

    # Define movement for each orientation
    moves = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}

    # Process commands
    for command in commands:
        if command == 'L':
            # Turn left
            direction_index = (direction_index - 1) % 4
        elif command == 'R':
            # Turn right
            direction_index = (direction_index + 1) % 4

        if command == 'F' or command == 'R' or command == 'L':
            # Move forward in the current direction
            dx, dy = moves[orientations[direction_index]]
            x += dx
            y += dy

            # Ensure the robot stays within bounds
            x = max(0, min(height - 1, x))
            y = max(0, min(width - 1, y))

        # Update the grid after each move
        grid_tile(gridFrame, rows, cols, (x, y, orientations[direction_index]))
        windowGrid.update_idletasks()  # Refresh the window to reflect changes

    # Final orientation
    final_orientation = orientations[direction_index]

    # Return final position and orientation
    return f"{x} {y} {final_orientation}"


"""
Project: Robot for Devoteam
Module: Internship Test
Author: Ryan BERSIER
Start Date: 28.11.24
Latest Update: 02.12.24
Version: 0.3
"""

# Libraries
from tkinter import *
from tkinter import messagebox
import time

def display_grid_page(grid_width, grid_height, start_x, start_y, start_orientation):
    """
    Displays the grid page where the robot is placed and controlled.

    :param grid_width: Width of the grid (number of columns).
    :param grid_height: Height of the grid (number of rows).
    :param start_x: Starting x-coordinate of the robot.
    :param start_y: Starting y-coordinate of the robot.
    :param start_orientation: Starting orientation of the robot ('N', 'E', 'S', 'W').
    """
    global grid_frame, order_frame, grid_window, command_entry, grid_rows, grid_cols, grid_size, robot_position

    # Create the grid window
    grid_window = Tk()
    grid_window.title("Robot Grid Controller")
    window_height = grid_height * 100
    window_width = grid_width * 90

    if grid_width <= 4:
        window_height += 100
    if grid_height <= 2:
        window_width += 100

    grid_window.geometry(f"{window_width}x{window_height}")
    grid_window.configure(background="grey")

    # Create frames for layout
    title_frame = Frame(grid_window, bg="grey")
    grid_frame = Frame(grid_window, bg="grey")
    order_frame = Frame(grid_window, bg="grey")

    title_frame.pack(side=TOP, pady=10)
    grid_frame.pack(side=TOP, pady=10)
    order_frame.pack(side=TOP, pady=10)

    # Add a title label
    title_label = Label(title_frame, text="🤖 Robot Grid 🤖", font=("Arial", 24), bg="grey")
    title_label.pack(side=TOP)

    # Command input and submit button
    command_entry = Entry(order_frame, font=("Arial", 12))
    submit_button = Button(order_frame, text="Submit", font=("Arial", 12), command=process_commands)

    command_entry.pack(side=LEFT, padx=5)
    submit_button.pack(side=LEFT, padx=5)

    # Grid parameters
    grid_rows, grid_cols = grid_width, grid_height
    grid_size = (grid_width, grid_height)
    robot_position = (start_x, start_y, start_orientation)

    # Draw the grid
    draw_grid(grid_frame, grid_rows, grid_cols, robot_position)


def draw_grid(grid_frame, rows, cols, robot_position):
    """
    Creates a grid and places the robot in its initial position.

    :param grid_frame: Frame where the grid is drawn.
    :param rows: Number of rows in the grid.
    :param cols: Number of columns in the grid.
    :param robot_position: Tuple containing the robot's starting x, y, and orientation.
    """
    global grid_tiles
    grid_tiles = []

    # Create grid cells
    for i in range(rows):
        row_tiles = []
        for j in range(cols):
            tile = Label(
                grid_frame, text=f"({i},{j})", borderwidth=2, relief="solid", width=4, height=2, bg="white", font=("Arial", 20))
            tile.grid(row=i, column=j)
            row_tiles.append(tile)
        grid_tiles.append(row_tiles)

    # Set the initial robot position
    start_x, start_y, orientation = robot_position
    for i in range(rows):
        for j in range(cols):
            grid_tiles[i][j].configure(text=f"({i},{j})", bg="white")

    # Determine the emoji corresponding to the orientation
    emoji_mapping = {'N': '🢁', 'E': '🢂', 'S': '🢃', 'W': '🢀'}
    robot_emoji = emoji_mapping[orientation]

    grid_tiles[start_x][start_y].configure(text=robot_emoji, bg="lightblue")



def process_commands():
    """
    Processes the commands entered by the user and updates the robot's position on the grid.
    """
    global grid_size, robot_position

    # Get and validate commands
    commands = command_entry.get().strip().upper()
    if not commands:
        messagebox.showerror("Invalid Input", "Please provide a sequence of commands (L, F, R).")
        return

    letter_commands = list(commands)
    for i in range(len(letter_commands)):
        if not (letter_commands[i] == "L" or letter_commands[i] == "F" or letter_commands[i] == "R"):
            messagebox.showerror("Invalid Input", "Only L, F, R commands are allowed.")
            return

    try:
        # Execute the movement
        result = execute_movement(grid_size, robot_position, commands)
        final_x, final_y, final_orientation = result.split()

        # Update the robot's position for future commands
        robot_position = (int(final_x), int(final_y), final_orientation)

        # Show final position
        messagebox.showinfo("Robot Position", f"The final position is:\n{final_x} {final_y} {final_orientation}")
    except Exception as error:
        messagebox.showerror("Error", str(error))


def execute_movement(grid_size, start_position, commands):
    """
    Executes movement commands for the robot.

    :param grid_size: Tuple containing grid width and height.
    :param start_position: Tuple containing the robot's initial x, y, and orientation.
    :param commands: String of commands (L, F, R).
    :return: String with the final x, y, and orientation.
    """
    width, height = grid_size
    x, y, orientation = start_position

    # Orientation mapping
    orientations = ['N', 'E', 'S', 'W']
    direction_index = orientations.index(orientation)
    moves = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}

    for command in commands:
        if command == 'L':
            # Turn left
            direction_index = (direction_index - 1) % 4
        elif command == 'R':
            # Turn right
            direction_index = (direction_index + 1) % 4

        orientation = orientations[direction_index]
        dx, dy = moves[orientation]

        if command == 'F' or command == 'R' or command == 'L':
            # Move forward
            new_x, new_y = x + dx, y + dy

            # Check boundaries
            if 0 <= new_x < height and 0 <= new_y < width:
                x, y = new_x, new_y
            else:
                messagebox.showwarning("Boundary Reached", "The robot cannot move outside the grid.")

        # Update the grid
        draw_grid(grid_frame, grid_rows, grid_cols, (x, y, orientation))
        grid_window.update_idletasks()  # Refresh the UI
        time.sleep(0.1)

    return f"{x} {y} {orientation}"


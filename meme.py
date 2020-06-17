import numpy as np

# Get number input from user. Prompt for integer if required.
input_request = True
while input_request:
    number = input("Length of square: ")
    try:
        number = int(number)
        input_request = False
    except:
        print("Enter a positive number!")

# Create an n x n grid
grid = np.zeros((number, number))
count = 1 # Initiating first count at 1
centre = (number - 1)/2 # Initiating centre of the grid
current_row = current_col = int(centre)
grid[current_row, current_col] = count
new_col = current_col + 1
count += 1
action = None

# Define functions for a single step in the four directions
def up():
    global current_col
    global current_row
    global count
    global action
    new_row = current_row - 1
    grid[new_row, current_col] = count
    current_row = new_row
    count += 1
    action = "up"

def down():
    global current_col
    global current_row
    global count
    global action
    new_row = current_row + 1
    grid[new_row, current_col] = count
    current_row = new_row
    count += 1
    action = "down"

def left():
    global current_col
    global current_row
    global count
    global action
    new_col = current_col - 1
    grid[current_row, new_col] = count
    current_col = new_col
    count += 1
    action = "left"

def right():
    global current_col
    global current_row
    global count
    global action
    new_col = current_col + 1
    grid[current_row, new_col] = count
    current_col = new_col
    count += 1
    action = "right"

# Function to execute a single step in a chosen direction
def move():
    global current_col
    global current_row
    #if previous step = right, try down. Else continue right.
    global action
    if action == "right":
        new_row = current_row + 1
        if grid[new_row, current_col] == 0:
            down()
            action = "down"
        else:
            right()

    #if previous step = down, try left. Else continue down.
    if action == "down":
        new_col = current_col - 1
        if grid[current_row, new_col] == 0:
            left()
            action = "left"
        else:
            down()

    #if previous step = left, try up. Else continue left.
    if action == "left":
        new_row = current_row - 1
        if grid[new_row, current_col] == 0:
            up()
            action = "up"
        else:
            left()

    #if previous step = up, try right. Else continue up.
    if action == "up":
        new_col = current_col + 1
        if grid[current_row, new_col] == 0:
            right()
            action = "right"
        else:
            up()
            
# Take the first step to the right to initiate the clockwise spiral
right()

loop = True
while loop:
    move()
    if not any([0 in grid[i] for i in range(number)]):
        loop = False

print(grid)

"""
print("Welcome to Coding Club")
"""
# Firstly, we need to install our dependencies
import numpy as np  # Used for the grid
import pygame  # Used for graphics
from surrounding import *

x_length = 5
y_length = 5

grid = [[0]*x_length]*y_length
grid = np.array(grid)


"""
KEY
---
Starting Position (sp) - /
Current Position (cp) - *
Blocked Position (bp) - +
Finish Position (fp) - =
"""
# Starting Position
sp = (0, 0)
# Finishing position
fp = (
    x_length - 1,
    y_length - 1
)
# Current Position - copy the starting position
cp = sp
# Blocked positions
bp = [(2, 2), (1, 2)]

# Need to add the blocked squares to the array. The function modifies grid itself
addBP(bp, grid)
# Initial positions
path = [sp]
direct = []
direct_checked = []
# {(x,y): float} of checked weights
checked = {}
weights = []
possible = True

# this is a depth first search algorithm finder
# First explore the squares around, explore all the ones that have not already been explored, find the one with the highest weight and move the agent to that square. From there calculate the weights of all the new squares, repeat, each time check that the square is not the end destination, if it is return the path found and end the program.


# How the weights are calculated, for now just a crude the closer to the end you are the better.

# Search till the algorithm is solved
while True:
    # Check to make sure position is not the destination
    if cp == fp:
        break
    # Bind the weight_func
    weight_func = calc_weight(checked, fp)
    # surrounding needs to get the weights of all the squares that are possible to travel to
    sur_weights = surrounding(cp, grid, weight_func)
    print(sur_weights, checked)

    # Set the best next square to the cp
    cp = get_best_weight(sur_weights)
    print(cp)

# Find the largest weight
# Make the position = largest weight

print("WE have solved it!!!")

# BYUI-I Course: CSE110
# Author: Mikhail Cedras

# Input: Have user input a color
# Process: Set color variable and add the variable to string
# Output: String with desired phrase with the user's input color

import time

# Get user input
userColor = input('Please type your favorite color: ')

# Print output
print('\nYour favorite color is: ' + userColor.title() + '!')
time.sleep(1)
print('\nHmmm...')
time.sleep(2)
print('\nIt looks like we have something in common, ' + userColor.lower() + ' is my favorite color too!')


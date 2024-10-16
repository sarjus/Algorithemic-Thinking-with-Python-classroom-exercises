'''
Write a Python program that takes a number as input
from the user and finds the factorial of that number
using a while loop.

Author: Sarju S
'''
# Input: Take the value from the user
num = int(input("Enter a positive integer: "))

# Initialize the factorial result
factorial = 1

# Using a while loop to calculate factorial directly with num
while num > 1:
    factorial *= num  # Multiply the result by the current number
    num -= 1  # Decrease num itself

print(f"The factorial is {factorial}.")

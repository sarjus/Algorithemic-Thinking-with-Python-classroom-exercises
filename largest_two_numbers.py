'''
Python program that takes two numbers as input
from the user and prints the larger of the two numbers.
If both numbers are equal, print "The numbers are equal."
Author: Sarju S
'''

# Solution
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(f"The larger number is {num1}.")
elif num2 > num1:
    print(f"The larger number is {num2}.")
else:
    print("The numbers are equal.")

'''
Write a Python program to calculate the sum of the first N natural numbers
using a for loop. The user will input N.

Author: Sarju S
'''

# Input: Take the value of N from the user
N = int(input("Enter a positive integer N: "))

# Initialize the sum
total_sum = 0

# Using a for loop to calculate the sum
for i in range(1, N + 1):
    total_sum += i  # Add the current number to the sum

print(f"The sum of the first {N} natural numbers is {total_sum}.")






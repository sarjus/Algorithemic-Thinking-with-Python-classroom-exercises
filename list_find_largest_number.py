'''
Objective: How to loop through a list and find the largest element.
Instructions:
Create a list of numbers: [12, 75, 34, 99, 45, 67].
Write a loop to find the largest number in the list.
Print the largest number.

Author: Sarju S
Date: 24-10-2024
'''
# Step 1: Creating the list of numbers
numbers = [12, 75, 34, 99, 45, 67]

# Step 2: Finding the largest number
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

# Step 3: Printing the largest number
print("The largest number is:", largest)  # Output: 99

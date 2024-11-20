'''
Objective:Python program to input the number
 of rows and columns from the user, then create a 
 rows × columns matrix using NumPy.
Author: Sarju S
Date: 21-11-2024
'''
import numpy as np

# Input the dimensions of the array
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Initialize an empty list to store the elements
data = []

# Accepting the elements
print("Enter the elements one by one:")
for i in range(rows):
    row = []  # Temporary list for each row
    for j in range(cols):
        value = int(input(f"Enter the value for element ({i+1}, {j+1}): "))
        row.append(value)
    data.append(row)  # Append the completed row to the data list

# Convert the list of lists into a NumPy array
array = np.array(data)

print("\nTwo-dimensional array created:")
print(array)

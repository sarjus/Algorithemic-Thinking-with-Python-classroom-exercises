'''
Objective: Remove duplicate elements from a list using a loop or set.
Approach:
Create an empty list to store unique elements.
Loop through the original list, and for each element, check if it is already in the new list.
If the element is not in the new list, add it.


Author: Sarju S
Date: 24-10-2024
'''
# Original list with duplicates
original_list = [1, 3, 2, 4, 3, 2, 5, 1, 6, 5]

# List to store unique elements
unique_list = []

# Iterate over the original list
for element in original_list:
    # If the element is not already in unique_list, append it
    if element not in unique_list:
        unique_list.append(element)

# Print the unique list
print("Original list:", original_list)
print("List without duplicates:", unique_list)

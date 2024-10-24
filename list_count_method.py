'''
Objective: Use the count() method to count occurrences of a value in a list.
Instructions
Create a list: ["apple", "banana", "cherry", "apple", "apple", "banana"].
Count how many times "apple" appears in the list.
Count how many times "banana" appears in the list.


Author: Sarju S
Date: 24-10-2024
'''
# Step 1: Creating the list
fruits = ["apple", "banana", "cherry", "apple", "apple", "banana"]

# Step 2: Counting occurrences of "apple"
apple_count = fruits.count("apple")

# Step 3: Counting occurrences of "banana"
banana_count = fruits.count("banana")

# Printing the results
print("Apple appears", apple_count, "times.")  # Output: 3
print("Banana appears", banana_count, "times.")  # Output: 2

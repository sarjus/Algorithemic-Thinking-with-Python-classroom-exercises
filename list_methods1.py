'''
Objective: Practice the append(), insert(), and remove() methods.
Instructions:
Start with an empty list called colors.
Use append() to add "red", "green", and "blue" to the list.
Use insert() to add "yellow" at the second position.
Use remove() to remove "green" from the list.
Print the final list.

Author: Sarju S
'''
# Step 1: Creating an empty list
colors = []

# Step 2: Using append() to add elements
colors.append("red")
colors.append("green")
colors.append("blue")

# Step 3: Using insert() to add "yellow" at the second position
colors.insert(1, "yellow")

# Step 4: Using remove() to remove "green"
colors.remove("green")

# Step 5: Printing the final list
print(colors)  # Output: ['red', 'yellow', 'blue']

'''
Description:
       The store wants to remove specific items from the inventory when they are out of stock. 
       Use remove() or discard() to handle this.
Author: Sarju S
Date: November 13, 2024
Version: 1.0
'''
# Current inventory
inventory = {"apples", "bananas", "oranges", "grapes"}

# Remove out-of-stock item using remove()
inventory.remove("bananas")

# Try removing an item that may not exist using discard()
inventory.discard("pineapple")  # No error if not in the inventory

# Output updated inventory
print("Inventory after removal:", inventory)


# Output updated inventory
print("Updated inventory:", inventory)

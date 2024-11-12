'''
Description:
        Updates a store's inventory with items from a new shipment, ensuring no duplicate items.
Author: Sarju S
Date: November 13, 2024
Version: 1.0
'''
# Initial inventory
inventory = {"apples", "bananas", "oranges"}

# New shipment
new_items = {"bananas", "grapes", "kiwis"}

# Update inventory with new items
inventory.update(new_items)

# Output updated inventory
print("Updated inventory:", inventory)

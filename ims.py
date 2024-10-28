'''
A retail store wants to create an inventory system that stores each item as a tuple containing:

The item name (string)
The quantity in stock (integer)
The unit price (float)
The store needs to:

Calculate the total value of the stock for each item.
Find the item with the highest value in stock.
Write code to:

Define a list of tuples to represent the inventory.
Calculate and display the total stock value for each item.
Find and print the item with the highest total stock value.
Author: Sarju S
'''
# Inventory data as tuples (item_name, quantity, unit_price)
inventory = [
    ("Laptop", 5, 1200.00),
    ("Headphones", 15, 100.00),
    ("Mouse", 50, 25.00),
    ("Keyboard", 20, 45.00),
    ("Monitor", 10, 300.00)
]

print("Total stock values:")
highest_value = 0
highest_value_item = None

for item in inventory:
    name, price, quantity = item
    
    total_value = quantity * price
    print(f"{name}: ${total_value:.2f}")

    # Track the item with the highest total value
    if total_value > highest_value:
        highest_value = total_value
        highest_value_item = item

print("\nItem with the highest stock value:")
print(f"{highest_value_item[0]} - Total Value: ${highest_value:.2f}")

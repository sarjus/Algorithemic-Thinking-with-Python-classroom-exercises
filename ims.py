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
# Inventory data with tuples (item_name, quantity, unit_price)
inventory = [
    ("Laptop", 5, 1200.00),
    ("Headphones", 15, 100.00),
    ("Mouse", 50, 25.00),
    ("Keyboard", 20, 45.00),
    ("Monitor", 10, 300.00)
]

# Calculate and display the total stock value for each item
def calculate_total_value(item):
    name, quantity, price = item
    return quantity * price

print("Total stock values:")
for item in inventory:
    name = item[0]
    total_value = calculate_total_value(item)
    print(f"{name}: ${total_value:.2f}")

# Find the item with the highest total stock value
max_value_item = max(inventory, key=calculate_total_value)
print("\nItem with the highest stock value:")
print(f"{max_value_item[0]} - Total Value: ${calculate_total_value(max_value_item):.2f}")

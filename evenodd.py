'''
Python program that prompts the user to enter a number
and checks if the number is even or odd. If the number is even,
print "The number is even." If the number is odd,
print "The number is odd."
Author: Sarju S
'''

# Solution
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

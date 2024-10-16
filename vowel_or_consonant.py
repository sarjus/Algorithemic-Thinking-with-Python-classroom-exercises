'''
Write a Python program that takes a single
character as input from the user and checks
if it is a vowel or a consonant.
If the input is not an alphabetic character, print "Invalid input."

Author: Sarju S
'''

# Program to check if a character is a vowel or consonant
char = input("Enter a single character: ")

# Check if the input is a single alphabetic character
if char.isalpha():
    if char in 'AEIOUaeiou':  # Check if the character is a vowel
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Invalid input.")


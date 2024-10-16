'''
Python program that takes a year as input and checks if the year is a leap year. 
If the year is divisible by 400, it is a leap year.
If the year is divisible by 100 but not 400, it is not a leap year.
If the year is divisible by 4 but not 100, it is a leap year.

Author: Sarju S
'''

# Program to check if a year is a leap year
year = int(input("Enter a year: "))

# Check the conditions for a leap year
if year % 400 == 0:
    print(f"{year} is a leap year.")
elif year % 100 == 0:
    print(f"{year} is not a leap year.")
elif year % 4 == 0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")



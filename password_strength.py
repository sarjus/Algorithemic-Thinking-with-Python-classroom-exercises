'''
Python program that checks the strength
of a password entered by the user.
The program should categorize the password as:
"Weak" if it is less than 6 characters.
"Medium" if it is between 6 and 10 characters.
"Strong" if it is more than 10 characters.


Author: Sarju S
'''

# Solution
password = input("Enter a password: ")
length = len(password)

if length < 6:
    print("Password strength: Weak")
elif 6 <= length <= 10:
    print("Password strength: Medium")
else:
    print("Password strength: Strong")




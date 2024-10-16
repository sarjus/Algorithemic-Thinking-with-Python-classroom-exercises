'''
Write a Python program that takes a student's marks as input 
and prints their grade based on the following criteria:
Marks >= 90: A
Marks 80–89: B
Marks 70–79: C
Marks 60–69: D
Marks < 60: F

Author: Sarju S
'''

# Solution
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")


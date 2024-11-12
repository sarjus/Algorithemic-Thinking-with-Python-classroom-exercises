'''
Python program to Generate Prime Numbers upto N

In Python, an else clause can be used with loops, not just if statements. 
This is an interesting feature, and it works a bit differently than the else 
clause you might be used to with if. Here’s how it works with a for loop in the context of this code.

How else Works with Loops
When an else is attached to a loop (for or while), the else block executes only 
if the loop completes without hitting a break statement. In other words:

If the loop completes all its iterations without break, the else block runs.
If the loop encounters a break (and therefore exits early), the else block does not run.

Author: Sarju S
Date: 12-11-2024
'''
N = int(input("Enter a number"))
print(f"Prime Number Less than {N} are:")
for num in range(2,N):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num, end=" ")


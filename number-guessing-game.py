'''
Objective: At start-up, the user enters the smallest number
and the largest number in the range.
The computer then selects a number from this range.
On each pass through the loop, the user enters a number
to attempt to guess the number selected by the computer.
The program responds by saying
“You’ve got it,” “Too large, try again,” or “Too small, try again.”
When the user finally guesses the correct number,
the program congratulates him and tells him the total number of guesses.

Author: Sarju S
Date: 14-11-2024
'''
import random
smallest = int(input("Enter a small number: "))
largest = int(input("Enter a a big number: "))
guess= random.randint(smallest,largest)
no_of_tries= 0
while True:
    user_input = int(input("Guess a number: "))
    no_of_tries+=1
    if user_input < guess:
        print("Too small, enter a bigger number")
    elif user_input > guess:
        print("Too big, enter a smaller number")
    else:
        print("Congrats! You guessed the number!")
        print("The number of tries is", no_of_tries)
        break

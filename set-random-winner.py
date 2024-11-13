'''
Description:
       A school is organizing a raffle with unique student IDs. 
       Write a program to randomly select a winner 
       from the list of participants using pop().

Author: Sarju S
Date: November 13, 2024
Version: 1.0
'''
# Set of participants
participants = {"STUD001", "STUD002", "STUD003", "STUD004"}

# Draw a winner
winner = participants.pop()

# Output the winner and remaining participants
print("Raffle winner:", winner)
print("Remaining participants:", participants)


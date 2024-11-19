'''
Objective:
Create a telephone directory using a dictionary. The name of the individual
and the telephone number will be key and value, respectively. Write a
Python program that allows the user to perform the following operations:
(a) Add a Contact: Add a new contact with a name and phone number
to the directory.
(b) Update a Contact: Update the phone number of an existing contact.
(c) Delete a Contact: Remove a contact from the directory.
(d) Search for a Contact: Look up the phone number of a contact by
their name.
(e) Display All Contacts: Print all contacts in the directory.
(f) Exit the program.
Use a menu-driven approach.

Author: Sarju S
Date: 19-11-2024
'''
# Telephone Directory Program
telephone_directory = {}

while True:
    print("\n--- Telephone Directory ---")
    print("1. Add a Contact")
    print("2. Update a Contact")
    print("3. Delete a Contact")
    print("4. Search for a Contact")
    print("5. Display All Contacts")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        # Add a Contact
        name = input("Enter contact name: ")
        if name in telephone_directory:
            print("This contact already exists.")
        else:
            phone_number = input("Enter phone number: ")
            telephone_directory[name] = phone_number
            print("Contact added successfully!")

    elif choice == "2":
        # Update a Contact
        name = input("Enter the name of the contact to update: ")
        if name in telephone_directory:
            new_number = input(f"Enter the new phone number for {name}: ")
            telephone_directory[name] = new_number
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    elif choice == "3":
        # Delete a Contact
        name = input("Enter the name of the contact to delete: ")
        if name in telephone_directory:
            del telephone_directory[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == "4":
        # Search for a Contact
        name = input("Enter the name of the contact to search: ")
        if name in telephone_directory:
            print(f"{name}'s phone number is {telephone_directory[name]}")
        else:
            print("Contact not found!")

    elif choice == "5":
        # Display All Contacts
        if telephone_directory:
            print("\nAll Contacts:")
            for name, number in telephone_directory.items():
                print(f"Name: {name}, Phone Number: {number}")
        else:
            print("The directory is empty!")

    elif choice == "6":
        # Exit the program
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")

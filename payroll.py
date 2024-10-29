'''
A company wants to manage its employee information and includes each employee as a tuple containing:
Employee name (string)
Department (string)
Monthly salary (float)
The company needs to:
Display all employees who have a monthly salary above a specified threshold.
Find the total annual payroll expense for all employees in the company.
Write code to:
Define a list of tuples with employee information.
Display employees earning above a salary threshold.
Calculate and display the total annual payroll expense.

Author: Sarju S
'''
# Employee data as tuples (name, department, monthly_salary)
employees = [
    ("Alice", "HR", 3000.00),
    ("Bob", "Engineering", 4500.00),
    ("Charlie", "Sales", 4000.00),
    ("Diana", "Marketing", 3500.00),
    ("Eve", "Engineering", 5000.00)
]


# Input the salary threshold from the user
threshold = float(input("Enter the monthly salary threshold to filter employees: "))

# Display employees with monthly salary above a certain threshold
print(f"Employees earning above ${threshold} per month:")
for employee in employees:
    name, department, salary = employee
    if salary > threshold:
        print(f"{name} ({department}) - ${salary:.2f}")

# Calculate total annual payroll expense
total_annual_expense = 0
for employee in employees:
    salary = employee[2]  # Access the salary from the tuple
    total_annual_expense += salary * 12  # Add the annual salary to the total
print(f"\nTotal annual payroll expense: ${total_annual_expense:.2f}")


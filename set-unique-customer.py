'''
Description:
        Takes a list of customer IDs and returns a set of unique customer IDs for the day.

Author: Sarju S
Date: November 13, 2024
Version: 1.0
'''
# Start with an empty set
customers_today = set()

# Add customer IDs (simulate adding IDs)
customers_today.add("CUST1001")
customers_today.add("CUST1002")
customers_today.add("CUST1001")  # Duplicate visit
customers_today.add("CUST1003")

# Output unique customer IDs
print("Unique customers today:", customers_today)

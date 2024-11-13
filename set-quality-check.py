'''
Description:
       A warehouse has a set of products ready for shipment, 
       but one product fails the quality check and must be removed. 
       Use discard() to remove it safely without raising an error if it’s missing.


Author: Sarju S
Date: November 13, 2024
Version: 1.0
'''
# Set of products
products = {"PROD1001", "PROD1002", "PROD1003", "PROD1004"}

# Product fails quality check
products.discard("PROD1003")

# Output updated list of products
print("Products after quality check:", products)

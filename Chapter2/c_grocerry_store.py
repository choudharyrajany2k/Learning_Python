#!/usr/bin/python
"""
    Purpose:
        Grocesory Store
"""
result_Highlighter = 10
cost_of_rice_per_kg = 53 # preKg
cost_of_wheat_per_kg = 34 #PerKg

# qty_of_rice_in_kg = 20 
# qty_of_wheat_in_kg = 90

qty_of_rice_in_kg = int(input('Enter qty of rice:'))
qty_of_wheat_in_kg = int(input('Enter qty of wheat:'))

print("Entered quantity of rice : ",qty_of_rice_in_kg)
print("Entered quantity of white : ",qty_of_wheat_in_kg)

print("tyoe(qty_of_rice_in_kg)",type(qty_of_rice_in_kg))
print("tyoe(qty_of_wheat_in_kg)",type(qty_of_wheat_in_kg))

sp_of_rice = cost_of_rice_per_kg * qty_of_rice_in_kg
sp_of_wheat =cost_of_wheat_per_kg *qty_of_wheat_in_kg

total_cost = sp_of_rice+sp_of_wheat
print("Estimated Cost : ",total_cost)

#Discount of 10%
discount = (10/100)*total_cost
discounted_price = total_cost-discount

print(result_Highlighter*"*")
print("Discounted Price : ",discounted_price)
print(result_Highlighter*"*")

#Apply Gst 5%
gst_tax = (5/100)*discounted_price

print(result_Highlighter*"*")
print("To be paid",gst_tax+discounted_price)
print(result_Highlighter*"*")



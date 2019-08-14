#!/usr/bin/python
"""
	Purpose: Mandatory and defult args together
"""


# def addition1(num1,num2=0,num3):   # SyntaxError: non-default argument follows default argument
#     return num1+num2+num3

def addition1(num1,num2=0,num3=0):  
    return num1+num2+num3
print(addition1(11,22,33))
print(addition1(11,22))
print(addition1(11))

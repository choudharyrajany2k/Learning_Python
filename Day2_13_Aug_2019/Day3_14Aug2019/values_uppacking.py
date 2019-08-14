#!/usr/bin/python
"""
	Purpose: values Unpacking
"""
def getValues():
    return "helo"

print(f"getvalues() :{getValues()}")

num1,num2 = [1,12]
print(f"num1 - >{num1}")

num1,num2 = {1,2}
print(f"num1 - >{num1}")
print(f"num2 - >{num2}")
print("=> Dict unpacking")
num1,num2 = {1:"1",2:"2"}
print(f"num1 - >{type(num1)}")
print(f"num2 - >{num2}")


print("=> function overwriting")

def addition(num1,num2):
    return num1+num2
print(addition(1,2))
#print(addition(1,2,3))  This fails 
def addition1(num1,num2,num3):
    return num1+num2+num3
#print(addition(1,2,3))

print("=> Function overloading")
def addition(num1,num2,num3 = 0):
    return num1+num2+num3


print("===============>Math")

import math
print(math.floor(9.99999))
print(math.fabs(-9.99999))

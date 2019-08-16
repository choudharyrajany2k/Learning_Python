#!/usr/bin/python
"""
    FILE NAME: test_decorators.py
    Purpose: Test for decorators by SMART DIVISION

    SMART DIVISION - Always divides gretater number by lesser number irrespective of the sequence of parameters

    Decorators changes the behavior of the function on which it is applied by injecting 
    addon behavior or completly overriding the behaviour.

    Explanation for SMART DIVISION

    When ever there is a decorator on a function in the module , first of all that is called. smartdivision_decorator just returns the defined function inside it.
    As every thing in python is a object, division is reassined like 
    division = smartdivision_decorator(division)

"""

def smartdivision_decorator(func):
    def inside(a,b):
        if a<b:
            a,b = b,a
            return func(a,b)
        else:
            return func(a,b)
    return inside

@smartdivision_decorator   # meaning of Decorator is division = smartdivision_decorator(division)
def division(a,b):
    return a/b

if __name__ == "__main__":
    print(f'division(10,12) : {division(10,12)}')
    print(f'division(12,10) : {division(12,10)}')

#OUTPUT
# division(10,12) : 1.2
# division(12,10) : 1.2


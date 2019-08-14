#!/usr/bin/python
"""
	Purpose: Recursions Functions
"""

def factorial(num):
    print(f"num {num}")
    if(num==1):
        print(num)
        return 1
    return num *factorial(num-1)

factorial(5)

import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
#!/usr/bin/python
"""
	Purpose: Higher order functions
"""

def enev_odd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"

any_func = lambda num:("even" if num%2==0 else "odd")
print(any_func(2))

print()
multi_func = lambda *argv : print(argv)
print(multi_func(1,2,3,4))


from functools import reduce
_reduce = lambda x,y :x*y
print(reduce(_reduce,range(1,5)))

#help(map)
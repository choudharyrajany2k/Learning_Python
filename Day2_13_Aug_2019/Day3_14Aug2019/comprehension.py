#!/usr/bin/python
"""
Purpose : Demo Comprehension

"""

for i in [1,2,3,4]:
    print(f"i -> {i}")

# [print(f"i -> {i}") for i in [1,2,3,4]]   # list comprehension
# {print(f"i -> {i}") for i in [1,2,3,4]}   # dictionary comprehension
# (print(f"i -> {i}") for i in [1,2,3,4]) # genertor

(print(f"i -> {i}") for i in [1,2,3,4] if i%2==0) # comprehension


def getbanner(message):
    print(5*"*"+message+5*"*")

getbanner("terniary operator in python")
print("greater"if 1>2 else "lesser")

even = []
odd = []
for i in range(20):
    if i%2==0:
      even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
from 
getbanner("comprehension")
pprint({even.append(i) if i%2==0 else odd.append(i) for i in range(20)})


#!/usr/bin/python
"""
    Purpose: Demo Range Function
"""
numbers =range(9)
for num in numbers:
    print("num is ",num)

#Enumerate gives the index and the item e.g (index,item)
numbers =enumerate(range(9))
for num in numbers:
    print("num is :",num)
    print("type(num)",type(num))

# Output:
# num is : (0, 0)
# num is : (1, 1)
# num is : (2, 2)
# num is : (3, 3)
# num is : (4, 4)
# num is : (5, 5)
# num is : (6, 6)
# num is : (7, 7)
# num is : (8, 8)

numbers = range(90,1,1)
for num in numbers:
    print("num is ",num)
# No Output

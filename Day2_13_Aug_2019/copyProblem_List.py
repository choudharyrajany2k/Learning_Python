#!/usr/bin/python
"""
    Purpose: Demo for List
    Shallow and Deep Copy fo List
"""
import copy
myList = [1,2,3,4,345,2,2345]
# example of shallow copy i.e same memory location
myCopiedList =  myList
print(f"id(myList):{id(myList)}")
print(f"id(myCopiedList):{id(myCopiedList)}")

#example of Deep Copy for level1 i.e Different Address location
myDeepCopy = myList.copy()
print(f"id(myDeepCopy):{id(myDeepCopy)}")


print(10*"*")
mynestedList = [1,2,[1,2]]
mycopy = mynestedList.copy() # Does not work for Nested lists
mynestedList[2][0] = 908
print(f"mycopy {mycopy}")
print(f"mynestedList {mynestedList}")
print(f"id(mycopy) {id(mycopy)}")
print(f"id(mynestedList) {id(mynestedList)}")

print(10*"*")
mynestedList = [1,2]
mycopy = mynestedList.copy()
mynestedList[1] = 10
print(f"mycopy {mycopy}")
print(f"mynestedList {mynestedList}")

print(10*"*"+"Deep Copy Demo"+10*"*")
mynestedList = [1,2,[1,2]]
mycopy.deepcopy(mynestedList) # Does not work for Nested lists
mynestedList[2][0] = 908
print(f"mycopy {mycopy}")
print(f"mynestedList {mynestedList}")
print(f"id(mycopy) {id(mycopy)}")
print(f"id(mynestedList) {id(mynestedList)}")


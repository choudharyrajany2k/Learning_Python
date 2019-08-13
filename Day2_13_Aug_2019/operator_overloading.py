#!/usr/bin/python
"""
Purpose: Demo Overloading
"""
try:
    print(f'1+2: {1+2}')
    # print(f'1+2: {1+"1"}')
    print(sum([1,2,3]+[3,4,5]))
except Exception as ex:
    print(f'{ex}')

print('abx'.__add__('a'))
print(type(''.__add__))
print(type(''.count))
myList = [122,2,3,44,45,64,72,8,19]
# print(f'mylist.pop() {myList.pop()}')
# print(myList)

myList.sort()
print(myList)
print('soreted list with sorted',sorted(myList,reverse=True))
print(myList)
#deleting based on indexing
del myList[0:4]
print(myList)

#Python 2.x supports sort but not python 3.x
# myanotherlist = [(123,1234),None]  
# print(f"{myanotherlist.sort()}")
# print(f"{sorted(myanotherlist)}")
print(f"type(None) {type(None)}")




# A generator function that yields 1 for first time, 
# 2 second time and 3 third time 
def simpleGeneratorFun(): 
	yield 1			
	yield 2			
	yield 3			

print(f"type(simpleGeneratorFun) {type(simpleGeneratorFun)}")
# Driver code to check above generator function 
for value in simpleGeneratorFun(): 
    print(value) 

#generator is not a class

#!/usr/bin/python
"""
    Purpose: Demo Boolean operations
"""

print(True)
print(1==True)
print('bool(1223)',bool(1223))
print('bool(-7687)',bool(-7687))
print('bool(0)',bool(0))
print('bool(-0)',bool(-0))
print(None)
a = None
print("value of a: ",a)
print("value of bool(None) ",bool(None))

print("bool([])",bool([]))
print("bool(())",bool(()))
print("bool({})",bool({}))

a=''
if not a:
    print('a is having value')
else:
    print('a -No value')

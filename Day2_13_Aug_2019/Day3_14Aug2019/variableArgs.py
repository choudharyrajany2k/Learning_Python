#!/usr/bin/python
"""
	Purpose: variable args Function/ variadic functions
"""

def myfunc(*values):
    print(values)
    for target_list in values:
        print(target_list)
# myfunc("helo",234,1234,234)
myfunc()

myfunc("helo",234,1234,234,dict({1:"1"}))
# myfunc("helo",234,1234,234)
print("========================")

def myfunc(mand,*values):
    print(mand)
    for target_list in values:
        print(target_list)
# myfunc("helo",234,1234,234)
myfunc("helo",234,1234,234,dict({1:"1"}))
# myfunc("helo",234,1234,234)

print("=>****************************")
def myfunc(*values,mand):
    print(mand)
    for target_list in values:
        print(target_list)
# myfunc("helo",234,1234,234)
myfunc("helo",234,1234,234,mand = dict({1:"1"}))
# myfunc("helo",234,1234,234)
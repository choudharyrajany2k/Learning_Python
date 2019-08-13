#!/usr/bin/python
"""purrpose: While else Demo"""
i=0
while i<10:
    print(i)
    i+=1
else:
    print("out of the while loop")

print(10*"*"+"pass"+10*"*")
i=0
while i<10:
    if i==5:
        pass
    print(i)
    i+=1

else:
    print("out of the while loop")

print(10*"*"+"Sys.Exit()"+10*"*")
import sys
i=0
while i<10:
    if i==5:
        sys.exit()
    print(i)
    i+=1

else:
    print("out of the while loop")

    print(10*"*"+"pass"+10*"*")
    i=0
    while i<10:
        if i==5:
            pass
        print(i)
        i+=1
    
    else:
        print("out of the while loop")
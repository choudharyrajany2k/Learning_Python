#!/usr/bin/python
"""
Purpose: Demo String Formating
"""
j=1
while j<10:
    i=1
    while i<10:
        print("%d*%d=%d"%(i,j,i*j)) # string formating - old Style
        print("{:2}*{:2}={:2}".format(i,j,i*j)) # New Style
        print(f"{i:2}*{j:2}={i*j:2}") # latest way
        i+=1
    j+=1
#!/usr/bin/python
"""
	Purpose: File Operations Demo

    Buy Default it is read operation

"""
# fh = open('foo.txt','r')
fh = open('foo.txt','w')
fh.write("Hello Python\n")
fh.writelines(["Hello Python","Secondline"])

print("Name of the file",fh.name)
print("Operating mode",fh.mode)
fh.flush()
print("closed or open",fh.closed)

fh.close()
print("closed or open",fh.closed)

print(fh.writable())


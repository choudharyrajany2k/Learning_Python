#!/usr/bin/python
"""
    Purpose: CZar Problem Statement
"""
Problem_Statement="zoo"
output = ''
max_value = ord('z')
min_value = ord('a')
print("max_value",max_value)
print("min_value",min_value)
for char in Problem_Statement:
    output += chr(((ord(char)%max_value)+3)+min_value)
print(output)

#!/usr/bin/python
"""
    Purpose: To Encode a string with incement by 3
            ceaser cipher
"""
def encodeStringNew():
    max_index = ord('z')
    min_index =ord('a')
    output = ''
    to_be_encoded = str(input("Please Enter a value : "))
    for characters in to_be_encoded:
        output += chr(((ord(characters)%96)%26)+99)
    print(output)

def encodeString():
    max_index = ord('z')
    min_index =ord('a')
    output = ''
    to_be_encoded = str(input("Please Enter a value : "))
    for characters in to_be_encoded:
        difference = 0
        result_char=''
        incremented = ord(characters)+3
        if(incremented>max_index):
            difference = incremented%max_index
            result_char = str(chr(min_index+difference))
        else:
            result_char = str(chr(incremented))
        output += result_char
    print(output)

encodeStringNew()
#encodeString()

#!/usr/bin/python
"""
Purpose : Dictionaries
    Properties
        -  Keys shoukld be unique
        -Dict are mutable
"""
from pprint import pprint
mydict1 = {'name': 'python', 'name': 'django'}
print(mydict1)

mydict = {
    'name': 'python',
    1234: 123,
    (123, 34): 'sda',
    True: 'asdf',
    None: [452345, 2345],
    'mydict':mydict1,
    1:'here is i am' #true will be updated
    # [123,23]:'saddf'  Error : TypeError: unhashable type: 'list'
}
#allkeys should be immutable
print(mydict)
pprint(mydict)
#ordred dict is older version of Python as dict in older version used to have no respect for sequence


def getbanner(message):
    print(5*"*"+message+5*"*")

getbanner("       ")
getbanner("Zip Demo")

cities = ["bangalore","pune"]
states = ["kar","mah"]
print(dict(zip(cities,states)))

_str1 = "mynam"
_str2 = "rajan"
print(list(zip(_str1,_str2)))

getbanner("*******************************")
getbanner("Sort Dictionary")

print(sorted(dict(zip(_str1,_str2))))


# sorting of Dictionaries can be done on 
#   -item
#   -keys
#   -values

getbanner("Sorting by keys,values,items")

mydict1 = {1:"one",2:"two",3:"three"}
print(sorted(mydict1.items()))
print(sorted(mydict1.values()))
print(sorted(mydict1.items(),reverse = True,key = lambda x:x[0])) # sorting my keys



getbanner("Dictionary operations")
mydict = {1:"one",2:"two",3:"Three"}
print(f"mydict[1] {mydict[1]}")

mydict[2]="two1"
print(f"mydict {mydict}") #dictionaries are mutable

mydict[4] = "four"
print(f"mydict {mydict}") #updated dictionary

new_dict = {'a':"apple",'b':"bat",'c':"cat"}

#print(new_dict+mydict) +operator is NA

print(f"new_dict.update(mydict) : {new_dict.update(mydict)}")

print(type({})) #empty dict
print(type({""})) #empty set
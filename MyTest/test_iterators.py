#!/usr/bin/python
"""
    FILENAME : test_iterators.py
    Purpose: Demo iterator and iterable, also demo StopIteration
"""
#does not hits the Exception StopIteration
def test_myIterator():
    try:
        my_list = [12,12,24]
        for item in my_list:
            print(f"item : {item}")
    except StopIteration as identifier:
           print(f"identifier :{identifier}")

#OUTPUT test_myIterator()
# item : 12
# item : 12
# item : 24

#Hits Exception only once as soon as the count of the elemenst is breached
def test_iter_object():
    try:
        my_list = [12,34,45]
        iterator_object = iter(my_list)
        print(f'iterator_object.next() : { next(iterator_object)}')
        print(f'iterator_object.next() : { next(iterator_object)}')
        print(f'iterator_object.next() : { next(iterator_object)}')
        print(f'iterator_object.next() : { next(iterator_object)}')
        print(f'iterator_object.next() : { next(iterator_object)}')
        print(f'iterator_object.next() : { next(iterator_object)}')
    except StopIteration as identifier:
        print(f"identifier :{identifier.value}")

#OUTPUT test_iter_object()
# iterator_object.next() : 12
# iterator_object.next() : 34
# iterator_object.next() : 45
# identifier :None

#Helper Method of check_types_for_iterables()
def IsIterable(_types):
    try:
        iter(_types)
        return True
    except TypeError as identifier:
        return False
# To check if the element is iterable
def check_types_for_iterables():
    my_colorful_list = [12,12.34,"werwq",[1234,23],{1:"one",2:"two"},{1,2,3,4},(1,2,4,4),frozenset({1,2,3,4})]
    for different_types in my_colorful_list:
        print(f'{type(different_types)} Is Iterable {IsIterable(different_types)}')

#OUTPUT check_types_for_iterables
# <class 'int'> Is Iterable False
# <class 'float'> Is Iterable False
# <class 'str'> Is Iterable True
# <class 'list'> Is Iterable True
# <class 'dict'> Is Iterable True
# <class 'set'> Is Iterable True
# <class 'tuple'> Is Iterable True
# <class 'frozenset'> Is Iterable True
if __name__ == "__main__":
    check_types_for_iterables()


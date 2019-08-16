#!/usr/bin/python
"""
    Purpose: To give a good picture of Generators and List comprehension

    e.g for 
    
    list comprehension - [i for itenm in range(0,5) ]   #output is a memory stored list i.e [0,1,2,3,4]
    Genertor expresion  - (i for itenm in range(0,5) )  #output is a Iterable generator object

    NOTE: Difference is the ending closing brackets

    P.S : DONT'T ! NEVER EVER  get confused that generator expressions are tuple comprehension :)
    There is nothing called as tuple comprehension

    Time Complexity of Generator expression <<<<<< list compresension
    Space Complexity of generator expression <<<<<< list comprehension
"""
from sys import getsizeof
import timeit
#List all even numbers less than 100
def list_comprehension():
    return [item for item in range(20) if item % 2==0]

def generator_expression():
    return (item for item in range(20) if item % 2==0)

if __name__ == "__main__":
    print(f'_list_comprehension :{list_comprehension()}')
    #OUTPUT
    #_list_comprehension :[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    print(f'_generator_expression : {generator_expression()}')
    #OUTPUT
    #_generator_expression : <generator object generator_expression.<locals>.<genexpr> at 0x03D817F0>
    print(f'SpaceComplexity - _list_comprehension:{getsizeof(list_comprehension())} ')
    print(f'SpaceComplexity - _generator_expression:{getsizeof(generator_expression())} ')
    # check for the space complexity of list expression and generator_expression
    # output
    # SpaceComplexity - _list_comprehension:100
    # SpaceComplexity - _generator_expression:64
    time_listComprehension = timeit.timeit('''[item for item in range(20) if item % 2==0]''')
    time_generatorexpression = timeit.timeit('''(i for i in range(100) if i % 2 == 0)''')

    print(f'TimeComplexity - _list_comprehension:{time_listComprehension} ')
    print(f'TimeComplexity - _generator_expression:{time_generatorexpression} ')

# TimeComplexity - _list_comprehension:2.249734769
# TimeComplexity - _generator_expression:0.7590804029999996


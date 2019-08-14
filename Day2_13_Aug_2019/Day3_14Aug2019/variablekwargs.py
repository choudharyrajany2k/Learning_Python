#!/usr/bin/python
"""
	Purpose: variable keyword arguments
"""

def func1(**kwargs):
    print(kwargs)


func1(Hello="Helo",test='one')
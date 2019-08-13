#!/usr/bin/python
"""
purpose:  Demo for Debugging
         - Consiole based debgugging - pdb
         - IDE based debugging - pydevd
"""
# import pdb;pdb.set_trace()
breakpoint()
for i in range(9):
    if(i%2==0):
        print(i)
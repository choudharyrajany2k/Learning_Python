#!/usr/bin/python
"""
	Purpose: scoping in functions
"""

pi =  3.4146

# #Case 1 : using without passsing a args
# def myfunc():
#     print(f"pi {pi}")

# myfunc()


# #case2: changing a variable
# def myfunc():
#     print(f'before pi {pi}')  # UnboundLocalError: local variable 'pi' referenced before assignment
#     pi = 3.24
#     print(f'before pi {pi}')


#case 3 : changing the value from parameter
def myfunc(pi):
    print(f'before pi {pi}')  # UnboundLocalError: local variable 'pi' referenced before assignment
    pi = 3.24
    print(f'after pi {pi}')
myfunc(3000)

#!/usr/bin/python
"""
    Purpose Demo Tuple
"""
a= (12,234,523)
print(str(a))
print(a)

print(5*"*"+"Count Demo For tuple"+5*"*")
print(f"(12,22,34,45,222,(22)).count(22) {(12,22,34,45,222,(22)).count(22)}")
print(f"(12,22,34,45,222,(22)).count(22,) {(12,22,34,45,222,(22,)).count(22)}")

print(5*"*"+"Immutable Demo For tuple"+5*"*")
b=(12,234,523,23)
print(f"id(a) {id(a)}")
print(f"id(b) {id(b)}")

print( 'a is b', a is b)
print(f'hash(a):{hash(a)}\t hash(b):{hash(b)}')
#!/usr/bin/python
"""
    File Name: test_closures.py
    Purpose :  Demo for closures
"""

def demo_closures(text):
    print(f'rpintting tfrom outside {text}')
    text = text
    def nested_function():
        print(f'Prinnting from  inside {text}')
    return nested_function

def calling_method():
    result = demo_closures('Hello')
    result()

if __name__ == "__main__":
    calling_method()


#OUTPUT
# rpintting tfrom outside Hello
# Prinnting from  inside Hello
    

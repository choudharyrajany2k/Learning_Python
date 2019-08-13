#!/usr/bin/python
"""
Purpose: To test a functions
"""


def abc():
    a, b = 10, 12
    print(a, b)
# abc()


def multipleParameters(*rajan):
    for argument in rajan:
        print(argument)


def KeyWordArguments(**rajan):
    for keys, values in rajan.items():
        print(f"Keys:{keys} values:{values}")

def checkForList():
    print([(a,b)=(10,20);'This is a true' if a>b else 'This is false'])
if __name__ == '__main__':
    checkForList()
    # print(f'type of KeyWordArguments {type(KeyWordArguments)} id of KeyWordArguments {id(KeyWordArguments)}')
    # print(f'type of pow {type(pow)} id of pow {id(pow)}')
    # multipleParameters('Hello','This ','is ','multiple',1,True)
    # KeyWordArguments(hello="Hello",myword = "myword",test = "mytest")
    # def cube(x): return x*x*x
    # print(cube(7))


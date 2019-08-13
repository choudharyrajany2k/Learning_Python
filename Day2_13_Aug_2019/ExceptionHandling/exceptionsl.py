#!/usr/bin/python
"""Purpose: Exception Demo"""

# try:
#     x = 2/0
#     print("x = ", x)
# except Exception as ex:
#     print("error is ", ex)
#     print("error is ", str(ex))
#     print("error is ", repr(ex))   # raw exception

# try:
#     x = 2/0
#     print("x = ", x)
# except Exception as ex:
#     print("error is ", ex)
#     print("error is ", str(ex))
#     print("error is ", repr(ex))   # raw exception
# else:
#     print("try block has no Errror")
# finally:
#     print("Final Statenent")

"""
    When No Errror  - try-else- finally
    when error  - try-except-finally
"""


def printx(x):
    try:
        a = x/0
        return a
    except Exception as identifier:
        print("Error is ",identifier)
        raise Exception("raised the excpetion")

def hello():
    try:
        printx(2)
    except  (NameError,TypeError) as ex:
        print("Excpetion, ",ex)
    except Exception as ex:
        print("General Exception",repr(ex))
    else:
        print("No Exception Happened")
    finally:
        print('finally statement')
